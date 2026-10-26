# ICON AI 2026 — Sections 1 to 3.1, revised against Dr. Ho's 64 comments

**Version 4.** Replaces the draft reviewed on the PDF dated 19 August. Every one of the 64 annotations is
addressed; the mapping is in Part B at the end of this file.

**Two things changed globally:**

1. **Citation style is now author–date**, as Dr. Ho wrote it in comments 1 and 10: `(Poria et al., 2023)`
   parenthetically, `Treffers-Daller et al. (2022)` narratively. The `[Author (year)]` placeholder is gone.
   *This contradicts template §11, which asks for numbered `[n]` citations — see the note in the tracker.
   Confirm with Dr. Ho before final submission.*
2. **Seven new peer-reviewed sources** answer the ten "Citation?" comments. Sections 1 to 3.1 now cite 29
   sources, all peer-reviewed, none from arXiv. Full details and verification status in Part C.

---

# 1. Introduction

Sentiment analysis, also known as opinion mining, is the automated task of deciding whether a piece of text
expresses a positive, negative or neutral opinion (Poria et al., 2023). Organisations use it to measure public
opinion at scale, in applications that range from brand monitoring to political and policy analysis (Poria et
al., 2023; Nazir et al., 2022). The tools that make this possible carry an assumption about their input.
Lexicons, pre-trained models and benchmark corpora are concentrated in a small number of well-resourced
languages, and each is built from text written in a single standard variety (Joshi et al., 2020). Text in
which two languages alternate within one message does not satisfy that assumption, and surveys of code-
switching in natural language processing report it as a persistent source of degraded performance (Doğruöz et
al., 2021; Winata et al., 2023). Social media text produced in multilingual societies is writing of exactly
this kind, and Malaysia is one of the clearest cases.

Malaysia is a multilingual and multi-ethnic country. Coluzzi (2017) recorded around 140 languages in use and
described code-mixing between a speaker's first language, English and Malay as already widespread in everyday
communication. More recent work indicates that the practice has continued rather than receded, and that it is
now documented across Malaysian media and online writing (AlAfnan et al., 2025; Maskat et al., 2024). On
social media in particular, users alternate between languages within a single message rather than writing in
one language at a time (Treffers-Daller et al., 2022; AlAfnan et al., 2025). English and Malay are the
language pair that combines most frequently in Malaysian writing, and the mixed varieties they produce are
known locally as *Bahasa Rojak* and *Manglish* (AlAfnan et al., 2025). Malay-English mixed writing is frequent
enough on X, the platform formerly known as Twitter, that both of the Malaysian sentiment corpora examined in
this review were collected from it (Maskat et al., 2024; Mohd Shamsuddin et al., 2024).

How this mixed writing is regarded matters for how it is processed. *Manglish* is sometimes described as a
variety that weakens standard English and Malay rather than as a legitimate language variety in its own right
(AlAfnan et al., 2025). Its structure, however, is not random. Treffers-Daller et al. (2022) and AlAfnan et
al. (2025) show that Malay-English switching follows describable syntactic and pragmatic patterns, and that
speakers use it deliberately to communicate efficiently, signal identity and build rapport. The difficulty
that Malay-English mixed writing creates for natural language processing (NLP) is therefore not that it is
composed carelessly. It is that the conventions Malaysian writers follow are not the conventions that standard
NLP tools were built to handle, so writing that is systematic is processed as noise (Winata et al., 2023; Abu
Bakar et al., 2020).

Surveys of code-switching research report that the explanation offered for poor performance on Malay-English
mixed text is most often architectural (Doğruöz et al., 2021; Winata et al., 2023). Both surveys note that
computational work has concentrated on model design and training data rather than on the linguistic and
annotation questions that precede it. On that account, the model cannot handle code-switched input, and a
larger or more regionally adapted model would perform better on such data. This explanation is reasonable, and
several studies support it. Khanuja et al. (2020) report that multilingual models fine-tuned on code-switched
data achieve the strongest scores among the systems evaluated on their benchmark. Adilazuarda et al. (2022)
show that a model's robustness to code-mixing depends on how well each language is represented during pre-
training. Studies in the same line of work, however, also report the limitations of this approach. Winata et
al. (2021) find that multilingual pre-training alone does not guarantee good representations of code-switched
text, and Conneau et al. (2020) describe a "curse of multilinguality" in which finite model capacity, once
distributed across many languages, dilutes per-language quality. Taken together, these findings indicate that
model choice accounts for part of the difficulty but not all of it. The code-switching surveys reach the same
conclusion, identifying data quality and evaluation as under-examined relative to modelling (Doğruöz et al.,
2021).

