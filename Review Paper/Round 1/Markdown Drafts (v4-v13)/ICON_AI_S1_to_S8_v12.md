# ICON AI 2026 — Sections 1 to 8 (body complete)

**Version 12.** Replaces the draft reviewed on the PDF dated 19 August. Every one of the 64 annotations is
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
expresses a positive, negative or neutral opinion (Poria et al., 2023). Organisations use it to measure public
opinion at scale, in applications from brand monitoring to political and policy analysis (Poria et al., 2023;
Nazir et al., 2022). The tools that make this possible carry an assumption about their input: lexicons, pre-
trained models and benchmark corpora are concentrated in a small number of well-resourced languages, each
built from text written in a single standard variety (Joshi et al., 2020). Text in which two languages
alternate within one message does not satisfy that assumption, and surveys of code-switching in natural
language processing report it as a persistent source of degraded performance (Doğruöz et al., 2021; Winata et
al., 2023). Malaysian social media text is writing of exactly this kind.

Malaysia is a multilingual and multi-ethnic country in which Coluzzi (2017) recorded around 140 languages in
use, with code-mixing between a speaker's first language, English and Malay already widespread in everyday
communication. The practice has continued rather than receded, and on social media users alternate between
languages within a single message rather than writing in one language at a time (Treffers-Daller et al., 2022;
AlAfnan et al., 2025). English and Malay are the pair that combines most frequently in Malaysian writing, and
the mixed varieties they produce are known locally as *Bahasa Rojak* and *Manglish* (AlAfnan et al., 2025).
Malay-English mixed writing is frequent enough on X, the platform formerly known as Twitter, that both of the
Malaysian sentiment corpora examined in this review were collected from it (Maskat et al., 2024; Mohd
Shamsuddin et al., 2024).

How this mixed writing is regarded matters for how it is processed. *Manglish* is sometimes described as a
variety that weakens standard English and Malay rather than as a legitimate language variety in its own right
(AlAfnan et al., 2025). Its structure, however, is not random. Treffers-Daller et al. (2022) and AlAfnan et
al. (2025) show that Malay-English switching follows describable syntactic and pragmatic patterns, and that
speakers use it deliberately to communicate efficiently, signal identity and build rapport. The same
regularity holds at the level of spelling: Maskat and Rahman (2020) record the negator *tidak* written as *x*,
and *tidak ada* as *takde*, *xde* or *tade*. A reader who knows the convention recovers the word without
effort, but a lexicon compiled from standard Malay lists none of those forms. The difficulty that Malay-
English mixed writing creates for natural language processing (NLP) is therefore not carelessness. It is that
the conventions Malaysian writers follow are not the conventions standard NLP tools were built to handle, so
writing that is systematic is processed as noise (Winata et al., 2023; Abu Bakar et al., 2020).

When a sentiment model performs poorly on Malay-English mixed text, the explanation offered is most often
architectural (Doğruöz et al., 2021; Winata et al., 2023). On that account the model cannot handle code-
switched input, and a larger or more regionally adapted model would perform better. The evidence is mixed.
Khanuja et al. (2020) report that multilingual models fine-tuned on code-switched data achieve the strongest
scores among the systems evaluated on their benchmark, and Adilazuarda et al. (2022) show that robustness to code-mixing varies with the embedded language and with the composition of the pre-training corpus. Against that, Winata et al. (2021) find
that multilingual pre-training alone does not guarantee good representations of code-switched text, and
Conneau et al. (2020) describe a "curse of multilinguality" in which finite model capacity, spread across many
languages, dilutes per-language quality. Model choice therefore accounts for part of the difficulty but not
all of it.

The remainder of the difficulty does not originate in the model. It originates one step earlier, at the point
where the labels are created. Supervised sentiment analysis requires that every message be read and assigned a
sentiment label, by a human annotator or by an automatic one, before any model can be trained or evaluated on
it (Artstein & Poesio, 2008). This step is called annotation, and the labels it produces form the supervision
signal that a model learns from and is measured against. The consequences of incorrect labels reach beyond the
dataset. Label noise is learned during training and degrades the resulting classifier (Frénay & Verleysen,
2014), and incorrect labels in a test set distort the evaluation of model performance, so that reported
accuracy no longer reflects how the model actually behaves (Northcutt et al., 2021; Bowman & Dahl, 2021). An
unsound label therefore damages the model twice, once when it is trained and again when it is measured.

This review argues that for Malaysian Malay-English code-mixed sentiment data, the annotation label is at
present the more limiting problem, together with the evidence offered that the label is sound. Three findings
in the existing literature support that reading, and each of them returns in the sections that follow.

The first finding is that no available Malay-English sentiment resource combines the properties a general-
purpose corpus requires. Four such resources currently exist (Mohd Shamsuddin et al., 2024; Kasmuri & Basiron,
2019; Kong et al., 2023; Romadhona et al., 2022). None of them is simultaneously large, balanced across
sentiment classes, drawn from casual social media, and validated by human annotators. Each secures some of
these properties at the expense of the others.

