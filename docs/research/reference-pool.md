# Reference pool — Topic 1 (SocioMathLLM) and cross-topic bridges

Checked 2026-11-23. This pool supports an English UAS paper adjacent to Hwang and Utami's SocioMathLLM study (DOI `10.1109/TLT.2026.3677266`). All 50 entries are unique DOIs (deduplicated case-insensitively); no DOI is listed twice. Bibliographic metadata, publication type, and OpenAlex identifiers come from OpenAlex work records; DOI activity was checked by resolving `https://doi.org/<DOI>` and, where available, by Crossref registration metadata. "JOURNAL ARTICLE — DOI ACTIVE" means OpenAlex indexes the item as an `article` in a peer-reviewed journal and the DOI resolves; "JOURNAL REVIEW — DOI ACTIVE" is a peer-reviewed journal review; "CONFERENCE PAPER — DOI ACTIVE" is a peer-reviewed proceedings item. Every *Relevance* line is an analytical judgement for our study and is explicitly marked [INFERENCE]; the citation and verification lines are source-checked facts.

---

## Cluster 1 — Automatic math word problem generation and automatic question generation

**R1. Hwang, W.-Y., & Utami, I. Q. (2026). SocioMathLLM: A Multimodal Large Language Model Framework for Generating Authentic Mathematical Word Problems Driving Socialization. *IEEE Transactions on Learning Technologies, 19*, 271–285.** DOI: [10.1109/TLT.2026.3677266](https://doi.org/10.1109/TLT.2026.3677266). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Source paper for Topic 1: contextualization from authentic images, personalization with student profiles, and four socialization competencies provide the three-module design we extend.
- **Verification:** OpenAlex [W7140222536](https://openalex.org/W7140222536) (type: article); DOI resolves to IEEE Xplore document 11455325; Crossref registration confirmed.

**R2. Das, B., Majumder, M., Phadikar, S., & Sekh, A. A. (2021). Automatic question generation and answer assessment: a survey. *Research and Practice in Technology Enhanced Learning, 16*(1), Article 5.** DOI: [10.1186/s41039-021-00151-1](https://doi.org/10.1186/s41039-021-00151-1). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Maps question-generation and answer-assessment pipelines that parallel our generate-then-evaluate design for mathematical word problems.
- **Verification:** OpenAlex [W3143827210](https://openalex.org/W3143827210) (type: article); DOI resolves to Springer (Crossref was rate-limited at check time).

**R3. Kurdi, G. R., Leo, J., Parsia, B., Sattler, U., & Al-E'mari, S. (2019/2020). A Systematic Review of Automatic Question Generation for Educational Purposes. *International Journal of Artificial Intelligence in Education, 30*(1), 121–204.** DOI: [10.1007/s40593-019-00186-y](https://doi.org/10.1007/s40593-019-00186-y). **JOURNAL REVIEW — DOI ACTIVE**
- **Relevance [INFERENCE]:** Supplies the educational AQG taxonomy (pedagogical goals, inputs, outputs, evaluation) used to position our generation framework.
- **Verification:** OpenAlex [W2989613245](https://openalex.org/W2989613245) (type: review; publication_year 2019, Crossref published 2020-03); DOI resolves; Crossref registration confirmed.

**R4. Holling, H., Bertling, J., & Zeuch, N. (2009). Automatic item generation of probability word problems. *Studies in Educational Evaluation, 35*(2–3), 71–76.** DOI: [10.1016/j.stueduc.2009.10.004](https://doi.org/10.1016/j.stueduc.2009.10.004). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Early primary evidence that algorithmic item generation can produce controlled probability word problems, motivating template- and context-constrained generation.
- **Verification:** OpenAlex [W1997703011](https://openalex.org/W1997703011) (type: article); DOI resolves to Elsevier; Crossref registration confirmed.

**R5. Circi, R., Hicks, J., & Sikali, E. (2023). Automatic item generation: foundations and machine learning-based approaches for assessments. *Frontiers in Education, 8*, Article 858273.** DOI: [10.3389/feduc.2023.858273](https://doi.org/10.3389/feduc.2023.858273). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Clarifies how generated items are validated for assessment use, which informs our quality criteria beyond surface text similarity.
- **Verification:** OpenAlex [W4381573643](https://openalex.org/W4381573643) (type: article); DOI resolves to Frontiers (Crossref was rate-limited at check time).

**R6. Hommel, B. E., Wollang, F.-J., Kotova, V., Zacher, H., & Schmukle, S. C. (2022). Transformer-Based Deep Neural Language Modeling for Construct-Specific Automatic Item Generation. *Psychometrika, 87*(2), 749–772.** DOI: [10.1007/s11336-021-09823-9](https://doi.org/10.1007/s11336-021-09823-9). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Demonstrates construct-specific, model-based item generation, a precedent for constraining LLM output to a target mathematical construct.
- **Verification:** OpenAlex [W4226163610](https://openalex.org/W4226163610) (type: article); DOI resolves to Cambridge Core (Crossref was rate-limited at check time).

**R7. Bezirhan, U., & von Davier, M. (2023). Automated reading passage generation with OpenAI's large language model. *Computers and Education: Artificial Intelligence, 5*, Article 100161.** DOI: [10.1016/j.caeai.2023.100161](https://doi.org/10.1016/j.caeai.2023.100161). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Shows GPT-based passage generation for educational content and the need to evaluate generated text quality, analogous to our MWP evaluation.
- **Verification:** OpenAlex [W4385973406](https://openalex.org/W4385973406) (type: article); DOI resolves to Elsevier (Crossref was rate-limited at check time).

**R8. Ling, J., & Afzaal, M. (2024). Automatic question-answer pairs generation using pre-trained large language models in higher education. *Computers and Education: Artificial Intelligence, 6*, Article 100252.** DOI: [10.1016/j.caeai.2024.100252](https://doi.org/10.1016/j.caeai.2024.100252). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Provides a recent LLM-based Q/A generation and evaluation workflow directly comparable to our candidate-problem generation stage.
- **Verification:** OpenAlex [W4399476954](https://openalex.org/W4399476954) (type: article); DOI resolves to Elsevier; Crossref registration confirmed.

**R9. Xu, Y., Smeets, R., & Bidarra, R. (2021). Procedural generation of problems for elementary math education. *International Journal of Serious Games, 8*(2), 49–66.** DOI: [10.17083/ijsg.v8i2.396](https://doi.org/10.17083/ijsg.v8i2.396). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Offers a rule-driven alternative to LLM generation, useful for discussing controllability and diversity of generated math problems.
- **Verification:** OpenAlex [W3165921945](https://openalex.org/W3165921945) (type: article); DOI resolves to the journal PDF; Crossref registration confirmed.

**R10. Zhang, D., Wang, L., Zhang, L., Dai, B. T., & Shen, H. T. (2019/2020). The Gap of Semantic Parsing: A Survey on Automatic Math Word Problem Solvers. *IEEE Transactions on Pattern Analysis and Machine Intelligence, 42*(9), 2287–2305.** DOI: [10.1109/TPAMI.2019.2914054](https://doi.org/10.1109/TPAMI.2019.2914054). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Establishes the semantic-parsing background and the limits of earlier MWP systems that generative LLM approaches aim to overcome.
- **Verification:** OpenAlex [W2962927633](https://openalex.org/W2962927633) (type: article; publication_year 2019, volume 42 issue 9 dated 2020); DOI resolves to IEEE Xplore document 8703135; Crossref registration confirmed.

**R11. Liu, T., Fang, Q., Ding, W., Li, H., Wu, Z., & Liu, Z. (2021). Mathematical Word Problem Generation from Commonsense Knowledge Graph and Equations. In *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 4225–4240.** DOI: [10.18653/v1/2021.emnlp-main.348](https://doi.org/10.18653/v1/2021.emnlp-main.348). **CONFERENCE PAPER — DOI ACTIVE**
- **Relevance [INFERENCE]:** Primary precedent for generating MWPs from structured inputs (knowledge graph plus equations), the nearest non-LLM analogue to our structured prompts.
- **Verification:** OpenAlex [W3092766609](https://openalex.org/W3092766609) (type: conference-paper); DOI resolves to ACL Anthology; Crossref registration confirmed.

**R12. Shridhar, K., Mačina, J., El-Assady, M., Sinha, T., Kapur, M., & Sachan, M. (2022). Automatic Generation of Socratic Subquestions for Teaching Math Word Problems. In *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 4136–4149.** DOI: [10.18653/v1/2022.emnlp-main.277](https://doi.org/10.18653/v1/2022.emnlp-main.277). **CONFERENCE PAPER — DOI ACTIVE**
- **Relevance [INFERENCE]:** Links pedagogical questioning to MWP generation, supporting our use of instructional cues and scaffolded prompts.
- **Verification:** OpenAlex [W4385573161](https://openalex.org/W4385573161) (type: conference-paper); DOI resolves to ACL Anthology; Crossref registration confirmed.

---

## Cluster 2 — Multimodal / image-grounded LLM generation in education

**R13. Bewersdorff, A., Hartmann, C., Hornberger, M., Seßler, K., Bannert, M., Kasneci, E., Kasneci, G., Zhai, X., & Nerdel, C. (2025). Taking the next step with generative artificial intelligence: The transformative role of multimodal large language models in science education. *Learning and Individual Differences, 118*, Article 102601.** DOI: [10.1016/j.lindif.2024.102601](https://doi.org/10.1016/j.lindif.2024.102601). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Reviews how vision-capable LLMs interpret images and generate educational feedback, framing SocioMathLLM's image-to-problem module.
- **Verification:** OpenAlex [W4406232026](https://openalex.org/W4406232026) (type: article); DOI resolves to Elsevier; Crossref registration confirmed (author spelling Xiaoming Zhai checked against the publisher-author listing).

**R14. Lee, U., Jeon, M., Lee, Y., Byun, G., Son, Y., Shin, J., Ko, H., & Kim, H. (2024). LLaVA-docent: Instruction tuning with multimodal large language model to support art appreciation education. *Computers and Education: Artificial Intelligence, 7*, Article 100297.** DOI: [10.1016/j.caeai.2024.100297](https://doi.org/10.1016/j.caeai.2024.100297). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Empirical example of instruction-tuned multimodal generation for education, relevant to our image-grounded prompting and evaluation design.
- **Verification:** OpenAlex [W4402512478](https://openalex.org/W4402512478) (type: article); DOI resolves to Elsevier; Crossref registration confirmed.

**R15. Wang, S., Xu, T., Li, H., Zhang, C., Liang, J., Tang, J., Yu, P. S., & Wen, Q. (2025). Large Language Models for Education: A survey and outlook. *IEEE Signal Processing Magazine, 42*(6), 51–63.** DOI: [10.1109/MSP.2025.3594309](https://doi.org/10.1109/MSP.2025.3594309). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Broad LLM-in-education survey used to situate SocioMathLLM among generative tutoring and content-generation applications.
- **Verification:** OpenAlex [W7125975657](https://openalex.org/W7125975657) (type: article); DOI resolves to IEEE Xplore document 11364183; Crossref registration confirmed.

**R16. Kasneci, E., Seßler, K., Küchemann, S., Bannert, M., Dementieva, D., Fischer, F., Gasser, U., Groh, G., Günnemann, S., Hüllermeier, E., Krusche, S., Kutyniok, G., Michaeli, T., Nerdel, C., Pfeffer, J., Poquet, O., Sailer, M., Schmidt, A., Seidel, T., Stadler, M. J., Weller, J., Kühn, J., & Kasneci, G. (2023). ChatGPT for good? On opportunities and challenges of large language models for education. *Learning and Individual Differences, 103*, Article 102274.** DOI: [10.1016/j.lindif.2023.102274](https://doi.org/10.1016/j.lindif.2023.102274). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Authoritative statement of LLM opportunities and risks in education, supporting our discussion of validity and ethical limits.
- **Verification:** OpenAlex [W4323655724](https://openalex.org/W4323655724) (type: article); DOI resolves to Elsevier; Crossref registration confirmed.

**R17. Yan, L., Sha, L., Zhao, L., Li, Y., Martínez-Maldonado, R., Chen, G., Li, X., Jin, Y., & Gašević, D. (2023/2024). Practical and ethical challenges of large language models in education: A systematic scoping review. *British Journal of Educational Technology, 55*(1), 90–112.** DOI: [10.1111/bjet.13370](https://doi.org/10.1111/bjet.13370). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Supplies evaluation and ethics criteria that constrain any claim that generated problems are authentic or pedagogically safe.
- **Verification:** OpenAlex [W4385632485](https://openalex.org/W4385632485) (type: article; volume 55 issue 1 dated 2024); Crossref registration confirmed (doi.org returns HTTP 403 to automated clients, not a missing DOI).

**R18. Chen, J., Tang, J., Qin, J., Liang, X., Liu, L., Xing, E. P., & Lin, L. (2021). GeoQA: A Geometric Question Answering Benchmark Towards Multimodal Numerical Reasoning. In *Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021*, 513–523.** DOI: [10.18653/v1/2021.findings-acl.46](https://doi.org/10.18653/v1/2021.findings-acl.46). **CONFERENCE PAPER — DOI ACTIVE**
- **Relevance [INFERENCE]:** Primary multimodal-geometry benchmark, directly relevant to SocioMathLLM's 2-D geometry scope and its stated limitation.
- **Verification:** OpenAlex [W3176186248](https://openalex.org/W3176186248) (type: conference-paper); DOI resolves to ACL Anthology; Crossref registration confirmed.

**R19. Zhang, S., Qu, L., You, S., Yang, Z., & Zhang, J. (2017). Automatic Generation of Grounded Visual Questions. In *Proceedings of the Twenty-Sixth International Joint Conference on Artificial Intelligence (IJCAI)*, 4235–4243.** DOI: [10.24963/ijcai.2017/592](https://doi.org/10.24963/ijcai.2017/592). **CONFERENCE PAPER — DOI ACTIVE**
- **Relevance [INFERENCE]:** Founding method for image-grounded question generation, the technical ancestor of generating word problems from authentic images.
- **Verification:** OpenAlex [W2561296180](https://openalex.org/W2561296180) (type: conference-paper); DOI resolves to IJCAI proceedings; Crossref registration confirmed.

**R20. Li, S., Zhang, Z., Shi, Y., & Yao, C. (2026). Enhancing core competencies in digital education by multimodal large language models. *Discover Computing, 29*, Article 608.** DOI: [10.1007/s10791-026-10542-x](https://doi.org/10.1007/s10791-026-10542-x). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Recent GPT-4o-based multimodal teaching model with multi-dimensional competency evaluation, a close comparison point for SocioMathLLM's competency and socialization aims.
- **Verification:** OpenAlex [W7208749480](https://openalex.org/W7208749480) (type: article); DOI resolves to Springer (published 2026-09-04 per publisher page; Crossref was rate-limited at check time).

---

## Cluster 3 — Prompt engineering: zero-shot, few-shot, chain-of-thought, structured criteria

**R21. Debnath, T., Siddiky, M. N. A., Rahman, M. E., Das, P., Guha, A. K., Rahman, M. R., & Kabir, H. M. D. (2026). A comprehensive survey of prompt engineering and context engineering techniques in large language models. *Computer Science Review, 62*, Article 100979.** DOI: [10.1016/j.cosrev.2026.100979](https://doi.org/10.1016/j.cosrev.2026.100979). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Current taxonomy of prompting strategies used to describe the zero-shot candidate generation and few-shot instructional cues in SocioMathLLM.
- **Verification:** OpenAlex [W7164809986](https://openalex.org/W7164809986) (type: article); DOI resolves to Elsevier (Crossref was rate-limited at check time).

**R22. Liu, J., Liu, F., Wang, C., & Liu, S. (2025). Prompt Engineering in Clinical Practice: Tutorial for Clinicians. *Journal of Medical Internet Research, 27*, Article e72644.** DOI: [10.2196/72644](https://doi.org/10.2196/72644). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Tutorial on explicit prompt structure and criteria, transferable to our structured, criterion-based generation and selection prompts.
- **Verification:** OpenAlex [W4412884948](https://openalex.org/W4412884948) (type: article); DOI resolves to JMIR (Crossref was rate-limited at check time).

**R23. Sivarajkumar, S., Kelley, M., Samolyk-Mazzanti, A., Visweswaran, S., & Wang, Y. (2024). An Empirical Evaluation of Prompting Strategies for Large Language Models in Zero-Shot Clinical Natural Language Processing: Algorithm Development and Validation Study. *JMIR Medical Informatics, 12*, Article e55318.** DOI: [10.2196/55318](https://doi.org/10.2196/55318). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Controlled comparison of zero-shot prompt variants, a methodological model for our three-iteration prompt experiments.
- **Verification:** OpenAlex [W4394579747](https://openalex.org/W4394579747) (type: article); DOI resolves to JMIR (Crossref was rate-limited at check time).

**R24. Meshkin, H., Zirkle, J., Arabidarrehdor, G., Chaturbedi, A., Chakravartula, S., Mann, J., Thrasher, B., & Li, Z. (2024). Harnessing large language models' zero-shot and few-shot learning capabilities for regulatory research. *Briefings in Bioinformatics, 25*(5), Article bbae354.** DOI: [10.1093/bib/bbae354](https://doi.org/10.1093/bib/bbae354). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Empirical zero-shot versus few-shot comparison illustrating why SocioMathLLM reports separate zero-shot baselines and few-shot cues.
- **Verification:** OpenAlex [W4401798548](https://openalex.org/W4401798548) (type: article); Crossref registration confirmed (doi.org returns HTTP 403 to automated clients, not a missing DOI).

**R25. Beurer-Kellner, L., Fischer, M., & Vechev, M. (2023). Prompting Is Programming: A Query Language for Large Language Models. *Proceedings of the ACM on Programming Languages, 7*(PLDI), 1946–1969.** DOI: [10.1145/3591300](https://doi.org/10.1145/3591300). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Treats prompts as structured programs, supporting rigorous reporting and reproducibility of our prompt templates.
- **Verification:** OpenAlex [W4367185264](https://openalex.org/W4367185264) (type: article); Crossref registration confirmed (doi.org returns HTTP 403 to automated clients, not a missing DOI).

**R26. Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q. V., & Zhou, D. (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. In *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)*, 24824–24837.** DOI: [10.52202/068431-1800](https://doi.org/10.52202/068431-1800). **CONFERENCE PAPER — DOI ACTIVE**
- **Relevance [INFERENCE]:** Primary source for chain-of-thought prompting, the mechanism behind SocioMathLLM's CoT selection of candidate problems.
- **Verification:** OpenAlex [W7133224126](https://openalex.org/W7133224126) (type: conference-paper); DOI resolves to the Curran Associates proceedings record (Crossref was rate-limited at check time).

---

## Cluster 4 — LLM-as-judge, rubric design, interrater reliability (ICC), evaluation of generated text

**R27. Gu, J., Jiang, X., Shi, Z., Tan, H., Zhai, X., Xu, C., Li, W., Shen, Y., Ma, S., Liu, H.-Y., Wang, S., Zhang, K., Lin, Z., Zhang, B., Ni, L. M., Gao, W., Wang, Y., & Guo, J. (2026). A survey on LLM-as-a-judge. *The Innovation, 7*(6), Article 101253.** DOI: [10.1016/j.xinn.2025.101253](https://doi.org/10.1016/j.xinn.2025.101253). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Current review of LLM-based judging, needed to evaluate SocioMathLLM's LLM-as-judge scoring against teacher ratings.
- **Verification:** OpenAlex [W7120088840](https://openalex.org/W7120088840) (type: article); DOI resolves to ScienceDirect; publication year 2026 verified on publisher-indexed records (Crossref was rate-limited at check time).

**R28. Nadas, M. D. (2026). Large language models as judges: recent advances in LLM-based evaluation, critique, preference modeling, and feedback for text and code. *Artificial Intelligence Review, 59*(12), Article 279.** DOI: [10.1007/s10462-026-11652-0](https://doi.org/10.1007/s10462-026-11652-0). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Synthesizes judge reliability and bias issues that qualify the interpretation of our rubric-based scoring.
- **Verification:** OpenAlex [W7203980511](https://openalex.org/W7203980511) (type: article); DOI resolves to Springer; Crossref registration confirmed.

**R29. Crupi, G., Tufano, R., Velasco, A., Mastropaolo, A., Poshyvanyk, D., & Bavota, G. (2025). On the Effectiveness of LLM-as-a-Judge for Code Generation and Summarization. *IEEE Transactions on Software Engineering, 51*(8), 2329–2345.** DOI: [10.1109/TSE.2025.3586082](https://doi.org/10.1109/TSE.2025.3586082). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Provides empirical evidence on when LLM judges agree with human judgement, relevant to our human–LLM evaluation comparison.
- **Verification:** OpenAlex [W4412030659](https://openalex.org/W4412030659) (type: article); DOI resolves to IEEE Xplore document 11071936; Crossref registration confirmed.

**R30. Wang, R., Guo, J., Gao, C., Fan, G., Chong, C. Y., & Xia, X. (2025). Can LLMs Replace Human Evaluators? An Empirical Study of LLM-as-a-Judge in Software Engineering. *Proceedings of the ACM on Software Engineering, 2*(ISSTA), 1955–1977.** DOI: [10.1145/3728963](https://doi.org/10.1145/3728963). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Direct test of human–LLM judge agreement, supporting a cautious reading of SocioMathLLM's teacher/LLM dual evaluation.
- **Verification:** OpenAlex [W4411522868](https://openalex.org/W4411522868) (type: article); Crossref registration confirmed (doi.org returns HTTP 403 to automated clients, not a missing DOI).

**R31. Koo, T. K. K., & Li, M. Y. (2016). A Guideline of Selecting and Reporting Intraclass Correlation Coefficients for Reliability Research. *Journal of Chiropractic Medicine, 15*(2), 155–163.** DOI: [10.1016/j.jcm.2016.02.012](https://doi.org/10.1016/j.jcm.2016.02.012). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Standard reference for choosing and reporting ICC coefficients, exactly the statistic used for SocioMathLLM's teacher interrater results.
- **Verification:** OpenAlex [W2327037637](https://openalex.org/W2327037637) (type: article); DOI resolves to the journal site; Crossref registration confirmed.

**R32. ten Hove, D., Jorgensen, T. D., & van der Ark, L. A. (2024). Updated guidelines on selecting an intraclass correlation coefficient for interrater reliability, with applications to incomplete observational designs. *Psychological Methods, 29*(5), 967–979.** DOI: [10.1037/met0000516](https://doi.org/10.1037/met0000516). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Updated ICC guidance for incomplete rating designs, useful when teacher ratings of generated problems are not fully crossed.
- **Verification:** OpenAlex [W4294123474](https://openalex.org/W4294123474) (type: article); Crossref registration confirmed (doi.org returns HTTP 403 to automated clients, not a missing DOI).

**R33. Liljequist, D., Elfving, B., & Skavberg Roaldsen, K. (2019). Intraclass correlation — A discussion and demonstration of basic features. *PLoS ONE, 14*(7), Article e0219854.** DOI: [10.1371/journal.pone.0219854](https://doi.org/10.1371/journal.pone.0219854). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Explains what ICC variants measure, helping interpret the moderate ICC range reported for linguistic-complexity ratings.
- **Verification:** OpenAlex [W2963121203](https://openalex.org/W2963121203) (type: article); DOI resolves to PLOS (Crossref was rate-limited at check time).

**R34. Kumar, V., & Boulanger, D. (2020/2021). Automated Essay Scoring and the Deep Learning Black Box: How Are Rubric Scores Determined? *International Journal of Artificial Intelligence in Education, 31*(3), 538–584.** DOI: [10.1007/s40593-020-00211-5](https://doi.org/10.1007/s40593-020-00211-5). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Investigates how automated scoring reproduces rubric judgments, informing our rubric design and score-validation discussion.
- **Verification:** OpenAlex [W3087421864](https://openalex.org/W3087421864) (type: article; publication_year 2020, volume 31 issue 3 dated 2021); DOI resolves to Elsevier; Crossref registration confirmed.

**R35. Chang, Y., Wang, X., Wang, J., Wu, Y., Yang, L., Zhu, K., Chen, H., Yi, X., Wang, C., Wang, Y., Ye, W., Zhang, Y., Chang, Y., Yu, P. S., Yang, Q., & Xie, X. (2024). A Survey on Evaluation of Large Language Models. *ACM Transactions on Intelligent Systems and Technology, 15*(3), Article 22.** DOI: [10.1145/3641289](https://doi.org/10.1145/3641289). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Taxonomy of LLM evaluation dimensions and metrics, the context for our BLEU/METEOR/ROUGE-L/BLEURT/BERT comparison.
- **Verification:** OpenAlex [W4391136507](https://openalex.org/W4391136507) (type: article); Crossref registration confirmed (doi.org returns HTTP 403 to automated clients, not a missing DOI).

---

## Cluster 5 — Collaborative learning, mathematics socialization, collaborative problem solving

**R36. Esmonde, I. (2009). Ideas and Identities: Supporting Equity in Cooperative Mathematics Learning. *Review of Educational Research, 79*(2), 1008–1043.** DOI: [10.3102/0034654309332562](https://doi.org/10.3102/0034654309332562). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Foundational review of cooperative mathematics learning, grounding our treatment of SocioMathLLM's socialization competencies.
- **Verification:** OpenAlex [W2101188116](https://openalex.org/W2101188116) (type: article); Crossref registration confirmed (doi.org returns HTTP 403 to automated clients, not a missing DOI).

**R37. Isohätälä, J., Järvenoja, H., & Järvelä, S. (2016/2017). Socially shared regulation of learning and participation in social interaction in collaborative learning. *International Journal of Educational Research, 81*, 11–24.** DOI: [10.1016/j.ijer.2016.10.006](https://doi.org/10.1016/j.ijer.2016.10.006). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Explains socially shared regulation, a mechanism underlying collaboration and cooperation competencies in generated group problems.
- **Verification:** OpenAlex [W2556115049](https://openalex.org/W2556115049) (type: article; publication_year 2016, volume 81 dated 2017); DOI resolves to Elsevier; Crossref registration confirmed.

**R38. Cobb, P., Yackel, E., & Wood, T. (1992). Interaction and learning in mathematics classroom situations. *Educational Studies in Mathematics, 23*(1), 99–122.** DOI: [10.1007/BF00302315](https://doi.org/10.1007/BF00302315). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Classic socioconstructivist account of mathematical interaction, supporting the authenticity and socialization rationale of our target paper.
- **Verification:** OpenAlex [W1974157369](https://openalex.org/W1974157369) (type: article); DOI resolves to Springer; Crossref registration confirmed.

**R39. Lin, K.-Y., Yu, K.-C., Hsiao, H.-S., Chu, Y.-H., Chang, Y.-S., & Chien, Y.-H. (2015). Design of an assessment system for collaborative problem solving in STEM education. *Journal of Computers in Education, 2*(3), 301–322.** DOI: [10.1007/s40692-015-0038-x](https://doi.org/10.1007/s40692-015-0038-x). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Offers a CPS assessment design relevant to scoring the four socialization competencies in SocioMathLLM.
- **Verification:** OpenAlex [W873619677](https://openalex.org/W873619677) (type: article); DOI resolves to Springer; Crossref registration confirmed.

**R40. Turgut, S., & Turgut, İ. G. (2018). The Effects of Cooperative Learning on Mathematics Achievement in Turkey: A Meta-Analysis Study. *International Journal of Instruction, 11*(3), 663–680.** DOI: [10.12973/iji.2018.11345a](https://doi.org/10.12973/iji.2018.11345a). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Quantitative evidence that cooperative mathematics learning affects achievement, motivating generation of collaborative rather than individual problems.
- **Verification:** OpenAlex [W2811356578](https://openalex.org/W2811356578) (type: article); DOI resolves to the journal PDF; Crossref registration confirmed.

**R41. Ekström, S., Pareto, L., & Ljungblad, S. (2024). Teaching in a collaborative mathematic learning activity with and without a social robot. *Education and Information Technologies, 30*(1), 1301–1328.** DOI: [10.1007/s10639-024-12926-2](https://doi.org/10.1007/s10639-024-12926-2). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Empirical comparison of technology-mediated collaboration in mathematics education, a nearby example of the socialization setting we discuss.
- **Verification:** OpenAlex [W4401372949](https://openalex.org/W4401372949) (type: article); DOI resolves to Springer; Crossref registration confirmed.

**R42. Lazakidou, G., & Retalis, S. (2009/2010). Using computer supported collaborative learning strategies for helping students acquire self-regulated problem-solving skills in mathematics. *Computers & Education, 54*(1), 3–13.** DOI: [10.1016/j.compedu.2009.02.020](https://doi.org/10.1016/j.compedu.2009.02.020). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Links CSCL design to mathematics problem solving, relevant to transferring generated problems into collaborative classrooms.
- **Verification:** OpenAlex [W2095184141](https://openalex.org/W2095184141) (type: article; publication_year 2009, volume 54 issue 1 dated 2010); DOI resolves to Elsevier; Crossref registration confirmed (author transliteration checked against the publisher page).

---

## Cluster 6 — Graph-based context modelling and semantic query expansion (bridge to Topic 4)

**R43. Purwitasari, D., Maryamah, M., Mulia, S. K., & Adillion, I. G. (2025). Retrieval with Semantic Query Expansion Using Context-Based Graph Approaches. In *2025 International Electronics Symposium (IES)*, 777–782.** DOI: [10.1109/IES67184.2025.11160808](https://doi.org/10.1109/IES67184.2025.11160808). **CONFERENCE PAPER — DOI ACTIVE**
- **Relevance [INFERENCE]:** The assigned Topic 4 source: its context-graph query expansion is the method to map onto our prompt-context representation when comparing topics.
- **Verification:** OpenAlex [W4414463459](https://openalex.org/W4414463459) (type: conference-paper); DOI resolves to IEEE Xplore document 11160808; Crossref registration confirmed.

**R44. Azad, H. K., & Deepak, A. (2019). Query expansion techniques for information retrieval: A survey. *Information Processing & Management, 56*(5), 1698–1735.** DOI: [10.1016/j.ipm.2019.05.009](https://doi.org/10.1016/j.ipm.2019.05.009). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** General query-expansion taxonomy needed to explain how Topic 4's context graph differs from global and local expansion methods.
- **Verification:** OpenAlex [W2741307002](https://openalex.org/W2741307002) (type: article); DOI resolves to Elsevier (Crossref was rate-limited at check time).

**R45. Raza, M. A., Mokhtar, R. B., Noraziah, A., Pasha, M., & Pasha, U. (2019). A Taxonomy and Survey of Semantic Approaches for Query Expansion. *IEEE Access, 7*, 17823–17833.** DOI: [10.1109/ACCESS.2019.2894679](https://doi.org/10.1109/ACCESS.2019.2894679). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Semantic-expansion taxonomy (ontology, concept graph, word embeddings) used to classify the graph-based bridge method.
- **Verification:** OpenAlex [W2912157520](https://openalex.org/W2912157520) (type: article); DOI resolves to IEEE Xplore document 8625452; Crossref registration confirmed.

**R46. Jain, S., Seeja, K. R., & Jindal, R. (2021). A fuzzy ontology framework in information retrieval using semantic query expansion. *International Journal of Information Management Data Insights, 1*(1), Article 100009.** DOI: [10.1016/j.jjimei.2021.100009](https://doi.org/10.1016/j.jjimei.2021.100009). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Example of ontology-driven semantic expansion, a comparator for context-graph expansion in the cross-topic analysis.
- **Verification:** OpenAlex [W3134468011](https://openalex.org/W3134468011) (type: article); DOI resolves to Elsevier; Crossref registration confirmed.

**R47. ALMarwi, H., Ghurab, M., & Al-Baltah, I. A. (2020). A hybrid semantic query expansion approach for Arabic information retrieval. *Journal of Big Data, 7*(1), Article 39.** DOI: [10.1186/s40537-020-00310-z](https://doi.org/10.1186/s40537-020-00310-z). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Hybrid semantic expansion evidence showing how multiple expansion sources can be combined, analogous to combining image and text context.
- **Verification:** OpenAlex [W3037514716](https://openalex.org/W3037514716) (type: article); DOI resolves to Springer; Crossref registration confirmed.

**R48. Bounhas, I., Soudani, N., & Slimani, Y. (2019/2020). Building a morpho-semantic knowledge graph for Arabic information retrieval. *Information Processing & Management, 57*(6), Article 102124.** DOI: [10.1016/j.ipm.2019.102124](https://doi.org/10.1016/j.ipm.2019.102124). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Primary graph-construction method for semantic retrieval, directly bridging Topic 4's graph modelling with our prompt-context graph idea.
- **Verification:** OpenAlex [W2975214639](https://openalex.org/W2975214639) (type: article; publication_year 2019, volume 57 issue 6 dated 2020); DOI resolves to Elsevier; Crossref registration confirmed.

**R49. Ma, C., Chakrabarti, S., Khan, A., & Molnár, B. (2026). Knowledge Graph-based Retrieval-Augmented Generation for Schema Matching. *ACM Transactions on Knowledge Discovery from Data.* DOI: [10.1145/3862591](https://doi.org/10.1145/3862591). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Recent evidence that graph-grounded retrieval can structure LLM generation, supporting our proposed graph-to-prompt bridge.
- **Verification:** OpenAlex [W4406482986](https://openalex.org/W4406482986) (type: article); Crossref registration confirmed (doi.org returns HTTP 403 to automated clients, not a missing DOI).

**R50. Ghosh, S., & Mittal, G. (2025). Advancing engineering research through context-aware and knowledge graph–based retrieval-augmented generation. *Frontiers in Artificial Intelligence, 8*, Article 1697169.** DOI: [10.3389/frai.2025.1697169](https://doi.org/10.3389/frai.2025.1697169). **JOURNAL ARTICLE — DOI ACTIVE**
- **Relevance [INFERENCE]:** Combines context awareness with graph-based retrieval, the closest recent analogue to the cross-topic method synthesis we propose.
- **Verification:** OpenAlex [W4416402923](https://openalex.org/W4416402923) (type: article); DOI resolves to Frontiers; Crossref registration confirmed.

---

**Summary:** 50 unique entries, all with active verified DOIs — **43 peer-reviewed journal articles (OpenAlex type `article`) plus 1 peer-reviewed journal review = 44 journal publications with verified active DOIs** (exceeds the required 25), and 6 peer-reviewed conference papers with active DOIs; entries whose DOI could not be verified: **none** (eight publisher sites returned HTTP 403 to automated DOI-resolution requests, but Crossref registration metadata confirmed those DOIs are active).

## Cluster 7 — Coding-problem generation and collaborative debugging

These entries support the final paper direction recorded in `docs/SCOPE.md`. The full set of 30 DOI-verified works, including conference papers, is in `docs/research/coding-framework-fit.md`; the 12 journal articles/reviews are repeated here so the journal-count requirement remains auditable.

- **C01.** Jayathirtha, G., Fields, D. A., & Kafai, Y. B. (2024). Distributed debugging with electronic textiles. *Computer Science Education, 34*(4), 718-752. DOI: [10.1080/08993408.2023.2297738](https://doi.org/10.1080/08993408.2023.2297738). Empirical evidence on student pairs debugging together.
- **C02.** Kim, C., Vasconcelos, L., Belland, B. R., Umutlu, D., & Gleasman, C. (2022). Debugging behaviors of early childhood teacher candidates with or without scaffolding. *International Journal of Educational Technology in Higher Education, 19*(1), 26. DOI: [10.1186/s41239-022-00319-9](https://doi.org/10.1186/s41239-022-00319-9). Scaffolding changes debugging behaviour.
- **C03.** Hannay, J. E., Dybå, T., Arisholm, E., & Sjøberg, D. I. K. (2009). The effectiveness of pair programming: A meta-analysis. *Information and Software Technology, 51*(7), 1110-1122. DOI: [10.1016/j.infsof.2009.02.001](https://doi.org/10.1016/j.infsof.2009.02.001). Quantitative synthesis of pair work.
- **C04.** Hanks, B., Fitzgerald, S., McCauley, R., Murphy, L., & Zander, C. (2011). Pair programming in education: a literature review. *Computer Science Education, 21*(2), 135-173. DOI: [10.1080/08993408.2011.579808](https://doi.org/10.1080/08993408.2011.579808). Basis for collaboration criteria in a debugging rubric.
- **C05.** Hannay, J. E., Arisholm, E., Engvik, H. A., & Sjøberg, D. I. K. (2009). Effects of personality on pair programming. *IEEE Transactions on Software Engineering, 36*(1), 61-80. DOI: [10.1109/TSE.2009.41](https://doi.org/10.1109/TSE.2009.41). Motivation for pair-profile personalization.
- **C06.** Indriasari, T. D., Luxton-Reilly, A., & Denny, P. (2020). A review of peer code review in higher education. *ACM Transactions on Computing Education, 20*(3), 1-25. DOI: [10.1145/3403935](https://doi.org/10.1145/3403935). Peer review as educational socialization.
- **C07.** Wang, Y., Li, H., Feng, Y., Jiang, Y., & Liu, Y. (2012). Assessment of programming language learning based on peer code review model. *Computers & Education, 59*(2), 412-422. DOI: [10.1016/j.compedu.2012.01.007](https://doi.org/10.1016/j.compedu.2012.01.007). Learning-outcome evidence for peer review.
- **C08.** Indriasari, T. D., Denny, P., Lottridge, D. M., & Luxton-Reilly, A. (2022). Gamification improves the quality of student peer code review. *Computer Science Education, 33*(3), 458-482. DOI: [10.1080/08993408.2022.2124094](https://doi.org/10.1080/08993408.2022.2124094). Review quality is measurable.
- **C09.** Sabarinath, R., & Quek, C. L. G. (2020). Programming students' peer review of codes and their perceptions of the online learning environment. *Education and Information Technologies, 25*(5), 3553-3575. DOI: [10.1007/s10639-020-10111-9](https://doi.org/10.1007/s10639-020-10111-9). Learner acceptance of review prompts.
- **C10.** Kang, S., Chen, B., Yoo, S., & Lou, J.-G. (2024/2025). Explainable automated debugging via large language model-driven scientific debugging. *Empirical Software Engineering, 30*(2), 45. DOI: [10.1007/s10664-024-10594-x](https://doi.org/10.1007/s10664-024-10594-x). Source of rubric dimensions for justification.
- **C11.** Levin, K. H., van Kempen, N., Berger, E. D., & Freund, S. N. (2025). ChatDBG: Augmenting debugging with large language models. *Proceedings of the ACM on Software Engineering, 2*(FSE), 1892-1913. DOI: [10.1145/3729355](https://doi.org/10.1145/3729355). Debugging as a tool-supported practice.
- **C12.** Hou, X., Zhao, Y., Liu, Y., Yang, Z., Wang, K., Li, L., Luo, X., Lo, D., Grundy, J., & Wang, H. (2024). Large language models for software engineering: A systematic literature review. *ACM Transactions on Software Engineering and Methodology, 33*(8), 1-79. DOI: [10.1145/3695988](https://doi.org/10.1145/3695988). Broad anchor for LLM use in code tasks.

**Updated count:** 44 journal publications from clusters 1-6 plus 12 journal articles from cluster 7 = 56 journal references with active DOIs. All DOIs were verified on 2026-11-23 as recorded in `docs/research/coding-framework-fit.md` and the entries above.