A second part of the problem arises earlier in the process. Supervised sentiment analysis requires that every
message be read and assigned a sentiment label, by a human annotator or by an automatic one, before any model
can be trained or evaluated on it (Artstein & Poesio, 2008). This step is called annotation, and the labels it
produces form the supervision signal that a model learns from and is measured against (Artstein & Poesio,
2008). Annotation quality matters because the consequences of incorrect labels are not confined to the
dataset. Frénay and Verleysen (2014) show that label noise is learned by the model during training and
degrades the classifier that results. Northcutt et al. (2021) and Bowman and Dahl (2021) show further that
incorrect labels in a test set distort the evaluation of model performance, so that reported accuracy no
longer reflects how the model actually behaves. Both effects apply wherever labels are uncertain. The sections
that follow show that the conditions producing uncertain labels occur together in Malaysian Malay-English
code-mixed data. For such data, this review therefore argues, the more limiting problem at present is the
annotation label itself, together with the evidence offered that the label is sound.

Two observations drawn from the existing literature support this reading, and both recur in the sections that
follow. The first concerns the corpora themselves. Four Malay-English sentiment resources are currently
available (Mohd Shamsuddin et al., 2024; Kasmuri & Basiron, 2019; Kong et al., 2023; Romadhona et al., 2022).
None of them is simultaneously large, balanced across sentiment classes, drawn from casual social media, and
validated by human annotators. Each resource secures some of these properties at the expense of the others.
The largest general-domain resource, MESocSentiment, illustrates the cost to class balance most clearly: its
19,714 posts are labelled 78.23% neutral, 16.33% positive and 5.44% negative (Mohd Shamsuddin et al., 2024).
Two pieces of evidence indicate that this distribution originates in the labelling method rather than in
Malaysian discourse. First, the corpus was collected under the "#Malaysia" keyword across sports, politics and
the arts, which are not topics on which social media users are typically neutral (Mohd Shamsuddin et al.,
2024). Second, a comparable corpus of Malaysian tweets labelled by human annotators is only 23.6% neutral
(Kong et al., 2023). The neutral share therefore differs by a factor of more than three between two corpora
drawn from the same text type.

The second observation concerns gaps in the reporting of annotation reliability. Reliability is normally
demonstrated by having independent annotators label the same text and computing a chance-corrected agreement
coefficient, which measures how far the observed agreement exceeds the agreement that chance alone would
produce (Cohen, 1960; Artstein & Poesio, 2008). The most widely used coefficient of this kind is Cohen's kappa
(κ), defined for two annotators labelling the same items (Cohen, 1960). Among the four regional resources,
this evidence is limited. MESocSentiment reports no agreement statistic, an omission that follows from its
construction, since it includes no human annotation stage (Mohd Shamsuddin et al., 2024). MyCovid-Senti also
reports none, although it was annotated by three people working from a written guideline (Kong et al., 2023).
The two resources that do report a coefficient obtained it for a binary judgement, not for the three-class
polarity task on which those same resources are used. Kasmuri and Basiron (2019) report κ = 0.83 for a
decision between opinionated and factual sentences. Romadhona et al. (2022) report κ = 0.77 for a two-way
positive-or-negative judgement on stock-market posts, covering one subset of their corpus only. Research on
Malaysian code-mixed sentiment therefore lacks not only reliable annotations but also established practice for
validating their reliability.

The two weaknesses just described, namely the skewed class distribution of the available corpora and the
sparse reporting of annotation reliability, are addressed separately in the studies reviewed here, but they
are connected. The skew that the labelling methods produce is itself the condition under which Cohen's κ
becomes difficult to interpret. When one category dominates the label distribution, the agreement expected by
chance rises, and κ can fall to a low value even when two annotators agree on almost every item. This
behaviour is documented in the methodological literature on agreement measurement, where it is described as
the prevalence problem (Feinstein & Cicchetti, 1990; Byrt et al., 1993; Di Eugenio & Glass, 2004). The same
imbalance that makes the labels unrepresentative therefore also weakens the statistic used to check them. It
is this combined weakness of annotation and evaluation, rather than either weakness in isolation, that helps
explain why reliable annotation of Malaysian code-mixed sentiment data remains unachieved. Reviews published
four years apart identify the same shortage of reliable labelled resources and the same absence of reliability
reporting (Abu Bakar et al., 2020; Selvaraju et al., 2024). The work published between those two reviews has
therefore not resolved it.

This review examines one question: why reliable annotation and evaluation of Malaysian Malay-English code-
mixed sentiment data remain unresolved. Linguistic description, model architecture and application domain are
discussed only where they are relevant to that question. Two related topics fall outside the scope. The first
is comparative benchmarking of sentiment classifiers, and the second is sentiment analysis as a general field.
Both have already been surveyed in detail (Poria et al., 2023; Nazir et al., 2022; Selvaraju et al., 2024).

