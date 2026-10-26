# 8. Conclusion

This review examined one question: why reliable annotation and evaluation of Malaysian Malay-English code-
mixed sentiment data remain unresolved. The answer usually given is architectural, and the evidence assembled
here indicates that it is incomplete. Model choice accounts for part of the difficulty. The rest lies earlier,
in the sentiment labels themselves and in the evidence offered that those labels are sound.

Three findings support that reading. The review found no available Malay-English sentiment resource that is at
once large, balanced across sentiment classes, drawn from casual social media and validated by people. Each of
the four secures some of those properties at the expense of the others. It found that the class imbalance in
the largest of them originates in the labelling method rather than in Malaysian discourse. Two distinct causes
produce that imbalance, one belonging to the labelling tools and one to genuine uncertainty among annotators.
It found that annotation reliability is rarely reported, and that where a coefficient is given it was obtained
for a narrower task than the corpus is used to support.

The contribution this review claims is not any of those findings taken alone but the relation between them.
The linguistic properties of the text produce disagreement that is systematic rather than random. Systematic
disagreement makes fluent bilingual annotation necessary and expensive, which is why labelling is automated.
The tools available for that automation cover neither Malay nor Manglish, so pooling them ratifies a shared
error instead of cancelling it. The class skew that results is the precise condition under which the standard
agreement coefficient stops returning interpretable values, so the defect and the inability to detect the
defect have one cause rather than two. Each corpus built in this way then trains the annotators that build the
next. An intervention at any single point in that sequence is assessed by an instrument compromised at
another, which is why competent work at each link has not accumulated into progress.

The directions set out in Section 7 follow from that structure rather than from preference. The first of them,
an agreement measure that behaves interpretably under the class distributions these corpora actually exhibit,
is a precondition for evaluating the rest. Until reliability can be measured under the conditions this data
presents, no corpus built hereafter can be shown to improve on the ones examined here.

---
---

# Notes on Section 8

**389 words, 0.72 pages** against the 0.70 suggested. No citations, which is normal for a conclusion — every
statement in it restates a finding established and cited earlier, and the wording signals that ("The review
found…", "It found that…") so a reader does not mistake a restatement for a fresh claim.

**It does not propose a system.** Per your decision, the conclusion closes on the research agenda and the
precondition, consistent with the Introduction's promise that the review "does not propose, implement or
evaluate a system". Nothing here contradicts what Dr. Ho has already read.

**It does not repeat the abstract.** The abstract runs through the three contributions in order; the
conclusion runs through the three findings and then the chain that connects them, which is a different shape.
That matters because the two are read minutes apart.

**Structure:** question restated → the answer usually given is incomplete → three findings → the chain, which
is the actual contribution → the agenda and its precondition.

---

# Page budget — the body is complete

| Component | Pages |
|---|---|
| Title block | 0.50 |
| Abstract + keywords | 0.50 |
| 1 Introduction | 3.02 |
| 2 Review Methodology | 0.60 |
| 3 and subsections | 3.44 |
| 4 and subsections | 3.61 |
| 5 Models as Annotation Instruments | 0.93 |
| 6 Evaluating Annotation Reliability | 1.05 |
| 7 Synthesis | 2.82 |
| 8 Conclusion | 0.72 |
| Tables 1, 2, 3 | 0.72 |
| Figure 1 and caption | 0.38 |
| References, 37 entries at 8pt | 1.42 |
| **Total** | **19.73** |

**Under the 20-page cap, with 0.27 pages spare.** Worth knowing what that headroom is for: if you add the five
candidate references from the reference audit to reach Dr. Ho's 40+ target, that costs 0.19 pages, leaving
0.08. Anything beyond that has to come out of the body.

---

# The one content piece still outstanding

**The abstract has not been rewritten.** It still sits in the .docx from before this rewrite, and the paper
underneath it has changed substantially:

- The three contributions are worded differently now.
- The compounding chain, which is the paper's central claim, is not mentioned in it at all.
- It was written when the paper still closed by proposing a framework.

Dr. Ho reads the abstract first. If it describes a different paper from the one that follows, that is the
first thing he will notice. This is the last piece of writing the paper needs, and it should be written from
the finished body rather than patched.

---

# Reference list — 37 entries, unchanged

Section 8 adds no citations, so the list stands exactly as delivered. Reproduced here so this file is
self-contained. Template §11 format: all author names spelled out, no "et al." or "ibid.", single spacing,
8pt Times New Roman. The `.docx` version renders to 1.42 pages.

> **Still open with Dr. Ho.** These are author–date, per his comments 1 and 10. Template §11 asks for numbered
> `[n]` citations in order of appearance. Settle it before the final build.

Abu Bakar, M. F. R., Idris, N., Shuib, L., and Khamis, N. (2020). Sentiment analysis of noisy Malay text: State of art, challenges and future work. IEEE Access, 8, 24687–24696. https://doi.org/10.1109/ACCESS.2020.2968955

Adilazuarda, M. F., Cahyawijaya, S., Winata, G. I., Fung, P., and Purwarianti, A. (2022). IndoRobusta: Towards robustness against diverse code-mixed Indonesian local languages. Proceedings of the First Workshop on Scaling Up Multilingual Evaluation (SUMEval), 25–34.

AlAfnan, M. A., MohdZuki, S. F., and AlAfnan, S. M. (2025). Blending identities: Exploring the linguistic, cultural, and pragmatic dimensions of Manglish in the Malaysian society. Studies in Media and Communication, 13(3). https://doi.org/10.11114/smc.v13i3.7654

Artstein, R., and Poesio, M. (2008). Survey article: Inter-coder agreement for computational linguistics. Computational Linguistics, 34(4), 555–596. https://doi.org/10.1162/coli.07-034-R2

Bowman, S. R., and Dahl, G. (2021). What will it take to fix benchmarking in natural language understanding? Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, 4843–4855. https://doi.org/10.18653/v1/2021.naacl-main.385

Byrt, T., Bishop, J., and Carlin, J. B. (1993). Bias, prevalence and kappa. Journal of Clinical Epidemiology, 46(5), 423–429. https://doi.org/10.1016/0895-4356(93)90018-V

Cohen, J. (1960). A coefficient of agreement for nominal scales. Educational and Psychological Measurement, 20(1), 37–46. https://doi.org/10.1177/001316446002000104

Coluzzi, P. (2017). Language planning for Malay in Malaysia: A case of failure or success? International Journal of the Sociology of Language, 2017(244), 17–38. https://doi.org/10.1515/ijsl-2016-0055

Conneau, A., Khandelwal, K., Goyal, N., Chaudhary, V., Wenzek, G., Guzmán, F., Grave, E., Ott, M., Zettlemoyer, L., and Stoyanov, V. (2020). Unsupervised cross-lingual representation learning at scale. Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, 8440–8451. https://doi.org/10.18653/v1/2020.acl-main.747

Di Eugenio, B., and Glass, M. (2004). The kappa statistic: A second look. Computational Linguistics, 30(1), 95–101. https://doi.org/10.1162/089120104773633402

Doğruöz, A. S., Sitaram, S., Bullock, B. E., and Toribio, A. J. (2021). A survey of code-switching: Linguistic and social perspectives for language technologies. Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), 1654–1666. https://doi.org/10.18653/v1/2021.acl-long.131