The second finding is that the class imbalance in the largest of those resources originates in the labelling
method rather than in Malaysian discourse. MESocSentiment is the largest general-domain corpus, and its 19,714
posts are labelled 78.23% neutral, 16.33% positive and 5.44% negative (Mohd Shamsuddin et al., 2024). Two
pieces of evidence point to the method. The corpus was collected under the "#Malaysia" keyword across sports,
politics and the arts, which are not topics on which social media users are typically neutral (Mohd Shamsuddin
et al., 2024). A comparable corpus of Malaysian tweets labelled by human annotators is only 23.6% neutral
(Kong et al., 2023). The neutral share differs by a factor of more than three between two corpora of the same
text type, and what differs is who or what assigned the labels.

The third finding is that annotation reliability is rarely reported, and that where a figure is given it
measures a narrower task than the one the corpus is used for. Reliability is normally demonstrated by having
independent annotators label the same text and computing a chance-corrected agreement coefficient, the most
widely used of which is Cohen's kappa (κ) (Cohen, 1960; Artstein & Poesio, 2008). Two of the four regional
resources report no coefficient at all. The two that do report one obtained it for a binary judgement rather
than for the three-class polarity task those resources are used to support. Research on Malaysian code-mixed
sentiment therefore lacks not only reliable annotations but also established practice for validating their
reliability.

The second and third findings describe one condition rather than two, although the studies reviewed here
address them separately. The skew that the labelling methods produce is itself the condition under which
Cohen's κ becomes difficult to interpret. When one category dominates the label distribution, the agreement
expected by chance rises, and κ can fall to a low value even when two annotators agree on almost every item.
The effect is known as the prevalence problem and is documented in the methodological literature on agreement
measurement (Feinstein & Cicchetti, 1990; Byrt et al., 1993; Di Eugenio & Glass, 2004). The same imbalance
that makes the labels unrepresentative therefore also weakens the statistic used to check them. That is why
the difficulty has persisted: correcting either weakness alone leaves the other in place. A 2024 review of the
field still reports a lack of comprehensive datasets and annotated resources for code-mixed Malay text
(Selvaraju et al., 2024).

This review examines one question: why reliable annotation and evaluation of Malaysian Malay-English code-
mixed sentiment data remain unresolved. Linguistic description, model architecture and application domain are
discussed only where they are relevant to that question. Two related topics fall outside the scope. The first
is comparative benchmarking of sentiment classifiers, and the second is sentiment analysis as a general field.
Both have already been surveyed in detail (Poria et al., 2023; Nazir et al., 2022; Selvaraju et al., 2024).

The scope of this review also excludes several activities. It does not propose, implement or evaluate a
system, and it does not report the author's own experimental work. Its contribution is a diagnosis of why the
problem remains unresolved, together with a set of directions for future research.

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

## 3.3 Phonetic spelling multiplies the surface forms of a single word

The first two properties concern where the sentiment is and how it is to be read. The third concerns whether
the words carrying it can be recognised at all. Malaysian users spell phonetically rather than to a dictionary
standard, so a single word appears in many written forms. Maskat and Rahman (2020) provide a formal
categorisation of this variation for Malay. Working from a corpus of 6,241 Twitter posts collected between
2014 and 2018, they sort what they call Social Media Malay Language into five categories. The five are
spelling variants, Malay-English mixed sentences, loan words written with Malay phonology, slang-based
spellings, and vowel-less words.

The variation within each category is wide. Among the spelling variants Maskat and Rahman (2020) record,
*macam mana* appears as *mcmana*, *camne*, *camner*, *mcmner* and *cane*, and *tidak ada* appears as *takde*,
*xde* and *tade*. The vowel-less category reduces a word to consonants or to a single character, so *tidak* is
written *x*, *jangan* is written *jgn* and *pada* is written *pd*. The slang category adds a regional layer,
with *besar* written *besaq* in the north and *beso* on the east coast. The categories also combine, and the
same study gives *x suko* as a form drawing on the slang and vowel-less categories at once.

Whether this variation can be undone automatically is the question that matters for annotation, and Maskat and
Rahman (2020) tested it directly. They attempted to normalise two of the five categories, spelling variants
and vowel-less words, using n-gram similarity indices and Levenshtein distance. Their benchmark was a ground
truth of 1,176 similar-word pairs covering 435 unique words, identified by hand by a native Malay speaker.
Measured against that benchmark, the highest precision reported for any configuration is 0.43, and most
configurations fall well below it. The authors conclude that similarity matching can detect the two categories
but that a more sophisticated technique is needed, and they state that normalisation of the remaining three
categories is open for future research.

Two limits on this evidence should be noted. Only Selangor slang was handled, so the slang category is
represented more narrowly than the regional range the same paper describes. More consequentially for this
review, English words were removed before the experiment and code-mixed posts were excluded from the
evaluation subsets. The reported precision is therefore a measurement on Malay text with the English stripped
out, not on Malay-English mixed text, and no equivalent measurement for the mixed case is available.