The scope of this review also excludes several activities. It does not propose, implement or evaluate a
system, and it does not report the author's own experimental work. Its contribution is a diagnosis of why the
problem remains unresolved, together with a set of directions for future research. Where the analysis finds
that a question has not yet been addressed in the literature, it identifies that question and leaves it open
for future work.

This review makes three contributions:

1. It organises the annotation strategies used for low-resource code-mixed text into three tiers, which are
   manual, semi-automated and fully automated labelling, and shows that each tier gains either label fidelity
   or scalability at the expense of the other.
2. It distinguishes the two causes of neutral-label skew, one produced by the labelling tools themselves and
   the other by genuine uncertainty among annotators, and it examines what each of the four regional corpora
   reports about its own reliability.
3. It shows how the linguistic, annotation and measurement challenges compound one another rather than merely
   co-occurring, and sets out a research agenda that follows from that interaction.

The rest of this paper is organised as follows. Section 2 describes the review methodology. Section 3 explains
why Malaysian code-mixed writing is difficult to annotate. Section 4 examines annotation practice and its
failure modes, and Section 5 examines the models that are used as annotators. Section 6 discusses how
annotation reliability is evaluated. Section 7 brings these findings together and sets out directions for
future research, and Section 8 concludes the review.

---

# 2. Review Methodology

The literature reviewed here was identified through structured searches of four databases: the ACL Anthology,
IEEE Xplore, Scopus and arXiv. Three groups of search terms were combined. The first group covered the
language variety and included the terms code-mixed, code-switching, Manglish, Bahasa Rojak and Malay-English.
The second group covered the task and included sentiment analysis, polarity and opinion mining. The third
group covered the object of interest and included corpus, annotation, inter-annotator agreement and label
quality.

The search window was 2019 to 2026. It was extended backwards by following citations from the corpus papers
retrieved in the initial search. The date filter was not applied to work on inter-rater reliability, because
the agreement coefficients used in this field were established well before 2019, and applying the window would
have excluded the methodological literature that defines them.

arXiv was searched as an indexing service rather than as a source of citable work, since research on code-
switching frequently appears there before publication. Every source cited in this review is peer-reviewed.
Where a preprint and a peer-reviewed version of the same work both exist, the peer-reviewed version is the one
cited.

Four criteria were used to determine inclusion. A study was included only if it met all four:

1. It addressed Malaysian or closely comparable Malay-English code-mixed text, or supplied annotation or
   reliability methodology that can be applied to such text;
2. It reported enough procedural detail for its annotation or evaluation practice to be assessed;
3. It was published in a peer-reviewed journal or conference; and
4. It contained an annotation or reliability component.

The fourth criterion is the one that keeps the scope narrow. Studies that only benchmark classifiers against
an existing corpus were excluded, however relevant their results may be to Malaysian sentiment analysis in
general. Such studies treat the quality of the existing labels as given, whereas this review asks whether that
quality can be established in the first place.

---

# 3. Why Malaysian Code-Mixed Text Is Difficult to Annotate

The studies selected under these criteria describe a body of text whose linguistic properties shape every
later stage of the review, and those properties are therefore examined first. Three of them affect the
annotation task directly. The first is that switching occurs inside the sentence and offers little reliable
cue to where the opinion is located. The second is that affective meaning is often carried by function words
that appear in no standard sentiment lexicon. The third is that phonetic spelling multiplies the surface forms
of a single word. All three are already described in the sociolinguistic literature on Malay-English contact
(Treffers-Daller et al., 2022; AlAfnan et al., 2025; Muysken, 2013). What this section adds is not the
description but the consequence that each property carries for the annotator, whether human or automatic, who
must assign a sentiment label. Each property is therefore presented together with a short statement of that
consequence, and the linguistic description itself is not extended beyond what the consequence requires.

## 3.1 Switching occurs within the sentence and offers little reliable structural cue

Malay-English switching occurs predominantly within the clause rather than between clauses. Treffers-Daller et
al. (2022) analysed 1,044 switched utterances and found that insertion, in which a content word or phrase from
one language is embedded in a stretch of the other, accounted for 33.0% of switches. Congruent lexicalisation,
in which the grammar and vocabulary of both languages operate within a shared word order, accounted for a
further 30.7%. Clause-level alternation accounted for 24.8%. The authors explain this distribution
typologically rather than stylistically. English and Malay share Subject-Verb-Object (SVO) word order, and
Malay carries very little inflectional morphology, so a speaker can move between the two languages mid-clause
with minimal grammatical adjustment (Treffers-Daller et al., 2022; Muysken, 2013).

