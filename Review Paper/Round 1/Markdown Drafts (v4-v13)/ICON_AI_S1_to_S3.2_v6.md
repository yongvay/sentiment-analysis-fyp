# ICON AI 2026 — Sections 1 to 3.2

**Version 6.** Replaces the draft reviewed on the PDF dated 19 August. Every one of the 64 annotations is
addressed; the mapping is in Part B at the end of this file.

**What changed from v5:** Section 3.2 added. Every claim in it was checked against the source PDFs before
it was written, which turned up two errors in the plan — see "Section 3.2: what the sources actually say"
in Part C. Sections 1, 2 and 3.1 are unchanged from v5.

**What changed from v4:** the Introduction was restructured. v4 fixed every sentence Dr. Ho flagged but
introduced a readability problem of its own — it ran three overlapping enumerations at once ("a second part
of the problem", "two observations", "these two weaknesses"), so the reader had to track three labelled
pairs across five paragraphs. The Introduction now runs a single spine, modelled on Chapter 1 of the thesis:
one thesis sentence, then *the first finding / the second finding / the third finding*, then the synthesis.
Two further v4 faults are fixed: the topic sentence of the model-architecture paragraph is restored to the
front of that paragraph, and a concrete spelling example now appears in paragraph 3 instead of leaving the
reader in abstraction until the 78.23% figure. Sections 2 and 3.1 are unchanged from v4.

**Three things changed globally:**

1. **Citation style is now author–date**, as Dr. Ho wrote it in comments 1 and 10: `(Poria et al., 2023)`
   parenthetically, `Treffers-Daller et al. (2022)` narratively. The `[Author (year)]` placeholder is gone.
   *This contradicts template §11, which asks for numbered `[n]` citations — see the note in the tracker.
   Confirm with Dr. Ho before final submission.*
2. **Eight new peer-reviewed sources** answer the ten "Citation?" comments and supply the concrete spelling
   example. Sections 1 to 3.1 now cite 30 sources, all peer-reviewed, none from arXiv. Full details and
   verification status in Part C.
3. **The Introduction runs one numbered spine** rather than three competing pairs. Structure only — no
   sentence-level fix from the 64 comments was reversed.

---

# 1. Introduction

Sentiment analysis, also known as opinion mining, is the automated task of deciding whether a piece of text
expresses a positive, negative or neutral opinion (Poria et al., 2023). Organisations use it to measure
public opinion at scale, in applications that range from brand monitoring to political and policy analysis
(Poria et al., 2023; Nazir et al., 2022). The tools that make this possible carry an assumption about their
input. Lexicons, pre-trained models and benchmark corpora are concentrated in a small number of
well-resourced languages, and each is built from text written in a single standard variety (Joshi et al.,
2020). Text in which two languages alternate within one message does not satisfy that assumption, and
surveys of code-switching in natural language processing report it as a persistent source of degraded
performance (Doğruöz et al., 2021; Winata et al., 2023). Malaysian social media text is writing of exactly
this kind.

Malaysia is a multilingual and multi-ethnic country. Coluzzi (2017) recorded around 140 languages in use and
described code-mixing between a speaker's first language, English and Malay as already widespread in
everyday communication. More recent work indicates that the practice has continued rather than receded, and
that it is now documented across Malaysian media and online writing (AlAfnan et al., 2025; Maskat et al.,
2024). On social media in particular, users alternate between languages within a single message rather than
writing in one language at a time (Treffers-Daller et al., 2022; AlAfnan et al., 2025). English and Malay
are the language pair that combines most frequently in Malaysian writing, and the mixed varieties they
produce are known locally as *Bahasa Rojak* and *Manglish* (AlAfnan et al., 2025). Malay-English mixed
writing is frequent enough on X, the platform formerly known as Twitter, that both of the Malaysian
sentiment corpora examined in this review were collected from it (Maskat et al., 2024; Mohd Shamsuddin et
al., 2024).

How this mixed writing is regarded matters for how it is processed. *Manglish* is sometimes described as a
variety that weakens standard English and Malay rather than as a legitimate language variety in its own
right (AlAfnan et al., 2025). Its structure, however, is not random. Treffers-Daller et al. (2022) and
AlAfnan et al. (2025) show that Malay-English switching follows describable syntactic and pragmatic
patterns, and that speakers use it deliberately to communicate efficiently, signal identity and build
rapport. The same regularity holds at the level of spelling. Maskat and Rahman (2020) sort Malay social
media spelling into five categories and record, for example, that the negator *tidak* is written as *x*, and
that *tidak ada* appears as *takde*, *xde* or *tade*. A reader who knows the convention recovers the word
without effort, but a lexicon built for standard Malay returns no entry for any of those forms. The
difficulty that Malay-English mixed writing creates for natural language processing (NLP) is therefore not
that it is composed carelessly. It is that the conventions Malaysian writers follow are not the conventions
that standard NLP tools were built to handle, so writing that is systematic is processed as noise (Winata et
al., 2023; Abu Bakar et al., 2020).

When a sentiment model performs poorly on Malay-English mixed text, the explanation offered is most often
architectural (Doğruöz et al., 2021; Winata et al., 2023). On that account the model cannot handle
code-switched input, and a larger or more regionally adapted model would perform better. The explanation is
reasonable, and several studies support it. Khanuja et al. (2020) report that multilingual models fine-tuned
on code-switched data achieve the strongest scores among the systems evaluated on their benchmark.
Adilazuarda et al. (2022) show that a model's robustness to code-mixing depends on how well each language is
represented during pre-training. Studies in the same line of work, however, also report the limitations of
this approach. Winata et al. (2021) find that multilingual pre-training alone does not guarantee good
representations of code-switched text, and Conneau et al. (2020) describe a "curse of multilinguality" in
which finite model capacity, once distributed across many languages, dilutes per-language quality. Model
choice therefore accounts for part of the difficulty but not all of it, which is the conclusion the
code-switching surveys reach when they identify data quality and evaluation as under-examined relative to
modelling (Doğruöz et al., 2021).

The remainder of the difficulty does not originate in the model. It originates one step earlier, at the
point where the labels are created. Supervised sentiment analysis requires that every message be read and
assigned a sentiment label, by a human annotator or by an automatic one, before any model can be trained or
evaluated on it (Artstein & Poesio, 2008). This step is called annotation, and the labels it produces form
the supervision signal that a model learns from and is measured against (Artstein & Poesio, 2008). The
consequences of incorrect labels are not confined to the dataset. Frénay and Verleysen (2014) show that
label noise is learned by the model during training and degrades the classifier that results. Northcutt et
al. (2021) and Bowman and Dahl (2021) show further that incorrect labels in a test set distort the
evaluation of model performance, so that reported accuracy no longer reflects how the model actually
behaves. An unsound label therefore damages the model twice, once when it is trained and again when it is
measured.

This review argues that for Malaysian Malay-English code-mixed sentiment data, the annotation label is at
present the more limiting problem, together with the evidence offered that the label is sound. Three
findings in the existing literature support that reading, and each of them returns in the sections that
follow.

The first finding is that no available Malay-English sentiment resource combines the properties a
general-purpose corpus requires. Four such resources currently exist (Mohd Shamsuddin et al., 2024; Kasmuri
& Basiron, 2019; Kong et al., 2023; Romadhona et al., 2022). None of them is simultaneously large, balanced
across sentiment classes, drawn from casual social media, and validated by human annotators. Each secures
some of these properties at the expense of the others.

The second finding is that the class imbalance in the largest of those resources originates in the labelling
method rather than in Malaysian discourse. MESocSentiment is the largest general-domain corpus, and its
19,714 posts are labelled 78.23% neutral, 16.33% positive and 5.44% negative (Mohd Shamsuddin et al., 2024).
Two pieces of evidence point to the method rather than to the population. First, the corpus was collected
under the "#Malaysia" keyword across sports, politics and the arts, which are not topics on which social
media users are typically neutral (Mohd Shamsuddin et al., 2024). Second, a comparable corpus of Malaysian
tweets labelled by human annotators is only 23.6% neutral (Kong et al., 2023). The neutral share differs by
a factor of more than three between two corpora drawn from the same text type, and what differs between them
is who or what assigned the labels.

The third finding is that annotation reliability is rarely reported, and that where a figure is given it
measures a narrower task than the one the corpus is used for. Reliability is normally demonstrated by having
independent annotators label the same text and computing a chance-corrected agreement coefficient, which
measures how far the observed agreement exceeds the agreement that chance alone would produce (Cohen, 1960;
Artstein & Poesio, 2008). The most widely used coefficient of this kind is Cohen's kappa (κ), defined for
two annotators labelling the same items (Cohen, 1960). Among the four regional resources, this evidence is
limited. MESocSentiment reports no agreement statistic, an omission that follows from its construction,
since it includes no human annotation stage (Mohd Shamsuddin et al., 2024). MyCovid-Senti also reports none,
although it was annotated by three people working from a written guideline (Kong et al., 2023). The two
resources that do report a coefficient obtained it for a binary judgement, not for the three-class polarity
task on which those same resources are used. Kasmuri and Basiron (2019) report κ = 0.83 for a decision
between opinionated and factual sentences. Romadhona et al. (2022) report κ = 0.77 for a two-way
positive-or-negative judgement on stock-market posts, covering one subset of their corpus only. Research on
Malaysian code-mixed sentiment therefore lacks not only reliable annotations but also established practice
for validating their reliability.

The second and third findings are addressed separately in the studies reviewed here, but they describe one
condition rather than two. The skew that the labelling methods produce is itself the condition under which
Cohen's κ becomes difficult to interpret. When one category dominates the label distribution, the agreement
expected by chance rises, and κ can fall to a low value even when two annotators agree on almost every item.
This behaviour is documented in the methodological literature on agreement measurement, where it is
described as the prevalence problem (Feinstein & Cicchetti, 1990; Byrt et al., 1993; Di Eugenio & Glass,
2004). The same imbalance that makes the labels unrepresentative therefore also weakens the statistic used
to check them. That is why the difficulty has persisted: correcting either weakness alone leaves the other
in place. A review of the field published in 2024 still reports a lack of comprehensive datasets and annotated
resources for code-mixed Malay text (Selvaraju et al., 2024), which indicates that recent work has not closed
the shortage.

This review examines one question: why reliable annotation and evaluation of Malaysian Malay-English
code-mixed sentiment data remain unresolved. Linguistic description, model architecture and application
domain are discussed only where they are relevant to that question. Two related topics fall outside the
scope. The first is comparative benchmarking of sentiment classifiers, and the second is sentiment analysis
as a general field. Both have already been surveyed in detail (Poria et al., 2023; Nazir et al., 2022;
Selvaraju et al., 2024).

The scope of this review also excludes several activities. It does not propose, implement or evaluate a
system, and it does not report the author's own experimental work. Its contribution is a diagnosis of why
the problem remains unresolved, together with a set of directions for future research. Where the analysis
finds that a question has not yet been addressed in the literature, it identifies that question and leaves
it open for future work.

This review makes three contributions:

1. It organises the annotation strategies used for low-resource code-mixed text into three tiers, which are
   manual, semi-automated and fully automated labelling, and shows that each tier gains either label
   fidelity or scalability at the expense of the other.
2. It distinguishes the two causes of neutral-label skew, one produced by the labelling tools themselves and
   the other by genuine uncertainty among annotators, and it examines what each of the four regional corpora
   reports about its own reliability.
3. It shows how the linguistic, annotation and measurement challenges compound one another rather than
   merely co-occurring, and sets out a research agenda that follows from that interaction.

The rest of this paper is organised as follows. Section 2 describes the review methodology. Section 3
explains why Malaysian code-mixed writing is difficult to annotate. Section 4 examines annotation practice
and its failure modes, and Section 5 examines the models that are used as annotators. Section 6 discusses
how annotation reliability is evaluated. Section 7 brings these findings together and sets out directions
for future research, and Section 8 concludes the review.

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

## 3.2 Affective meaning is carried by particles that belong to neither standard language

Locating the opinion-bearing span is only the first difficulty. A second arises once the span has been found.
In Malay-English mixed writing, the element that carries the affect is often a Malay particle attached to a
clause that is otherwise entirely in English (Treffers-Daller et al., 2022). The construction is a distinct
type of code-switching, which Muysken (2013) terms back-flagging. Treffers-Daller et al. (2022) define it as
the attachment of a discourse marker or co-ordinate conjunction from a speaker's first language to a stretch
of speech in the second. Back-flagging accounts for 121 of the 1,044 switched utterances in their data, or
11.6%. Counted by syntactic category rather than by utterance, discourse markers make up 121 of the 1,217
individual switches recorded, or 9.9%, placing them fourth behind nouns, noun phrases and personal pronouns.
The particle involved most frequently is *lah*, which the same study reports can attach to a clause that is
entirely English, entirely Malay or mixed. Two examples it reproduces from earlier descriptive work are "Buy
this lah" and "you understand lah kan".

What these particles contribute is pragmatic rather than propositional, and the pragmatic work they do is
affective. AlAfnan et al. (2025) classify particles as a lexical feature that adds emphasis or tone and
signals politeness or informality. The same study identifies the softening of directives as one of their
pragmatic functions, giving "Don't disturb la, he's busy" as an instance in which the particle makes an
instruction less direct. Treffers-Daller et al. (2022), citing Tay et al. (2016), describe the effect more
precisely: *lah* shifts an utterance from a highly assertive tone to a polite request or a friendly
encouragement. These particles belong to Manglish rather than to either source language, and AlAfnan et al.
(2025) list them among the features that distinguish Manglish from standard English and standard Malay. In
both accounts the particle leaves unchanged what the sentence states. What it changes is how the sentence is
to be taken, which is the property a sentiment label is meant to record.

Two limits on this evidence should be noted, and they run in opposite directions. Treffers-Daller et al.
(2022) supply frequencies, but from classroom speech. Their corpus is fifteen hours of recorded teaching by
each of two university English lecturers, so the rates should not be read as rates for social media writing.
AlAfnan et al. (2025) describe Malaysian usage more broadly, but their data are scripted dialogue from
Malaysian television series such as *Kopitiam* and *KL Gangster*, examined through qualitative content
analysis. That study therefore reports what the particles do and not how often they occur. Neither source
establishes a frequency for particle use in Malaysian social media posts, and no such figure is currently
available. What both sources do establish is that the construction is regular and that it carries affect.

The consequence for annotation is that the particle fixes the tone of a message without fixing its polarity. A
reader of "Don't disturb la, he's busy" can see that the particle softens the instruction. Softening is
nonetheless compatible with a negative reading, in which the writer is irritated, and with a neutral one, in
which the writer is being polite. Treffers-Daller et al. (2022) concede the same point about the category as a
whole, observing that the specific meanings of discourse markers are often difficult to capture even where
their pragmatic functions can be evaluated. The affective signal is therefore carried by a token whose
contribution is real but underdetermined, and two annotators may read it differently while both reading it
competently.

Disagreement of this type is not removed by adding annotators. Pavlick and Kwiatkowski (2019) show that where
a task admits more than one defensible reading, disagreement between annotators is reproducible and persists
as further ratings are collected, rather than resolving toward a single label. A corpus built by majority vote
over such items therefore records the majority reading as though it were the only defensible one. The
variation it conceals is systematic rather than random. An agreement coefficient computed over these items
registers genuine interpretive difference and not annotator error.

The first property examined in this section produces disagreement about which part of a message to judge. The
second produces disagreement about how to judge a part whose reading is genuinely open.

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
| 12 | Citation attached to the claim sentence itself: *"When a sentiment model performs poorly on Malay-English mixed text, the explanation offered is most often architectural (Doğruöz et al., 2021; Winata et al., 2023)."* (v5 note: v4 buried this behind "Surveys of code-switching research report that…"; the topic sentence is restored.) |
| 13 | "performs poorly on this material" → "performs poorly on Malay-English mixed text". |
| 14 | "The argument is that…" → "On that account, the model cannot handle…". The second "argument" became "This explanation is reasonable". No bare "argument" remains. |
| 15 | "part of the literature supports it" → "several studies support it", followed immediately by Khanuja et al. (2020) and Adilazuarda et al. (2022). |
| 16 | "give the best results on their benchmark" → "achieve the strongest scores among the systems evaluated on their benchmark". |
| 17 | "The same literature, however" → "Studies in the same line of work, however". |
| 18 | "the limits of this route" → "the limitations of this approach". "pre-training on its own" → "pre-training alone". |
| 19 | Reframed as an inference from the cited evidence, with a source: *"Model choice therefore accounts for part of the difficulty but not all of it, which is the conclusion the code-switching surveys reach when they identify data quality and evaluation as under-examined relative to modelling (Doğruöz et al., 2021)."* |
| 20 | Citation moved onto the flagged sentence: *"Supervised sentiment analysis requires that every message be read and assigned a sentiment label … before any model can be trained or evaluated on it (Artstein & Poesio, 2008)."* |
| 21 | "sits earlier in the process" → *"The remainder of the difficulty does not originate in the model. It originates one step earlier, at the point where the labels are created."* |

## Page 3 (comments 22–44)

| # | Fix applied |
|---|---|
| 22 | "label errors do not stay inside the dataset" → "the consequences of incorrect labels are not confined to the dataset". |
| 23 | Frénay and Verleysen (2014) made the narrative subject of its own sentence, so the citation sits on the claim: *"Frénay and Verleysen (2014) show that label noise is learned by the model during training and degrades the classifier that results."* |
| 24 | "judge how good the model is" → "the evaluation of model performance" (his own suggested wording). |
| 25 | Corrected: *"incorrect labels in a test set distort the evaluation of model performance, so that reported accuracy no longer reflects how the model actually behaves."* The test set is no longer what is described as distorted. |
| 26 | The jump is now carried by a dedicated thesis paragraph that states the claim as the review's own argument before any evidence is given: *"This review argues that for Malaysian Malay-English code-mixed sentiment data, the annotation label is at present the more limiting problem…"* The preceding paragraph closes on the general point (*"An unsound label therefore damages the model twice…"*), so the general-to-specific move happens across a paragraph boundary rather than inside one sentence. |
| 27 | "Two observations" → *"Three findings in the existing literature support that reading, and each of them returns in the sections that follow."* (v5 note: v4 had two observations plus a separate "second part of the problem" pair; the Introduction now runs one enumeration only.) |
| 28 | "obtains some of these properties by giving up the others" → "Each secures some of these properties at the expense of the others." |
| 29 | The ambiguous "shows the cost most clearly" is gone. Finding 2 now states what it is about in its own topic sentence: *"The second finding is that the class imbalance in the largest of those resources originates in the labelling method rather than in Malaysian discourse."* |
| 30 | "the same kind of text" → "the same text type". |
| 31 | Rewritten: *"…computing a chance-corrected agreement coefficient, which measures how far the observed agreement exceeds the agreement that chance alone would produce (Cohen, 1960; Artstein & Poesio, 2008)."* |
| 32 | "this evidence is thin" → "this evidence is limited". |
| 33 | "which is unsurprising because" → "an omission that follows from its construction, since". |
| 34 | Completed the contrast and split the sentence: *"The two resources that do report a coefficient obtained it for a binary judgement, and not for the three-class polarity task that those two resources are used to support."* |
| 35 | "the resources are actually used" → "those two resources are used to support". |
| 36 | Cohen's kappa introduced before its first numeric use, with the founding citation: *"The most widely used coefficient of this kind is Cohen's kappa (κ), defined for two annotators labelling the same items (Cohen, 1960)."* |
| 37 | "The field therefore lacks" → "Research on Malaysian code-mixed sentiment therefore lacks". |
| 38 | The referent is now a number, not a demonstrative: *"The second and third findings are addressed separately in the studies reviewed here, but they describe one condition rather than two."* The two items are enumerated earlier in the section, so nothing has to be looked up. |
| 39 | Attributed: "are addressed separately in the studies reviewed here". |
| 40 | Mechanism explained and cited: *"When one category dominates the label distribution, the agreement expected by chance rises, and κ can fall to a low value even when two annotators agree on almost every item. This behaviour is documented in the methodological literature on agreement measurement, where it is described as the prevalence problem (Feinstein & Cicchetti, 1990; Byrt et al., 1993; Di Eugenio & Glass, 2004)."* |
| 41 | Corrected throughout: "the skewed class **distribution** of the available corpora", "when one category dominates the **label distribution**". |
| 42 | "the standard agreement statistic" → "Cohen's κ", named explicitly and defined earlier in the section. |
| 43 | "why the problem has proved persistent" → *"That is why the difficulty has persisted: correcting either weakness alone leaves the other in place."* The difficulty is named in the thesis paragraph and in each of the three findings. |
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
| Maskat & Rahman (2020) | The concrete spelling example in paragraph 3 | *International Journal on Advanced Science, Engineering and Information Technology*, 10(4), 1380–1386 ✅ Read directly from your PDF in `References/`. Table V lists `tidak = x`; Table I lists `tidak ada, takde, xde, tade` |
| Pontiki et al. (2016) | Comment 64 — OTE span marked before polarity assigned | SemEval-2016, pp. 19–30, DOI 10.18653/v1/S16-1002 ✅ Confirmed against the paper: Slot 2 is the opinion target expression given by character offsets, Slot 3 is polarity, and Phase B supplies gold Slot 1/2 annotations before participants return Slot 3 |

## Section 3.2: what the sources actually say

Everything in 3.2 was read out of the PDFs in `References/` before it was written. Two things in the plan
were wrong, and one figure needs a second pair of eyes.

### Correction 1 — *kan* is not in AlAfnan et al. (2025)

The plan said to source the particles *lah* and *kan* to AlAfnan et al. (2025). **The word *kan* does not
appear in that paper.** The particles it names are *lah* / *la*, *meh* and *ah*. *kan* comes from
Treffers-Daller et al. (2022), in the example "you understand lah kan", which they reproduce from Ozog
(1987). Section 3.2 attributes each particle to the source that actually contains it.

### Correction 2 — AlAfnan et al. (2025) has no frequency data at all

The plan treated it as evidence for how often particles appear. It is not. The methodology section states
that the study is a qualitative content analysis of **scripted dialogue from Malaysian television series** —
*Kopitiam*, *Oh My English!*, *Sepahtu Reunion Live* and *KL Gangster*. There is no corpus, no counts, and
no social media data. The paper itself flags the choice: "The focus on scripted media is justified by the
widespread use of Manglish in entertainment."

So 3.2 uses AlAfnan et al. (2025) only for **what the particles do**, and Treffers-Daller et al. (2022) only
for **how often they switch**. The paragraph on limits says this in the text rather than hiding it, which is
also the honest answer if Dr. Ho asks where the social media frequency figure is: there isn't one.

### Verified figures

Read directly from the tables in Treffers-Daller et al. (2022):

| Figure | Source | Verified |
|---|---|---|
| 1,044 switched utterances | "In total 1044 utterances with intrasentential switches were recorded" | ✅ |
| 1,217 individual switches | "The total number of switches is higher (1217), as many sentences contain more than one switch" | ✅ |
| Back-flagging 121, 11.6% | Table 3, Total row (denominator 1,044) | ✅ |
| Discourse markers 121, 9.9% | Table 4 (denominator 1,217) | ✅ |
| Fourth behind noun, NP, personal pronoun | Table 4: Noun 261 / 21.5%, NP 131 / 10.8%, Personal Pronoun 127 / 10.4%, Discourse Marker 121 / 9.9% | ✅ |
| Corpus: two university English lecturers, 15 h each | "Participants were a male (Ali) and a female (Azma) English language lecturer… seven classroom sessions (15 h) were video recorded for each participant" | ✅ |
| *lah* attaches to English, Malay or mixed clauses | Treffers-Daller et al. (2022), reporting Ozog (1987) | ✅ |
| *lah* shifts assertive tone to polite request or friendly encouragement | Treffers-Daller et al. (2022), reporting Tay et al. (2016) | ✅ |
| "the specific meanings of discourse markers are often difficult to capture" | Quoted verbatim from Treffers-Daller et al. (2022) | ✅ |

**One thing to check.** Back-flagging in Table 3 and Discourse Marker in Table 4 both come to exactly **121**.
That is plausible, because back-flagging is defined by the attachment of a discourse marker, but the two
counts have different denominators and the paper does not state that they are the same 121 items. Section
3.2 reports them separately with their own denominators and does not claim they are the same set. If a
reviewer asks, that is the honest position. Worth a look at the paper yourself before submission.

**Secondary citations.** Tay et al. (2016) and Ozog (1987) are named in the text but are **not** in the
reference list, because they were read through Treffers-Daller et al. (2022) rather than directly. That is
the correct APA treatment for a secondary source, and it is also the honest one.

## A source problem in FYP1.md that you should fix in the thesis too

While verifying the spelling example I read Maskat and Rahman (2020) in full. **It does not contain the form
*tk*.**

`FYP 1.md` says, in both Chapter 1 (Problem Statement, first problem) and Chapter 2 (§2.1, Orthographic
Noise):

> the Malay word *tidak* can appear as *tak*, *tk*, or *x* (Maskat & Rahman, 2020)

What the paper actually gives:

| Table | Category | Entries containing *tidak* |
|---|---|---|
| Table I | Spelling variants | `tidak ada, takde, xde, tade` · `tidak hendak, tanak, tak nak, xnak` · `tidak mahu, tak mahu, tak mau, tamau` · `tidak tahu, tak tahu, tak tau, tatau` |
| Table V | Vowel-less spelling | `tidak = x` · `pergi = g or p` · `jangan = jgn` · `yang = yg` · `nama = nm` · `pada = pd` |

So *x* is supported and *tak* is supported. ***tk* is not in the paper at all.** The vowel-less forms the
paper does list are *jgn*, *yg*, *nm* and *pd* — *tk* looks like it was inferred from that pattern rather
than read off the page.

This is the exact failure Dr. Ho named in Round 1 comment 8: *"Citation? Or else this is just your
assumption. Writing research paper directly forces you to double check everything you said and claim."* It
is currently in your thesis in two places, uncorrected. Either drop *tk*, or replace the example with one
taken verbatim from the paper. The review paper now uses the verbatim version.

## Comment 44 — checked, and the original claim was too strong

The v5 sentence read:

> Reviews published four years apart identify the same shortage of reliable labelled resources and the same
> absence of reliability reporting (Abu Bakar et al., 2020; Selvaraju et al., 2024).

I read Selvaraju et al. (2024) from your `References/C2/` folder. **It contains zero occurrences of
"kappa", "agreement" or "reliab".** It never discusses reliability reporting at all, so it cannot support
the second half of that sentence.

What it does support, verbatim: *"There is a lack of comprehensive datasets and resources specifically
designed for code mixing Malay text"*, *"the lack of comprehensive linguistic resources and tools specific
to code mixing Malay text"*, and *"the lack of annotated data"*.

The sentence is now narrowed to what the source actually says, and rests on Selvaraju et al. (2024) alone
rather than pairing it with a source I have not read:

> A review of the field published in 2024 still reports a lack of comprehensive datasets and annotated
> resources for code-mixed Malay text (Selvaraju et al., 2024), which indicates that recent work has not
> closed the shortage.

**Also worth knowing:** the file is named `Code mixing Malay online text sentiment analysis.pdf` but the
paper's actual title is *Sentiment Analysis in Code Mixing Malay Text: A Review* (AiDAS 2024, p. 280). It is
the right paper, just misnamed on disk.

## Still unread: Abu Bakar et al. (2020)

It is cited once in Section 1, alongside Winata et al. (2023), for the claim that systematic writing is
processed as noise. IEEE Xplore blocks automated access and there is no PDF in `References/`, so this is the
one source in the paper carrying a claim that neither of us has checked. It is a co-citation rather than the
sole support, so the risk is low — but download it before submission.

## Full reference list for Sections 1 to 3.2 — 31 entries, alphabetical

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

**Maskat, R., and Rahman, N. A. (2020). Categorization of Malay social media text and normalization of spelling variations and vowel-less words. *International Journal on Advanced Science, Engineering and Information Technology*, 10(4), 1380–1386.** *(new)*

Maskat, R., Azman, N. A., Nulizairos, N. S. S., Zahidin, N. A., Mahadi, A. H., Norshamsul, S. R., Mohd Sharif, M. M., and Mahdin, H. (2024). A bi-annotated Malay-English code-switching (Manglish) dataset of X posts for biological gender identification and authorship attribution. *Data in Brief*, 52, 110034. https://doi.org/10.1016/j.dib.2024.110034

Mohd Shamsuddin, A. M., Samson Juan, S., Chua, S., and Bramantoro, A. (2024). Semi-automatic sentiment identification for Malay-English code-switched data. *Journal of Advanced Research Design*, 123(1), 198–212. https://doi.org/10.37934/ard.123.1.198212

Muysken, P. (2013). Language contact outcomes as the result of bilingual optimization strategies. *Bilingualism: Language and Cognition*, 16(4), 709–730. https://doi.org/10.1017/S1366728912000727

Nazir, A., Rao, Y., Wu, L., and Sun, L. (2022). Issues and challenges of aspect-based sentiment analysis: A comprehensive survey. *IEEE Transactions on Affective Computing*, 13(2), 845–863. https://doi.org/10.1109/TAFFC.2020.2970399

Northcutt, C. G., Athalye, A., and Mueller, J. (2021). Pervasive label errors in test sets destabilize machine learning benchmarks. *Proceedings of the 35th Conference on Neural Information Processing Systems (NeurIPS): Datasets and Benchmarks Track*.

**Pavlick, E., and Kwiatkowski, T. (2019). Inherent disagreements in human textual inferences. *Transactions of the Association for Computational Linguistics*, 7, 677–694. https://doi.org/10.1162/tacl_a_00293** *(new)*

**Pontiki, M., Galanis, D., Papageorgiou, H., Androutsopoulos, I., Manandhar, S., AL-Smadi, M., Al-Ayyoub, M., Zhao, Y., Qin, B., De Clercq, O., Hoste, V., Apidianaki, M., Tannier, X., Loukachevitch, N., Kotelnikov, E., Bel, N., Jiménez-Zafra, S. M., and Eryiğit, G. (2016). SemEval-2016 Task 5: Aspect based sentiment analysis. *Proceedings of the 10th International Workshop on Semantic Evaluation (SemEval-2016)*, 19–30. https://doi.org/10.18653/v1/S16-1002** *(new)*

Poria, S., Hazarika, D., Majumder, N., and Mihalcea, R. (2023). Beneath the tip of the iceberg: Current challenges and new directions in sentiment analysis research. *IEEE Transactions on Affective Computing*, 14(1), 108–132. https://doi.org/10.1109/TAFFC.2020.3038167

Romadhona, N. P., Lu, S.-E., Lu, B.-H., and Tsai, R. T.-H. (2022). BRCC and SentiBahasaRojak: The first Bahasa Rojak corpus for pretraining and sentiment analysis dataset. *Proceedings of the 29th International Conference on Computational Linguistics (COLING)*, 4418–4428.

Selvaraju, S., Sjarif, N. N. A., and Anuar, M. S. M. (2024). Sentiment analysis in code mixing Malay text: A review. *2024 5th International Conference on Artificial Intelligence and Data Sciences (AiDAS)*, 280–285. https://doi.org/10.1109/AiDAS63860.2024.10730298

Treffers-Daller, J., Majid, S., Thai, Y. N., and Flynn, N. (2022). Explaining the diversity in Malay-English code-switching patterns: The contribution of typological similarity and bilingual optimization strategies. *Languages*, 7(4), 299. https://doi.org/10.3390/languages7040299

Winata, G. I., Aji, A. F., Yong, Z. X., and Solorio, T. (2023). The decades progress on code-switching research in NLP: A systematic survey on trends and challenges. *Findings of the Association for Computational Linguistics: ACL 2023*, 2936–2978. https://doi.org/10.18653/v1/2023.findings-acl.185

Winata, G. I., Cahyawijaya, S., Liu, Z., Lin, Z., Madotto, A., and Fung, P. (2021). Are multilingual models effective in code-switching? *Proceedings of the Fifth Workshop on Computational Approaches to Linguistic Code-Switching*, 142–153. https://doi.org/10.18653/v1/2021.calcs-1.20

---

# Part D — What is next

**Section 3.3 is the last piece of Section 3.** Phonetic spelling multiplies the surface forms of one word.
Maskat and Rahman (2020) sort Malay social media spelling into five categories — spelling variants,
Malay-English mixed sentences, loan words, slang-based spellings and vowel-less words — and report
normalising only two of them by similarity matching, leaving the rest as open research. The annotation
consequence is the one the other two subsections have been building toward: human and automatic annotators
break on *different* inputs. A person reads *x* as *tidak* without effort; a lexicon returns
out-of-vocabulary and contributes no polarity signal at all. That asymmetry is what makes the choice of
annotator a substantive one rather than a matter of cost, and it sets up Section 4.

Sources already verified for it: Maskat and Rahman (2020), read in full for this revision, including Tables
I, III, IV and V. Abu Bakar et al. (2020) is cited in Section 1 but has not been read against its claims —
worth staging before 3.3 is written.

After 3.3, Sections 4 to 8 remain. Dr. Ho has never annotated past page 4 of the full paper, so all fifteen
rules in the master tracker apply to them unread.

---

# Part E — Page budget: you are on track to overrun

Measured at the template's 537 words per page and 26 references per page at 8pt.

| Component | Planned | Now | Delta |
|---|---|---|---|
| Title block | 0.50 | 0.50 | — |
| Abstract + keywords | 0.50 | 0.50 | — |
| 1 Introduction | 1.75 | **3.52** | **+1.77** |
| 2 Review Methodology | — | 0.60 | +0.60 |
| 3 + 3.1 + 3.2 | 1.50 | **2.30** | **+0.80** |
| 3.3, still to write (estimate) | — | 1.00 | +1.00 |
| Sections 4–8, per the conversion plan | 12.50 | 12.50 | — |
| References at 8pt, 45 entries | 2.50 | 1.73 | −0.77 |
| **Total** | **19.25** | **22.65** | **+3.40** |

**The cap is 20 pages. The projection is 22.65.**

Two causes, both introduced by the revisions rather than by the plan. Citations take space: answering ten
"Citation?" comments added sources, and each parenthetical costs three to six words. And the register fixes
are longer than what they replaced — "at the expense of the others" is four words longer than "by giving up
the others", and that pattern repeats about twenty times.

The Introduction is where the overrun concentrates. At 1,892 words it is double the plan. It reads well now,
so this is not a rewrite — it is a trim, and there are two obvious candidates:

- **The three findings could carry less evidence in Section 1** and hand it to Sections 4 to 6, which are
  supposed to carry it anyway. Finding 3 currently reports all four corpora and both κ values in the
  Introduction, then Section 6 reports them again. Cutting the Introduction to the headline of each finding
  saves roughly 400 words, or 0.75 pages, and removes a repetition a reviewer would notice.
- **Paragraphs 1 to 3 could lose about 150 words** without losing a citation.

That is about one page. The other 1.65 has to come from Sections 4 to 8, which means writing them under
budget rather than trimming them afterwards.

**Worth deciding before 3.3 is written, not after Section 8.** The alternative reading is that the plan's
allocation was simply wrong — the Introduction of a review paper carrying a three-part diagnosis may
genuinely need 3 pages, in which case the 12.5 allocated to Sections 4 to 8 is what should shrink. Either
way the decision is better made now.

---