The consequence for annotation is an asymmetry between the two types of annotator, and it is visible inside
the study just described. A single native speaker recovered 1,176 word pairs by hand, reliably enough for the
result to serve as ground truth. Automated matching against that same ground truth reached a highest precision
of 0.43. A human reader recovers *x* as *tidak* without effort. The automatic procedure largely does not. The
two types of annotator therefore do not break on the same inputs, and they do not break at the same rate.

That asymmetry changes what the choice of annotator is. If human and automatic annotation differed only in
cost and speed, the choice would be a matter of budget. Because they break on different inputs, the choice
determines which errors a corpus will contain, and a corpus labelled entirely by one type carries that type's
blind spot throughout.

The three properties examined in this section therefore place three distinct demands on annotation. The first
makes the opinion-bearing span difficult to locate. The second leaves its reading underdetermined once
located. The third makes the tokens themselves unrecoverable to an automatic annotator while they remain
transparent to a human one. Section 4 examines the annotation strategies used in response, and the trade-offs
each one accepts.

---

# 4. Annotation Practice and Its Failure Modes

Section 3 described what makes Malaysian code-mixed text hard to label. This section examines what has been
done about it. The strategies reported in the reviewed studies are set out first, arranged by the trade-off
each one accepts. The distribution of labels they produce is examined next, and the practice of pooling
several annotators is examined last, because it is the remedy most often proposed, and the one the regional
evidence tests most directly.

## 4.1 Annotation strategies and the fidelity-scalability trade-off

For low-resource code-mixed text, label fidelity and scale pull against each other. A corpus can be labelled
carefully or it can be labelled in volume. The strategies in the literature are best read not as competing
solutions to one problem, but as different decisions about which of the two to give up. Read that way they
fall into three tiers.

The first tier is manual annotation by people. Two of the four regional corpora were built this way, and they
are the only two whose labels come from human judgement. Kasmuri and Basiron (2019) drew 5,849 sentences from
23 personal blogs, selected 4,191 for annotation, and retained 2,316 in the finished corpus, reporting κ =
0.83 for the judgement of whether a sentence was opinionated or factual. Kong et al. (2023) collected 108,246
tweets and manually annotated 11,568 of them into three sentiment classes, using three independent annotators
working from a written guideline. What both illustrate is the cost of the decision rather than a defect in the
method. Kasmuri and Basiron kept 40% of the sentences they started with, and Kong et al. labelled 11% of what
they collected. The labour that produces reliable labels is the same labour that prevents either corpus from
reaching the scale a general-purpose Manglish resource would require.

The second tier is semi-automated annotation, which trades in the opposite direction by using existing tools
to label at volume and accepting the tools' limitations as the price. Mohd Shamsuddin et al. (2024) built
MESocSentiment this way. They collected 229,566 tweets carrying the "#Malaysia" keyword, reduced the set to
138,646 in pre-processing, applied the Malaya and Lingua libraries to identify code-switched posts, and
arrived at 20,226 tweets. Sentiment labels were then assigned by majority vote among three existing analysers.
The authors state the motivation plainly. The language identification libraries "reduced the need to find
fluent speakers in Malay and English to classify the tweets", and the sentiment analysers "eliminated the need
to find speakers fluent in Malay and English to label the dataset". The reasoning is defensible, and there is
evidence from other labelling tasks that automated annotators can match or exceed human crowd workers (Gilardi
et al., 2023). What the tier concedes is that the labels can be no more competent than the tools producing
them, and inherit whatever those tools cannot read.

The third tier replaces those tools with generative models used directly as annotators. Because a generative
model is not restricted to a fixed vocabulary, it can in principle interpret an unfamiliar spelling or an
unseen slang term from context, which is the capability the second tier lacks. In principle this dissolves the
trade-off. The peer-reviewed evidence does not yet support that reading. Jadhav et al. (2025) evaluated
generative annotators on Marathi across four tasks: sentiment analysis, two-class hate speech detection, four-
class hate speech detection, and news classification. They found GPT-4o and Llama 3.1 405B trailing a fine-
tuned BERT baseline by average accuracy margins of 10.2% and 14.1% respectively. They conclude that fine-tuned
transformers remain necessary where linguistic resources are scarce. Marathi is morphologically rich where
Malay is not, so the result bounds the tier's promise rather than measuring it in this setting. That it is the
only peer-reviewed study of the question available to this review is itself part of the finding. The third
tier is the least evidenced of the three, and no published study evaluates generative annotation on Malaysian
code-mixed text.

**Table 1.** Annotation strategies for Malaysian Malay-English code-mixed sentiment data

| Tier | Regional example | Scale achieved | Evidence of fidelity | What is conceded |
|---|---|---|---|---|
| Manual | Kasmuri and Basiron (2019) | 2,316 sentences retained from 5,849 candidates, drawn from 23 blogs | κ = 0.83, for a binary opinionated-or-factual judgement | Scale |
| Manual | Kong et al. (2023) | 11,568 tweets annotated from 108,246 collected | Three annotators and a written guideline; no coefficient reported | Scale |
| Semi-automated | Mohd Shamsuddin et al. (2024) | 19,714 posts from 229,566 collected | None reported; the pipeline has no human annotation stage | Demonstrable fidelity |
| Fully automated, generative | None published for Malay-English | — | — | Reliability precisely where linguistic resources are scarce (Jadhav et al., 2025) |

