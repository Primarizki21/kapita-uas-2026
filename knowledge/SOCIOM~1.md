IEEE TRANSACTIONS ON LEARNING TECHNOLOGIES, VOL. 19, 2026                                                                                                      271




    SocioMathLLM: A Multimodal Large Language
      Model Framework for Generating Authentic
   Mathematical Word Problems Driving Socialization
                                                  Wu-Yuin Hwang              and Ika Qutsiati Utami


   Abstract—Large language models (LLMs) have demonstrated                         the application function of mathematics [3]. Beyond this, MWPs
significant advancements in automatic question generation (AQG),                   have been employed to engage students’ interest in mathematics,
contributing to enhanced learning and teaching efficiency by fa-                   nurture creative thinking, enhance problem-solving strategies,
cilitating the creation of human-like educational content and as-
sessment materials. However, in mathematics education, where                       and facilitate the acquisition and development of new mathemat-
generating extensive sets of math word problems (MWPs) requires                    ical concepts and skills [4]. However, designing effective MWPs
significant time and effort, the use of LLMs to design tasks that                  remains a significant challenge for educators. Creating many
foster socialization competencies such as group collaboration, coop-               high-quality MWPs that are contextually rich, pedagogically
eration, negotiation, and ideas-sharing among students remains un-
                                                                                   sound, and appropriately aligned with curricular goals requires
explored. This study makes the first attempt to develop a specialized
multimodal LLM framework, SocioMathLLM, which integrates                           both time and expertise [5], [6]. Teachers often face difficulties
an innovative prompt engineering strategy to incorporate multi-                    in generating diverse problem sets that address varying levels of
modal authentic contextual information (text and image), group                     student ability while maintaining authenticity and relevance [7],
background information, and socialization criteria (i.e., group size,              [8].
task nature, social goal, social frequency, social-quality, interaction
                                                                                      Recent advancements in large language models (LLMs) have
quantity, and social interdependency) to generate MWPs aimed
at fostering group socialization. SocioMathLLM was evaluated                       opened new opportunities to address this issue through au-
through automatic metrics, human evaluation, and LLM-based                         tomatic MWPs generation. LLMs can leverage vast amounts
evaluation. The automatic evaluation result demonstrates good                      of linguistic and mathematical knowledge to create varied,
performance in generating MWPs that promote socialization with                     context-specific, and adaptive word problems on a scale [9].
an average precision of 0.906, recall of 0.943, and F1 score of 0.925.
                                                                                   Their ability to integrate contextual details, adjust complexity,
A total of 100 evaluation cases by humans and LLM also validated
the robustness of SocioMathLLM, highlighting its potential for                     and produce personalized content has made them a promising
application in collaborative mathematics learning and assessment                   tool for supporting teachers and enhancing students’ learning
contexts.                                                                          experiences [10]. While these methods hold great promise,
  Index Terms—Authentic math word problems (MWPs),                                 they still face challenges for effective application in fostering
automatic question generation (AQG), education, large language                     mathematics socialization [11]. Within the mathematics edu-
model (LLM), multimodality, socialization, technology.                             cation research community, there is currently no consensus on
                                                                                   how to conceptualize the use of LLMs to drive collaboration,
                            I. INTRODUCTION                                        cooperation, negotiation, and idea-sharing as part of the social-
                                                                                   ization competencies in mathematics [12], [13]. However, from
        ATHEMATICAL word problems (MWPs) constitute an
M       important part of mathematics education worldwide [1],
[2]. Historically, they have been designed to serve multiple
                                                                                   a sociocultural perspective, mathematics learning is not only
                                                                                   an individual cognitive process but also a socially mediated
                                                                                   activity shaped by language, interaction, and participation in
purposes, with one of the most significant being to bridge                         mathematical practices [14], [15]. Addressing this gap is crucial
classroom learning and real-world contexts through applied                         to ensure that LLM-generated MWPs support not only individ-
problem solving and mathematical modeling, thereby fostering                       ual problem-solving but also the collaborative construction of
                                                                                   mathematical understanding.
  Received 27 August 2025; revised 16 January 2026 and 4 March 2026;                  This article develops an innovative multimodal framework
accepted 22 March 2026. Date of publication 24 March 2026; date of current
version 10 April 2026. (Corresponding author: Ika Qutsiati Utami.)                 for generating MWPs to drive group socialization called So-
  Wu-Yuin Hwang is with the Department of Computer Science and Information         cioMathLLM. It integrates three modules: 1) a multimodal
Engineering, National Dong Hwa University, Hualien 974, Taiwan, and also           contextualization module for extracting authentic contextual
with the Graduate Institute of Network Learning Technology, National Central
University, Taoyuan 320, Taiwan (e-mail: wyhwang1206@gmail.com).                   information from images and translating it into textual data;
  Ika Qutsiati Utami is with the Data Science Technology, Engineering De-          2) a personalization module for processing diverse group back-
partment, Faculty of Advanced Technology and Multidiscipline, Universitas          ground information; and 3) a socialization module for producing
Airlangga, Surabaya 60115, Indonesia, and also with the Graduate Institute
of Network Learning Technology, National Central University, Taoyuan 320,          MWPs for four different socialization competencies, includ-
Taiwan (e-mail: ika.q.utami@ftmm.unair.ac.id).                                     ing collaboration, cooperation, negotiation, and ideas-sharing.
  Digital Object Identifier 10.1109/TLT.2026.3677266                               The contribution of this study lies in the development of a
      1939-1382 © 2026 IEEE. All rights reserved, including rights for text and data mining, and training of artificial intelligence and similar technologies.
Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.


            Authorized licensed use limited to: Universitas Airlangga. Downloaded on May 04,2026 at 03:23:10 UTC from IEEE Xplore. Restrictions apply.
272                                                                                      IEEE TRANSACTIONS ON LEARNING TECHNOLOGIES, VOL. 19, 2026



SocioMathLLM framework that integrates multimodal authen-                      across different subject domains [21]. Moreover, within a socio-
tic contextual information, group background information, and                  cultural perspective, learning mathematics involves participa-
socialization criteria to facilitate automatic generation of MWP               tion in certain established mathematics cultural practices [22].
for driving group socialization.                                               Consequently, the types of communication, as well as activities
   In addition, conducting evaluations in automatic genera-                    in which teachers involve students, such as collaboration and
tion of MWP is crucial because it ensures that the generated                   cooperation, influence the cultural meanings about mathemat-
MWPs are accurate, meaningful for improving mathematical                       ics that students develop [23]. Furthermore, in mathematics
socialization, pedagogically valuable, and suitable for the tar-               problem-solving, communication is important in developing
get audience. In this study, first, we conducted a comparison                  mathematical understanding [15]. From a sociocultural perspec-
analysis between our proposed approach and the zero-shot                       tive, students who share their reasoning about ideas with others
prompting method for MWP generation, driving socialization                     (ideas-sharing) and listen to others share their thinking create an
to scientifically validate the effectiveness and reliability of our            understanding of culturally established mathematical practices
approach. Second, we reported a more comprehensive eval-                       [24]. The Principles and Standards for School Mathematics also
uation of our proposed framework using automatic metrics,                      identified the importance of communication in the learning and
human evaluation, and LLM-based evaluation. Then, we exam-                     understanding of mathematics [25]. Through communication,
ine whether the generated questions reflect group background                   ideas become objects of reflection, refinement, discussion, and
information to guarantee personalization and contextual fit of                 amendment [26]. Moreover, based on Vygotsky’s theories in
the MWP. Three research questions are addressed in this study as               mathematics education, communication is a cultural tool, and
follows.                                                                       language is a human instrument of communication [14]. Indi-
   1) What are the differences in terms of quality of the gen-                 viduals come to learn the meanings of a culture by internalizing
       erated MWPs using SocioMathLLM compared to the                          the meanings and being transformed by them as they learn to
       zero-shot approach?                                                     speak the language of the culture. Thus, students create their
   2) What are the results of automatic evaluation, human eval-                own knowledge and develop mathematical meanings as they
       uation, and LLM-based evaluation of SocioMathLLM in                     learn to explain and justify their thinking to others. As they learn
       generating MWPs driving socialization?                                  to speak mathematical language, they transform their thinking
   3) Can the proposed SocioMathLLM create MWPs driving                        into mathematical concepts. Mathematical language comes from
       socialization that align with the specific group background             society, and thought (concept) comes from the individual [15].
       information?                                                               In addition, according to social cognitive theory (SCT), in-
                                                                               dividuals form their self-efficacy beliefs by interpreting infor-
                     II. LITERATURE REVIEW                                     mation from four sources: mastery experience, vicarious expe-
                                                                               rience, social persuasions, and physiological or affective states
A. Socio-Cultural and Socio-Cognitive Perspective of                           [27]. Furthermore, in the social cognitive theoretical framework,
Mathematics                                                                    human functioning is viewed as the product of the reciprocal
   Socialization refers to the process of entering a new social                influences of personal, behavioral, and environmental determi-