Feinstein, A. R., and Cicchetti, D. V. (1990). High agreement but low kappa: I. The problems of two paradoxes. Journal of Clinical Epidemiology, 43(6), 543–549. https://doi.org/10.1016/0895-4356(90)90158-L

Frénay, B., and Verleysen, M. (2014). Classification in the presence of label noise: A survey. IEEE Transactions on Neural Networks and Learning Systems, 25(5), 845–869. https://doi.org/10.1109/TNNLS.2013.2292894

Gilardi, F., Alizadeh, M., and Kubli, M. (2023). ChatGPT outperforms crowd workers for text-annotation tasks. Proceedings of the National Academy of Sciences, 120(30), e2305016120. https://doi.org/10.1073/pnas.2305016120

Hutto, C. J., and Gilbert, E. (2014). VADER: A parsimonious rule-based model for sentiment analysis of social media text. Proceedings of the International AAAI Conference on Web and Social Media, 8(1), 216–225.

Jadhav, S., Shanbhag, A., Thakurdesai, A., Sinare, R., and Joshi, R. (2025). On limitations of LLM as annotator for low resource languages. Proceedings of the 8th International Conference on Natural Language and Speech Processing (ICNLSP-2025), 277–282.

Joshi, P., Santy, S., Budhiraja, A., Bali, K., and Choudhury, M. (2020). The state and fate of linguistic diversity and inclusion in the NLP world. Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, 6282–6293. https://doi.org/10.18653/v1/2020.acl-main.560

Kasmuri, E., and Basiron, H. (2019). Building a Malay-English code-switching subjectivity corpus for sentiment analysis. International Journal of Advanced Soft Computing and Its Applications, 11(1), 112–130.

Khanuja, S., Dandapat, S., Srinivasan, A., Sitaram, S., and Choudhury, M. (2020). GLUECoS: An evaluation benchmark for code-switched NLP. Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, 3575–3585. https://doi.org/10.18653/v1/2020.acl-main.329

Kong, J. T. H., Juwono, F. H., Ngu, I. Y., Nugraha, I. G. D., Maraden, Y., and Wong, W. K. (2023). A mixed Malay-English language COVID-19 Twitter dataset: A sentiment analysis. Big Data and Cognitive Computing, 7(2), 61. https://doi.org/10.3390/bdcc7020061

Manukonda, D. P., and Kodali, R. G. (2025). byteSizedLLM@DravidianLangTech 2025: Fake news detection in Dravidian languages using transliteration-aware XLM-RoBERTa and transformer encoder-decoder. Proceedings of the Fifth Workshop on Speech, Vision, and Language Technologies for Dravidian Languages, 176–181.