Read across the rows, each tier resolves one constraint by giving up another, and the concession follows from
what the strategy is rather than from how carefully it was carried out. No strategy in the reviewed literature
secures fidelity and scale together for this data.

## 4.2 Two causes of neutral-label skew

The clearest regional evidence of what the second tier costs is the class distribution of the corpus it
produced. MESocSentiment is labelled 78.23% neutral, 16.33% positive and 5.44% negative across 19,714 posts
(Mohd Shamsuddin et al., 2024). Section 1 gave two reasons for reading that distribution as an artefact of the
labelling method rather than a property of Malaysian discourse. This section separates the two distinct causes
at work in it, because they produce identical labels and require opposite responses.

The first cause is the behaviour of a scoring function that finds nothing to score. Lexicon-based sentiment
tools work by matching each word or phrase in a text against a sentiment lexicon and aggregating the scores of
the matched words into an overall score (Selvaraju et al., 2024). That score is then divided into classes by
threshold. VADER, one of the three analysers used to build MESocSentiment, sets its classification thresholds
at −0.05 and +0.05 on a normalised score running from −1 to 1 (Hutto and Gilbert, 2014). Two consequences
follow from combining those two facts, and this review states them as an inference rather than as a reported
finding. A text whose affective tokens are absent from the lexicon contributes little or nothing to the
aggregate. Its score therefore stays inside the neutral band, and it is returned as neutral. On that reading,
neutral is not always a judgement that a text is affectively balanced. It can also be the default output when
nothing was recognised.

The corpus authors' own error analysis indicates that the mechanism fires on this data. Alongside the corpus,
Mohd Shamsuddin et al. (2024) present two small tables comparing the ensemble's label with the correct one.
All three of the misclassified examples they give are neutral labels that should have been positive, and in
all three the sentiment is carried by Malay: *memang cantik sangat*, *selamat deepavali* and *raih gelar
juara*. In the correctly classified negative example, the sentiment is carried by an English word,
*worthless*. Six author-selected examples are illustrative rather than statistical, and no error rate can be
computed from them. Their uniformity is nonetheless difficult to dismiss: where the ensemble succeeded, the
affect was in a language its tools covered, and in every case where it failed, the affect was not.

The second cause has nothing to do with tooling. Some posts are genuinely hard to judge, and the annotators of
the regional corpora say so. Kasmuri and Basiron (2019) note that low agreement in sentiment annotation arises
because sentiment texts are subjective, so evaluations differ from one annotator to another and are shaped by
each annotator's background. Kong et al. (2023) make the same point about their own task, observing that
tagging text with sentiment labels is highly subjective and influenced by personal beliefs, and that a clear
guideline is needed for this reason. As Section 3.2 established, disagreement of this kind is not removed by
collecting more judgements (Pavlick and Kwiatkowski, 2019).

Separating the two causes matters because the labels they produce are indistinguishable and the responses they
require are opposite. A genuinely neutral post is correctly labelled and belongs in the corpus. A falsely
neutral post is an error that a better-resourced annotator would not have made. A single-model pipeline is
structurally unable to tell them apart, because the evidence that would distinguish them, namely the affect
the annotator could not read, is exactly the evidence that annotator does not have.

The consequence is more damaging than the headline percentage suggests, because a false neutral does not only
inflate one class. It also depletes another. Every strongly polarised post absorbed into the neutral class is
a training example removed from a minority class that a downstream classifier needs most. At a 5.44% negative
share, the smallest class in the corpus is also the one most exposed to that erosion.

## 4.3 What consensus does with disagreement

Pooling several annotators is the intuitive remedy for an unreliable one, and MESocSentiment is evidence
against the intuition, because it already was a consensus pipeline. Three sentiment analysers labelled every
post and the majority label was assigned. The corpus skewed anyway.

The reason is visible in the corpus authors' own reporting, and it is not the one that might be expected.
Voting cancels error only to the extent that voters fail independently, and the usual guarantee of
independence is architectural difference. Table 2 shows that architectural difference was present and did not
help.

**Table 2.** The three annotators used to build MESocSentiment, and the labels each assigned (Mohd Shamsuddin et al., 2024)

| Analyser | How the corpus authors describe it | Languages it is described as covering | Neutral labels assigned, of 19,714 |
|---|---|---|---|
| TextBlob | "a Python library used to process textual data" | Not stated | 14,305 (72.6%) |
| VADER | "a rule-based model … made to focus on social media texts" | Not stated | 13,115 (66.5%) |
| pysentimiento | A toolkit "trained for sentiment analysis in English, Spanish, Portugeuse, and Italian" | English, Spanish, Portuguese, Italian | 16,916 (85.8%) |
| Majority vote | — | — | 15,422 (78.2%) |