context and acquiring knowledge, skills, and behavior to act in                nants. A person’s abilities could be physically and psycholog-
and become part of this context [16]. Socialization can enable                 ically different from each other due to their growth environ-
groups to develop the appropriate attitude and action for knowl-               ment and social practices. SCT emphasized the bidirectional
edge transfer in collaboration with partners [17]. This process                influence between personal, environmental factors, and behavior
is critical for the development of personal identity and social                [28]. Mathematics socialization remains under-theorized and
interactions [18]. Literature has also considered the important                under-researched in mathematics education [29]. Few studies
role of peer groups in socialization, elucidating how children                 have specifically investigated mathematical socialization [19].
establish shared understandings, negotiate rules and identities,               According to Barwell [30], socialization is usually considered in
and create friendships and peer culture within their activities                terms of communicative and interactive activities. Mathematics
[16]. According to Vygotsky, human beings learn and grow                       socialization encompasses the experiences that individuals and
within a specific historical and cultural environment [17]. This               groups have within various mathematical contexts [31]. These
is why human learning should be understood in the context                      interactions at school, at home, or in the community reinforce or
of the social and cultural environment in which they exist.                    discourage meaningful mathematical interactions. It is through
Children first learn from social activities and then internalize               these experiences that learners come to hold beliefs and expecta-
them into their own mental structures. Among other things,                     tions regarding their ability to perform in mathematical contexts.
socialization events provide possibilities to share explanations               While students are learning mathematics, they are also learning
of mathematical thinking [19].                                                 how it is defined, how valuable it is, how it is to be learned, who
   In addition, students’ socialization can be promoted through                should learn it, and what mathematical reasoning requires [4].
collaborative and cooperative learning, and to achieve this, how
teachers design and organize mathematics tasks to facilitate col-
                                                                               B. Potential of Prompt Engineering for LLMs in Automatic
laboration and cooperation is particularly important [17]. Coop-
                                                                               Question Generation (AQG)
eration has become the theme of social development nowadays
[20]. Cooperative learning is widely recognized as a pedagogical                 AQG is the process of generating syntactically fluent and
practice that promotes learning and socialization among students               semantically relevant questions from an input context [32].
        Authorized licensed use limited to: Universitas Airlangga. Downloaded on May 04,2026 at 03:23:10 UTC from IEEE Xplore. Restrictions apply.
HWANG AND UTAMI: SOCIOMATHLLM: A MULTIMODAL LLM FRAMEWORK FOR GENERATING AUTHENTIC MWP DRIVING SOCIALIZATION                                           273



Historically, research in question generation relied heavily on                                                TABLE I
                                                                                                EXISTING PROMPT ENGINEERING TECHNIQUES
rule-based methods [3]. These approaches utilized hand-written
rules, linguistic features (such as Part-of-Speech) tags, entities,
and syntax labels), and language resources (e.g., WordNet) that
necessitated a deep understanding of linguistics [33]. Rule-based
AQG methods often focus on transforming declarative sentences
into questions using syntactic patterns and semantic constraints.
While effective to some extent, these methods required exten-
sive manual effort and expertise, limiting their scalability and
adaptability to diverse educational content. Shifting focus to
the broader applications of LLMs in education, these models
have revolutionized the field with their vast capabilities [34].
LLMs are an evolution of pretrained language models (PLMs)
with much larger model sizes, significantly more data, and much
longer training times. In addition to improved performance on
downstream tasks, LLMs demonstrate novel capabilities (emer-
gent abilities), such as in-context learning, instruction following,
and step-by-step reasoning [35]. With these new abilities, their
usage has become widespread, particularly in the field of edu-
cation.
   For instance, ChatGPT, one of the most prominent tools pow-
ered by LLMs, has been shown to support teachers in designing
instructional materials, lesson outlines, and classroom activities
[36]. On a broader scale, it can generate a complete course
syllabus [37]. At a more detailed level, the tool can leverage
its extensive knowledge base to create targeted lesson plans and
tailored learning tasks [38]. According to Topsakal and Topsakal
                                                                                goals [43]. In the context of MWP generation, prompt engi-
[39], ChatGPT can also be used to generate conversational dia-
                                                                                neering has been shown to increase the mathematical validity,
logues that facilitate foreign language learning. Zhai [40] further
                                                                                contextual relevance, and cognitive demand of the problems
illustrated its application in designing assessments aligned with
                                                                                produced, reducing common issues such as unsolvable tasks [7].
specific performance standards. In addition, Abdelghani et al.
                                                                                Furthermore, the effective prompt design is not only a technical
[41] utilized GPT-3 to provide prompts that stimulated primary
                                                                                optimization but also a pedagogical tool, enabling educators and
school students’ question-asking abilities. Collectively, these
                                                                                researchers to steer LLM outputs toward curriculum-aligned and
studies emphasize the broad capabilities of LLMs in education,
                                                                                learner-centered outcomes [44]. Table I summarizes the existing
ranging from content and activity generation to feedback provi-
                                                                                prompt engineering techniques for improving output quality by
sion and assessment design.
                                                                                LLM.
   More specifically, within the domain of automatic MWP
generation, recent studies have explored the application of LLMs
to design, adapt, and refine problem statements for educa-                               III. PROPOSED FRAMEWORK: SOCIOMATHLLM
tional purposes. For example, some researchers have employed                       In the present study, we generated MWPs for driving four
LLMs to automatically generate MWPs with varying levels                         different socialization competencies (i.e., collaboration, coop-
of difficulty, enabling alignment with students’ grade levels                   eration, negotiation, and ideas-sharing) by instructing the LLM
and cognitive abilities [2], [7], [8]. Others have examined the                 with four prompt strategies, each differing in socialization skill
capacity of LLM models to improve the linguistic quality and                    criteria. These prompts followed specific techniques and gen-
contextual authenticity of problems, ensuring that tasks are not                eration criteria derived from the literature review and expert
only mathematically valid but also engaging and accessible [34],                review. The proposed prompt engineering method to generate
[42]. Collectively, this body of work highlights the potential of               MWPs for driving socialization mainly has three modules (see
LLMs in automating MWP generation, with implications for                        Fig. 1). In the contextualization module, the prompt encouraged
scaling instructional resources and supporting adaptive learning                the model to generate five candidates of MWPs as the original
environments.                                                                   base of the problem. To ensure the outputs were relevant to
   Moreover, an emerging line of research emphasizes the role                   geometry topics, we embedded authentic contextual information
of prompt engineering techniques in enhancing the quality of                    directly related to 2-D geometric shapes, including their real-
question generation with LLMs. By carefully designing prompts                   world measurement properties such as length and width. The
through methods such as chain-of-thought (CoT) prompting,                       prompts incorporated multimodal contextual information, such
few-shot exemplars, or role-based instructions, researchers have                as annotated diagrams and real-life photographs of objects such
been able to improve not only the grammaticality and clarity of                 as tiles, windows, or playgrounds, to strengthen the connection
generated questions but also their alignment with pedagogical                   between abstract geometric concepts and tangible experiences.

          Authorized licensed use limited to: Universitas Airlangga. Downloaded on May 04,2026 at 03:23:10 UTC from IEEE Xplore. Restrictions apply.
274                                                                                        IEEE TRANSACTIONS ON LEARNING TECHNOLOGIES, VOL. 19, 2026




Fig. 1.   Proposed SocioMathLLM framework.




Fig. 2.   Example of image data and the corresponding authentic contextual information.




For example, a problem might include an image of a classroom                     proper alignment with real-world applications. In this module,
floor plan with labeled dimensions or a photo of a triangular gar-               the prompts were augmented with zero-shot instructions to make
den with a value of side lengths, prompting students to apply ge-                the LLM generate problems without relying on pre-existing
ometric reasoning in realistic contexts. To enhance authenticity,                examples, thereby testing its ability to construct authentic MWPs
in this stage, the prompts were designed around scenarios from                   from context alone. These zero-shot prompts explicitly guided
students’ daily lives, ensuring the tasks were meaningful and                    the model to embed real-world scenarios, measurement data, and
situated in familiar environments (see Fig. 2). We also integrated               everyday objects into the problem statement. When combined
a set of explicit rules for LLM to ensure contextual accuracy and                with multimodal inputs such as labeled images of geometric

          Authorized licensed use limited to: Universitas Airlangga. Downloaded on May 04,2026 at 03:23:10 UTC from IEEE Xplore. Restrictions apply.
HWANG AND UTAMI: SOCIOMATHLLM: A MULTIMODAL LLM FRAMEWORK FOR GENERATING AUTHENTIC MWP DRIVING SOCIALIZATION                                           275



objects, the zero-shot approach encouraged the LLM to infer                                                   TABLE II
                                                                                        DEVELOPED CRITERIA USED TO GENERATE AND EVALUATE THE
