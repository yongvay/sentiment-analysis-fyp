# References used in the ICON AI 2026 review paper

**37 references, Sections 1 to 7.** Every one is peer-reviewed. None is an arXiv preprint.

I cross-checked the list against every in-text citation in the body, in both directions:

- **Cited but missing from the list: none.**
- **Listed but never cited: none.**

The one apparent exception is deliberate. Tay et al. (2016) and Ozog (1987) are named in Section 3.2 but do
not appear in the reference list, because they were read through Treffers-Daller et al. (2022) rather than
directly. Naming the original in the text while listing only the source you actually read is the correct APA
treatment for a secondary citation, and it is also the honest one.

---

## Where each reference is used

| Reference | Sections | PDF in your folder | How far I verified it |
|---|---|---|---|
| Abu Bakar (2020) | §1 | ✅ | ⚠ metadata only |
| Adilazuarda (2022) | §1, §5 | open access | ✅ read in full |
| AlAfnan (2025) | §1, §3, §3.2 | ✅ | ✅ read in full |
| Artstein & Poesio (2008) | §1, §6, §7 | open access | ✅ read in full |
| Bowman & Dahl (2021) | §1 | open access | ⚠ metadata only |
| Byrt (1993) | §1, §6, §7 | ✅ | ✅ read in full |
| Cohen (1960) | §1, §6 | ✅ | ✅ read in full |
| Coluzzi (2017) | §1 | ✅ | ⚠ metadata only |
| Conneau (2020) | §1 | open access | ⚠ metadata only |
| Di Eugenio & Glass (2004) | §1 | open access | ⚠ metadata only |
| Doğruöz (2021) | §1 | open access | ✅ read in full |
| Feinstein & Cicchetti (1990) | §1, §6, §7 | ✅ | ✅ read in full |
| Frénay & Verleysen (2014) | §1 | ✅ | ⚠ metadata only |
| Gilardi (2023) | §4.1 | open access | ⚠ metadata only |
| Hutto & Gilbert (2014) | §4.2 | open access | ✅ read in full |
| Jadhav (2025) | §4.1, §5 | open access | ✅ read in full |
| Joshi (2020) | §1 | open access | ⚠ metadata only |
| Kasmuri & Basiron (2019) | §1, §4.1, §4.2, §6 | ✅ | ✅ read in full |
| Khanuja (2020) | §1 | open access | ⚠ metadata only |
| Kong (2023) | §1, §4.1, §4.2, §6, §7 | ✅ | ✅ read in full |
| Manukonda (2025) | §5 | ✅ | ✅ read in full |
| Maskat (2020) | §1, §3.3 | ✅ | ✅ read in full |
| Maskat (2024) | §1 | open access | ⚠ metadata only |
| Mohammad (2016) | §7 | open access | ✅ read in full |
| Mohd Shamsuddin (2024) | §1, §3.1, §4.1, §4.2, §4.3, §6, §7 | ✅ | ✅ read in full |
| Muysken (2013) | §3, §3.1, §3.2 | ✅ | ⚠ metadata only |
| Nazir (2022) | §1, §3.1 | ✅ | ⚠ metadata only |
| Northcutt (2021) | §1 | open access | ⚠ metadata only |
| Pavlick & Kwiatkowski (2019) | §3.2, §4.2, §7 | open access | ✅ read in full |
| Pontiki (2016) | §3.1 | open access | ✅ read in full |
| Poria (2023) | §1 | ✅ | ⚠ metadata only |
| Romadhona (2022) | §1, §6 | ✅ | ✅ read in full |
| Selvaraju (2024) | §1, §4.2 | ✅ | ✅ read in full |
| Treffers-Daller (2022) | §1, §3, §3.1, §3.2 | ✅ | ✅ read in full |
| Uma (2021) | §4.3, §7 | open access | ✅ read in full |
| Winata (2021) | §1 | open access | ⚠ metadata only |
| Winata (2023) | §1 | open access | ⚠ metadata only |

---

## What the columns mean

**PDF in your folder** — ✅ means the file is in `References/`, 18 of 37. "Open access" means it is not
on your disk but I can read it from the ACL Anthology, AAAI, JAIR or a publisher's open page, so nothing is
unverifiable for want of a download. Worth having them locally anyway: if a source is cited in your paper,
you should be able to produce it in a viva.

**How far I verified it** — 21 of 37 were read in full and checked against the specific claim they support.
The remaining 16 were verified for citation metadata only: authors, year, title, venue, volume, pages, DOI.
Those all sit under claims that are either general or co-cited with a source I did read, so the risk is low.
The ones carrying the most weight — Mohd Shamsuddin, Treffers-Daller, Maskat and Rahman, Kasmuri and Basiron,
Kong, Romadhona, Feinstein and Cicchetti, Byrt, Artstein and Poesio — were all read in full, and reading them
is what caught the six errors corrected over the course of this rewrite.

---

## Against Dr. Ho's target

Round 1, comment 80: *"If possible, try increase the volume of references to at least 40. 24 references can be
a little low for a review paper."*

You are at **37**, up from 24. Three short, with Section 8 still to write. Five candidates that would each
earn their place rather than padding the count:

| Candidate | Where it would go | Why |
|---|---|---|
| Chakravarthi et al. (2022), *Language Resources and Evaluation* 56 | §4.2 | The sharper version of the second cause of neutral-label skew: neutral and mixed-feelings are the hardest categories for annotators. Currently carried by Kasmuri and Kong. |
| Landis and Koch (1977), *Biometrics* 33(1) | §6 | The other conventional κ interpretation scale. Artstein and Poesio already covers the CL convention, so this would add the biomedical one for contrast. |
| Gwet (2008), *British Journal of Mathematical and Statistical Psychology* 61(1) | §7, direction 2 | AC1, the best-known prevalence-robust alternative. Byrt's PABAK covers the point; Gwet would strengthen it. |
| Plank, Hovy and Søgaard (2014), ACL | §3.2, §4.2 | A second source for systematic rather than random annotator disagreement, alongside Pavlick and Kwiatkowski. |
| Ziems et al. (2024), *Computational Linguistics* 50(1) | §4.1, §5 | Peer-reviewed treatment of LLMs as annotators, which would partly replace what was lost when the Negi preprint was dropped. |

All five are peer-reviewed. Adding them takes you to 42.

---

## The list itself

Formatted per template §11: all author names spelled out, no "et al." and no "ibid.", single spacing, 8pt
Times New Roman. The `.docx` alongside this file is ready to paste into the paper and renders to 1.4 pages.

> **Citation style note.** These entries are author-date, following Dr. Ho's comments 1 and 10. Template §11
> asks for numbered `[n]` citations in order of appearance. That conflict is still unresolved — get one line
> from him before the final build, because converting 37 entries and roughly 90 in-text citations either way
> is a mechanical but tedious pass.


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