Two things follow. The first is that every analyser skewed neutral before any vote was taken, so the skew was
not produced by the voting rule. The second is that the analyser skewing hardest, at 85.8%, is pysentimiento,
which is the transformer-based tool of the three. The shared weakness is therefore not shallow processing,
since the deepest model performed worst. None of the three is described by the corpus authors as covering
Malay, and one is explicitly described as trained on four other languages. The property the three voters share
is the language they cannot read, and a Malay affective token invisible to one is invisible to all. The
ensemble does not cancel that error. It ratifies it, and unanimity produced this way is indistinguishable from
confidence.

The second weakness concerns the posts the ensemble cannot agree on. Where all three analysers returned
different labels there was no majority, and the authors state their response directly: ambiguous cases "were
removed to ensure the corpus only contains tweets from absolute categories". This affected 512 posts, or 2.53%
of the 20,226 labelled. The difficulty is not the proportion but the composition. A post on which three
analysers disagree is one where the signal is contested, or is carried by material none of them reads
confidently. That description fits the heavily code-switched and particle-laden cases Section 3 identified as
the hard core of the problem. The rule therefore removes the examples a robust classifier would most need, and
removes them systematically rather than at random.

The effect on the corpus can be computed from the paper's own tables, and it runs in the wrong direction.
Removing the contested posts left the neutral count unchanged at 15,422 while reducing the total from 20,226
to 19,714, so the neutral share rose by roughly two percentage points. Taken with the first weakness, static
voting has a double effect: it keeps the labels it is confident about and wrong about, and deletes the ones it
is uncertain about and would have learned from.

The methodological literature on annotation supports treating that deletion as a loss rather than a cleanup.
Uma et al. (2021) survey learning from disagreement and question the assumption that a single correct
interpretation exists for every item. They report that models trained on the full distribution of annotator
judgements can outperform models trained on aggregated or even gold labels. On that view, the 512 discarded
posts were not noise removed from the corpus but signal removed from it.

What the reviewed literature does not contain is any evaluation of a better procedure on this data. No
published study adjudicates annotator disagreement on Malaysian code-mixed sentiment text, and the premise
that annotators of different types fail independently, which is what licenses aggregation in the first place,
is asserted rather than measured on this material. The evidence assembled above suggests that independence
fails when the annotators share a language gap, but a suggestion is not a measurement and this review does not
treat it as one. Both points are recorded here and returned to in Section 7 as questions for future research.

---

# 5. Models as Annotation Instruments

Section 4 established that the choice of annotator determines which errors a corpus will contain. This section
asks where each family of model breaks down when used as an annotator. The question is not which architecture
classifies best, which belongs to the comparative benchmarking placed outside the scope in Section 1. It is
what each family cannot read, because that limitation is inherited by every corpus it labels.

Fine-tuned multilingual encoders acquire their competence from exposure. Manukonda and Kodali (2025)
illustrate the mechanism. They fine-tuned XLM-RoBERTa using masked language modelling over original, fully
transliterated and partially transliterated versions of the same text, and report a macro F1 of 0.90 on the
shared-task test set. The model handled the variant spellings because it had been shown them in training. A
corollary follows from the method rather than from any claim the authors make. An encoder resolves the
variation it has been trained on, so the coverage of a fine-tuned annotator is bounded by the coverage of its
fine-tuning data. Extending that coverage requires more annotated or transliterated regional data, which is
the resource whose scarcity motivated automated annotation in the first place. Two limits should be noted: the
study is a shared-task system description rather than a full investigation, and the task is fake news
detection in Malayalam rather than sentiment analysis in Malay. What transfers is the mechanism, not the
result.

Generative models locate their competence differently. Because they are not restricted to a task-specific
vocabulary, they can in principle interpret an unfamiliar spelling or an unseen slang term from context. This
is the capability the encoder lacks, and it is why generative annotation is attractive for a variety that
changes faster than its resources. The competence is distributed unevenly across languages, and not in the way
resource volume alone would predict. Jadhav et al. (2025) found frontier models trailing a fine-tuned BERT
baseline by 10.2% and 14.1% accuracy when annotating Marathi. Adilazuarda et al. (2022) tested Indonesian
code-mixed with four embedded languages, namely English, Sundanese, Javanese and Malay, and found robustness
to English mixing lower than robustness to Javanese and Malay mixing across all models tested. They attribute
the difference to the composition of the pre-training corpus. The direction is worth stating plainly. The
embedded language best represented in pre-training was the one the models handled least robustly. Robustness
to code-mixing therefore does not follow directly from how much of a language a model has seen.

The operative point is not the relative standing of the two families but the shape of their respective
limitations. The encoder is reliable on what it has been shown and blind to what it has not. The generative
model reasons about the unfamiliar, but its robustness on a given language pair cannot be predicted from the
volume of data behind either language. Selecting an annotator is therefore not selecting a level of quality.
It is selecting a failure mode, and the labels a corpus contains carry the signature of whichever mode was
selected.

---