spatial relationships and measurement properties autonomously.                              AUTHENTICITY AND LINGUISTIC ASPECTS OF MWPS
This design ensured that the resulting geometry MWPs were
not only mathematically accurate but also contextually rich,
grounded in authentic environments familiar to students.
   In the personalization module, we provide a persona of two
students in one group to the LLM prompt by giving their back-
ground information, such as group size, gender, socio-economic
status, cognitive level, reading comprehension level, mathe-
matics response time, demographic data, and their learning
progress. This personalization ensured that the generated MWPs
were tailored to the students’ educational needs and cognitive
characteristics. At this stage, the five candidate MWPs produced
in the first stage were fed back into the model along with CoT
prompting instructions. The LLM was guided to review each                                                    TABLE III
                                                                                        DEVELOPED CRITERIA USED TO GENERATE AND EVALUATE THE
candidate systematically, evaluating them against key mathe-                                       MATHEMATICAL ASPECT OF MWPS
matics criteria, such as problem answerability, structure and
clarity, supporting multiple solution strategies, and alignment
with students’ background information. Through step-by-step
reasoning, the model compared the five options and selected the
single best MWP to advance to the next stage of refinement.
This CoT-based evaluation process increased the quality and
educational relevance of the final problem while ensuring it was
both context-sensitive and pedagogically appropriate.
   In the socialization module, the most suitable candidate of
MWP selected from the previous stage was used as the basis for
a redesign and modification process. The personalized problem
was refined to align with targeted socialization competencies,
                                                                                realistic, and aligned with the intended educational outcomes,
specifically collaboration, cooperation, negotiation, and idea-
                                                                                we consulted with experts for feedback and validation. The
sharing. To achieve this, we developed four distinct prompts,
                                                                                criteria were also subjected to iterative review and refinement,
each embedding a clear definition and explicit criteria for one
                                                                                allowing for adjustments based on emerging insights and evolv-
of the socialization skills. These prompts served as structured
                                                                                ing instructional needs. This systematic approach ensured that
guidelines for the LLM, ensuring that the generated MWPs could
                                                                                the LLM-generated MWPs were both pedagogically sound and
elicit the intended type of group interaction. To further enhance
                                                                                effective in promoting socialization competencies.
the quality of interactional discourse, we employed a few-shot
prompting method that provided the LLM with examples of
instructional hints directed at students. The few-shot prompt-                                                 IV. METHOD
ing demonstrated how to guide students to interact effectively                     Our study consists of two parts. We use modern LLMs
during problem-solving. These instructions included prompts                     for generating MWPs automatically in the first part through
for exchanging ideas, dividing tasks, justifying reasoning, and                 various prompting strategies. Training a language model from
coconstructing solutions collaboratively. By learning from these                scratch or fine-tuning the available models is expensive due to
structured instructional patterns, the LLM was able to generate                 constraints in the availability of educational data and the cost
MWPs that incorporated clear guidance, encouraging students to                  associated with training. Therefore, in this study, MWPs for
engage in meaningful interaction. This combination of explicit                  driving socialization were generated using the GPT-4o model
socialization criteria and few-shot instructional cues ensured that             developed by OpenAI through its official API. The deployment
the final MWPs supported both mathematical reasoning and the                    process involved designing structured prompts that explicitly
development of socialization skills. Fig. 3 shows the details of                specified mathematical topics integrated with authenticity crite-
the proposed prompt design, and Fig. 5 shows an example of the                  ria, student background characteristics, contextual constraints,
generated MWPs.                                                                 linguistic requirements, and targeted socialization objectives.
   Furthermore, in this study, we designed a set of well-defined                These prompts were programmatically submitted to the GPT-4o
criteria to guide the LLM in generating meaningful MWPs that                    model via secure API calls, enabling automated and scalable
foster socialization skills (see Tables II, III, and XI). The criteria          batch generation of MWPs. The overall system architecture
development process began by clearly articulating the goals                     incorporated input validation mechanisms, prompt templating,
and learning objectives for integrating social interaction into                 response parsing, and postprocessing steps to ensure mathe-
mathematical problem-solving. After that, we identified key fac-                matical coherence, contextual relevance, and alignment with
tors influencing these objectives through an extensive review of                predefined socialization outcomes. No additional fine-tuning
relevant literature. To ensure that each criterion was measurable,              was conducted; instead, the model leveraged its pretrained

          Authorized licensed use limited to: Universitas Airlangga. Downloaded on May 04,2026 at 03:23:10 UTC from IEEE Xplore. Restrictions apply.
276                                                                                        IEEE TRANSACTIONS ON LEARNING TECHNOLOGIES, VOL. 19, 2026




Fig. 3.   Proposed prompt design.



knowledge to generate contextually grounded and pedagogically                    reliability using the Intraclass Correlation Coefficient (ICC)
appropriate problems. MWPs were generated using default API                      between human evaluation conducted by mathematics teachers
parameters (temperature = 1, top_p = 1, frequency penalty = 0,                   and LLM-based evaluation.
and presence penalty = 0), allowing balanced creativity while
maintaining response stability, consistency, and completeness.                   A. Developed Criteria
Each prompt was executed in three iterations, and the generated
                                                                                    In this study, we developed different criteria derived from a
outputs were compared to assess consistency and alignment with
                                                                                 literature review and expert review to instruct LLM to generate
the intended socialization objectives. The MWPs driving social-
                                                                                 meaningful output for MWPs driving socialization. There are
ization were generated for an elementary school-level geometry
                                                                                 three established criteria, including authenticity and linguistics
course comprising topics ranging from single 2-dimensional
                                                                                 (see Table II), mathematics (see Table III), and socialization (see
(2-D) shapes, such as rectangles, squares, triangles, parallel-
                                                                                 Table XI).
ograms, and trapezium to compound 2-D shapes. We provide
domain-specific information or context on these topics to the
LLM model for problem generation.                                                B. Evaluation Metrics
   In the second part, we perform automatic evaluations using au-                   To assess the quality of the generated MWPs designed
tomatic metrics, human evaluation, and LLM-based evaluation                      to foster socialization, we employed a combination of auto-
to assess the quality of generated MWPs driving socialization.                   matic evaluation, human evaluation, and LLM-based evaluation.
We also conducted statistical tests to examine the interrater                    For automatic assessment, we applied several metrics such as
          Authorized licensed use limited to: Universitas Airlangga. Downloaded on May 04,2026 at 03:23:10 UTC from IEEE Xplore. Restrictions apply.
HWANG AND UTAMI: SOCIOMATHLLM: A MULTIMODAL LLM FRAMEWORK FOR GENERATING AUTHENTIC MWP DRIVING SOCIALIZATION                                          277



BLEU (Bilingual Evaluation Understudy), METEOR, ROUGE-                                                         TABLE IV
                                                                                                        PERFORMANCE COMPARISON
L, BLEURT, and BERT-based semantic similarity metrics using
precision, recall, and F1-score to measure linguistic and con-
textual alignment between the generated MWPs and reference
problems. BLEU scores provided insights into the lexical preci-
sion of the generated text, while BERT-based evaluation offered
a deeper semantic analysis, capturing meaning beyond surface-
level word overlap. In addition, METEOR, ROUGE-L, and
BLEURT are complementary automatic evaluation metrics used
to assess the quality of generated problems by measuring lexical
overlap (METEOR), structural similarity (ROUGE-L), and se-
                                                                                                          TABLE V
mantic similarity and overall generation quality (BLEURT) be-                   PERFORMANCE COMPARISON BETWEEN WITH AND WITHOUT THE PROPOSED
tween generated outputs and reference problems. Complement-                                  METHOD USING LLM-BASED EVALUATION
ing these automated methods, we conducted a human evaluation
by employing five mathematics teachers as raters who assessed
each MWP against a rubric developed in this study. All teachers
had more than five years of experience teaching mathematics,
including geometry instruction, MWPs design, and facilitation
of group-based learning. Before scoring, they attended an ori-
entation session on the evaluation rubric, covering the scoring
criteria and example cases. The raters then completed a calibra-
tion activity by independently scoring a shared set of sample
problems and discussing their results to align interpretations.
During the main evaluation, rating disagreements were resolved
through structured discussion and reference to the rubric until
consensus was achieved. The rubric is derived from the criteria
in Tables II, III, and XI. Each problem was scored on a 5-point
scale, and ICC was calculated to ensure consistency across eval-
uators. We also implemented an LLM-based evaluation, where
the LLM, instructed with our developed criteria, reviewed and
scored the generated MWPs. This process leveraged the LLM’s
ability to perform comparative judgments and reason through
the alignment of each problem with socialization competencies.
The combination of automatic metrics, human expert review,
and LLM-based evaluation provided a triangulated assessment
approach, ensuring the performance of the proposed method and
the educational effectiveness of the generated MWPs.

                  V. RESULT AND DISCUSSION
A. RQ1. What are the Differences in Terms of Quality of the
Generated MWPs Using SocioMathLLM Compared to the
                                                                               in n-gram overlap with reference texts. Using a BERT-based
