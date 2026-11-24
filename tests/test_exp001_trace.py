"""Runnable checks for the reusable trace core and its generic reader."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from experiment_report import load_events, summarize
from experiment_trace import ConfigChangedError, RunLog, canonical_config_sha256, sha256_text


class TraceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.run_dir = self.root / "committed"
        self.local_dir = self.root / "local"

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def make_log(self, config: dict) -> RunLog:
        return RunLog(
            "EXP-TEST",
            run_dir=self.run_dir,
            local_dir=self.local_dir,
            config=config,
            repo=self.root,
        )

    def test_attempt_increments_and_config_change_is_refused(self) -> None:
        config = {"seed": 1}
        expected = canonical_config_sha256(config)
        with self.make_log(config) as trace:
            trace.start(mode="prepare", config_sha256=expected)
        first = load_events(self.run_dir / "events.jsonl")
        self.assertEqual(first[0]["config_sha256"], expected)
        self.assertEqual(first[0]["attempt"], 1)
        self.assertEqual(first[0]["event"], "started")
        self.assertEqual(first[0]["mode"], "prepare")

        with self.make_log({"seed": 1}) as trace:
            trace.start(mode="prepare")
        self.assertEqual(load_events(self.run_dir / "events.jsonl")[-1]["attempt"], 2)

        with self.assertRaises(ConfigChangedError):
            self.make_log({"seed": 2})

    def test_failed_before_start_still_consumes_an_attempt(self) -> None:
        trace = self.make_log({"seed": 1})
        try:
            with trace:
                raise RuntimeError("boom")
        except RuntimeError:
            pass
        with self.make_log({"seed": 1}) as next_trace:
            next_trace.start(mode="prepare")
        self.assertEqual(next_trace.attempt, 2)

    def test_events_stages_items_artifacts_and_provenance(self) -> None:
        with self.make_log({"seed": 1}) as trace:
            trace.start(mode="prepare", data_sha256="abc")
            with trace.stage("compile"):
                with trace.item("lab-1"):
                    trace.event("item_compiled", compiled=True, passed=1, total=2)
                reference = trace.artifact("gcc-err.txt", "compiler output")
                trace.event("compile_failed", error_class="CompileError", output_ref=reference)
            trace.write_provenance(data_sha256="abc")
            trace.finish(n_items=1)

        events = load_events(self.run_dir / "events.jsonl")
        names = [event["event"] for event in events]
        self.assertEqual(
            names,
            ["started", "stage_started", "item_compiled", "compile_failed",
             "stage_completed", "completed"],
        )
        self.assertEqual(events[2]["item_id"], "lab-1")
        self.assertEqual(events[2]["stage"], "compile")
        self.assertTrue(all({"timestamp_utc", "t_s", "run_id", "attempt"} <= set(e) for e in events))
        self.assertEqual(events[3]["output_ref"]["sha256"], sha256_text("compiler output"))
        self.assertEqual((self.local_dir / "gcc-err.txt").read_text(encoding="utf-8"), "compiler output")
        provenance = json.loads((self.run_dir / "provenance.json").read_text(encoding="utf-8"))
        self.assertEqual(provenance["data_sha256"], "abc")
        self.assertEqual(provenance["run_id"], events[0]["run_id"])

    def test_failure_writes_error_log_and_failed_event(self) -> None:
        trace = self.make_log({"seed": 1})
        try:
            with trace:
                trace.start(mode="prepare")
                raise RuntimeError("boom")
        except RuntimeError:
            pass
        events = load_events(self.run_dir / "events.jsonl")
        self.assertEqual(events[-1]["event"], "failed")
        self.assertEqual(events[-1]["error_class"], "RuntimeError")
        self.assertIn("RuntimeError: boom", (self.local_dir / "errors.log").read_text(encoding="utf-8"))

    def test_summarize_links_runs_stages_and_errors(self) -> None:
        trace = self.make_log({"seed": 1})
        try:
            with trace:
                trace.start(mode="full")
                with trace.stage("generation"):
                    with trace.item("lab-1"):
                        trace.event("judge_scored", dimension="collaboration", score=4)
                raise RuntimeError("boom")
        except RuntimeError:
            pass
        summary = summarize(load_events(self.run_dir / "events.jsonl"))
        self.assertEqual(summary["runs"][0]["status"], "failed")
        self.assertEqual(summary["runs"][0]["mode"], "full")
        self.assertEqual(summary["stages"][0]["stage"], "generation")
        self.assertIsNotNone(summary["stages"][0]["duration_s"])
        self.assertEqual(summary["items"]["lab-1"]["score"], [4])
        self.assertEqual(summary["errors"][0]["error_class"], "RuntimeError")


if __name__ == "__main__":
    unittest.main()