# 6. Evaluating Annotation Reliability

Sections 4 and 5 concerned how labels are produced. This section concerns how the labels that result are shown
to be sound. Reliability is normally demonstrated with a chance-corrected agreement coefficient, of which
Cohen's κ is the most widely used (Cohen, 1960). The coefficient measures how far the agreement two annotators
actually reach exceeds the agreement expected by chance. Magnitudes are then read against conventions. In
computational linguistics, values above 0.8 are generally treated as good reliability, and values between 0.67
and 0.8 as allowing tentative conclusions (Artstein and Poesio, 2008).

Those conventions assume that expected chance agreement is stable across datasets, and it is not. Feinstein
and Cicchetti (1990) show that an imbalance in the marginal totals of an agreement table can convert a high
observed agreement into a low coefficient. Their worked example is worth reproducing. Holding observed
agreement at 0.85, an expected chance agreement of 0.50 yields κ = 0.70, while an expected chance agreement of
0.78 yields κ = 0.32. The annotators agreed on the same 85% of items in both cases. Byrt et al. (1993)
formalise the effect, showing that κ reflects the distribution of data across categories as well as agreement,
and propose a prevalence-adjusted coefficient in response. Artstein and Poesio (2008) state the consequence
for annotation directly: when one category is very common, high agreement can result from indiscriminate
coding rather than from an ability to distinguish between categories.

That is the condition Malaysian code-mixed sentiment data is in. Section 4 established that the labelling
methods available for this text produce heavily skewed class distributions, the largest corpus standing at
78.23% neutral. A skew of that size raises expected chance agreement, which is the quantity the correction
depends on. The property that makes the labels unrepresentative is therefore the property that makes the
statistic used to check them difficult to read. The difficulty runs in both directions. A low coefficient may
indicate unreliable annotation, or a dominant class. A high one may indicate reliable annotation, or
indiscriminate coding. Neither reading can be ruled out from the coefficient alone. This is the sense in which
the annotation problem and the evaluation problem are one problem rather than two, and the reason correcting
either alone leaves the other in place.

What the four regional corpora report about their own reliability is set out in Table 3.

**Table 3.** Reliability evidence reported by the four Malay-English sentiment corpora

| Corpus | Annotators | Written guideline | Coefficient reported | What the coefficient measured |
|---|---|---|---|---|
| MESocSentiment (Mohd Shamsuddin et al., 2024) | None; three automatic analysers | Not applicable | None | — |
| MyCovid-Senti (Kong et al., 2023) | Three, independent | Yes | None | — |
| MY-EN-CS (Kasmuri and Basiron, 2019) | Two undergraduates proficient in Malay and English | Yes; the guideline is the paper's contribution | κ = 0.83 | Whether a sentence is opinionated or factual |
| SentiBahasaRojak (Romadhona et al., 2022) | Five native Bahasa Rojak experts | Not stated | "Kappa" = 0.77; the variant is not specified | Whether a stock-market post is bullish or bearish |

Three observations follow. Half of the regional corpora report no agreement coefficient at all, including one
annotated by three people working from a written guideline. The two coefficients that are reported were
obtained for binary judgements, and neither is the three-class polarity task the corpora are used to support.
Romadhona et al. (2022) report a kappa value without stating which coefficient it is. Their annotation used
five experts with the final label set by majority vote, and Cohen's κ is defined for two annotators.

No corpus in the regional literature therefore supplies what a reliability claim requires: a coefficient of a
stated type, computed for the task the labels are used for, over annotators whose number and qualification are
recorded. A corpus that did supply them would still face the interpretation problem above, because the class
distributions these methods produce are the distributions under which the coefficient becomes hard to read.
Establishing reliability for this data is not only unreported. With the instruments currently in use, it is
not clearly achievable.

---

# 7. Synthesis: How the Challenges Compound

Sections 3 to 6 examined linguistic structure, annotation practice, model capability and reliability
measurement in turn, which is how the literature itself is organised. Read separately they describe four
difficulties. Read together they describe one sequence, in which each difficulty creates the conditions for
the next and the sequence returns to its own starting point. Figure 1 sets it out. Establishing that this
structure exists is the contribution this review claims, and the directions in the second half of this section
are traced to points within it.

![Figure 1](fig/fig1.png)

**Figure 1.** The compounding chain in Malaysian code-mixed sentiment annotation

The first link runs from linguistic structure to systematic disagreement. Section 3 established three
properties of this text. Switching occurs inside the clause and offers little cue to where the opinion lies.
Affect is often carried by particles belonging to neither standard language. Phonetic spelling multiplies the
surface forms of a word. The consequence is not only that agreement is harder to reach. It is that
disagreement takes a particular form. Where one annotator reads *lah* as a softener and another reads it as a
marker of sarcasm, and each reading is stable, the disagreement recurs on the same construction in the same
direction. Random disagreement is reduced by recruiting more annotators, because independent errors average
out. Systematic disagreement is not, because additional annotators bring their own stable readings rather than
noise around a shared one (Pavlick and Kwiatkowski, 2019). The usual response to unreliable annotation is
therefore unsuited to the type of unreliability this text produces.