Zero-Shot Approach?                                                            semantic metric, we also observed improvements in precision
   In this study, we conducted a comparative analysis of the                   (0.859 to 0.906, +0.047), recall (0.778 to 0.943, +0.165), and F1
LLM-generated MWPs produced with and without our pro-                          (0.817 to 0.925, +0.108). The particularly large gain in BERT
posed method. We analyze the quality of the generated MWPs                     recall suggests SocioMathLLM produces output that covers
driving socialization by comparing the proposed method with                    substantially more of the reference content, while the increase in
the zero-shot prompting method using automatic metrics and                     precision indicates fewer irrelevant or incorrect elements. Fur-
LLM-based evaluation across four dimensions, i.e., authenticity                thermore, SocioMathLLM achieves higher ROUGE-L scores
and linguistics, mathematics, personalization, and socialization.              (0.570 compared with 0.124) and METEOR scores (0.665 com-
Each criterion is rated by LLM on a scale of 1 to 5. In addition,              pared with 0.076), indicating notable improvements in structural
the researchers assist in validating the evaluations performed                 coherence and lexical alignment with the reference problems.
by LLMs. The result of automatic evaluation comparison in                      In addition, the BLEURT score is higher for SocioMathLLM
Table IV indicates that SocioMathLLM substantially outper-                     (0.485 compared with 0.343), suggesting enhanced semantic
formed the zero-shot baseline across both surface-level and                    similarity and overall generation quality. Collectively, these
semantic evaluation metrics. On BLEU, the model’s score in-                    results demonstrate the effectiveness of the proposed approach
creased from 0.002 to 0.408, indicating a large improvement                    in generating better-quality MWPs than zero-shot prompting.

         Authorized licensed use limited to: Universitas Airlangga. Downloaded on May 04,2026 at 03:23:10 UTC from IEEE Xplore. Restrictions apply.
278                                                                                      IEEE TRANSACTIONS ON LEARNING TECHNOLOGIES, VOL. 19, 2026



                           TABLE VI                                            MWPs differ substantially from the reference text. This is not
EVALUATION METRICS RELATING TO THE QUALITY OF THE MWP GENERATED
BY THE PROPOSED MODELS (CONSIDERING CONTEXTUAL INFORMATION AND
                                                                               unexpected for open-ended tasks such as MWP generation for
                 THE ORIGINAL GENERATED MWP)                                   socialization, where semantic equivalence is often more impor-
                                                                               tant than literal word matching. BLEU is an automatic metric
                                                                               used to evaluate the similarity between generated text and refer-
                                                                               ence texts. It is computed by measuring the overlap of n-grams
                                                                               (continuous sequences of words) between the generated text
                                                                               and the reference, typically using precision scores for unigrams,
                                                                               bigrams, trigrams, and four-grams. The BLEU score ranges from
                                                                               0 to 1, with higher scores indicating greater similarity to the
                                                                               reference text. In the context of MWP generation, BLEU pro-
                                                                               vides a reproducible way to assess the linguistic and structural
   The LLM-based evaluation comparison in Table V also in-                     consistency of model outputs. While it does not capture the
dicates that applying our criteria and prompting strategies led                semantic correctness or pedagogical quality of problems fully,
to problems that were more contextually authentic, more con-                   it complements human evaluation by quantifying how reliably
textualized, and required a higher level of reasoning with better              the model generates problems that follow the intended patterns
engagement. Zero-shot problems tend to be simpler and discon-                  and structures necessary to drive socialization in collaborative
nected from realistic contexts (x̄ = 2.790). Furthermore, both                 learning. In such contexts, BLEU scores tend to underestimate
methods create answerable and structurally clear problems, but                 quality when surface forms vary. However, the BERT scores
the SocioMathLLM outperforms in supporting multiple solution                   show a high degree of semantic similarity between the generated
paths (x̄ = 4.890) and cognitive demand (x̄ = 4.620), which is                 and reference MWPs. The precision score (0.853) indicates
crucial for open-ended discussion and higher order mathematical                that most of the content in the generated MWPs is relevant
thinking. Furthermore, SocioMathLLM provides MWPs that                         and matches well with contextual information as the reference.
are more meaningful and offer greater linguistic richness and                  Recall score (0.906) suggests that the generated MWPs captured
appropriate math challenges, whereas zero-shot problems are                    almost all the important contextual information as input. In
overly simplistic and less personalized. In terms of scope person-             addition, the F1 score (0.879) balances both precision and recall,
alization, SocioMathLLM achieved a substantially higher mean                   affirming that the generated MWPs are not only semantically rel-
score (x̄ = 4.590) compared to zero-shot prompting (x̄ = 1.580),               evant but also consistently aligned with the intent and structure
indicating its capability to produce MWPs tailored to learners’                of the input information. The low standard deviations (in the
backgrounds and contexts. Regarding linguistic complexity, So-                 range 0.01–0.013) across BERT metrics further indicate stable
cioMathLLM also performed better (x̄ = 4.290), suggesting                      performance across examples, showing the model generates se-
that it generates problems with richer and more contextually                   mantically consistent MWPs. Furthermore, the mean ROUGE-L
appropriate language structures. Similarly, for mathematical                   score of 0.465 indicates consistent structural alignment with the
complexity, SocioMathLLM obtained a higher mean score (x̄                      reference texts, while the mean METEOR score of 0.562 reflects
= 3.810) than zero-shot prompting (x̄ = 2.960), reflecting its                 stable lexical similarity across instances. The mean BLEURT
effectiveness in crafting problems with more suitable mathe-                   score suggests comparatively consistent semantic quality among
matical depth and challenge.                                                   the generated outputs. Overall, these results indicate that the
   Most importantly, SocioMathLLM performed better in all                      proposed method produces reliable and semantically coherent
socialization criteria, indicating the proposed method gener-                  MWPs.
ates MWPs that are explicitly designed for social interaction,                    Moreover, the automatic evaluation also examines how au-
supporting group problem-solving, shared responsibility, and                   tomatically the final generated MWPs align with the original-
peer dialogue. This is nearly absent in zero-shot MWP gen-                     based MWPs across four targeted social competencies, using
eration. Our proposed method is better aligned with social-                    both surface-level and semantic-level metrics (see Fig. 4). We
ization objectives and more effective in eliciting collabora-                  found that collaboration-related MWPs show the highest perfor-
tive discourse among students. In contrast, the MWPs gen-                      mance in all automatic metrics. The high BLEU-4 score shows
erated without our method tended to lack clear social in-                      strong consistency in word choice and structure compared to the
teraction cues and demonstrated fewer connections to real-                     original base MWPs. In addition, the high score of BERT Recall
life contexts that affect meeting the targeted educational                     and F1 score also indicates that generated MWPs successfully
goals.                                                                         capture the full meaning and intent of the references and confirm
                                                                               consistent quality. This may reflect the fact that collaboration-
                                                                               focused scenarios have more standardized structures and re-
B. RQ2. What are the Results of Automatic Evaluation,                          curring vocabulary (e.g., shared tasks, mutual roles), making
Human Evaluation, and LLM-Based Evaluation of                                  them easier for the model to replicate accurately. In addition,
SocioMathLLM in Generating MWPs Driving Socialization?                         this performance may reflect the clear roles, shared tasks, and
  This study found that the BLEU score in Table VI, which                      structured interactions typically involved in collaborative tasks,
measures n-gram, is relatively low. A mean score of 0.153                      which are more easily captured by both lexical and semantic
suggests that the exact wording and phrasing of the generated                  measures.

        Authorized licensed use limited to: Universitas Airlangga. Downloaded on May 04,2026 at 03:23:10 UTC from IEEE Xplore. Restrictions apply.
HWANG AND UTAMI: SOCIOMATHLLM: A MULTIMODAL LLM FRAMEWORK FOR GENERATING AUTHENTIC MWP DRIVING SOCIALIZATION                                            279



                                                              TABLE VII
AVERAGE AUTOMATIC EVALUATION SCORES AND INTERRATER RELIABILITY SCORES FOR DIFFERENT SOCIALIZATION COMPETENCIES BY HUMAN EVALUATOR AND
                                        LLM, CONSIDERING AUTHENTICITY AND LINGUISTIC ASPECT




                                                                                    Besides the automatic evaluation, we also conducted hu-
                                                                                 man evaluation and LLM-based evaluation to triangulate the
                                                                                 quality assessment of the generated MWPs driving socializa-
                                                                                 tion across multiple dimensions, including authenticity and
                                                                                 linguistics, mathematics, personalization, and socialization.
                                                                                 This multiperspective approach ensures a more comprehensive
                                                                                 and reliable understanding of the quality of SocioMathLLM.
                                                                                 Table VII illustrates that human evaluators consistently rated
                                                                                 the MWPs highly on the authenticity dimension, with scores
                                                                                 ranging from 4.880 to 4.960, indicating that the tasks were
                                                                                 perceived as highly relevant and engaging across all socialization
                                                                                 competencies. LLM-based evaluations also produced relatively
                                                                                 high scores, although slightly lower scores were found for col-
