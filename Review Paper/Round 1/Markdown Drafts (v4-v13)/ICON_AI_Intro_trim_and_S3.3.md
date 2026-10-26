# ICON AI 2026 — trimmed Introduction and new Section 3.3

Only the two pieces you asked for. Sections 2, 3 opener, 3.1 and 3.2 are unchanged and are not repeated
here; the complete paper is in `ICON_AI_S1_to_S3.3_v7.md` in the same folder.

| | Before | After |
|---|---|---|
| Section 1 Introduction | 1,887 w · 3.51 pp | **1,611 w · 3.00 pp** |
| Section 3.3 | — | **623 w · 1.16 pp** |

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
scores among the systems evaluated on their benchmark, and Adilazuarda et al. (2022) show that robustness
depends on how well each language is represented during pre-training. Against that, Winata et al. (2021) find
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

# What was cut from the Introduction, and why

The spine is untouched — thesis sentence, three findings, synthesis. Nothing that answers one of Dr. Ho's
64 comments was removed. Six paragraphs shrank.

| Paragraph | Before | After | What went |
|---|---|---|---|
| Finding 3 (reliability) | 229 w | 119 w | **The duplication.** It listed all four corpora individually, both κ values and both narrower tasks — all of which Section 6 covers properly. It now states the finding, defines Cohen's κ once (κ is needed in the synthesis paragraph), and reports the shape of the evidence: two of four report nothing, the other two measured a binary judgement. |
| Architectural explanation | 191 w | 128 w | The closing clause restating the code-switching surveys, which the paragraph's opening citation already carried. "Several studies support that reading" → "The evidence is mixed", which is shorter and more accurate. |
| Manglish is rule-governed | 206 w | 175 w | Tightened. The *tidak* / *takde* / *xde* / *tade* example stays — it is the concrete anchor the paragraph needed. |
| Annotation as the earlier step | 175 w | 155 w | Three narrative citations converted to parenthetical. Same evidence, fewer words. |
| Synthesis | 171 w | 155 w | The Selvaraju sentence shortened to one clause. |
| Finding 2 (neutral skew) | 144 w | 128 w | Redundant qualifiers. Both pieces of evidence and both figures kept — the 78.23% against 23.6% contrast is the strongest single fact in the paper. |

**What deliberately stayed.** The three contributions (106 w) answer comments 49–53 word for word. The
scope paragraphs (127 w) answer 45, 46, 47 and 48. The roadmap (73 w) is required by the structure Dr. Ho
asked for in Round 1 comment 68. Cutting any of those would trade a page for a comment.

---

# Section 3.3: what the sources actually say

Everything below was read out of `References/Maskat, R., & Rahman, N. A. (2020)…pdf`.

| Claim in 3.3 | Verified against |
|---|---|
| Corpus of 6,241 Twitter posts, 2014–2018 | "Our corpus has 6,269 reviews from Twitter covering over four years, from 2014 to 2018. After duplicate removal, the size is 6,241." ✅ |
| Five SMML categories | "spelling variations, Malay-English mix sentences, loan words/phrases, slang-based words, and vowel-less words" ✅ |
| *macam mana* → *mcmana, camne, camner, mcmner, cane*; *tidak ada* → *takde, xde, tade* | Table I, verbatim ✅ |
| *tidak* = *x*, *jangan* = *jgn*, *pada* = *pd* | Table V, verbatim ✅ |
| *besar* → *besaq* north, *beso* east coast | Table IV, verbatim ✅ |
| *x suko* combines two categories | "'x suko' is a combination between Categories 4 and 5" ✅ |
| Only two of five normalised | "we conducted a normalization on two of the SMML categories, spelling variations, and vowel-less words" ✅ |
| Remaining three left open | "Normalization of the rest of the categories is open for future research works" ✅ |
| Ground truth: 1,176 pairs, 435 unique words, one native speaker | "we have identified and manually annotated similar words by the service of a native Malay human speaker. The ground truth set size is 1,176 pairs… consists of 435 unique words" ✅ |
| Highest precision 0.43 | Table VIII. Every reported value: 0.269, 0.176, **0.429**, 0, 0.142, 0.278, 0.196, 0.39, 0.015, 0.067, 0.39, 0.347, 0.23, 0.264, 0.327, 0.391, 0.051, 0.159, 0.292, 0.411, 0.007, 0.025, 0.124, 0.287, 0.212, 0.026, 0.007. Maximum is 0.429 ✅ |
| Only Selangor slang handled | "In this work, only Selangor slang words are handled" ✅ |
| English removed, code-mixed excluded | "Additionally, English words are removed, leaving only non-English words" and "English reviews, [en] and [en, others], consisted of code-mixing text and were also excluded" ✅ |

**The limit that matters, and why 3.3 states it in the body.** Maskat and Rahman ran their experiment with
English stripped out and code-mixed posts excluded. Their precision figures are therefore not a measurement
on Malay-English mixed text. It would be easy to present 0.43 as the failure rate for the case this review
is about; it is not, and the paragraph on limits says so. If Dr. Ho asks whether the number transfers, the
answer is that no measurement for the mixed case exists — which is itself a gap worth naming in Section 7.

**Why the argument works.** The asymmetry is demonstrated inside one paper rather than assembled from two.
One native speaker produced the ground truth by hand; automated matching against that same ground truth
reached 0.43. Human recovery is the benchmark, and machine recovery fails against it. That is a cleaner
piece of evidence than citing a human study and a machine study separately, and it is harder to argue with.

**No new references.** Maskat and Rahman (2020) was already in the list from the Introduction's spelling
example. Sections 1 to 3.3 still cite 31 sources.

---

# Page budget after both changes

| Component | Planned | v6 | Now |
|---|---|---|---|
| Title block | 0.50 | 0.50 | 0.50 |
| Abstract + keywords | 0.50 | 0.50 | 0.50 |
| 1 Introduction | 1.75 | 3.52 | **3.00** |
| 2 Review Methodology | — | 0.60 | 0.60 |
| 3 + 3.1 + 3.2 | 1.50 | 2.30 | 2.30 |
| 3.3 | — | 1.00 est. | **1.16** |
| Sections 4–8 | 12.50 | 12.50 | 12.50 |
| References at 8pt, 45 entries | 2.50 | 1.73 | 1.73 |
| **Total** | **19.25** | **22.65** | **22.29** |

The trim bought 0.51 pages and 3.3 came in 0.16 over its estimate, so the net gain is 0.35. **The projection
is 22.29 against a 20-page cap.**

There is no more slack in Sections 1 to 3 that does not cost a comment. So the arithmetic hands the problem
forward: **Sections 4 to 8 have 10.2 pages, not 12.5.** That is an 18% compression on the plan, and it has
to be built in while writing rather than recovered afterwards.

Where it can come from, in the plan's own terms: *Evolution of sentiment analysis models* and *Evaluation
practices* were both listed as release valves at 0.75 pages each instead of 1.25, which is 1.0 page. The
remaining 1.3 would have to come out of *Critical discussion*, currently budgeted at 3.75. Cutting the core
*Corpus construction and annotation* section is the one option to avoid — it is the paper.

I will report the running page total with each section from here on, so this stays visible rather than
arriving as a surprise in the last week.