The second link runs from disagreement to automation. Competent annotation of this material requires a fluent
bilingual reader, and that requirement follows from the linguistic properties of the text rather than from any
general fact about annotation. The corpus papers give cost and annotator availability as their reason for
automating, and Mohd Shamsuddin et al. (2024) state that their tools "eliminated the need to find speakers
fluent in Malay and English to label the dataset". Automation on this material is therefore downstream of the
linguistic difficulty rather than an independent methodological preference.

The third link runs from automation to a shared blind spot. Annotators chosen under cost pressure are chosen
for availability, and the tools available are those built for well-resourced languages. Section 4.3 showed
what follows in the one regional case where the composition is documented. None of the three analysers used to
build MESocSentiment is described as covering Malay, each skewed neutral before any vote was taken, and the
most neutral-skewed of them was the transformer. Voting cancels error only to the extent that voters fail
independently. Where the property they share is the language none of them reads, the ensemble ratifies the
error instead of cancelling it, and unanimity produced that way is indistinguishable from confidence.

The fourth link runs from the shared blind spot to class skew. False neutrals accumulate rather than being
corrected, and the corpus acquires a class distribution that no participant intended. MESocSentiment reaches
78.23% neutral. Section 4.2 separated the two mechanisms that produce this, but one of them deserves restating
here, because it is the point at which the process turns on itself. Posts on which the three analysers could
not agree were removed, 512 of them, on the stated ground of retaining only "absolute categories". Those posts
are not a random sample. They are the contested, heavily code-switched cases that the first link identifies as
the source of the difficulty, and removing them raised both the neutral share and the measured agreement.

The fifth link runs from class skew to the reliability instrument, and it is where the two halves of this
review meet. The distribution produced at the fourth link is the specific condition under which a chance-
corrected coefficient stops returning interpretable values (Feinstein and Cicchetti, 1990; Byrt et al., 1993).
A researcher who suspects the labels are unsound and computes a coefficient obtains a low value, which is
consistent with poor annotation and equally consistent with competent annotation of a skewed corpus. Raw
agreement carries the same ambiguity in the opposite direction (Artstein and Poesio, 2008). The defect and the
inability to detect the defect have one cause. That is what separates an unresolved problem from a merely
difficult one: here the quality check is least informative exactly where quality is lowest.

The sixth link closes the cycle. Corpora whose reliability was never established are released, trained on and
evaluated against, so every downstream comparison inherits an error term that nobody has quantified. The more
consequential edge is the one that returns. The annotators used to build the next corpus are fine-tuned on the
last, and Section 5 showed that a fine-tuned encoder resolves only the variation it has been shown. The blind
spots of one generation of labels are transmitted to the instruments that produce the next, so the chain does
not merely persist. It reproduces itself.

Read as a whole, the chain explains a pattern that the individual studies cannot. Each reviewed work
intervenes at one link and does so competently. None addresses the chain as a chain, and an intervention at
one link is assessed with an instrument compromised at another, so the assessment cannot establish whether the
intervention worked. That is why effort in this area has been absorbed without accumulating.

The chain identifies where intervention would matter, not which intervention would succeed. The five
directions below are framed as work that remains to be done rather than as a programme any particular study
should adopt. Each is traced to a link, since a direction that cannot be traced to a finding is a preference
rather than a conclusion.

The first direction is agreement measurement under class skew, and it follows from the fifth link. Prevalence-
adjusted coefficients exist (Byrt et al., 1993) but have not been evaluated on code-mixed sentiment data, so
it is not known which behaves best under the distributions these corpora actually exhibit. The study requires
no new data collection, only an existing annotated corpus, a set of candidate coefficients, and a comparison
of how they behave as skew increases. It is a precondition for the others, because until reliability can be
measured under prevailing conditions, no corpus built hereafter can be shown to improve on the ones described
here.

The second direction is a minimum reporting standard, and it follows from Table 3. A minimum set for any newly
released corpus would comprise five elements: (1) the number of annotators and their stated qualification; (2)
the availability of the annotation guideline; (3) the variant of the coefficient and the task it was computed
for; (4) per-class rather than aggregate agreement; and (5) the full class distribution. Per-class agreement
deserves particular emphasis, since an aggregate figure on a skewed corpus is dominated by the majority class
and can conceal near-total disagreement on the minority polarities that matter most.

The third direction is a shared annotation convention for affect-bearing particles, and it follows from the
first link. Because the disagreement these particles generate is systematic rather than random, the
appropriate remedy is a shared convention rather than additional annotators, and no such convention exists for
*lah*, *kan* and their equivalents. A model is available. Mohammad (2016) proposes a questionnaire that
separates the speaker's emotional state, the target of the opinion and the attitude taken toward it. It also
treats sarcasm, ridicule and mockery as a distinct response rather than folding them into polarity, which is
precisely the ambiguity Section 3.2 identified. Kong et al. (2023) adapt this scheme into a four-question
guideline for Malaysian tweets. What is absent is not the design but its adaptation to Malaysian particles and
its adoption across projects.