Fig. 4. Average automatic evaluation scores for different socialization com-     laboration (4.560) and cooperation (4.360), suggesting a minor
petencies (considering original MWP and modified MWP).
                                                                                 underestimation of contextual engagement by LLM. In terms of
                                                                                 linguistic clarity and cultural appropriateness, both human and
   Cooperation-related MWPs also demonstrated strong seman-                      LLM yielded high and closely aligned scores, with LLM ratings
tic alignment, although with a lower BLEU score than collabora-                  slightly exceeding those of human evaluators in all categories
tion MWPs. This finding suggests that while generated problems                   and most notably achieving perfect scores for cooperation, ne-
differ more in wording, they still capture the essential meaning                 gotiation, and ideas-sharing. This high agreement demonstrates
and instructional content of reference MWPs. The difference                      that the LLM was effective in recognizing linguistic clarity and
between BLEU and BERT metrics here highlights the flexibility                    culturally appropriate phrasing, aligning well with expert human
in language use in cooperative settings, which may vary more in                  judgment. Together, these findings support the validity of using
phrasing and task structure than collaborative ones. In addition,                LLM-based evaluation to assess the authenticity and linguistic
the negotiation MWPs score slightly lower than cooperation                       quality of MWPs.
but still exhibit strong semantic fidelity. The BLEU score is                       In Table VIII, we found that both human and LLM showed
the second lowest, which may be attributed to the diverse and                    strong agreement on problem answerability, with all scores
context-driven language typical of negotiation scenarios, such as                ranging between 4.800 and 5.000. Notably, human evaluators
tradeoffs, choices, and persuasive dialogue. However, the BERT                   provided perfect scores for three of the four socialization com-
F1 remains high, suggesting that generated MWPs successfully                     petencies, indicating that the problems were perceived as highly
retain the intent and instructional objectives behind negotiation                solvable and clearly framed in all contexts. For problem structure
activities. These problems benefit from semantic-aware eval-                     and clarity, scores were consistently high, with LLM ratings
uation, as they often require nonstandard sentence structures                    slightly exceeding or matching human evaluations except for
to simulate real negotiation dynamics. Furthermore, the idea-                    ideas-sharing, where the LLM gave a noticeably lower score
sharing MWPs exhibit a pattern like negotiation, relatively lower                (4.720) compared to the human score (4.960), possibly reflect-
BLEU-4, but high semantic consistency. The high BERT Recall                      ing a stricter interpretation of structural precision. Regarding
(0.941) indicates that generated ideas-sharing MWPs include                      multiple solution strategies, human evaluators rated all MWPs
most of the key content from reference problems, even if the                     at the highest level, suggesting strong potential for open-ended
expression is more open-ended. This reflects the inherently                      reasoning and flexibility.
flexible and creative nature of idea-sharing tasks, where encour-                   In contrast, the LLM produced slightly lower scores across
aging diverse student responses may lead to less rigid phrasing                  all categories, most notably for collaboration (4.600). This
but strong conceptual alignment. These results reinforce the                     gap suggests that while the model recognizes varied solu-
appropriateness of semantic-based evaluation methods for tasks                   tion paths, it may be slightly conservative in identifying tasks
prioritizing meaning over form.                                                  that allow for diverse strategies. Overall, the high level of

           Authorized licensed use limited to: Universitas Airlangga. Downloaded on May 04,2026 at 03:23:10 UTC from IEEE Xplore. Restrictions apply.
280                                                                                        IEEE TRANSACTIONS ON LEARNING TECHNOLOGIES, VOL. 19, 2026




Fig. 5.   Comparison of MWP driving socialization with and without our proposed approach.

                                                             TABLE VIII
AVERAGE AUTOMATIC EVALUATION SCORES AND INTERRATER RELIABILITY SCORES FOR DIFFERENT SOCIALIZATION COMPETENCIES BY HUMAN EVALUATOR AND
                                              LLM, CONSIDERING THE MATHEMATICS ASPECT




consistency across most ratings reinforces the LLM’s utility                     and LLM perspectives across seven key criteria. On average,
as an evaluative tool, while highlighting subtle differences                     human evaluators provided higher ratings than the LLM for
in how humans and AI perceive openness and structure in                          how well the MWPs supported socialization (e.g., collaboration,
problem-solving design. In addition, Human and LLM ratings                       cooperation, negotiation, and idea-sharing). This suggests that
for the number of solution steps showed strong alignment, with                   the LLM might not be as capable as humans in recognizing or
nearly identical scores across all socialization competencies                    interpreting the subtle aspects of how social interaction happens
(ranging from 4.84 to 5.00), indicating that the LLM was                         in a learning task. For instance, humans may better understand
highly accurate in assessing whether the problems required a                     whether the MWPs encourage meaningful conversation, mutual
suitable level of procedural complexity. However, some diver-                    support, shared goals, or idea exchange, while the LLM may
gence appeared in the evaluation of cognitive demand. While                      miss or underscore these. These are things humans naturally
both human and LLM ratings were generally high, the LLM                          perceive, but which are harder for LLM to assess accurately.
tended to assign slightly higher scores, particularly in nego-                   Humans see more social value in the tasks than the LLM
tiation and ideas-sharing MWPs. This suggests that the LLM                       does, likely because human evaluators can better detect the
may tend to slightly overestimate the cognitive challenge posed                  complex interpersonal elements that the LLM still struggles
by certain tasks, especially in open-ended or idea-generating                    to fully understand. Furthermore, collaboration MWPs receive
 contexts.                                                                       the highest scores from both humans and the LLM, suggesting
   Furthermore, Table IX reveals important insights into how                     that MWPs designed for collaboration most effectively promote
effectively the MWPs promote socialization through both human                    socialization. Ideas-sharing MWPs also received high scores,
          Authorized licensed use limited to: Universitas Airlangga. Downloaded on May 04,2026 at 03:23:10 UTC from IEEE Xplore. Restrictions apply.
HWANG AND UTAMI: SOCIOMATHLLM: A MULTIMODAL LLM FRAMEWORK FOR GENERATING AUTHENTIC MWP DRIVING SOCIALIZATION                                          281



                                                              TABLE IX
AVERAGE AUTOMATIC EVALUATION SCORES AND INTERRATER RELIABILITY SCORES FOR DIFFERENT SOCIALIZATION COMPETENCIES BY HUMAN EVALUATOR AND
                                             LLM, CONSIDERING THE SOCIALIZATION ASPECT




                                                               TABLE X
AVERAGE AUTOMATIC EVALUATION SCORES AND INTERRATER RELIABILITY SCORES FOR DIFFERENT SOCIALIZATION COMPETENCIES BY HUMAN EVALUATOR AND
                                            LLM, CONSIDERING THE PERSONALIZATION ASPECT




particularly in group size and social interdependency, indicating              learners’ diverse contexts in one group as a critical aspect of
that they can foster active participation and mutual reliance.                 personalized learning design. However, we obtained moderate
On the other hand, negotiation MWPs, while strong in human                     interrater reliability scores (in the range 0.551–0.714), indicating
evaluations, show lower LLM scores in aspects such as social                   moderate to substantial agreement between human evaluators
frequency and social interdependency, implying challenges in                   and the LLM in assessing whether the language complexity
automatic recognition of negotiation dynamics.                                 level of the generated by MWPs matches the learners’ reading
   In summary, MWPs designed for collaboration are the most                    or comprehension level. The relatively higher score for
effective in fostering rich social interactions, followed by ideas-            negotiation (0.714) may indicate that the model generates more
sharing. Negotiation and cooperation may be less prominent in                  appropriate or readable language in negotiation-based tasks.
driving high-quality and frequent social exchanges, particularly               However, moderate consistency in collaboration, cooperation,
from the LLM’s perspective. The gap between human and LLM                      and ideas-sharing MWPs may reflect that the model sometimes
scores indicates that while humans perceive the MWPs to be                     produces vocabulary or sentence structures that are too complex
socially engaging, the LLM may underrepresent subtle elements                  or inconsistent with the learners’ actual abilities. Furthermore,
of social interaction. This finding aligns with the study by Chan              the proposed model performs well in adjusting math difficulty,
et al. [10] stating that AI remains constrained in its ability to              although some variations in agreement suggest room for
stimulate constructive discussions, promote open-minded per-                   improvement, especially in idea-sharing MWPs.
spectives, and manage conflict resolution.                                        In summary, the proposed model can create MWPs that drive
                                                                               socialization and are relatable to specific group background
                                                                               information, particularly in terms of scope personalization,
C. RQ3. Can the Proposed SocioMathLLM Create MWPs                              with high interrater reliability scores across all socialization
Driving Socialization That Align With the Specific Group                       competencies. However, while there is reasonable alignment
Background Information??                                                       between human and LLM evaluations regarding linguistic and
   Table X lists personalization evaluation results, which means               mathematical complexity, the lower interrater reliability scores