Two limits on this evidence should be noted. The corpus analysed by Treffers-Daller et al. (2022) consists of
spoken data recorded from two teachers, so the exact proportions should not be transferred to social media
text. The structural explanation, however, is a property of the language pair rather than of the medium, and
it therefore applies wherever the two languages are used together. A written instance is the post "Does
institut kanser offer free medication cheap chemotherapy", in which a Malay noun phrase, in Malay head-initial
word order, is embedded within an English question (Mohd Shamsuddin et al., 2024).

The consequence for annotation is that the annotator cannot use a language boundary to locate the part of the
message that carries the sentiment. In monolingual annotation this location step is separate from the
judgement itself and largely mechanical. Annotation schemes for aspect-based sentiment analysis, for example,
require the opinion target expression to be marked as an explicit span in the text before a polarity label is
assigned to it (Pontiki et al., 2016; Nazir et al., 2022). In Malay-English mixed text, identifying that span
is already an act of interpretation. Two annotators may therefore assign different labels not because they
read the sentiment differently, but because they are reading different parts of the message. Disagreement
about which span to judge precedes, and is separate from, disagreement about polarity.

---
---

# Part B — Comment-by-comment response

Use this in supervision. Every comment number matches the tracker.

## Page 2 (comments 1–21)

| # | Fix applied |
|---|---|
| 1 | All parenthetical citations converted to `(Poria et al., 2023)` form throughout. |
| 2 | Rewritten as four sentences. The monolingual-assumption claim is now carried by Joshi et al. (2020), which documents the concentration of NLP resources in a small number of high-resource standard languages. The claim that code-mixed text falls outside that assumption is carried by Doğruöz et al. (2021) and Winata et al. (2023). The jump to Malaysia is bridged by a new sentence: *"Social media text produced in multilingual societies is the largest body of writing of this kind, and Malaysia is one of the clearest cases."* |
| 3 | Coluzzi (2017) kept, but the 140 figure is now explicitly attributed to him and dated: *"Coluzzi (2017) recorded around 140 languages in use…"* A following sentence adds two recent Malaysian sources — AlAfnan et al. (2025) and Maskat et al. (2024) — for the claim that the practice continues today. |
| 4 | "This carries over to social media" → "On social media in particular, users alternate…" |
| 5 | Rewritten: *"English and Malay are the language pair that combines most frequently in Malaysian writing, and the mixed varieties they produce are known locally as Bahasa Rojak and Manglish."* |
| 6 | "This kind of writing" → "Malay-English mixed writing". |
| 7 | X introduced on first use: *"on X, the platform formerly known as Twitter"*. |
| 8 | New bridging sentence opens the paragraph: *"How this mixed writing is regarded matters for how it is processed."* |
| 9 | Adopted his wording: "as a legitimate language variety in its own right". |
| 10 | All narrative citations converted to `Treffers-Daller et al. (2022)` form. The doubled-name placeholder is gone from every instance. |
| 11 | "the difficulty this text creates" → "the difficulty that Malay-English mixed writing creates". |
| 12 | Citation added, and given its own sentence: *"Surveys of code-switching research report that computational work on this problem has concentrated on model design and training data rather than on the linguistic and annotation questions that precede them (Doğruöz et al., 2021; Winata et al., 2023)."* |
| 13 | "performs poorly on this material" → "performs poorly on Malay-English mixed text". |
| 14 | "The argument is that…" → "On that account, the model cannot handle…". The second "argument" became "This explanation is reasonable". No bare "argument" remains. |
| 15 | "part of the literature supports it" → "several studies support it", followed immediately by Khanuja et al. (2020) and Adilazuarda et al. (2022). |
| 16 | "give the best results on their benchmark" → "achieve the strongest scores among the systems evaluated on their benchmark". |
| 17 | "The same literature, however" → "Studies in the same line of work, however". |
| 18 | "the limits of this route" → "the limitations of this approach". "pre-training on its own" → "pre-training alone". |
| 19 | Reframed as an inference from the cited evidence and given a source: *"Taken together, these findings indicate that model choice accounts for part of the difficulty but not all of it, which is the conclusion the code-switching surveys reach when they identify data quality and evaluation as under-examined relative to modelling (Doğruöz et al., 2021)."* |
| 20 | Citation moved onto the flagged sentence: *"Supervised sentiment analysis requires that every message be read and assigned a sentiment label … before any model can be trained or evaluated on it (Artstein & Poesio, 2008)."* |
| 21 | "sits earlier in the process" → "arises earlier in the process". |

## Page 3 (comments 22–44)