Maskat, R., and Rahman, N. A. (2020). Categorization of Malay social media text and normalization of spelling variations and vowel-less words. International Journal on Advanced Science, Engineering and Information Technology, 10(4), 1380–1386.

Maskat, R., Azman, N. A., Nulizairos, N. S. S., Zahidin, N. A., Mahadi, A. H., Norshamsul, S. R., Mohd Sharif, M. M., and Mahdin, H. (2024). A bi-annotated Malay-English code-switching (Manglish) dataset of X posts for biological gender identification and authorship attribution. Data in Brief, 52, 110034. https://doi.org/10.1016/j.dib.2024.110034

Mohammad, S. M. (2016). A practical guide to sentiment annotation: Challenges and solutions. Proceedings of the 7th Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis (WASSA), 174–179.

Mohd Shamsuddin, A. M., Samson Juan, S., Chua, S., and Bramantoro, A. (2024). Semi-automatic sentiment identification for Malay-English code-switched data. Journal of Advanced Research Design, 123(1), 198–212. https://doi.org/10.37934/ard.123.1.198212

Muysken, P. (2013). Language contact outcomes as the result of bilingual optimization strategies. Bilingualism: Language and Cognition, 16(4), 709–730. https://doi.org/10.1017/S1366728912000727

Nazir, A., Rao, Y., Wu, L., and Sun, L. (2022). Issues and challenges of aspect-based sentiment analysis: A comprehensive survey. IEEE Transactions on Affective Computing, 13(2), 845–863. https://doi.org/10.1109/TAFFC.2020.2970399

Northcutt, C. G., Athalye, A., and Mueller, J. (2021). Pervasive label errors in test sets destabilize machine learning benchmarks. Proceedings of the 35th Conference on Neural Information Processing Systems (NeurIPS): Datasets and Benchmarks Track.

Pavlick, E., and Kwiatkowski, T. (2019). Inherent disagreements in human textual inferences. Transactions of the Association for Computational Linguistics, 7, 677–694. https://doi.org/10.1162/tacl_a_00293

Pontiki, M., Galanis, D., Papageorgiou, H., Androutsopoulos, I., Manandhar, S., AL-Smadi, M., Al-Ayyoub, M., Zhao, Y., Qin, B., De Clercq, O., Hoste, V., Apidianaki, M., Tannier, X., Loukachevitch, N., Kotelnikov, E., Bel, N., Jiménez-Zafra, S. M., and Eryiğit, G. (2016). SemEval-2016 Task 5: Aspect based sentiment analysis. Proceedings of the 10th International Workshop on Semantic Evaluation (SemEval-2016), 19–30. https://doi.org/10.18653/v1/S16-1002

Poria, S., Hazarika, D., Majumder, N., and Mihalcea, R. (2023). Beneath the tip of the iceberg: Current challenges and new directions in sentiment analysis research. IEEE Transactions on Affective Computing, 14(1), 108–132. https://doi.org/10.1109/TAFFC.2020.3038167

Romadhona, N. P., Lu, S.-E., Lu, B.-H., and Tsai, R. T.-H. (2022). BRCC and SentiBahasaRojak: The first Bahasa Rojak corpus for pretraining and sentiment analysis dataset. Proceedings of the 29th International Conference on Computational Linguistics (COLING), 4418–4428.

Selvaraju, S., Sjarif, N. N. A., and Anuar, M. S. M. (2024). Sentiment analysis in code mixing Malay text: A review. 2024 5th International Conference on Artificial Intelligence and Data Sciences (AiDAS), 280–285. https://doi.org/10.1109/AiDAS63860.2024.10730298

Treffers-Daller, J., Majid, S., Thai, Y. N., and Flynn, N. (2022). Explaining the diversity in Malay-English code-switching patterns: The contribution of typological similarity and bilingual optimization strategies. Languages, 7(4), 299. https://doi.org/10.3390/languages7040299

Uma, A. N., Fornaciari, T., Hovy, D., Paun, S., Plank, B., and Poesio, M. (2021). Learning from disagreement: A survey. Journal of Artificial Intelligence Research, 72, 1385–1470. https://doi.org/10.1613/jair.1.12752

Winata, G. I., Aji, A. F., Yong, Z. X., and Solorio, T. (2023). The decades progress on code-switching research in NLP: A systematic survey on trends and challenges. Findings of the Association for Computational Linguistics: ACL 2023, 2936–2978. https://doi.org/10.18653/v1/2023.findings-acl.185

Winata, G. I., Cahyawijaya, S., Liu, Z., Lin, Z., Madotto, A., and Fung, P. (2021). Are multilingual models effective in code-switching? Proceedings of the Fifth Workshop on Computational Approaches to Linguistic Code-Switching, 142–153. https://doi.org/10.18653/v1/2021.calcs-1.20