how well the generated MWPs driving socialization align with                   in those two areas, especially linguistic complexity, indicate
group-specific background information. We found that the                       areas needing refinement. It is important to provide the model
proposed model can create MWPs driving socialization that                      with clearer reading comprehension status and mathematical
are relatable to the specific group background information,                    processing information of the group.
as evidenced by high interrater reliability scores (ICC >
0.75) for scope personalization across all four socialization
                                                                                          VI. THREATS TO VALIDITY AND LIMITATIONS
competencies. These values demonstrate that the proposed
model is consistently capable of generating MWPs that human                       Despite the promising results, this study is subject to several
evaluators agree are relevant and meaningful to the targeted                   limitations that should be considered when interpreting the

         Authorized licensed use limited to: Universitas Airlangga. Downloaded on May 04,2026 at 03:23:10 UTC from IEEE Xplore. Restrictions apply.
282                                                                                      IEEE TRANSACTIONS ON LEARNING TECHNOLOGIES, VOL. 19, 2026



                                                                TABLE XI
                          DEVELOPED CRITERIA USED TO GENERATE AND EVALUATE THE SOCIAL COGNITIVE ASPECT OF MWPS




findings. First, socialization competencies such as                            inherent limitations in generating MWPs that meaningfully
collaboration, cooperation, negotiation, and idea-sharing                      promote student socialization. These models are primarily
are complex and multifaceted constructs. While the                             optimized for linguistic coherence and content plausibility
evaluation rubric was carefully designed to capture these                      rather than pedagogically grounded social-interaction goals,
dimensions, it may not fully represent all aspects of                          which often results in MWPs that emphasize individual problem
students’ social interactions. In addition, rubric-based                       solving over authentic group dynamics. Moreover, they lack
assessments inherently involve subjective judgment, which                      an explicit understanding of classroom social structures,
may introduce measurement bias despite consistency checks.                     learner roles, and interactional dependencies. Finally, this
Second, SocioMathLLM relies on the quality of input data,                      study is limited to MWPs in the domain of 2-D geometry,
including group background information, multimodal authentic                   which may restrict the generalizability of the findings to other
contextual information, and prompt specifications. Inaccurate or               mathematical topics. The framework was also evaluated using
incomplete inputs may affect the relevance and effectiveness of                a single LLM based on GPT-4o. The study does not include
the generated MWPs driving socialization. In addition, despite                 cross-model validation with open-source LLMs, such as Llama
strong generative capabilities, general LLM tools exhibit                      4 or Mistral, which may exhibit different generative behaviors,

        Authorized licensed use limited to: Universitas Airlangga. Downloaded on May 04,2026 at 03:23:10 UTC from IEEE Xplore. Restrictions apply.
HWANG AND UTAMI: SOCIOMATHLLM: A MULTIMODAL LLM FRAMEWORK FOR GENERATING AUTHENTIC MWP DRIVING SOCIALIZATION                                              283



reasoning patterns, or contextual sensitivity. Consequently,                   of tasks that are not only mathematically sound but also pedagog-
the generalizability of the framework across different model                   ically aligned with mathematics collaborative learning practices.
architectures and training paradigms remains to be examined                       Automatic evaluations showed substantial improvements in
in future research. In addition, the human evaluation primarily                both surface-level and semantic quality, while human- and
relied on expert judgment, without direct validation from                      LLM-based evaluations further validated the framework’s ef-
students’ learning experiences or outcomes. Future studies                     fectiveness across multiple dimensions. Human evaluators rated
should extend the framework to broader domains and                             the MWPs highly in authenticity, linguistic clarity, cultural
incorporate student-centered evaluations and a quasi-experiment                appropriateness, answerability, and openness to multiple so-
to better assess its educational impact. In future work, we plan to            lution strategies, confirming that the problems were engaging,
extend this research by fine-tuning or training domain-adapted                 contextually relevant, and supportive of higher order thinking.
LLMs and by evaluating the framework using powerful                            LLM-based evaluations aligned closely with human judgments,
open-source multimodal LLMs, such as Llama 4 or Qwen3.5,                       particularly in authenticity, linguistic quality, and problem struc-
to better support the generalization of our proposed framework in              ture, although the model occasionally underestimated contextual
science education contexts, particularly in the mathematics area.              engagement or solution diversity. These findings reinforce both
                                                                               the reliability of the framework in producing high-quality MWPs
                                                                               for driving socialization and the utility of LLMs as complemen-
                        VII. CONCLUSION                                        tary evaluation tools.
   This study proposed and validated a prompt engineering                         In conclusion, this study advances AI-supported mathematics
framework called SocioMathLLM for generating MWPs that                         education by presenting a technically grounded LLM-based
integrate mathematics socialization objectives. Specifically, the              framework for generating MWPs that explicitly promote socio-
framework was designed to foster four distinct socialization                   interactional learning in collaborative settings. By formalizing
competencies, such as collaboration, cooperation, negotiation,                 pedagogical and socialization principles into a structured prompt
and idea-sharing through three interconnected modules: contex-                 design, integrating authenticity, linguistic, mathematical, and
tualization, personalization, and socialization.                               socialization criteria, and incorporating authentic multimodal
   The contextualization module ensured authenticity and rele-                 contexts and group background information, the proposed ap-
vance by embedding real-world scenarios, multimodal represen-                  proach moves beyond conventional MWP generation focused on
tations, and measurement data related to 2-D geometry into the                 individual cognition or content difficulty. The comprehensive
MWPs. This design grounded abstract mathematical concepts in                   evaluation combining automatic metrics, human expert judg-
familiar and meaningful contexts for students. The personaliza-                ment, and LLM-based assessment demonstrates the robustness
tion module further tailored the tasks by incorporating learner                and educational relevance of the framework. Positioned as an
profiles, including cognitive, socio-economic, and demographic                 educational design study with technical significance, this work
factors, and employed an evaluation process to refine problem                  contributes a reusable and model-agnostic approach for align-
quality and educational alignment. Finally, the socialization                  ing LLM-based problem generation with collaborative learning
module transformed personalized MWPs into social interaction-                  objectives, offering meaningful implications for the design of
oriented tasks by embedding explicit socialization criteria and                future learning technologies.
instructional cues, thereby guiding students toward meaningful
group discourse and cooperative problem-solving.
   Furthermore, this study demonstrated that the proposed So-                                                    REFERENCES
cioMathLLM framework substantially improves the quality                         [1] W. Qin, X. Wang, Z. Hu, L. Wang, Y. Lan, and R. Hong, “Math word prob-
of LLM-generated MWPs compared to zero-shot prompting.                              lem generation via disentangled memory retrieval,” ACM Trans. Knowl.
Across both automatic metrics and LLM-based evaluations, our                        Discov. Data, vol. 18, no. 5, pp. 1–21, Mar. 2024, doi: 10.1145/3639569.
                                                                                [2] G. Kai, “Bidirectional training for generating math word problems us-
method consistently outperformed the zero-shot result in authen-                    ing pre-trained model and prompt,” in Proc. 20th Int. Comput. Conf.
ticity, mathematics aspect, personalization, and socialization.                     Wavelet Act. Media Technol. Inf. Process., 2023, pp. 1–6, doi: 10.1109/IC-
Automatic evaluation showed significant improvements, with                          CWAMTIP60502.2023.10387053.
                                                                                [3] G. Kurdi, J. Leo, B. Parsia, U. Sattler, and S. Al-Emari, “A system-
BLEU increasing from 0.002 to 0.408 and BERT-based F1 rising                        atic review of automatic question generation for educational purposes,”
from 0.817 to 0.925, indicating that the generated MWPs were                        Int. J. Artif. Intell. Educ., vol. 30, no. 1, pp. 121–204, Mar. 2020, doi:
both more semantically accurate and more contextually relevant.                     10.1007/s40593-019-00186-y.
                                                                                [4] L. Verschaffel, S. Schukajlow, J. Star, and W. Van Dooren, “Word problems
This finding was further supported by additional automatic eval-                    in mathematics education: A survey,” ZDM - Math. Educ., vol. 52, no. 1,
uation metrics, including METEOR, ROUGE-L, and BLEURT.                              pp. 1–16, Apr. 2020, doi: 10.1007/s11858-020-01130-4.
   Beyond surface-level quality, the evaluation further revealed                [5] Q. Wu, Q. Zhang, and X. Huang, “Automatic math word problem gen-
                                                                                    eration with topic-expression co-attention mechanism and reinforcement
that SocioMathLLM produces problems that are richer in                              learning,” IEEE/ACM Trans. Audio Speech Lang. Process., vol. 30,
linguistic variety, mathematically more challenging, and better                     pp. 1061–1072, 2022, doi: 10.1109/TASLP.2022.3155284.
tailored to students’ profiles in one group. Importantly, the                   [6] W. Y. Hwang and I. Q. Utami, “Contextualized and personalized math word
                                                                                    problem generation using GPT and authentic contextual recognition,”
