# Citation fact check of the revised review paper

Audit date: 13 October 2026

Manuscript: NYV ID71 (Revising).docx, as read during this audit. Reference numbers below follow its 43-entry reference list. Locations use section titles, table numbers and identifiable wording rather than unverified Word page numbers. The manuscript has not been edited.

## Overall finding

The manuscript's central distinction between annotation agreement and label correctness is supported. Much of the dataset reporting and most of the general methodological discussion are also supported. However, the manuscript is not yet ready to be described as fully citation-verified. There are substantive problems with the MY-EN-CS class distribution and agreement scope, the summary of the Marathi LLM experiment, and the description of the ActiveAED evaluation. Several other sentences need narrower wording or clearer attribution as the review author's inference.

The audit covers the substantive claim groups throughout the abstract, Sections 1–7, and Tables 1–3, together with all 43 reference entries. Relevant original-source passages and tables were inspected; the two most consequential numerical findings were also checked against rendered source pages. This is a claim-support audit, not a replication of the underlying studies, a complete audit of their datasets, or a guarantee that the original papers are themselves correct.

Primary-source evidence was available for most references. Poplack [8] was not independently verified from accessible original full text; the general definition is supported by the co-cited review [7]. Krippendorff [39] was checked indirectly through Artstein and Poesio [26], not against the original 1980 book. Broad application claims supported by [3–6,20] were checked against accessible publisher/repository text or abstracts sufficient for those limited claims. Author-reported search dates, screening decisions and AI use cannot be authenticated from external citations.

Status meanings:

- **Supported:** the cited source supports the claim at approximately the stated scope.
- **Revise:** a number, scope, attribution or wording is inaccurate or stronger than the evidence.
- **Inference/proposal:** reasonable analytical reasoning or a recommendation, but not a demonstrated finding of the cited study.
- **Unverified:** insufficient original-source access or author records to establish the claim.

## Priority corrections

### 1. Correct the MY-EN-CS class distribution

**Locations:** Section 5 paragraph introducing Table 3; Table 3 MY-EN-CS row.

**Current claim:** the final 2,316-sentence corpus is 52% opinionated and 48% factual.

**Finding: Revise — the denominator and subset are mismatched.** Kasmuri and Basiron [22], Section 4.3, printed p. 126, describe 52%/48% in the discussion of the larger annotation exercise. Figure 6 reports 1,098 CS-MY-OPI sentences, 220 CS-EN-OPI sentences and 998 CS-FAC sentences. Sections 3.7 and 4.3 establish that those three categories form the delivered 2,316-sentence code-switched corpus. The aggregate prose in the source is not an adequate basis for assigning 52%/48% to that final subset.

For the final corpus, combining the two opinionated categories gives:

- Opinionated: (1,098 + 220) / 2,316 = **56.91%**.
- Factual: 998 / 2,316 = **43.09%**.

**Recommended Table 3 entry:** “Yes. 56.91% opinionated and 43.09% factual, calculated from the final-corpus counts in Figure 6 of [22].”

**Recommended prose:** “For the final MY-EN-CS corpus, combining the two opinionated categories gives 1,318 opinionated sentences (56.91%) and 998 factual sentences (43.09%), calculated from the published category counts [22].”

Remove the description of the final corpus as having a 52%/48% distribution. Make the aggregation and calculation explicit rather than presenting the new percentages as directly reported by the authors.

### 2. Do not describe MY-EN-CS kappa as a verified binary subjectivity coefficient

**Locations:** abstract; Introduction paragraph beginning “The second gap”; Table 2; Section 5 paragraph beginning “The studies introducing”; relevant summaries elsewhere.

**Current wording includes:** “Binary subjectivity annotation: opinionated versus factual. The reported kappa = 0.83 assesses subjectivity agreement.”

**Finding: Revise — the score is real, but this precise binary interpretation is not established.** The original paper [22], Sections 3.2–3.7 and 4.3, describes language-and-subjectivity categories: EN-OPI, EN-FAC, MY-OPI, MY-FAC, CS-EN-OPI, CS-MY-OPI and CS-FAC. It reports kappa = 0.83 for the annotation exercise. It does not provide a confusion matrix or an explicit calculation showing that kappa was computed after collapsing those categories into a binary opinionated/factual decision on the final subset. The exact coefficient variant is also not clearly documented.

**Recommended Table 2 scope:** “Language/subjectivity annotation scheme; kappa = 0.83 reported. Exact calculation and assessed subset are insufficiently specified. No positive/negative/neutral polarity agreement coefficient is reported.”

**Recommended prose:** “Kasmuri and Basiron [22] report a kappa value of 0.83 for their language-and-subjectivity annotation scheme. This is not evidence of agreement on positive, negative and neutral sentiment polarity labels.”

The broad distinction between subjectivity and polarity remains valid. The correction concerns how specifically the reported agreement score is characterised. Prefer “polarity agreement was not reported” to an assertion about an unreported procedure never having been performed.

### 3. Correct the summary of Jadhav et al.

**Location:** Section 4.1, paragraph beginning “Generative models offer another way”.

**Current claim:** GPT-4o and Llama 3.1 405B performed worse than a fine-tuned BERT model on four Marathi classification tasks, including sentiment analysis.

**Finding: Revise — contradicted by Table 1 of the cited published paper.** Jadhav et al. [33] evaluate six task/dataset configurations across three broad categories: sentiment, hate speech and news classification. For MahaSent, few-shot GPT-4o scores 0.82 and few-shot Llama 3.1 405B scores 0.81, compared with 0.80 for the fine-tuned BERT-based baseline. Their zero-shot scores are lower, and their average performance across the six configurations is lower than the BERT-based baselines. The broad narrative in the source must be read alongside its actual table.

**Recommended replacement:** “Jadhav et al. [33] evaluated LLMs on six Marathi classification configurations covering sentiment analysis, hate speech detection and news classification. GPT-4o and Llama 3.1 405B had lower average accuracy than the fine-tuned BERT-based baselines, although their few-shot scores on MahaSent were slightly higher. These results indicate that annotation performance depends on the task and prompting setup; they do not establish performance on Malay-English code-switched sentiment data.”