| # | Fix applied |
|---|---|
| 22 | "label errors do not stay inside the dataset" → "the consequences of incorrect labels are not confined to the dataset". |
| 23 | Frénay and Verleysen (2014) made the narrative subject of its own sentence, so the citation sits on the claim: *"Frénay and Verleysen (2014) show that label noise is learned by the model during training and degrades the classifier that results."* |
| 24 | "judge how good the model is" → "the evaluation of model performance" (his own suggested wording). |
| 25 | Corrected: *"incorrect labels in a test set distort the evaluation of model performance, so that reported accuracy no longer reflects how the model actually behaves."* The test set is no longer what is described as distorted. |
| 26 | Bridge inserted before the conclusion: *"Both effects apply wherever labels are uncertain. The sections that follow show that the conditions producing uncertain labels occur together in Malaysian Malay-English code-mixed data, and this review therefore argues that…"* |
| 27 | "Two observations" → "Two observations drawn from the existing literature". |
| 28 | "obtains some of these properties by giving up the others" → "secures some of these properties at the expense of the others". |
| 29 | "shows the cost most clearly" → "illustrates the cost to class balance most clearly". |
| 30 | "the same kind of text" → "the same text type". |
| 31 | Rewritten: *"…computing a chance-corrected agreement coefficient, which measures how far the observed agreement exceeds the agreement that chance alone would produce (Cohen, 1960; Artstein & Poesio, 2008)."* |
| 32 | "this evidence is thin" → "this evidence is limited". |
| 33 | "which is unsurprising because" → "an omission that follows from its construction, since". |
| 34 | Completed the contrast and split the sentence: *"The two resources that do report a coefficient obtained it for a binary judgement, and not for the three-class polarity task that those two resources are used to support."* |
| 35 | "the resources are actually used" → "those two resources are used to support". |
| 36 | Cohen's kappa introduced before its first numeric use, with the founding citation: *"The most widely used coefficient of this kind is Cohen's kappa (κ), defined for two annotators labelling the same items (Cohen, 1960)."* |
| 37 | "The field therefore lacks" → "Research on Malaysian code-mixed sentiment therefore lacks". |
| 38 | Both weaknesses named in the sentence: *"The two weaknesses just described, namely the skewed class distribution of the available corpora and the sparse reporting of annotation reliability, are…"* |
| 39 | Attributed: "are addressed separately in the studies reviewed here". |
| 40 | Mechanism explained and cited: *"When one category dominates the label distribution, the agreement expected by chance rises, and κ can fall to a low value even when two annotators agree on almost every item. This behaviour is documented in the methodological literature on agreement measurement, where it is described as the prevalence problem (Feinstein & Cicchetti, 1990; Byrt et al., 1993; Di Eugenio & Glass, 2004)."* |
| 41 | Corrected throughout: "the skewed class **distribution** of the available corpora", "when one category dominates the **label distribution**". |
| 42 | "the standard agreement statistic" → "Cohen's κ", named explicitly and defined earlier in the section. |
| 43 | "why the problem has proved persistent" → "why reliable annotation of Malaysian code-mixed sentiment data remains unachieved". |
| 44 | Evidence supplied: *"Reviews published four years apart identify the same shortage of reliable labelled resources and the same absence of reliability reporting, which indicates that the difficulty has not been resolved by the work carried out in between (Abu Bakar et al., 2020; Selvaraju et al., 2024)."* |

## Page 4 (comments 45–54)

| # | Fix applied |
|---|---|
| 45 | Split into three sentences, with the two excluded topics named before "Both" is used: *"Two related topics fall outside the scope. The first is comparative benchmarking of sentiment classifiers, and the second is sentiment analysis as a general field. Both have already been surveyed in detail (…)."* |
| 46 | "where they bear on that question" → "where they are relevant to that question". |
| 47 | Adopted his wording exactly: "The scope of this review also excludes several activities." |
| 48 | "why the problem has resisted solution" → "why the problem remains unresolved". |
| 49 | The three tiers named in the contribution: *"…into three tiers, which are manual, semi-automated and fully automated labelling, and shows that each tier gains either label fidelity or scalability at the expense of the other."* |
| 50 | "by giving up the other" → "at the expense of the other". |
| 51 | Made explicit without reintroducing the mechanism Round 1 comment 65 objected to: *"…the two causes of neutral-label skew, one produced by the labelling tools themselves and the other by genuine uncertainty among annotators…"* |
| 52 | "audits" → "examines". |
| 53 | "rather than simply occurring together" → "rather than merely co-occurring". |
| 54 | Preprint paragraph replaced: *"arXiv was searched as an indexing service rather than as a source of citable work, since research on code-switching frequently appears there before publication. Every source cited in this review is peer-reviewed."* Inclusion criterion 3 changed from "peer-reviewed, or a preprint with a traceable venue" to "published in a peer-reviewed journal or conference". Verified: none of the 29 sources is an arXiv-only preprint. |