framework embeds explicit social interaction hints, supporting                      in Proc. 12th Int. Conf. Inf. Educ. Technol., 2024, pp. 177–181, doi:
collaborative discourse, shared responsibility, and negotiation                     10.1109/ICIET60671.2024.10542742.
among learners, where those dimensions are commonly absent                      [7] W. Y. Hwang and I. Q. Utami, “Using GPT and authentic contex-
                                                                                    tual recognition to generate math word problems with difficulty lev-
in zero-shot MWPs. The integration of contextualization, per-                       els,” Educ. Inf. Technol., vol. 29, no. 13, pp. 1–29, Sep. 2024, doi:
sonalization, and socialization modules enabled the generation                      10.1007/s10639-024-12537-x.
         Authorized licensed use limited to: Universitas Airlangga. Downloaded on May 04,2026 at 03:23:10 UTC from IEEE Xplore. Restrictions apply.
284                                                                                            IEEE TRANSACTIONS ON LEARNING TECHNOLOGIES, VOL. 19, 2026



 [8] I. Q. Utami, W. Y. Hwang, and U. Hariyanti, “Contextualized and per-            [28] W. Lim, H. Yoon, Y. Bae, and O. N. Kwon, “The development of so-
     sonalized math word problem generation in authentic contexts using gen-              ciomathematical norms in the transition to tertiary exam-oriented individu-
     erative pre-trained transformer and its influences on geometry learning,”            alistic mathematics education in an East Asian context,” Educ. Stud. Math.,
     J. Educ. Comput. Res., vol. 62, no. 6, pp. 1604–1639, Oct. 2024, doi:                vol. 113, no. 1, pp. 57–78, May 2023, doi: 10.1007/s10649-022-10203-y.
     10.1177/07356331241249225.                                                      [29] A. R. Davis, “The mathematics socialization experiences of racially and
 [9] Y. S. Kıyak and E. Emekli, “ChatGPT prompts for generating multiple-                 ethnically diverse pre-service early childhood teachers,” J. Math. Educ.,
     choice questions in medical education and evidence on their validity: A              vol. 14, no. 2, pp. 64–80, Nov. 2021, doi: 10.26711/007577152790074.
     literature review,” Postgraduate Med. J., vol. 100, no. 1189, pp. 858–865,      [30] R. Barwell, “Learning mathematics in a second language: Language
     Nov. 2024, doi: 10.1093/postmj/qgae065.                                              positive and language neutral classrooms,” J. Res. Math. Educ., vol. 51,
[10] P. S. Bhullar, M. Joshi, and R. Chugh, “ChatGPT in higher educa-                     no. 2, pp. 150–178, 2020, doi: 10.5951/jresematheduc-2020-0018.
     tion - A synthesis of the literature and a future research agenda,”             [31] E. N. Walker, “The importance of communities for mathematics learning
     Educ. Inf. Technol., vol. 29, no. 16, pp. 21501–21522, Nov. 2024, doi:               and socialization 1,” 2016. [Online]. Available: http://education.gsu.edu/
     10.1007/s10639-024-12723-x.                                                          JUME
[11] H. Crompton and D. Burke, “The educational affordances and challenges           [32] N. Mulla and P. Gharpure, “Automatic question generation: A review of
     of ChatGPT: State of the field,” TechTrends, vol. 68, no. 2, pp. 380–392,            methodologies, datasets, evaluation metrics, and applications,” Prog. Artif.
     Mar. 2024, doi: 10.1007/s11528-024-00939-0.                                          Intell., vol. 12, no. 1, pp. 1–32, 2023, doi: 10.1007/s13748-023-00295-9.
[12] J. Han, S. Yeo, E. Kim, S. Hwang, and J. Cai, “A systematic review of           [33] S. Al Faraby, A. Adiwijaya, and A. Romadhony, “Review on neural
     literature on mathematical problem posing in Korea,” Korean Soc. Educ.               question generation for education purposes,” Int. J. Artif. Intell. Educ., vol.
     Stud. Math. - J. Educ. Res. Math., vol. 33, no. 3, pp. 607–637, Aug. 2023,           34, no. 3, pp. 1008–1045, Sep. 2024, doi: 10.1007/s40593-023-00374-x.
     doi: 10.29275/jerm.2023.33.3.607.                                               [34] X. Kang, Z. Wang, X. Jin, W. Wang, K. Huang, and Q. Wang, “Template-
[13] J. B. Jaffe and D. J. Bolger, “Cognitive processes, linguistic factors,              driven LLM-paraphrased framework for tabular math word problem gener-
     and arithmetic word problem success: A review of behavioral stud-                    ation,” in Proc. AAAI Conf. Artif. Intell., vol. 39, no. 23, pp. 24303–24311,
     ies,” Educ. Psychol. Rev., vol. 35, no. 4, Dec. 2023, Art. no. 105, doi:             2025, doi: 10.1609/aaai.v39i23.34607.
     10.1007/s10648-023-09821-6.                                                     [35] T. Zhao, C. Chai, J. Liu, G. Li, J. Feng, and Z. Liu, “A topic-aware data
[14] K. Das, “Realistic mathematics & Vygotsky’s theories in mathematics                  generation framework for math word problems,” in (Lecture Notes in Com-
     education,” Shanlax Int. J. Educ., vol. 9, no. 1, pp. 104–108, Dec. 2020,            puter Science, including Subseries Lecture Notes in Artificial Intelligence
     doi: 10.34293/education.v9i1.3346.                                                   and Lecture Notes in Bioinformatics). Berlin, Germany: Springer-Verlag,
[15] D. F. Steele, “Using sociocultural theory to teach mathematics: A Vygot-             2023, pp. 286–302, doi: 10.1007/978-3-031-30678-5_22.
     skian perspective,” Sch. Sci. Math., vol. 101, no. 8, pp. 404–416, Dec. 2001,   [36] J. M. Lodge, K. Thompson, and L. Corrin, “Mapping out a research agenda
     doi: 10.1111/j.1949-8594.2001.tb17876.x.                                             for generative artificial intelligence in tertiary education,” in Australas. J.
[16] K. Montiegel, “Peer socialization in an oral preschool class-                        Educ. Technol., vol. 39, no. 1, pp. 1–8, 2023, doi: 10.14742/ajet.8695.
     room,” Lang. Commun., vol. 89, pp. 63–77, Mar. 2023, doi:                       [37] E. Kasneci et al., “ChatGPT for good? On opportunities and challenges of
     10.1016/j.langcom.2023.01.001.                                                       large language models for education,” Learn. Individual Differences, vol.
[17] Y. Zhu, “Language socialization in the classroom: Collaborative learn-               103, 2023, Art. no. 102274, doi: 10.1016/j.lindif.2023.102274.
     ing model,” J. Educ. Educ. Res., vol. 4, pp. 140–142, 2023, doi:                [38] E. Bonner, R. Lege, and E. Frazier, “Large language model-based arti-
     10.54097/jeer.v4i3.11398.                                                            ficial intelligence in the language classroom: Practical ideas for teach-
[18] V. Titz-Mohácsi and K. Széll, “Attachment and socialization of sib-                  ing,” Teach. English Technol., vol. 2023, no. 1, pp. 23–41, 2023, doi:
     lings in Hungarian residential care: An ethnographic study,” Child.                  10.56297/bkam1691/wieo1749.
     Youth Serv. Rev., vol. 174, Jul. 2025, Art. no. 108346, doi:                    [39] O. Topsakal and E. Topsakal, “Framework for a foreign language teaching
     10.1016/j.childyouth.2025.108346.                                                    software for children utilizing AR, voicebots and ChatGPT (large lan-
[19] E. Aminifar, M. Malaki, U. Ryan, and H. Mesgarani, “A long-term shift                guage models),” J. Cogn. Syst., vol. 7, no. 2, pp. 33–38, Dec. 2022, doi:
     to include students’ first language in the mathematics teaching practice:            10.52876/jcs.1227392.
     Socialization events and learning opportunities,” Educ. Stud. Math.,            [40] X. Zhai, “ChatGPT user experience: Implications for education,” 2022.
     vol.     116,      no.     1,    pp. 113–135,          May     2024,     doi:        [Online]. Available: https://orcid.org/0000-0003-4519-1931
     10.1007/s10649-024-10307-7.                                                     [41] R. Abdelghani et al., “GPT-3-driven pedagogical agents to train children’s
[20] R. Abdu and B. Schwarz, “Split up, but stay together: Col-                           curious question-asking skills,” Int. J. Artif. Intell. Educ., vol. 34, no. 2,
     laboration and cooperation in mathematical problem solving,”                         pp. 483–518, 2024, doi: 10.1007/s40593-023-00340-7.
     Instructional Sci., vol. 48, no. 3, pp. 313–336, Jun. 2020,                     [42] K. Norberg et al., “Rewriting math word problems with large language
     doi: 10.1007/s11251-020-09512-7.                                                     models,” 2023. [Online]. Available: http://ceur-ws.org