Do not describe the small MahaSent difference as statistically significant: the inspected table does not establish that.

Source: [published paper, Sections 3–6 and Table 1](https://aclanthology.org/2025.icnlsp-1.27.pdf).

### 4. State that ActiveAED simulated annotator corrections

**Location:** Section 6.5, “Weber and Plank [42] found that adding human corrections…”

**Finding: Revise — the reported improvement is supported, but the experimental qualification is missing.** ActiveAED repeatedly incorporates corrections into error detection. In the experimental setup, the authors explicitly simulate an annotator using gold-standard corrections; they do not model inter- or intra-annotator variation. Thus the evaluation is not direct evidence of a newly recruited human review team improving detection in practice.

**Recommended replacement:** “Weber and Plank [42] found that iteratively incorporating gold-standard corrections, used to simulate annotator feedback, improved annotation error detection over static baselines on most evaluated datasets.”

The paper reports improvements on seven of eight datasets, with gains up to six percentage points in average precision. The proposed human validation design for Manglish can remain clearly labelled as a future study.

Evidence: [42], experimental setup, PDF p. 4; [published record](https://aclanthology.org/2023.findings-acl.562/).

### 5. Remove an unsupported causal attribution to MESocSentiment

**Location:** Section 6.1, paragraph beginning “A highly skewed label distribution”.

**Problematic connection:** a model learns errors from noisy training labels, then propagates those same errors into new labels, “as illustrated by the sentiment analysers used to label MESocSentiment [24]”.

**Finding: Revise.** Frénay and Verleysen [19] support possible adverse effects of training-label noise. Mohd Shamsuddin et al. [24] report automatic labelling limitations and illustrative potentially incorrect labels. They do not establish that those errors originated in the analysers' own training labels. VADER and TextBlob also should not collectively be characterised as supervised classifiers trained on noisy labels without model-specific evidence.

**Recommended replacement:** “Label noise can reduce predictive performance [19]. Separately, using automatic systems to label new data can transfer their prediction errors into the resulting dataset. The examples reported for MESocSentiment illustrate potentially incorrect automatic labels [24], but do not establish the origin of those errors.”

### 6. Narrow the claim about the spelling-normalisation evaluation

**Location:** Section 3.3, “the evaluation excluded English words and code-mixed posts”.

**Finding: Revise the scope; retain the precision result.** Maskat and Rahman [13], Section II.A and Section III, report a highest precision of 0.429. Rounding to 0.43 is appropriate. The experiment focused on automatically detected “Undefined” and “Others” review subsets and excluded specified language-detection groups, including English/code-mixed review groups. It does not establish that every English word or every actual code-mixed item was absent from the evaluated material. Its similar-word-pair task is also narrower than end-to-end sentiment-preserving normalisation.

**Recommended replacement:** “The highest reported precision for identifying similar word pairs was 0.429 [13]. The evaluation focused on the ‘Undefined’ and ‘Others’ language-detection subsets and excluded identified English/code-mixed review groups. It therefore does not directly establish normalisation performance on Malay-English code-switched sentiment text.”

### 7. Attach the right evidence to mBERT's training data

**Location:** Introduction, “mBERT [9] … Wikipedia in the case of mBERT”.

**Finding: Citation fit needs improvement.** Devlin et al. [9] support BERT pretraining and downstream fine-tuning, but the inspected original BERT paper describes BooksCorpus and English Wikipedia and is not the best direct source for the multilingual Wikipedia training claim. The already-cited sources [7] and [15] explicitly discuss mBERT's multilingual Wikipedia data.

**Action:** retain [9] for BERT's architecture/pretraining approach; attach [7,15] to the specific mBERT-versus-XLM-R corpus comparison. Avoid implying that [9] alone documents the multilingual model's training corpus.

### 8. Make the kappa explanation conditional on annotator marginals

**Location:** Section 5, “When one label is far more common than the others, the agreement expected by chance rises, causing kappa to decrease…”; related Section 6.1 discussion.

**Finding: Supported principle, but overly automatic wording.** Kappa depends on observed agreement and both annotators' marginal distributions. At fixed observed agreement, larger expected agreement lowers kappa. A final dataset's majority-label distribution alone does not determine either expected agreement or kappa.

**Recommended replacement:** “When both annotators use the same category disproportionately, expected agreement can be high. For a fixed level of observed agreement, this reduces kappa [27–29]. The final class distribution alone is insufficient to calculate this effect; paired annotation data are needed.”

The manuscript correctly reproduces Di Eugenio and Glass's two examples: 90% observed agreement, with kappa 0.80 versus approximately −0.048. Retain those examples.

### 9. Attribute the reliability thresholds precisely

**Location:** Section 5, discussion of [26,39].

**Finding: Partly supported through a secondary source; improve precision.** Artstein and Poesio [26], Section 3.4, printed p. 576, discuss thresholds originally associated with Krippendorff's alpha and explain the history and limitations of transferring them to other coefficients. The manuscript's caution against universal cutoffs is appropriate, but “a reliability measure” is unnecessarily vague in a paragraph centred on Cohen's kappa.

**Recommended replacement:** “Artstein and Poesio [26] discuss interpretive guidance associated with Krippendorff's alpha, including the 0.8 and 0.67 thresholds, while warning that agreement values depend on the task and measurement choices. These thresholds should not be treated as universal pass/fail criteria for Cohen's kappa or as evidence of label correctness.”

The original 1980 book [39] was not directly verified in this audit. If you have not consulted it, use an explicit secondary attribution to [26] rather than implying firsthand consultation.

### 10. Qualify proposed extensions of binary agreement adjustments

**Location:** Section 6.3, final sentence.

**Finding: Proposal, not an established application to three classes.** The two-rater, binary setting of Byrt et al. [28] and the binary examples and adjustments in Di Eugenio and Glass [29] are correctly recognised. However, “applying these analyses” to three-class sentiment needs an explicit qualification: binary formulas should not simply be reused unchanged.

**Suggested addition:** “Any extension to three sentiment classes would require an explicitly justified multicategory formulation and evaluation.”

The claim that these particular diagnostics are not reported in the four resource papers is supported by inspection of those papers. It is not a claim that no other researchers have used them.

### 11. Replace absolute or unmeasured language-frequency claims

**Locations:** Section 6.1, “Manglish text is usually written with non-standard spellings”; Section 6.4, “lah and kan … cues that no lexicon entry can capture”.

**Finding: Revise.** The cited linguistic and noisy-text papers support the occurrence and contextual importance of informal forms, but do not establish “usually” for Manglish text generally. Context dependence does not prove that no lexicon entry can encode any useful information about a particle. The immediate citations [31] and [10] concern sentiment guidelines rather than direct evidence about lah and kan.

**Suggested wording:** “Manglish social-media text can contain non-standard spellings and context-dependent particles [12–14,32].”

**Suggested wording:** “Guidelines should include worked examples of context-dependent particles such as lah, whose contribution cannot reliably be represented by a fixed positive or negative lexical score alone [12,32].”

Retain kan only with a directly checked source for the specific pragmatic claim. The recommendation to develop such guidance is the review's proposal, not a finding that these particular guidelines have already been tested.

### 12. Clarify what the social-media comparison actually measures

**Locations:** Introduction comparison dimensions; Table 3 “Social-media language” column; Section 5.

**Finding: The source descriptions are supported; representativeness is an author judgement.** Blog origin, COVID-related tweets, stock-forum posts and generated product/movie examples are documented. These sources do not establish statistical representativeness of everyday Malaysian social-media language. Blogs are also a form of social media, so “Partly. Blog posts” requires a stated criterion rather than treating blog origin itself as evidence of partial social-media status.

**Recommended table change:** use “Text source and domain” and record “personal blog sentences”, “generated product/movie reviews plus 693 stock-forum posts”, “COVID-related tweets”, and “tweets collected using #Malaysia”. Discuss any judgement about everyday relevance separately.

### 13. Keep the language-resource scope accurate

**Locations:** descriptions of the four resources in the Introduction and resource tables.

**Finding: Add a qualification.** MyCovid-Senti includes Malay and English material rather than a demonstrated collection containing only within-message Malay-English switching. SentiBahasaRojak also includes Chinese in its augmentation design. Calling these resources “relevant to Malay-English sentiment analysis” is defensible; implying that every item is naturally occurring Malay-English code-switched text is not.

**Suggested clarification:** “These resources differ in language composition and construction: they include subjectivity labels, monolingual as well as mixed-language material, and both naturally occurring and automatically generated text.”

The present Section 4.1 already acknowledges generated examples and Chinese for SentiBahasaRojak; carry that precision into the comparative framing.

### 14. Distinguish the source authors' positive judgements from demonstrated Malay polarity cues

**Location:** Introduction, “three contain Malay expressions with positive polarity”; related abstract/conclusion summaries.

**Finding: Use the more defensible attribution already present in Section 4.2.** [24] provides three neutral-labelled examples which its authors judged positive. It does not establish that all three are unambiguous positive Malay expressions. In particular, the championship report does not unambiguously express the writer's attitude; [24] also acknowledges language-identification noise in its corpus.

**Recommended wording throughout:** “Three published examples were labelled neutral by the tools but interpreted as positive by the original authors [24]. Their interpretation depends partly on the annotation guidelines.”

Retain the review's more detailed distinction between the village description, the greeting and the sporting-result report. Present the alternative sporting interpretation as your analysis informed by Mohammad [31], not as a reannotation performed in either cited study. Six selected examples do not establish an error rate or the prevalence of missed cues.

### 15. Clarify the subjectivity-versus-event example

**Location:** Section 4.1, after “An opinionated label does not indicate whether the sentiment expressed is positive or negative.”

**Current next sentence:** “It may report a positive or negative event without expressing the writer's opinion…”

**Finding: Ambiguous referent affects the claim.** “It” appears to refer to an opinionated label or opinionated text, whereas the intended example is a factual event description. Mohammad [31] supports distinguishing event valence from speaker attitude.

**Recommended replacement:** “Conversely, a factual sentence may describe a favourable or unfavourable event without expressing the writer's attitude. Its sentiment label depends on the annotation guidelines [31].”

### 16. Fix an omitted reference author

**Location:** reference [17], GLUECoS.

**Finding: Bibliographic error.** The published paper has five authors: Simran Khanuja, Sandipan Dandapat, Anirudh Srinivasan, Sunayana Sitaram and **Monojit Choudhury**. The manuscript omits Choudhury.

Add “and Choudhury, M.” to [17]. The DOI and cited substantive result are appropriate. [Official bibliographic record](https://aclanthology.org/2020.acl-main.329/).

### 17. Distinguish missing agreement coefficients from no reliability assessment

**Location:** Section 5, “the reviewed studies do not provide evidence that label reliability has been assessed for the three-class sentiment distinction”.

**Finding: Narrow the conclusion.** The publications do not report the particular human inter-annotator agreement coefficient sought here. That is narrower than demonstrating an absence of any label-quality assessment. For example, [24] includes manually checked examples, which your review itself discusses. Those examples are limited evidence, not a comprehensive reliability estimate, but should not disappear under a blanket absence claim.

**Recommended replacement:** “None of the four reviewed publications reports a human inter-annotator agreement coefficient specifically for three-class positive, negative and neutral sentiment annotation. The limited qualitative checks reported for MESocSentiment do not provide an overall reliability estimate.”

## Numerical verification

| Manuscript quantity | Check | Result |
|---|---|---|
| Maskat et al.: 709,012 posts from 50 public figures | [11], abstract/specifications | Supported; these are raw posts. The processed corpus has 650,409 posts. Adding “raw” improves precision. |
| MY-EN-CS: 2,316 sentences | [22], Section 4.3 and conclusion | Supported. |
| MY-EN-CS: 52%/48% in the final corpus | [22], Figure 6 and final-corpus selection | Revise to calculated 56.91%/43.09%, with aggregation explained. |
| MY-EN-CS: kappa 0.83 | [22], Section 4.3 | Value supported; binary interpretation and exact assessed subset not established. |
| SentiBahasaRojak: 2,285 items | [23], Table 7: 893 + 699 + 693 | Supported. |
| SentiBahasaRojak: 693 natural stock posts | [23], Section 3.4.3/Table 7 | Supported. The remaining 1,592 product/movie examples use augmentation. |
| SentiBahasaRojak: five annotators, kappa 0.77 | [23], Section 3.4.3 | Supported for stock subset; the coefficient calculation is not specified. Majority voting determined final stock labels. |
| MyCovid-Senti: 11,568 tweets | [10], Table 3 | Supported. |
| MyCovid-Senti: 23.6% neutral | 2,728 / 11,568 × 100 = 23.5823% | Supported rounding. |
| MyCovid-Senti: largest class 48.9% | 5,655 negative / 11,568 × 100 = 48.8849% | Supported rounding; no absolute-majority class. |
| MESocSentiment: 20,226 before exclusions, 512 excluded, 19,714 retained | [24], Tables 3–4 | Supported: 20,226 − 512 = 19,714. |
| MESocSentiment: 15,422 neutral, 3,219 positive, 1,073 negative | [24], Table 4 | Supported; sum = 19,714. |
| MESocSentiment: 78.23%, 16.33%, 5.44% | Counts divided by 19,714 | Supported rounding. |
| Table 1 TextBlob: 14,305 and 72.56% | [24], Table 8; divide by 19,714 | Supported. |
| Table 1 VADER: 13,115 and 66.53% | [24], Table 8; divide by 19,714 | Supported. |
| Table 1 pysentimiento: 16,916 and 85.81% | [24], Table 8; divide by 19,714 | Supported. |
| Neutral share before removal: 76.25% | 15,422 / 20,226 × 100 = 76.2484% | Supported recalculation. Original [24] prints 76.23%; your recalculation correctly avoids repeating that arithmetic discrepancy. |
| Increase after exclusion: 1.98 percentage points | 78.2287 − 76.2484 = 1.9803 | Supported. Clarify that the pre-exclusion denominator includes the no-majority items. |
| Six manual examples, including three authors judge positive despite neutral labels | [24], Tables 6–7 | Supported as illustrative examples; not a random error-rate estimate. |
| Spelling-match precision 0.43 | [13], Section III/Table VIII: 0.429 | Supported rounding; not normalisation accuracy over all text. |
| Pavlick and Kwiatkowski: 50 judgements per item | [36], Section 3.2 | Supported for the relevant NLI collection. |
| Di Eugenio and Glass: 90% agreement with kappa 0.80 vs −0.048 | [29], Figure 3 | Supported. |
| Marathi classification described as four tasks with uniformly worse LLM performance | [33], Sections 3–6/Table 1 | Revise: six configurations; few-shot MahaSent exception. |

## Claim coverage by manuscript location

Related clauses with the same evidence are grouped below. Repeated claims in the abstract and conclusion inherit the same verdict as the detailed treatment. “Supported” does not mean the cited work proves universal applicability or independently establishes the correctness of its own data.

| Location and claim group | Citation(s) | Verdict and action |
|---|---|---|
| Abstract: reliable labels matter for training/evaluation | Body evidence [19–21] | Supported rationale. |
| Abstract: studies selected from named databases | Author methods | Author-reported; external citations cannot verify. Reconcile database list with Section 2, which includes Google Scholar. |
| Abstract: linguistic features and three annotation approaches | [12–14,22–24,32–33] in body | Supported as thematic organisation; revise the detailed LLM finding in 4.1. |
| Abstract: four resources compared without universal size threshold | Review design | Author-defined scope, not a cited empirical result. Appropriate when stated that way. |
| Abstract: two resources lack agreement coefficients | [10,24] in body | Supported as “not reported in the reviewed papers”. |
| Abstract: MY-EN-CS and SentiBahasaRojak agreement scope | [22,23] | Revise MY-EN-CS precision; stock-subset restriction is supported. |
| Abstract: agreement does not prove correctness | [26] in body | Supported. |
| Abstract: neutral proportion, six examples, sporting caveat | [24,31] in body | Counts supported; alternative interpretation is the review's inference. |
| Abstract: missed cues, shared errors, imbalance and research priorities | [26–29,34–43] in body | Supported principles and clearly framed proposals; do not imply causal mechanisms were tested on MESocSentiment. |
| Introduction: sentiment analysis/opinion mining definition | [1] | Supported. |
| Introduction: applications in products, health, politics and finance | [2–5] | Broad application domains supported. “Sentiment analysis is used/studied in…” is more precise than implying every source documents deployed organisational use. |
| Introduction: resource inequality across languages | [6] | Supported. |
| Introduction: code-switching definition | [7,8] | Supported by [7]; [8] original full text unverified. Definition should allow switching across utterances as well as within one. |
| Introduction: monolingual training and reduced performance on switched text | [7] | Supported, qualified with “may/can”. |
| Introduction: lexicon/model can miss other-language sentiment | [7] and analytical explanation | Plausible inference; not a measured Malay-English effect established by that survey. |
| Introduction: pretrained models can be fine-tuned | [9] | Supported. The review's “sentiment tool” versus “language model” terminology is its operational distinction; the categories can overlap. |
| Introduction: Malaysian mixed-language social-media use | [10] | Supported as occurrence; avoid interpreting the study as a nationally representative frequency survey. |
| Introduction: 709,012 raw posts, 50 public figures | [11] | Supported; source selected accounts with approximately 60% or more Manglish posts. |
| Introduction: definition of Manglish limited to Malay-English switching | Review definition | Acceptable operational scope; not a claim that every linguistic use of “Manglish” has this definition. |
| Introduction: switching patterns, x/tidak and camne/macam mana | [12,13] | Supported. |
| Introduction: noisy spelling can hinder systems | [14] | Supported general concern; model-specific coverage is an inference. |
| Introduction: multilingual corpora and capacity tradeoff | [7,9,15] | [7,15] support corpus and capacity discussion. Reattach mBERT training-data claim to appropriate evidence. |
| Introduction: multilingual pretraining does not guarantee switched representations | [16] | Supported by the paper's conclusion; findings concern its evaluated language pairs/tasks. |
| Introduction: further switched-data training can help and varies by conditions | [17,18] | Supported; [17] uses synthetic switched data; [18] studies Indonesian combinations and tuning strategies. |
| Introduction: noisy training labels can damage predictions | [19] | Supported as a possibility, not inevitability. |
| Introduction: erroneous test labels affect evaluation/model comparisons | [20] | Supported. |
| Introduction: valid benchmarks, statistical power, harmful social bias | [21] | Supported by proposed criteria; these are the source authors' recommendations. |
| Introduction: abbreviation practices and Malayanization examples | [14,22] | Supported, including kompem and hensem. |
| Introduction: agreement/correctness distinction and defensible disagreement | [26,31,35] | Supported conceptual synthesis. |
| Introduction: four comparison dimensions and >50% definition | Review design | Valid explicit definitions; source data must be correct and representativeness must not be assumed. |
| Introduction: neutral majority and three “positive Malay expressions” | [24] | Counts supported; narrow language/positive attribution as correction 14. |
| Introduction: agreement gaps across resources | [10,22–24] | Absence of reported coefficients supported; revise binary MY-EN-CS interpretation. |
| Introduction: Cohen's kappa and multirater alternatives | [25,26] | Supported. Artstein/Poesio use multi-π for Fleiss's generalisation of Scott's π and multi-κ for the generalisation of Cohen's κ. |
| Introduction: sensitivity to label marginals | [27–29] | Supported with the conditional explanation in correction 8. |
| Introduction: publicly accessible Manglish resources scarce | [11] | Supported as that paper's observation; add “Maskat et al. [11] noted…” to avoid an unverified exhaustive current claim. |
| Introduction: comparison with earlier reviews | [1,7,14,30] | Their described topics are supported. Your novelty positioning is a reasoned comparison, not proof that no similar review exists. |
| Section 2: dates, search tools, criteria, AI assistance, screening and extraction | Author methods | Cannot be externally authenticated. Report only actual practice; “all relevant resources identified through our search” is not proof of exhaustive coverage. |
| Section 2: four resources and fields extracted | [10,22–24] and manuscript tables | Resource identities/fields check out; correct the derived values and scope in the tables. |
| 3.1: classroom switching and limits of social-media generalisation | [12] | Supported. “Within-sentence switching” matches the source's explicit framing more closely than treating its sample as a general estimate of within-clause frequency. |
| 3.1: bilingual competence alone insufficient; multiple targets need guidance | [31] | Supported principle; specific Manglish extension is analytical. |
| 3.2: lah pragmatics, secondary Tay attribution, softened instruction | [12,32] | Supported. The “Don't disturb la, he's busy” example is in [32], Table 4. Secondary attribution to Tay is correctly explicit. |
| 3.2: a fixed positive/negative score is inadequate; guidelines needed | [12,32] and synthesis | Reasonable inference/proposal; not a sentiment-annotation experiment in those papers. |
| 3.3: jgn/mcmana and nonstandard spelling | [13] | Supported by its spelling tables. |
| 3.3: 0.43 precision and excluded material | [13] | Precision supported; narrow exclusion and task scope as correction 6. |
| 3.3: missed x negation can alter sentiment; preserve sentiment when normalising | [13] plus inference | x/tidak mapping supported; effect and evaluation criterion are plausible inference/proposal. |
| 4.1: bilingual human annotation requires time/proficiency | [24] | Supported motivation; any superiority claim should remain “may”, as written. |
| 4.1: MY-EN-CS human labelling and MyCovid-Senti three annotators/guidelines | [22,10] | Supported. |
| 4.1: subjectivity differs from polarity | [22,31] | Supported; clarify factual event example and avoid claiming the kappa is binary. |
| 4.1: SentiBahasaRojak generated product/movie examples and human stock labels | [23] | Supported, including Chinese augmentation and five experts. |
| 4.1: three tools, majority voting and semi-automatic construction | [24] | Supported. The sentiment assignment is automatic; limited published manual checks are correctly acknowledged later. |
| 4.1: Marathi LLM experiment | [33] | Substantive correction required: task count, averages, few-shot exception. |
| 4.1: no reviewed study tests generative Manglish sentiment annotation | Selected-paper scope | Supported for the cited set as inspected; do not expand to “no study exists”. |
| 4.2: MESocSentiment class distribution and alternative causes | [24] | Counts supported; causal alternatives are hypotheses. |
| 4.2: MyCovid-Senti neutral comparison | [10,24] | Numbers supported and domain caveat appropriate. Difference alone does not demonstrate mislabelling. |
| 4.2: VADER lexicon/rules and neutral range | [34] | Supported at mechanism level. Malay cue failure is plausible, not demonstrated by an isolated tool-level error analysis here. |
| 4.2: six examples and their interpretations | [24,31] | Source descriptions supported; retain attribution, task dependence and no-error-rate caveat. |
| 4.2: human label variation and 50 NLI judgements | [35,36] | Supported. |
| 4.2: more context increased disagreement in the cited experiment | [36] | Supported for that context experiment, not a universal law. |
| 4.2: distinguish neutral, unclear and mixed cases | [31,35] and proposal | Appropriate task-definition recommendation. Neutral is not defined identically in every dataset. |
| 4.3: majority voting weights equally and fails with wrong majority | [37] | Supported; the condition is the same incorrect label winning, not merely several different errors. |
| 4.3/Table 1: all tools assign majority neutral | [24] | Supported; all four displayed percentages recalculate correctly. |
| 4.3: pysentimiento languages and English-tweet model rationale | [24] | Supported as the toolkit description/use reported in 2024. Phrase historically rather than as a verified current software inventory. |
| 4.3: totals cannot identify shared errors | [24] and logic | Correct; joint predictions and independent reference judgements are required. |
| 4.3: exclusions and denominator effect | [24] plus calculation | Supported. A tie among three distinct sentiment classes implies one vote each. |
| 4.3: preserve disagreeing items and labels | [38] and proposal | Supported methodological motivation; no proof the excluded MESocSentiment items were permanently destroyed. |
| Section 5: agreement is not correctness; shared bias possible | [25,26] | Supported. |
| Section 5: reliability thresholds | [26,39] | Secondary support only for [39]; name alpha and preserve caution. |
| Section 5: prevalence example and item-level correspondence | [29] | Supported; final majority counts alone are inadequate. |
| Section 5: per-class reporting and no universal single coefficient | [26,29] and proposal | Reasonable recommendation; specify which per-class agreement measure will be used in future empirical work. |
| Table 2: MY-EN-CS evidence | [22] | Two bilingual students and 0.83 supported; binary scope needs correction. |
| Table 2: SentiBahasaRojak evidence | [23] | Supported; other subsets' text is generated, which should not be confused with proving their inherited labels were freshly machine-annotated. |
| Table 2: MyCovid-Senti/MESocSentiment absent coefficients | [10,24] | Supported as absence in the original papers. |
| Section 5: five annotators and unspecified kappa calculation | [23,25,26] | Supported concern. Narrow the final absence-of-evidence sentence as correction 17. |
| Table 3: corpus sizes, majority classes and agreement summaries | [10,22–24] | Sizes and most class counts supported; MY-EN-CS proportions/scope and social-media judgements need correction. |
| 6.1: connected linguistic/tool/annotation challenges | Earlier evidence | Reasoned synthesis; soften “usually” and avoid asserting measured shared errors. |
| 6.1: automatic labelling motivated by time/cost | [24] | Supported as motivation, not a quantified cost comparison. |
| 6.1: training-label errors caused errors in MESocSentiment | [19,24] | Unsupported causal connection; separate the two claims. |
| 6.2: provenance, annotator backgrounds, language variety | [40] | Supported by Data Statements. |
| 6.2: retaining individual annotations avoids loss of variation | [41] | Supported motivation. The 512 removals document exclusion from the final corpus, not the authors' private retention practices. |
| 6.3: bias/prevalence reporting | [28,29] | Supported in specified settings; multicategory extension is a proposed investigation. |
| 6.4: contextual particle guidance | [12,32] should be attached | Proposal supported by linguistic rationale; “no lexicon entry” is too absolute. |
| 6.4: Mohammad framework and Kong adaptation | [31,10] | Supported; Kong explicitly cites the semantic-role-based questionnaire. |
| 6.4: distinguish plausible variation from errors | [35] | Supported. Guidelines may reduce avoidable ambiguity but cannot eliminate all legitimate disagreement. |
| 6.5: independent validation and proposed bilingual review design | [26,37] plus proposal | Reasonable proposal; independent labels are not guaranteed ground truth. Allow unresolved cases. |
| 6.5: ActiveAED improvement | [42] | Supported after stating gold-standard simulated feedback. |
| 6.5: VariErr explanations and validity judgements | [43] | Supported. Same annotators returned as judges; the separate reviewer group in your text is your proposed adaptation. |
| 6.5: comparison “would show” shared errors | Proposal | Prefer “could help assess” because human reference labels can also be fallible. |
| 6.6: missing records, single reviewer, no independent reannotation | Author methods | Unverified externally; must accurately reflect your own work. |
| 6.6: task/domain differences limit comparability; absent evidence does not prove unusability | Reviewed sources and logic | Supported interpretation. |
| Conclusion: limited evidence and future validation | Body evidence | Broad conclusion supported after propagating the MY-EN-CS and source-scope corrections. |

## Reference-by-reference evidence ledger

“Source location” identifies the relevant evidence, not an assertion that every page of a long book or survey was exhaustively evaluated. Source links and local copies follow in the final section.

| Ref. | Evidence used | Assessment of its use in this manuscript |
|---|---|---|
| 1 Poria et al. | Introduction and survey scope | Supports sentiment-analysis definition and broad review comparison. |
| 2 Liu | Author-hosted book; applications and supervised sentiment classification | Supports products/services applications and labelled-training explanation. |
| 3 Zunic et al. | Publisher/PMC abstract and review scope | Supports health/well-being application area. |
| 4 Chauhan et al. | Publisher abstract and paper scope | Supports social-media sentiment/election application area. |
| 5 Du et al. | Author-hosted published survey, abstract/introduction | Supports financial applications. |
| 6 Joshi et al. | ACL abstract | Directly supports resource/language representation inequality; only this broad claim was needed. |
| 7 Doğruöz et al. | Sections on computational limitations and monolingual pretraining, PDF pp. 6–7 | Supports code-switching background, corpus exposure and performance concerns. |
| 8 Poplack | Original full text not obtained | Unverified individually. Co-citation [7] supports the general definition. |
| 9 Devlin et al. | Pretraining/fine-tuning sections | Supports BERT approach; use [7,15] for multilingual Wikipedia details. |
| 10 Kong et al. | Sections 2.2–2.3/Table 3; paper searched for agreement reporting | Supports 11,568, three annotators, class counts and adapted questionnaire; no agreement coefficient found. |
| 11 Maskat et al. | Abstract/specifications, Background and limitations | Supports raw/processed counts, 50 figures, Manglish selection threshold and contemporary scarcity observation. |
| 12 Treffers-Daller et al. | Particle discussion and empirical classroom study | Supports switching and contextual particles; does not measure social-media prevalence. |
| 13 Maskat and Rahman | Spelling tables, experiment subsets, precision results | Examples/result supported; narrow the exclusion claim and task interpretation. |
| 14 Abu Bakar et al. | Abstract/introduction, preprocessing discussion | Supports noisy Malay spelling and abbreviation challenges; keep pretrained-model implications cautious. |
| 15 Conneau et al. | Corpus description, model-capacity/language-number analysis | Supports Common Crawl, mBERT Wikipedia comparison and curse of multilinguality. |
| 16 Winata et al. | Conclusion and evaluated tagging tasks | Supports lack of guarantee from multilingual pretraining. |
| 17 Khanuja et al. | Abstract/introduction, synthetic-data adaptation | Supports improvement claim; add omitted author Choudhury. |
| 18 Adilazuarda et al. | Sections 3–4, Table 2 | Supports dependence on language/task/training setup; Indonesian scope, not direct Manglish evidence. |
| 19 Frénay and Verleysen | Abstract and label-noise consequences | Supports possible reduced predictive accuracy; not the origin of MESocSentiment errors. |
| 20 Northcutt et al. | NeurIPS abstract with corrected-label model comparisons | Supports effects of evaluation-label errors on model comparisons. |
| 21 Bowman and Dahl | Figure 1 and proposed benchmark criteria | Supports validity, annotation, power and bias discussion. |
| 22 Kasmuri and Basiron | Sections 3.2–3.7, 4.3, Figure 6 | Supports corpus and procedure, but requires correction of final-subset proportions and binary-kappa interpretation. |
| 23 Romadhona et al. | Sections 3.4.1–3.4.3/Table 7 | Supports total size, generation, five experts and stock-subset kappa; class distribution/variant not specified in inspected paper. |
| 24 Mohd Shamsuddin et al. | Methods, Tables 3–8, discussion/conclusion | Supports counts, tools, removal and examples; not a training-noise causal experiment or overall error-rate estimate. |
| 25 Cohen | Coefficient definition and chance term | Supports two-rater nominal kappa. |
| 26 Artstein and Poesio | Sections 2.1, 2.5, 3.4 and recommendations | Supports agreement/validity distinction, multiple-rater terminology and contextual interpretation. |
| 27 Feinstein and Cicchetti | Abstract and two-observer binary paradox discussion | Supports high-agreement/low-kappa concern with marginals. |
| 28 Byrt et al. | Abstract and binary derivation | Supports bias/prevalence diagnostics; not automatic multicategory application. |
| 29 Di Eugenio and Glass | Figure 3 and concluding recommendations | Supports 0.80/−0.048 example and companion diagnostic measures. |
| 30 Nazir et al. | Abstract/survey scope | Supports broad aspect-based sentiment-review comparison. |
| 31 Mohammad | Challenges and proposed questionnaires | Supports target/attitude distinction, valenced-event ambiguity and guideline design. |
| 32 AlAfnan et al. | Methods and pragmatic-functions Table 4 | Supports scripted-dialogue particle examples, not prevalence in spontaneous social-media text. |
| 33 Jadhav et al. | Sections 3–6/Table 1 visually checked | Current summary incorrect; replace with average-performance finding plus sentiment exception. |
| 34 Hutto and Gilbert | Lexicon/rules and classification thresholds | Supports VADER mechanism; Malay failure mechanism is a hypothesis. |
| 35 Plank | Abstract and human-label-variation argument | Supports reasonable disagreement and criticism of single-label reduction. |
| 36 Pavlick and Kwiatkowski | Section 3.2 and context experiment | Supports 50 raters and increased disagreement in that experiment. |
| 37 Hovy et al. | Introduction's majority-voting/spammer example | Supports equal weighting and possible wrong majority; application to sentiment tools is a valid conditional analogy. |
| 38 Uma et al. | Disagreement-preserving datasets and learning framework | Supports retaining disagreement; not a finding about the content of removed MESocSentiment posts. |
| 39 Krippendorff | Indirectly via [26], Section 3.4 | Original book unverified; make secondary attribution explicit. |
| 40 Bender and Friedman | Data Statement schema, language/speaker/annotator fields | Supports provenance/background recommendation. |
| 41 Mostafazadeh Davani et al. | Introduction and individual-annotator modelling | Supports retaining individual variation rather than only majority labels. |
| 42 Weber and Plank | Abstract/results and experimental setup | Improvement supported; human feedback simulated with gold corrections. |
| 43 Weber-Genzel et al. | Sections 3.1–3.2 | Supports explanations and subsequent validity judgements in English NLI. |

## Source access and audit boundaries

External verification establishes what a paper reports, not whether its dataset labels are truly correct. “No agreement coefficient reported” is scoped to the inspected publications; this audit does not rule out subsequent repositories or publications containing additional analyses. Current software language support was not audited; describe pysentimiento as used/reported in [24]. General causal suggestions about Manglish remain hypotheses unless a cited experiment actually tests them.

Section 2 contains statements only you can authenticate: dates, actual database use, search and screening procedure, whether themes were set before reading, author roles, use of AI and completeness of the selected set. These should not receive a “verified” stamp merely because the manuscript states them. Likewise, neither a narrative-review label nor an explicit limitation establishes exhaustive coverage.

A bibliography-format audit of every conference date, name initial and punctuation mark was outside the core claim-support check. The omitted author in [17] is a confirmed metadata issue encountered during verification.

### Primary web sources used for references not already available locally

- [2 Liu, author-hosted book](https://www.cs.uic.edu/~liub/FBS/SentimentAnalysis-and-OpinionMining-Survey-Book.pdf)
- [3 Zunic et al., PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC7013658/)
- [4 Chauhan et al., publisher article](https://link.springer.com/article/10.1007/s12652-020-02423-y)
- [5 Du et al., author-hosted survey](https://sentic.net/financial-sentiment-analysis-survey.pdf)
- [6 Joshi et al., ACL record](https://aclanthology.org/2020.acl-main.560/)
- [16 Winata et al.](https://aclanthology.org/2021.calcs-1.20.pdf)
- [17 Khanuja et al.](https://aclanthology.org/2020.acl-main.329.pdf)
- [18 Adilazuarda et al.](https://aclanthology.org/2022.sumeval-1.5.pdf)
- [20 Northcutt et al., NeurIPS record](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/f2217062e9a397a1dca429e7d70bc6ca-Abstract-round1.html)
- [21 Bowman and Dahl](https://aclanthology.org/2021.naacl-main.385.pdf)
- [33 Jadhav et al.](https://aclanthology.org/2025.icnlsp-1.27.pdf)
- [38 Uma et al., author-hosted article](https://www.dirkhovy.com/publication/2021-learning_from_disagreement_survey/2021-learning_from_disagreement_survey.pdf)
- [41 Mostafazadeh Davani et al.](https://aclanthology.org/2022.tacl-1.6.pdf)
- [43 Weber-Genzel et al.](https://aclanthology.org/2024.acl-long.123.pdf)

Local source copies used are listed below with manuscript reference numbers. Page numbers mentioned in findings refer to these original papers, not to the review manuscript.


- Reference [1]: [Poria, S., Hazarika, D., Majumder, N., and Mihalcea, R. (2023).pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/Review Paper/Poria, S., Hazarika, D., Majumder, N., and Mihalcea, R. (2023).pdf>)
- Reference [7]: [Doğruöz (2021).pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/Review Paper/Doğruöz (2021).pdf>)
- Reference [9]: [Devlin et al. (2019), BERT.pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/C3/Devlin et al. (2019), BERT.pdf>)
- Reference [10]: [Kong(2023) A mixed Malay-English language COVID-19 Twitter dataset A sentiment analysis.pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/General/Kong(2023) A mixed Malay-English language COVID-19 Twitter dataset A sentiment analysis.pdf>)
- Reference [11]: [Maskat et al. (2024).pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/C3/Maskat et al. (2024).pdf>)
- Reference [12]: [Treffers-Daller (2022).pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/Review Paper/Treffers-Daller (2022).pdf>)
- Reference [13]: [Maskat, R., & Rahman, N. A. (2020). Categorization of Malay social media text and normalization of spelling variations and vowel-less words.pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/General/Maskat, R., & Rahman, N. A. (2020). Categorization of Malay social media text and normalization of spelling variations and vowel-less words.pdf>)
- Reference [14]: [Abu Bakar, M. F. R., Idris, N., Shuib, L., and Khamis, N. (2020).pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/Review Paper/Abu Bakar, M. F. R., Idris, N., Shuib, L., and Khamis, N. (2020).pdf>)
- Reference [15]: [Conneau et al. (2020), XLM-R.pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/C3/Conneau et al. (2020), XLM-R.pdf>)
- Reference [19]: [Frénay, B., and Verleysen, M. (2014).pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/Review Paper/Frénay, B., and Verleysen, M. (2014).pdf>)
- Reference [22]: [Kasmuri, E., & Basiron, H. (2019). Building a Malay-English code-switching subjectivity corpus for sentiment analysis.pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/General/Kasmuri, E., & Basiron, H. (2019). Building a Malay-English code-switching subjectivity corpus for sentiment analysis.pdf>)
- Reference [23]: [Romadhona (2022). The first Bahasa Rojak corpus for pretraining and sentiment analysis dataset.pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/General/Romadhona (2022). The first Bahasa Rojak corpus for pretraining and sentiment analysis dataset.pdf>)
- Reference [24]: [Mohd Shamsuddin(2024).pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/Review Paper/Mohd Shamsuddin(2024).pdf>)
- Reference [25]: [Cohen, J. (1960). A coefficient of agreement for nominal scales. Educational and Psychological Measurement.pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/Review Paper/Cohen, J. (1960). A coefficient of agreement for nominal scales. Educational and Psychological Measurement.pdf>)
- Reference [26]: [Artstein and Poesio (2008).pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/Review Paper/Artstein and Poesio (2008).pdf>)
- Reference [27]: [Feinstein, A. R., and Cicchetti, D. V. (1990)..pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/Review Paper/Feinstein, A. R., and Cicchetti, D. V. (1990)..pdf>)
- Reference [28]: [Byrt, T., Bishop, J., and Carlin, J. B. (1993).pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/Review Paper/Byrt, T., Bishop, J., and Carlin, J. B. (1993).pdf>)
- Reference [29]: [Di Eugenio and Glass (2004).pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/Review Paper/Di Eugenio and Glass (2004).pdf>)
- Reference [30]: [Nazir, A., Rao, Y., Wu, L., and Sun, L. (2022).pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/Review Paper/Nazir, A., Rao, Y., Wu, L., and Sun, L. (2022).pdf>)
- Reference [31]: [Mohammad (2016) A Practical Guide to Sentiment Annotation Challenges and Solutions.pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/C3/Mohammad (2016) A Practical Guide to Sentiment Annotation Challenges and Solutions.pdf>)
- Reference [32]: [AlAfnan et al. (2025).pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/Review Paper/AlAfnan et al. (2025).pdf>)
- Reference [34]: [Hutto, C. J., and Gilbert, E. (2014).pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/Review Paper/Hutto, C. J., and Gilbert, E. (2014).pdf>)
- Reference [35]: [Plank, B. (2022)..pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/Review Paper/Plank, B. (2022)..pdf>)
- Reference [36]: [Pavlick, E., and Kwiatkowski, T. (2019)..pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/Review Paper/Pavlick, E., and Kwiatkowski, T. (2019)..pdf>)
- Reference [37]: [Hovy et al. (2013).pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/Review Paper/Hovy et al. (2013).pdf>)
- Reference [40]: [Bender, E. M., and Friedman, B. (2018).pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/Review Paper/Bender, E. M., and Friedman, B. (2018).pdf>)
- Reference [42]: [Weber, L., and Plank, B. (2023).pdf](<C:/Users/Lenovo/Desktop/Sentiment Analysis FYP/References/Review Paper/Weber, L., and Plank, B. (2023).pdf>)