The fourth direction is to publish label distributions rather than only resolved labels, and it follows from
the fourth link. Current practice resolves disagreement by majority rule or removes it, discarding the
information that the case was contested. Uma et al. (2021) report that models trained on the full distribution
of annotator judgements can outperform models trained on aggregated labels. Publishing that distribution would
preserve the cases present pipelines delete. It would also make the fourth link visible, since a corpus that
reports what it discarded allows a reader to judge whether its reported reliability was earned or obtained by
attrition.

The fifth direction is to test the independence premise, and it follows from the third link. Every consensus
mechanism in this literature depends on the premise that annotators of different construction fail
independently, and on this material the premise is asserted throughout and measured nowhere. The study is a
direct one: label a common sample with annotators of deliberately different competence, and measure the
correlation of their errors rather than their individual accuracies. Low correlation would justify the
aggregation strategies already in use. High correlation would indicate that consensus on this material adds
confidence without adding evidence.

These are directions rather than results. The claim of this review is not that they will succeed. It is that
the chain in Figure 1 identifies where effort in this area is currently absorbed without accumulating, and
that the first direction is a precondition for knowing whether any of the others have worked.

---

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

## Full reference list for Sections 1 to 8 — 37 entries, alphabetical

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

**Gilardi, F., Alizadeh, M., and Kubli, M. (2023). ChatGPT outperforms crowd workers for text-annotation tasks. *Proceedings of the National Academy of Sciences*, 120(30), e2305016120. https://doi.org/10.1073/pnas.2305016120** *(new)*

Frénay, B., and Verleysen, M. (2014). Classification in the presence of label noise: A survey. *IEEE Transactions on Neural Networks and Learning Systems*, 25(5), 845–869. https://doi.org/10.1109/TNNLS.2013.2292894

**Jadhav, S., Shanbhag, A., Thakurdesai, A., Sinare, R., and Joshi, R. (2025). On limitations of LLM as annotator for low resource languages. *Proceedings of the 8th International Conference on Natural Language and Speech Processing (ICNLSP-2025)*, 277–282.** *(new)*

**Hutto, C. J., and Gilbert, E. (2014). VADER: A parsimonious rule-based model for sentiment analysis of social media text. *Proceedings of the International AAAI Conference on Web and Social Media*, 8(1), 216–225.** *(new)*

**Joshi, P., Santy, S., Budhiraja, A., Bali, K., and Choudhury, M. (2020). The state and fate of linguistic diversity and inclusion in the NLP world. *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics*, 6282–6293. https://doi.org/10.18653/v1/2020.acl-main.560** *(new)*

Kasmuri, E., and Basiron, H. (2019). Building a Malay-English code-switching subjectivity corpus for sentiment analysis. *International Journal of Advanced Soft Computing and Its Applications*, 11(1), 112–130.

Khanuja, S., Dandapat, S., Srinivasan, A., Sitaram, S., and Choudhury, M. (2020). GLUECoS: An evaluation benchmark for code-switched NLP. *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics*, 3575–3585. https://doi.org/10.18653/v1/2020.acl-main.329

Kong, J. T. H., Juwono, F. H., Ngu, I. Y., Nugraha, I. G. D., Maraden, Y., and Wong, W. K. (2023). A mixed Malay-English language COVID-19 Twitter dataset: A sentiment analysis. *Big Data and Cognitive Computing*, 7(2), 61. https://doi.org/10.3390/bdcc7020061

**Maskat, R., and Rahman, N. A. (2020). Categorization of Malay social media text and normalization of spelling variations and vowel-less words. *International Journal on Advanced Science, Engineering and Information Technology*, 10(4), 1380–1386.** *(new)*

**Manukonda, D. P., and Kodali, R. G. (2025). byteSizedLLM@DravidianLangTech 2025: Fake news detection in Dravidian languages using transliteration-aware XLM-RoBERTa and transformer encoder-decoder. *Proceedings of the Fifth Workshop on Speech, Vision, and Language Technologies for Dravidian Languages*, 176–181.** *(new)*

Maskat, R., Azman, N. A., Nulizairos, N. S. S., Zahidin, N. A., Mahadi, A. H., Norshamsul, S. R., Mohd Sharif, M. M., and Mahdin, H. (2024). A bi-annotated Malay-English code-switching (Manglish) dataset of X posts for biological gender identification and authorship attribution. *Data in Brief*, 52, 110034. https://doi.org/10.1016/j.dib.2024.110034

**Mohammad, S. M. (2016). A practical guide to sentiment annotation: Challenges and solutions. *Proceedings of the 7th Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis (WASSA)*, 174–179.** *(new)*

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

**Uma, A. N., Fornaciari, T., Hovy, D., Paun, S., Plank, B., and Poesio, M. (2021). Learning from disagreement: A survey. *Journal of Artificial Intelligence Research*, 72, 1385–1470. https://doi.org/10.1613/jair.1.12752** *(new)*

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