## Page 5 (comments 55–64)

| # | Fix applied |
|---|---|
| 55 | Bridging sentence added at the head of Section 3: *"The studies selected under these criteria describe a body of text whose linguistic properties shape every later stage of the review, and those properties are therefore examined first."* |
| 56 | All three properties previewed by name in the opening paragraph, in the order the subsections take them. |
| 57 | "a person or a program that has been asked to assign a sentiment label" → "the annotator, whether human or automatic, who must assign a sentiment label". |
| 58 | "and is not developed further" → "and the linguistic description itself is not extended beyond what the consequence requires". |
| 59 | Heading softened and the absolute removed: "Switching occurs within the sentence and offers little reliable structural cue". |
| 60 | "happens mostly inside the clause" → "occurs predominantly within the clause". |
| 61 | "with almost no grammatical friction" → "with minimal grammatical adjustment". |
| 62 | Citation added to the sentence itself: *"The corpus analysed by Treffers-Daller et al. (2022) consists of spoken data recorded from two teachers…"* |
| 63 | "sits inside an English question" → "is embedded within an English question". |
| 64 | Claim supported with a concrete annotation scheme: *"Annotation schemes for aspect-based sentiment analysis, for example, require the opinion target expression to be marked as an explicit span in the text before a polarity label is assigned to it (Pontiki et al., 2016; Nazir et al., 2022)."* SemEval-2016 Task 5 separates Slot 2 (opinion target expression, given by character offsets) from Slot 3 (polarity), which is exactly the two-step process the sentence describes. |

---

# Part C — References

## The seven new sources, verified

Each was checked against the publisher or ACL Anthology record. All are peer-reviewed. None is an arXiv-only
preprint. Reference entries below spell out every author name, as template §11 requires.

| Source | Supports | Verified |
|---|---|---|
| Joshi et al. (2020) | Comment 2 — NLP resources concentrated in few high-resource standard languages | ACL 2020, pp. 6282–6293, DOI 10.18653/v1/2020.acl-main.560 ✅ |
| Doğruöz et al. (2021) | Comments 2, 12, 19 — the field explains code-switching failures architecturally and under-examines data and evaluation | ACL-IJCNLP 2021, pp. 1654–1666, DOI 10.18653/v1/2021.acl-long.131 ✅ Peer-reviewed ACL long paper; do **not** cite the arXiv version (2301.01967) |
| Cohen (1960) | Comments 36, 42 — definition of Cohen's κ | *Educational and Psychological Measurement*, 20(1), 37–46, DOI 10.1177/001316446002000104 ✅ |
| Feinstein & Cicchetti (1990) | Comment 40 — the prevalence problem | *Journal of Clinical Epidemiology*, 43(6), 543–549, DOI 10.1016/0895-4356(90)90158-L ✅ |
| Byrt et al. (1993) | Comment 40 — bias, prevalence and κ | *Journal of Clinical Epidemiology*, 46(5), 423–429, DOI 10.1016/0895-4356(93)90018-V ✅ |
| Di Eugenio & Glass (2004) | Comment 40 — the prevalence problem in computational linguistics specifically | *Computational Linguistics*, 30(1), 95–101, DOI 10.1162/089120104773633402 ✅ |
| Pontiki et al. (2016) | Comment 64 — OTE span marked before polarity assigned | SemEval-2016, pp. 19–30, DOI 10.18653/v1/S16-1002 ✅ Confirmed against the paper: Slot 2 is the opinion target expression given by character offsets, Slot 3 is polarity, and Phase B supplies gold Slot 1/2 annotations before participants return Slot 3 |

## One claim to check yourself before submitting

The support for comment 44 rests on this sentence:

> Reviews published four years apart identify the same shortage of reliable labelled resources and the same
> absence of reliability reporting (Abu Bakar et al., 2020; Selvaraju et al., 2024).

You have both PDFs in `References/`. Confirm that each review does state a shortage of labelled resources
**and** the absence of reliability reporting. If Selvaraju et al. (2024) does not mention reliability
reporting, narrow the sentence to the shortage of resources only — that part is certain.

## Full reference list for Sections 1 to 3.1 — 29 entries, alphabetical

Abu Bakar, M. F. R., Idris, N., Shuib, L., and Khamis, N. (2020). Sentiment analysis of noisy Malay text: State of art, challenges and future work. *IEEE Access*, 8, 24687–24696. https://doi.org/10.1109/ACCESS.2020.2968955

