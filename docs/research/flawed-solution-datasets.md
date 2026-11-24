# Data feasibility of the "collaboratively debug a partner's flawed worked solution" design

**Working date: 2026-11-23.** All URLs below were fetched directly on that date (GitHub raw/README and tarball listings, Hugging Face Hub API/dataset-server, ACL Anthology PDFs/pages, doi.org redirection); counts and hashes obtained by downloading files say so explicitly. **[INFERENCE]** marks analytical judgements. Verification performed by the dataset-research subagents is labelled "subagent-verified".

## Bottom line

**Yes — the design can run on existing public data without creating our own dataset.** Several public corpora put, **on the same item**, (a) a mathematical word problem, (b) an incorrect worked solution / annotated wrong step, and (c) the correct answer or correct worked solution. The best-fit three are **StepVerify**, **MathDial**, and **EIC-Math** (§2–3).

**Two caveats [INFERENCE]:**
1. The dialogue in these datasets is **tutor–student**, not peer–peer. The "two students collaborating" framing must come from our prompt, not be claimed as a property of the data.
2. None of the top three is multimodal. The already-decided MathVista testmini fallback has images and answers but no flawed solutions. Multimodality therefore requires either dropping the image in this adaptation, or an explicitly documented join of two public sources (§5).

---

## 1. Selection criterion

An item must contain all three in one record, with no synthesis by us:

- **(a)** a mathematical word problem (natural-language statement);
- **(b)** an incorrect/flawed worked solution, wrong step, or documented student error;
- **(c)** the correct answer or correct solution.

Datasets that record only a final wrong answer or only a wrong multiple-choice option are **not** sufficient for "locate **and justify correcting** a flawed worked solution" [INFERENCE].

---

## 2. Ranked top three

| Rank | Dataset | Items | Triple on same item? | Licence | Main caveat |
|---|---|---|---|---|---|
| **1** | **StepVerify** (`eth-nlped/stepverify`; verify-then-generate) | **1,002** rows (HF `/size`, fetched) | **Yes**: `problem`, `student_incorrect_solution`, `incorrect_step`, `error_description`, `reference_solution`, `student_correct_response`, plus `dialog_history` | **Unclear**: GitHub README text says CC BY-SA 4.0 while its badge says CC BY 4.0; HF card declares no licence | Licence conflict; "student" solutions are likely simulated (subagent inference) |
| **2** | **MathDial** (`eth-nlped/mathdial`) | **2,861** dialogues: 2,262 train / 599 test (HF `/size`, fetched) | **Yes**: `question`, `student_incorrect_solution`, `ground_truth`, `conversation` (teacher questions that locate the error) | **CC BY 4.0** (README + HF card; README notes alignment from earlier CC BY-SA wording in Nov 2026); GSM8K source is MIT | Errors are LLM-simulated students; tutor–student, not peer dialogue |
| **3** | **EIC-Math** (`LittleCirc1e/EIC`) | Paper: **1,800** cases; pinned repo: **2,607 rows** counted in 18 `generated_cases_clean.jsonl` files | **Yes**: `question`, `original_solution`, `original_answer`, `transformed_solution`, `wrong_step`, `wrong_type`, `explanation` | No `LICENSE` file found in pinned archive | Synthetic GPT-4 perturbations; no declared licence |

Ranking logic [INFERENCE]: StepVerify has the richest per-item correction evidence (first-error location, error description, corrected response); MathDial is the largest cleanly licensed option with dialogue; EIC has the most explicit machine-readable error schema.

---

## 3. Detailed cards for the top three

### 3.1 StepVerify / Verify-Then-Generate — best per-item evidence