[21] R. M. Gillies, “Cooperative learning: Review of research and practice,”         [43] Y. Qian, “Prompt engineering in education: A systematic review of ap-
     Australian J. Teacher Educ., vol. 41, no. 3, pp. 39–54, Jan. 2016, doi:              proaches and educational applications,” J. Educ. Comput. Res., vol. 63,
     10.14221/ajte.2016v41n3.3.                                                           no. 7/8, pp. 1782–1818, Dec. 2025, doi: 10.1177/07356331251365189.
[22] J. N. Moschkovich, “Language and learning mathematics: A socio-                 [44] B. Chen, Z. Zhang, N. Langrené, and S. Zhu, “Unleashing the potential
     cultural approach to academic literacy in mathematics,” in Proc. 14th                of prompt engineering for large language models,” Patterns, vol. 6, no. 6,
     Int. Congr. Math. Educ., II, Invited Lectures, 2024, pp. 459–472, doi:               Jun. 2025, Art. no. 101260, doi: 10.1016/j.patter.2025.101260.
     10.1142/9789811287183_0031.                                                     [45] W. Wang, V. W. Zheng, H. Yu, and C. Miao, “A survey of zero-shot
[23] J. Yang, “The characteristics of mathematical communication in sec-                  learning: Settings, methods, and applications,” ACM Trans. Intell. Syst.
     ondary school students’ collaborative problem solving,” in Students’                 Technol., vol. 10, no. 2, pp. 1–37, Jan. 2019, doi: 10.1145/3293318.
     Collaborative Problem Solving in Mathematics Classrooms: An empir-              [46] T. B. Brown et al., “Language models are few-shot learn-
     ical Study. Berlin, Germany: Springer-Verlag, 2024, pp. 127–157, doi:                ers,” Adv. Neural Inf. Process. Syst., vol. 33, pp. 1877–1901,
     10.1007/978-981-99-7386-6_6.                                                         2020. [Online]. Available: https://papers.nips.cc/paper/2020/hash/
[24] B. P. Uyen, D. H. Tong, and N. T. B. Tram, “Developing mathematical                  1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html
     communication skills for students in grade 8 in teaching congruent triangle     [47] M. Lewis et al., “BART: Denoising sequence-to-sequence pre-training for
     topics,” Eur. J. Educ. Res., vol. 10, no. 3, pp. 1287–1302, 2021, doi:               natural language generation, translation, and comprehension,” in Proc.
     10.12973/eu-jer.10.3.1287.                                                           58th Annu. Meeting Assoc. Comput. Linguistics, 2020, pp. 7871–7880,
[25] C. W. Midgett and S. K. Eddins, “NCTM’s principles and standards for                 doi: 10.18653/v1/2020.acl-main.703.
     school mathematics: Implications for administrators,” NASSP Bulletin,           [48] J. Liu et al., “Generated knowledge prompting for commonsense
     vol. 85, no. 623, pp. 35–42, doi: 10.1177/019263650108562305.                        reasoning,” in Proc. 60th Annu. Meeting Assoc. Comput. Lin-
[26] K. G. Wilkins, B. L. Bernstein, and J. M. Bekki, “Measuring communi-                 guistics, Dublin, Ireland, vol. 1, May 2022, pp. 3154–3169, doi:
     cation skills: The STEM interpersonal communication skills assessment                10.18653/v1/2022.acllong.225.
     battery,” J. Eng. Educ., vol. 104, no. 4, pp. 433–453, Oct. 2015, doi:          [49] J. Wei et al., “Chain-of-thought prompting elicits reasoning in large
     10.1002/jee.20100.                                                                   language models,” in Proc. 36th Int. Conf. Neural Inf. Proc. Syst., New
[27] E. L. Usher, “Sources of middle school students? self-efficacy in math-              Orleans, LA, USA, 2023, pp. 1–14.
     ematics: A qualitative investigation,” Am. Educ. Res. J., vol. 46, no. 1,       [50] X. Wang et al., “Self-consistency improves chain of thought reasoning in
     pp. 275–314, 2009, doi: 10.3102/0002831208324517.                                    language models,” 2023, arXiv:2203.11171.



          Authorized licensed use limited to: Universitas Airlangga. Downloaded on May 04,2026 at 03:23:10 UTC from IEEE Xplore. Restrictions apply.
HWANG AND UTAMI: SOCIOMATHLLM: A MULTIMODAL LLM FRAMEWORK FOR GENERATING AUTHENTIC MWP DRIVING SOCIALIZATION                                                        285



[51] S. Yao et al., “Tree of thoughts: Deliberate problem solving with                                          Wu-Yuin Hwang received his Ph.D. in computer sci-
     large language models,” in Proc. 37th Int. Conf. Neural Inf. Pro-                                          ence from National Tsing Hua University of Taiwan,
     cess. Syst., Red Hook, NY, USA Curran Associates Inc. 2023,                                                Taiwan, China, in 1997.
     pp. 11809–11822.                                                                                              He is a Professor affiliated with both the Depart-
[52] Z. Li, B. Peng, P. He, M. Galley, J. Gao, and X. Yan, “Guiding large                                       ment of Computer Science and Information Engi-
     language models via directional stimulus prompting,” in Proc. 37th Int.                                    neering, College of Science and Engineering, Na-
     Conf. Neural Inf. Process. Syst., Red Hook, NY, USA: Curran Associates                                     tional Dong Hwa University, Hualien, Taiwan, and the
     Inc., 2023, pp. 62630–62656.                                                                               Institute of Network Learning Technology, National
[53] N. Klang, N. Karlsson, W. Kilborn, P. Eriksson, and M. Karlberg, “Math-                                    Central University, Taoyuan, Taiwan. His current re-
     ematical problem-solving through cooperative learning—The importance                                       search interests include the integration of IOT, AI, and
     of peer acceptance and friendships,” Front. Educ., vol. 6, 2021, Art. no.                                  multimedia sensors of mobile devices for learning and
     710296, doi: 10.3389/feduc.2021.710296.                                         interactions among humans and all things in AR contexts, such as smart buildings
[54] G. Williams, “Collaborative problem solving in mathematics: The nature          and campuses.
     and function of task complexity,” 2000. [Online]. Available: https://www2.         Dr. Hwang was a recipient of the Outstanding Research Award from the
     merga.net.au/documents/RP_Williams_2000.pdf                                     Ministry of Science and Technology, Taiwan, in 2021. He is also ranked in
[55] L. A. Guerrero, R. Alarcdn, C. Collazos, J. A. Pino, and D. A. Fuller,          the top seven scholars of the world in terms of high-quality journal publication
     “Evaluating cooperation in group work,” in Proc. 6th Int. Workshop              performance of instructional design and technology.
     Groupware.,      Madeira,     Portugal,    2000,     pp.     28–35,      doi:
     0.1109/CRIWG.2000.885152.                                                                               Ika Qutsiati Utami received the B.S. degree in in-
[56] B. B. Schwarz, O. Swidan, N. Prusak, and A. Palatnik, “Collaborative                                    formation systems from the Faculty of Computer
     learning in mathematics classrooms: Can teachers understand progress of                                 Science, Brawijaya University, Malang, Indonesia,
     concurrent collaborating groups?,” Comput. Educ., vol. 165, May 2021,                                   in 2016, and the M.S. and Ph.D. degrees from the
     Art. no. 104151, doi: 10.1016/j.compedu.2021.104151.                                                    Graduate Institute of Network Learning Technology,
[57] G. Krummheuer, “Negotiation, argumentation and participation: Three                                     College of Electrical Engineering and Computer Sci-
     basic concepts referring to everyday procedures in teaching and learning                                ence, National Central University, ROC, Taiwan, in
     situations in mathematics classes,” Theory Pract., vol. 62, no. 1, pp. 70–78,                           2018 and 2026, respectively.
     2023, doi: 10.1080/00405841.2022.2135901.                                                                  She is a Lecturer with the Data Science Tech-
[58] J. Yang, “The characteristics of mathematical communication in sec-                                     nology Study Program, under the Faculty of Ad-
     ondary school students’ collaborative problem solving,” in Students’                                    vanced Technology and Multidiscipline, Universitas
     Collaborative Problem Solving in Mathematics Classrooms: An Empir-              Airlangga, Surabaya, Indonesia. Her research interests include the areas of
     ical Study. Berlin, Germany: Springer-Verlag, 2024, pp. 127–157, doi:           human–computer interaction, AI/ML for future education, and educational data
     10.1007/978-981-99-7386-6_6.                                                    science.




            Authorized licensed use limited to: Universitas Airlangga. Downloaded on May 04,2026 at 03:23:10 UTC from IEEE Xplore. Restrictions apply.