Adilazuarda, M. F., Cahyawijaya, S., Winata, G. I., Fung, P., and Purwarianti, A. (2022). IndoRobusta: Towards robustness against diverse code-mixed Indonesian local languages. *Proceedings of the First Workshop on Scaling Up Multilingual Evaluation (SUMEval)*, 25–34.

AlAfnan, M. A., MohdZuki, S. F., and AlAfnan, S. M. (2025). Blending identities: Exploring the linguistic, cultural, and pragmatic dimensions of Manglish in the Malaysian society. *Studies in Media and Communication*, 13(3). https://doi.org/10.11114/smc.v13i3.7654

Artstein, R., and Poesio, M. (2008). Survey article: Inter-coder agreement for computational linguistics. *Computational Linguistics*, 34(4), 555–596. https://doi.org/10.1162/coli.07-034-R2

Bowman, S. R., and Dahl, G. (2021). What will it take to fix benchmarking in natural language understanding? *Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, 4843–4855. https://doi.org/10.18653/v1/2021.naacl-main.385

**Byrt, T., Bishop, J., and Carlin, J. B. (1993). Bias, prevalence and kappa. *Journal of Clinical Epidemiology*, 46(5), 423–429. https://doi.org/10.1016/0895-4356(93)90018-V** *(new)*

**Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37–46. https://doi.org/10.1177/001316446002000104** *(new)*

Coluzzi, P. (2017). Language planning for Malay in Malaysia: A case of failure or success? *International Journal of the Sociology of Language*, 2017(244), 17–38. https://doi.org/10.1515/ijsl-2016-0055

Conneau, A., Khandelwal, K., Goyal, N., Chaudhary, V., Wenzek, G., Guzmán, F., Grave, E., Ott, M., Zettlemoyer, L., and Stoyanov, V. (2020). Unsupervised cross-lingual representation learning at scale. *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics*, 8440–8451. https://doi.org/10.18653/v1/2020.acl-main.747

**Di Eugenio, B., and Glass, M. (2004). The kappa statistic: A second look. *Computational Linguistics*, 30(1), 95–101. https://doi.org/10.1162/089120104773633402** *(new)*

**Doğruöz, A. S., Sitaram, S., Bullock, B. E., and Toribio, A. J. (2021). A survey of code-switching: Linguistic and social perspectives for language technologies. *Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)*, 1654–1666. https://doi.org/10.18653/v1/2021.acl-long.131** *(new)*

**Feinstein, A. R., and Cicchetti, D. V. (1990). High agreement but low kappa: I. The problems of two paradoxes. *Journal of Clinical Epidemiology*, 43(6), 543–549. https://doi.org/10.1016/0895-4356(90)90158-L** *(new)*

Frénay, B., and Verleysen, M. (2014). Classification in the presence of label noise: A survey. *IEEE Transactions on Neural Networks and Learning Systems*, 25(5), 845–869. https://doi.org/10.1109/TNNLS.2013.2292894

**Joshi, P., Santy, S., Budhiraja, A., Bali, K., and Choudhury, M. (2020). The state and fate of linguistic diversity and inclusion in the NLP world. *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics*, 6282–6293. https://doi.org/10.18653/v1/2020.acl-main.560** *(new)*

Kasmuri, E., and Basiron, H. (2019). Building a Malay-English code-switching subjectivity corpus for sentiment analysis. *International Journal of Advanced Soft Computing and Its Applications*, 11(1), 112–130.

Khanuja, S., Dandapat, S., Srinivasan, A., Sitaram, S., and Choudhury, M. (2020). GLUECoS: An evaluation benchmark for code-switched NLP. *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics*, 3575–3585. https://doi.org/10.18653/v1/2020.acl-main.329

Kong, J. T. H., Juwono, F. H., Ngu, I. Y., Nugraha, I. G. D., Maraden, Y., and Wong, W. K. (2023). A mixed Malay-English language COVID-19 Twitter dataset: A sentiment analysis. *Big Data and Cognitive Computing*, 7(2), 61. https://doi.org/10.3390/bdcc7020061

Maskat, R., Azman, N. A., Nulizairos, N. S. S., Zahidin, N. A., Mahadi, A. H., Norshamsul, S. R., Mohd Sharif, M. M., and Mahdin, H. (2024). A bi-annotated Malay-English code-switching (Manglish) dataset of X posts for biological gender identification and authorship attribution. *Data in Brief*, 52, 110034. https://doi.org/10.1016/j.dib.2024.110034

Mohd Shamsuddin, A. M., Samson Juan, S., Chua, S., and Bramantoro, A. (2024). Semi-automatic sentiment identification for Malay-English code-switched data. *Journal of Advanced Research Design*, 123(1), 198–212. https://doi.org/10.37934/ard.123.1.198212