- **Official release:** [HF `eth-nlped/stepverify`](https://huggingface.co/datasets/eth-nlped/stepverify) (card fetched) and [GitHub `eth-lre/verify-then-generate`](https://github.com/eth-lre/verify-then-generate) (README fetched, `dataset/` present, no `LICENSE` file). HF revision pinned as `c80445dd89bb21fab744d6284ea28a2e0cf5791b` (Hub API `sha`, 2026-11-23).
- **Count and fields:** HF `/size` → **1,002 rows**, one `train` split; `/info` → 10 features: `problem`, `topic`, `reference_solution`, `student_incorrect_solution`, `incorrect_index`, `incorrect_step`, `error_category`, `error_description`, `dialog_history`, `student_correct_response`. The EMNLP 2024 paper calls it ~1K stepwise chains with teacher-annotated first error steps; a later EMNLP 2025 paper refers to the 1,002-item VtG subset (subagent-verified).
- **Download:**
  ```bash
  pip install -U datasets
  python -c 'from datasets import load_dataset; load_dataset("eth-nlped/stepverify")'
  # or: hf download eth-nlped/stepverify stepverify.json --repo-type dataset
  # code: git clone https://github.com/eth-lre/verify-then-generate.git
  ```
- **Hash pinning:** no official SHA-256 (file is a non-LFS git blob). Downloaded and computed locally on 2026-11-23: `stepverify.json`, 2,641,752 bytes, SHA-256 `335351285ae4b58176a671e6590d5ca29448df98f6b59c2ab8e5598cc8106cbf` — reproducible only against the pinned HF revision.
- **Licence caveat:** fetched README lines 151–155 say "This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License", while the badge at line 3 says CC BY 4.0; the HF card has no licence field. Resolve with the authors before releasing any derived artifact [INFERENCE].
- **Primary paper:** Daheim, N., Mačina, J., Kapur, M., Gurevych, I., & Sachan, M. (2024). *Stepwise Verification and Remediation of Student Reasoning Errors with Large Language Model Tutors.* EMNLP 2024, pp. 8386–8411. DOI [10.18653/v1/2024.emnlp-main.478](https://doi.org/10.18653/v1/2024.emnlp-main.478); verified via OpenAlex [W4404782691](https://openalex.org/W4404782691), Mendeley (subagent-verified), and doi.org → `aclanthology.org/2024.emnlp-main.478/` (200).

### 3.2 MathDial — best licensed and largest dialogue corpus

- **Official release:** [GitHub `eth-nlped/mathdial`](https://github.com/eth-nlped/mathdial) and [HF `eth-nlped/mathdial`](https://huggingface.co/datasets/eth-nlped/mathdial). HF revision `acc3878459e0bd8c04ab840056572f0b8b1abe1f` (Hub API, 2026-11-23); README states the dataset contains all 2,861 conversations.
- **Count and fields:** HF `/size` → 2,861 rows; split sizes 2,262 train + 599 test. `/info` features: `question` (GSM8K MWP), `student_incorrect_solution`, `ground_truth`, `conversation`, `student_profile`, `teacher_described_confusion`, `qid`, `scenario`, `self-correctness`, `self-typical-confusion`, `self-typical-interactions`. The dialogue is the closest public demonstration of locating and justifying an error [INFERENCE].
- **Download:**
  ```bash
  git clone https://github.com/eth-nlped/mathdial.git
  # data under data/train.{csv,jsonl}, data/test.{csv,jsonl}
  # or: hf download eth-nlped/mathdial --repo-type dataset
  ```
- **Hash pinning:** no official SHA-256. Downloaded and computed locally 2026-11-23: `train.jsonl` 7,181,555 bytes, SHA-256 `d6135869c02dccf8d14756fa2f0367c5352922bb263ec22dc0eeace4da815d43`; `test.jsonl` 1,858,054 bytes, SHA-256 `3ec54ee8ab921dc6191bf5e2ee766d4e7916b4264394eb17a6be9b3fe486e50b`.
- **Licence:** fetched README lines 96–103 explicitly state CC BY 4.0, note that earlier versions said CC BY-SA 4.0 and were aligned in November 2026; HF card metadata is `cc-by-4.0`; underlying GSM8K is MIT.
- **Primary paper:** Mačina, J., Daheim, N., Chowdhury, S. P., Sinha, T., Kapur, M., Gurevych, I., & Sachan, M. (2023). *MathDial: A Dialogue Tutoring Dataset with Rich Pedagogical Properties Grounded in Math Reasoning Problems.* Findings of EMNLP 2023, pp. 5602–5621. DOI [10.18653/v1/2023.findings-emnlp.372](https://doi.org/10.18653/v1/2023.findings-emnlp.372); verified via OpenAlex [W4389518941](https://openalex.org/W4389518941), Mendeley (subagent-verified), and doi.org → ACL Anthology (200).

### 3.3 EIC-Math — cleanest typed error schema

- **Official release:** [github.com/LittleCirc1e/EIC](https://github.com/LittleCirc1e/EIC); GitHub `HEAD` = `be8132a826dd7890d5ba92bd0c87451a3275874a` (from `git ls-remote`); the data branch is `master` (a `main` tarball request returned no files).
- **Fields (official README, fetched):** `question`, `original_solution`, `original_answer`, `transformed_solution`, `transformed_answer`, `wrong_step`, `wrong_type`, `is_single_error`, `explanation`.
- **Count:** paper states **1,800** cases (9 error types × 100 × GSM8K and MathQA); direct line count of the 18 `generated_cases_{GSM8K,MathQA}/*/*/generated_cases_clean.jsonl` files at the pinned commit gave **1,291 + 1,316 = 2,607 rows** (2026-11-23). The mismatch with the paper count is observed, not explained [INFERENCE].
- **Download:**
  ```bash
  git clone https://github.com/LittleCirc1e/EIC.git
  cd EIC && git checkout be8132a826dd7890d5ba92bd0c87451a3275874a
  ```
- **Hash pinning:** no per-file checksums found; codeload `master` tarball SHA-256 computed locally as `ea5013510d7da4bedec81cc26de989fb67ca95fcef2e75ba27118bd01602ba65` (248,288,735 bytes). Prefer the git commit SHA, since GitHub can regenerate archives [INFERENCE].
- **Licence:** no `LICENSE`/`COPYING` file in the pinned tarball (checked 2026-11-23) — unspecified.
- **Primary paper:** Li, X., Wang, W., Li, M., Guo, J., Zhang, Y., & Feng, F. (2024). *Evaluating Mathematical Reasoning of Large Language Models: A Focus on Error Identification and Correction.* Findings of ACL 2024, pp. 11316–11360. DOI [10.18653/v1/2024.findings-acl.673](https://doi.org/10.18653/v1/2024.findings-acl.673); verified via OpenAlex [W4402670352](https://openalex.org/W4402670352), Mendeley (subagent-verified), doi.org → ACL Anthology (200).

---

## 4. Other public candidates assessed

| Dataset | Counts / licence / pin (verified 2026-11-23) | Triple? | Verdict |
|---|---|---|---|
| **PRM800K** ([GitHub](https://github.com/openai/prm800k), [HF mirror](https://huggingface.co/datasets/tasksource/PRM800K)) | Paper: **800,000** step labels / 75,000 solutions / 12,000 MATH problems; HF mirror commit `547b19506677a59037ee888838834b65e9b1ddd4`; **MIT**; official LFS SHA-256 for `phase2_train.jsonl` = `1110237feeb51d1bc200cb37b8f965cfdc1036eac7d506094049366fe7dc1089`, `phase2_test.jsonl` = `6b172efa884ac8341a946dd82e06947c135b7254109fb3f7aa907c715d98aaad` | **Yes** (`problem`, `ground_truth_solution`, `ground_truth_answer`, `pre_generated_steps`, step ratings) | Huge and cleanly licensed, but competition MATH problems and model-generated errors. Paper: *Let's Verify Step by Step*, DOI [10.48550/arXiv.2305.20050](https://doi.org/10.48550/arXiv.2305.20050), OpenAlex [W4379089709](https://openalex.org/W4379089709) |
| **PARC error-detection-negatives** ([HF](https://huggingface.co/datasets/PARC-DATASETS/error-detection-negatives)) | **214** items (57 GSM8K, 44 MATH, 59 MetaMathQA, 54 Orca-Math); MIT; commit `5ef7eafcb58fdc0a4f45211141d21437fb410ea5`; parquet SHA-256 `2305a3fae7ccf3b7ae9173c5fdb2197a3389c0c840be715d5be5da33084fa933` verified locally | **Yes** (`question`, `ground_truth_solution`, `ground_truth_answer`, `steps`, `error_annotation`) | Small but perfectly pinned; no dataset paper located via OpenAlex (subagent-verified) |
| **GSM8K-SC** ([HF](https://huggingface.co/datasets/kenhktsui/gsm8k_sc)) | **1,313** `test` rows; no dataset licence; commit `f9c0af7f82ec882372c91a155bd3588aa81b5bad`; official LFS SHA-256 `995ae737fdb69f22946161b380cfed9511547cd555aa56028de0936f399eb019` | **Yes** (`question`, `answer`, `reasoning_steps_with_one_mistake`, `mistake_step`, `type_of_mistake`) | Strong text-only alternative; no publisher DOI verified (arXiv:2507.02778) |
| **Bi-GSM8K** ([HF](https://huggingface.co/datasets/Tutoruslabs/bi-gsm8k)) | **500 English + 500 Korean** public rows (paper describes a larger set — discrepancy observed); no dataset licence; commit `9f904499354c1be7797aa57d7c816fccaa315b2b`; official LFS SHA-256 en `2da87c9a80117b421cbedb2aa8805ddba777ccc50ff9ebf7f890c2dde989dac4`, ko `cc3afb0a92eb9492baf867daec15f43cdd4a9cd8d24222d59bcd7da49770c2e4` | **Yes** (`problem`, `correct_solution_steps`, `error_solution_steps`, `initial_error_step`) | Expert-simulated errors; DOI [10.18653/v1/2026.findings-eacl.85](https://doi.org/10.18653/v1/2026.findings-eacl.85) (subagent-verified) |
| **MaE / algebra_misconceptions** ([HF](https://huggingface.co/datasets/nanote/algebra_misconceptions)) | **220** examples covering **55** algebra misconceptions; **MIT**; revision `afce3dbe2323b3732784447b933ee81db87d2a36` (subagent-verified) | **Yes** (separate `question` / `incorrect_answer` / `correct_answer` files) | Clean and licensed, but researcher-designed diagnostic items, not authentic student work; DOI [10.1007/s44217-025-00742-w](https://doi.org/10.1007/s44217-025-00742-w) (subagent-verified) |
| **CogTutorBugs** ([GitHub](https://github.com/umass-ml4ed/CogTutorBugs)) | **5,339** usable erroneous steps, 19 error categories; **CC BY 4.0**; commit `518930ecc399beee668b54234478fe2bb94484d2` (subagent-verified) | **Partial** (algebra step errors + corrective feedback, not full MWP worked solutions) | Best for authentic student step errors; DOI [10.1007/978-3-031-36272-9_30](https://doi.org/10.1007/978-3-031-36272-9_30) (subagent-verified) |
| **ErrorRadar** ([HF](https://huggingface.co/datasets/ErrorRadar/ErrorRadar)) | **2,500** rows; no declared licence; commit `5c298559830b77f0e7704e33f1bf9191e133cd45`; fields include `content_image` | **Yes** (`content`, `user_answer_steps`, `error_step`, `answer`) | Only multimodal option found; image URLs reportedly 403 and licence unspecified (subagent-verified) → not usable as primary without rights/access check [INFERENCE] |
| **ProcessBench** ([HF](https://huggingface.co/datasets/Qwen/ProcessBench)) | **3,400** items (400/1,000/1,000/1,000); Apache-2.0; commit `3bdcd5371ed567559a78f559c01c13a6deee7604`; locally computed SHA-256 of `gsm8k.json` = `fb1c59dfd1e83e1c5a48dbe598db27e4bc0b8bc524a09445f2d4b69178f61349`, `math.json` = `60cb0d7a69cbec98d43cf50855b9b7e7294599c3c9a24bdd031abd18c3b6b136` | **Partial**: no correct-solution/answer field, only `final_answer_correct` + first-error index | Would require a documented join with GSM8K/MATH. DOI [10.18653/v1/2025.acl-long.50](https://doi.org/10.18653/v1/2025.acl-long.50), OpenAlex [W4412886965](https://openalex.org/W4412886965) |
| **MathEDU** ([GitHub](https://github.com/NYCU-NLP-Lab/MathEDU)) | **4,048** annotated solutions (3,050 correct, 998 incorrect); commit `acb1873f1569048d72c90855febc6f367b1e3356`; no `LICENSE` file | **Partial**: `id` maps to MathQA, problem text not stored in record | Authentic student work + teacher feedback, but needs a join; DOI [10.18653/v1/2026.eacl-long.132](https://doi.org/10.18653/v1/2026.eacl-long.132), OpenAlex [W7140106567](https://openalex.org/W7140106567) |
| **MWP-MISTAKE** ([ACL paper](https://aclanthology.org/2025.acl-long.1313/)) | Official link [aka.ms/MWP-MISTAKE](https://aka.ms/MWP-MISTAKE) → `github.com/joykirat18/MWP-MISTAKE`; tarball of current HEAD `413a3fc1623dee4823af375852615b21553cf075` contains **README.md only**, saying "dataset and code will be released soon!!" | Conceptually ideal | **Not available as public data on 2026-11-23**; DOI [10.18653/v1/2025.acl-long.1313](https://doi.org/10.18653/v1/2025.acl-long.1313), OpenAlex [W4412889880](https://openalex.org/W4412889880) |
| **Eedi 2024 / Eedi MAP / ASSISTments / EdNet / DataShop raw logs** | Distractors + misconception labels (Eedi 2024, CC BY-NC 4.0); authentic student explanations of a selected option (MAP); binary `correct`/attempt counts (ASSISTments, EdNet, DataShop; subagent-verified) | **No**: no worked wrong solution paired with a correct worked solution | Use only as contextual literature, not as the claimed data source |
| **MathVista testmini fallback** | Public multimodal MWP benchmark with answers; no flawed solutions | **No** | Problem source only if the flawed solution is added at inference time (§6) |

---

## 5. The multimodal gap and the smallest substitution

- **Observed:** StepVerify, MathDial, EIC, PRM800K and PARC are text-only. ErrorRadar has images but no declared licence and unreliable image access (subagent-verified).
- **Smallest substitution that keeps public data only [INFERENCE]:** run the main experiment on **StepVerify or MathDial as-is** and describe the module as *textual contextualization* in this adaptation; do not fabricate image inputs. If an image is mandatory, the smallest documented alternative is a **join of two public datasets**: a multimodal MWP item from MathVista testmini (public) with a text error item from the same family where possible (e.g. GSM8K-derived MathDial/StepVerify items). This must be recorded in the data manifest with both sources, revisions and hashes. It is not "self-built" in the sense of collecting or labelling new data, but it is a derived combination and must be disclosed [INFERENCE].
- Do **not** claim MWP-MISTAKE supplies the data — it is unreleased (§4).

---

## 6. Would generating the flawed solution with the LLM violate "no self-built dataset"?

**Short answer [INFERENCE]: it depends on whether the generated flaws are stored and used as a dataset.**

1. **Runtime-only generation (probably acceptable):** prompt the model at inference time to produce "a partner's plausible wrong solution" for a public MWP, exactly as SocioMathLLM generates five candidate problems at inference time, and publish only prompts, code and metrics — no new corpus. The underlying problems and correct answers stay public (e.g. MathVista testmini or GSM8K). This is a prompting strategy, not a dataset contribution [INFERENCE]. It must be disclosed, and the generated text must not be described as "annotated student errors".
2. **Stored/selected generated flaws (violates the constraint):** generating wrong solutions in bulk, filtering them, freezing them into JSONL/parquet and evaluating against that file creates a new derived dataset, even if source problems are public [INFERENCE].
3. **Validity caveat [INFERENCE]:** runtime-generated flaws have no verified `wrong_step` or `wrong_type`, so they cannot support a rigorous "locate and justify the correction" rubric. StepVerify/MathDial/EIC — where the error and its location are annotated — are the defensible primary sources; runtime generation is acceptable only for a clearly labelled qualitative pilot.

---

## 7. Manifest-ready pinning summary

| Dataset | Source | Pin | SHA-256 status |
|---|---|---|---|
| StepVerify | `eth-nlped/stepverify` | HF `c80445dd89bb21fab744d6284ea28a2e0cf5791b` | locally computed `stepverify.json` `335351285ae4b58176a671e6590d5ca29448df98f6b59c2ab8e5598cc8106cbf` |
| MathDial | `eth-nlped/mathdial` | HF `acc3878459e0bd8c04ab840056572f0b8b1abe1f` | locally computed `train.jsonl` `d6135869c02dccf8d14756fa2f0367c5352922bb263ec22dc0eeace4da815d43`, `test.jsonl` `3ec54ee8ab921dc6191bf5e2ee766d4e7916b4264394eb17a6be9b3fe486e50b` |
| EIC | `LittleCirc1e/EIC` | commit `be8132a826dd7890d5ba92bd0c87451a3275874a` | archive hash only, `ea5013510d7da4bedec81cc26de989fb67ca95fcef2e75ba27118bd01602ba65` |
| PRM800K | `openai/prm800k` / `tasksource/PRM800K` | HF `547b19506677a59037ee888838834b65e9b1ddd4` | official LFS OIDs for both phase-2 files (§4) |
| PARC | `PARC-DATASETS/error-detection-negatives` | `5ef7eafcb58fdc0a4f45211141d21437fb410ea5` | official + locally verified `2305a3fae7ccf3b7ae9173c5fdb2197a3389c0c840be715d5be5da33084fa933` |
| GSM8K-SC | `kenhktsui/gsm8k_sc` | `f9c0af7f82ec882372c91a155bd3588aa81b5bad` | official LFS OID `995ae737fdb69f22946161b380cfed9511547cd555aa56028de0936f399eb019` |
| Bi-GSM8K | `Tutoruslabs/bi-gsm8k` | `9f904499354c1be7797aa57d7c816fccaa315b2b` | official LFS OIDs en/ko (§4) |

**Unverified / cautions:** StepVerify's licence conflict (§3.1) and EIC/MathEDU/ErrorRadar's missing licence declarations (§3.3, §4) must be resolved before releasing any derived artifact; MWP-MISTAKE data are unreleased; EIC's repo row count differs from its paper count; some ErrorRadar image URLs returned 403 to the subagent. Everything else was read from the live source on 2026-11-23.