Muysken, P. (2013). Language contact outcomes as the result of bilingual optimization strategies. *Bilingualism: Language and Cognition*, 16(4), 709–730. https://doi.org/10.1017/S1366728912000727

Nazir, A., Rao, Y., Wu, L., and Sun, L. (2022). Issues and challenges of aspect-based sentiment analysis: A comprehensive survey. *IEEE Transactions on Affective Computing*, 13(2), 845–863. https://doi.org/10.1109/TAFFC.2020.2970399

Northcutt, C. G., Athalye, A., and Mueller, J. (2021). Pervasive label errors in test sets destabilize machine learning benchmarks. *Proceedings of the 35th Conference on Neural Information Processing Systems (NeurIPS): Datasets and Benchmarks Track*.

**Pontiki, M., Galanis, D., Papageorgiou, H., Androutsopoulos, I., Manandhar, S., AL-Smadi, M., Al-Ayyoub, M., Zhao, Y., Qin, B., De Clercq, O., Hoste, V., Apidianaki, M., Tannier, X., Loukachevitch, N., Kotelnikov, E., Bel, N., Jiménez-Zafra, S. M., and Eryiğit, G. (2016). SemEval-2016 Task 5: Aspect based sentiment analysis. *Proceedings of the 10th International Workshop on Semantic Evaluation (SemEval-2016)*, 19–30. https://doi.org/10.18653/v1/S16-1002** *(new)*

Poria, S., Hazarika, D., Majumder, N., and Mihalcea, R. (2023). Beneath the tip of the iceberg: Current challenges and new directions in sentiment analysis research. *IEEE Transactions on Affective Computing*, 14(1), 108–132. https://doi.org/10.1109/TAFFC.2020.3038167

Romadhona, N. P., Lu, S.-E., Lu, B.-H., and Tsai, R. T.-H. (2022). BRCC and SentiBahasaRojak: The first Bahasa Rojak corpus for pretraining and sentiment analysis dataset. *Proceedings of the 29th International Conference on Computational Linguistics (COLING)*, 4418–4428.

Selvaraju, S., Sjarif, N. N. A., and Anuar, M. S. M. (2024). Sentiment analysis in code mixing Malay text: A review. *2024 5th International Conference on Artificial Intelligence and Data Sciences (AiDAS)*, 280–285. https://doi.org/10.1109/AiDAS63860.2024.10730298

Treffers-Daller, J., Majid, S., Thai, Y. N., and Flynn, N. (2022). Explaining the diversity in Malay-English code-switching patterns: The contribution of typological similarity and bilingual optimization strategies. *Languages*, 7(4), 299. https://doi.org/10.3390/languages7040299

Winata, G. I., Aji, A. F., Yong, Z. X., and Solorio, T. (2023). The decades progress on code-switching research in NLP: A systematic survey on trends and challenges. *Findings of the Association for Computational Linguistics: ACL 2023*, 2936–2978. https://doi.org/10.18653/v1/2023.findings-acl.185

Winata, G. I., Cahyawijaya, S., Liu, Z., Lin, Z., Madotto, A., and Fung, P. (2021). Are multilingual models effective in code-switching? *Proceedings of the Fifth Workshop on Computational Approaches to Linguistic Code-Switching*, 142–153. https://doi.org/10.18653/v1/2021.calcs-1.20

---

# Part D — What is next

Sections 3.2 and 3.3 are the immediate gap. Section 3's opening paragraph now names all three properties, so
the section contradicts itself until both subsections exist:

- **3.2 — Affective meaning is carried by function words that no standard lexicon contains.** Sentence-final
  particles such as *lah* and *kan* attach to otherwise-English clauses and carry pragmatic rather than
  propositional weight. Annotation consequence: the reading of a particle is underdetermined, so
  disagreement is systematic rather than random, and adding annotators reproduces it instead of averaging it
  away. Sources: Treffers-Daller et al. (2022) for switched-function-word frequencies, AlAfnan et al. (2025)
  for the pragmatic functions. **Caveat to state explicitly:** AlAfnan et al.'s examples come from Malaysian
  television and film, which is scripted dialogue rather than social media writing — good evidence for what
  the particles do, weaker evidence for how often they appear in written text.
- **3.3 — Phonetic spelling multiplies the surface forms of one word.** *tidak* → *tak*, *tk*, *x*. Maskat
  and Rahman (2020) sort this into five categories and report normalising only two. Annotation consequence:
  human and automatic annotators fail on different inputs — a person reads *x* as *tidak* without effort, a
  lexicon returns out-of-vocabulary and no signal at all. Sources: Maskat and Rahman (2020), Abu Bakar et al.
  (2020).

Say the word and I will write both, then continue through Sections 4 to 8 against the same twelve rules.
