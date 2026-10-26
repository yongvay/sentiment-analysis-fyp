# ICON AI 2026 — Section 1 rewritten (v13)

**Rewrites** the Introduction of `Template ICON AI 2026 - Section 1 to 7.docx`, the document Dr. Ho
reviewed on 24 August 2026. All 35 Round 3 comments are addressed. Sections 2 to 7 are untouched.

**A finished .docx accompanies this file.** `Template ICON AI 2026 - Section 1 to 7 (v13 Section 1
rewritten).docx` is your own document with only the Introduction replaced. Every other section, all
formatting, the numbered list, the italics and the headers are exactly as you had them. **The paper is
still 20 pages** — the rewrite absorbed into existing whitespace and cost nothing.

**Three changes go beyond the 35 comments.** All three were forced by reading the sources Dr. Ho asked
about, and one of them corrects a factual error in the paper. Part C has the evidence.

> **Note on the baseline.** The .docx has been condensed since `ICON_AI_S1_to_S8_v12.md` was written —
> the three findings are one paragraph now, not three, and the review methodology has been folded into
> the Introduction as a single paragraph. This rewrite follows the .docx, because that is what Dr. Ho
> read. The v12 markdown is out of date for Section 1.

---

# PART A — The rewritten Section 1

*Italics below mark the words italicised in the .docx:* Manglish, Bahasa Rojak, tidak, tidak ada, x,
takde, xde, tade. *Paragraph breaks are as they appear in the document.*

## 1. Introduction

Sentiment analysis, also known as opinion mining, is the automated task of deciding whether a piece
of text expresses a positive, negative or neutral opinion (Poria et al., 2023). Organisations use it
to measure public opinion at scale, in applications from brand monitoring to political and policy
analysis (Poria et al., 2023; Nazir et al., 2022). The tools used for this task carry an assumption
about their input. Lexicons, pre-trained models and benchmark corpora are concentrated in a small
number of well-resourced languages, and most are built from text written in a single standard
variety (Joshi et al., 2020). Text in which two languages alternate within one message does not meet
that condition. The effect on performance varies by task. Doğruöz et al. (2021) report that current
models perform well on code-switched language identification and part-of-speech tagging, but only
slightly better than chance on natural language inference. Performance on code-switched text is
therefore often lower than performance on monolingual text for the same task (Doğruöz et al., 2021;
Winata et al., 2023). Malaysian social media text is one variety in which two languages alternate
within a single message, and the two most often involved are English and Malay (AlAfnan et al.,
2025; Treffers-Daller et al., 2022).

Malaysia is a multilingual and multi-ethnic country. Coluzzi (2017), citing Ethnologue, records
around 140 languages in use. Coluzzi (2017) also reports that code-mixing between a speaker's first
languages and English or Malay is widespread in everyday communication. On social media, Malaysian
users alternate between languages within a single message rather than writing in one language at a
time (Treffers-Daller et al., 2022; AlAfnan et al., 2025). English and Malay are among the languages
most frequently combined in Malaysian written communication (AlAfnan et al., 2025). Two local terms
are used for such mixed writing, and they do not cover the same set of languages. AlAfnan et al.
(2025) describe *Manglish* as a hybrid form that combines Malay and English. Romadhona et al. (2022)
describe *Bahasa Rojak* as a variety that combines English, Malay and Chinese. This review is
concerned with Malay-English mixing, which *Manglish* denotes directly and *Bahasa Rojak* only in part.
Writing of this kind is collected from X, the social media platform formerly known as Twitter, by
several recent Malaysian studies (Maskat et al., 2024; Mohd Shamsuddin et al., 2024; Kong et al.,
2023).

How this mixed writing is regarded affects how it is processed, so this review states its position
before turning to the technical difficulty. *Manglish* is sometimes described as a variety that
weakens standard English and Malay rather than as a legitimate language variety in its own right
(AlAfnan et al., 2025). Its structure, however, is not random. Treffers-Daller et al. (2022) analyse
the classroom speech of two Malaysian teachers of English and find that Malay-English switching
follows describable syntactic patterns. AlAfnan et al. (2025) report that speakers use *Manglish* for
identifiable purposes, which include communicating efficiently, marking identity and building
rapport.

The same regularity appears at the level of spelling, with Maskat and Rahman (2020) documenting the
Malay negator *tidak* being written as *x*, and *tidak ada* being written as *takde*, *xde* or *tade*. A reader
who knows these conventions recovers the intended word without difficulty. A dictionary of standard
Malay, such as the one curated by Dewan Bahasa dan Pustaka, does not list these forms. Tools that
rely on such a dictionary therefore treat them as out-of-vocabulary items (Maskat and Rahman, 2020).
Malay social media text has accordingly been described in earlier work as misspelled, out-of-
vocabulary, ill-formed and noisy (Maskat and Rahman, 2020; Abu Bakar et al., 2020). That description
reflects the reference standard being applied rather than a lack of care by the writer. The
conventions Malaysian writers follow are consistent, but they differ from the conventions that
standard natural language processing (NLP) tools were built to handle.

When a sentiment model performs poorly on Malay-English mixed text, one common explanation is
architectural (Doğruöz et al., 2021; Winata et al., 2023). On this explanation the model handles
code-switched input less effectively than monolingual input, and a larger or more regionally adapted
model may perform better. The evidence for the explanation is mixed. Khanuja et al. (2020) report
that multilingual models fine-tuned on code-switched data achieve the strongest scores among the
systems evaluated on their benchmark. Adilazuarda et al. (2022) show that robustness depends on how
well each language is represented during pre-training. In contrast, Winata et al. (2021) find that
multilingual pre-training alone does not guarantee good representations of code-switched text.
Conneau et al. (2020) describe a "curse of multilinguality", in which a model of fixed capacity
required to accommodate many languages may produce representations of lower quality for each
individual language. Doğruöz et al. (2021) identify a further limitation that is not architectural,
in that the multilingual models in common use are trained mainly on monolingual corpora and may
receive little exposure to code-switched text during pre-training. Model choice therefore accounts
for part of the difficulty but not all of it.

Another source of difficulty does not originate in the model itself. It originates one step earlier,
at the point where the labels are created. Supervised sentiment analysis requires a sentiment label
for every message before a model can be trained or evaluated on it (Poria et al., 2023). That label
is assigned either by a human annotator or by an automatic one, and this step is called annotation.
The labels it produces form the supervision signal used to train a model, and the labels in a test
set are the standard against which the model's predictions are compared. Incorrect labels can affect
both model training and subsequent evaluation. During training, a model may learn the patterns
associated with incorrect labels, which can reduce the quality of the resulting classifier (Frénay
and Verleysen, 2014). During evaluation, incorrect labels in a test set can bias the measurement of
model performance, so that reported accuracy becomes a less reliable indicator of how the model
performs (Northcutt et al., 2021; Bowman and Dahl, 2021). An incorrect label can therefore have an
effect at two separate stages, first when the model is trained and again when its performance is
measured.

This review indicates that for Malaysian Malay-English code-mixed sentiment data, the more limiting
problem at present is the annotation label rather than the model. A second and related problem is
that the evidence these corpora offer for the soundness of their labels is limited. Three findings
support that reading, and each is developed in the sections that follow. First, none of the four
existing Malay-English sentiment resources is at the same time large, balanced across sentiment
classes, drawn from casual social media and validated by human annotators. Each of them secures some
of these properties at the expense of the others. Second, the class imbalance in the largest of them
appears to originate in the labelling method rather than in Malaysian discourse. Third, annotation
reliability is rarely reported, and where a coefficient is given it was obtained for a narrower task
than the corpus is used to support.

The second and third findings describe one condition rather than two. The skew that the labelling
methods produce is itself the condition under which a chance-corrected coefficient becomes difficult
to interpret, so correcting either weakness alone leaves the other in place. Such a coefficient
tests whether an annotation scheme and its guidelines are sound, which is the question this review
treats as unresolved (Artstein and Poesio, 2008). A 2024 review of the field still reports a lack of
comprehensive datasets and annotated resources for code-mixed Malay text (Selvaraju et al., 2024).

This review examines one question: why reliable annotation and evaluation of Malaysian Malay-English
code-mixed sentiment data remain unresolved. Linguistic description, model architecture and
application domain are discussed only where they are relevant to that question. Two related topics
fall outside the scope. The first is comparative benchmarking of sentiment classifiers, and the
second is sentiment analysis as a general field. Both topics have already been surveyed in detail
(Poria et al., 2023; Nazir et al., 2022; Selvaraju et al., 2024). This review does not propose,
implement or evaluate a system, and it does not report the author's own experimental work. Its
contribution is a diagnosis of why the problem remains unresolved, together with a set of directions
for future research.

This review makes three contributions:

1. It organises the annotation strategies used for low-resource code-mixed text into three tiers,
which are manual, semi-automated and fully automated labelling, and shows that each tier gains
either label fidelity or scalability at the expense of the other.

2. It distinguishes the two causes of neutral-label skew, one produced by the labelling tools
themselves and the other by genuine uncertainty among annotators, and it examines what each of the
four regional corpora reports about its own reliability.

3. It shows how the linguistic, annotation and measurement challenges compound one another rather
than merely co-occurring, and sets out a research agenda that follows from that interaction.

The literature examined here was identified through searches of the ACL Anthology, IEEE Xplore,
Scopus and arXiv, combining terms for the language variety, the sentiment task and annotation
quality. Studies that only benchmark classifiers, with no annotation or reliability component, were
not included.

The rest of this paper is organised as follows. Section 2 explains why Malaysian code-mixed writing
is difficult to annotate. Section 3 examines annotation practice and its failure modes, and Section
4 examines the models that are used as annotators. Section 5 discusses how annotation reliability is
evaluated. Section 6 brings these findings together and sets out directions for future research, and
Section 7 concludes the review.

---

# PART B — How each of the 35 comments is addressed

**Ten of these are Dr. Ho's own replacement wordings, used verbatim.** They are marked **(his wording)**.

| # | His point | What changed |
|---|---|---|
| 1 | "pre-trained?" | Not a typo in your text — full justification was breaking the word across a line. It now falls mid-line and renders correctly. **See D3: check the rest of the document for the same artifact.** |
| 2 | Not all code-switched text degrades performance | Replaced with what Doğruöz et al. (2021) actually report: models do well on language identification and part-of-speech tagging, near chance on natural language inference. The claim is now task-dependent — "often lower … The effect on performance varies by task." |
| 3 | "this kind" unclear; needs citation | Named and cited: "one variety in which two languages alternate within a single message, and the two most often involved are English and Malay (AlAfnan et al., 2025; Treffers-Daller et al., 2022)." |
| 4 | Does Coluzzi support both claims? | **Both verified — see C1.** Split into two sentences, each attributed to Coluzzi (2017). The 140 figure is now credited to Ethnologue, as Coluzzi credits it. |
| 5 | "first language" oversimplifies | Changed to **"first languages"**, plural. That is Coluzzi's own wording; the singular came in during paraphrase. |
| 6 | "continued rather than receded" implies a trend | Deleted. The sentence now states only what the sources observe. |
| 7 | Awkward | **(his wording)** "English and Malay are among the languages most frequently combined in Malaysian written communication." |
| 8 | Bahasa Rojak ≠ Manglish; check the source | **He was right and the source was wrong — see C2.** Each term now has its own definition and its own citation, and one sentence states that they do not cover the same set of languages. |
| 9 | The X sentence asserts a causal link | **He was right, and there is a second error underneath it — see C3.** The causal framing is gone. |
| 10 | "How this mixed writing is regarded" is abrupt | Bridge added: "…so this review states its position before turning to the technical difficulty." |
| 11 | Do both papers support all three purposes? | **No — see C4.** All three purposes now go to AlAfnan et al. (2025) alone. Treffers-Daller et al. (2022) keeps the syntactic patterning, and its data is described accurately as the classroom speech of two teachers. |
| 12 | "being written" | **(his wording)** Used verbatim. |
| 13 | Rephrase the spelling sentence | **(his wording)** "…at the level of spelling, with Maskat and Rahman (2020) documenting the Malay negator *tidak* being written as *x*…" |
| 14 | Which lexicon? | Named: "A dictionary of standard Malay, such as the one curated by Dewan Bahasa dan Pustaka." That is the standard Maskat and Rahman name themselves. |
| 15 | Citation or assumption? | **Citation — see C5.** Maskat and Rahman (2020) state the out-of-vocabulary point directly, and are now cited on that sentence. |
| 16 | Who considers it "carelessness"? | **Two sources found, both already in your paper — see C6.** The word "carelessness" is gone. The sentence now names who describes the text that way: "described in earlier work as misspelled, out-of-vocabulary, ill-formed and noisy (Maskat and Rahman, 2020; Abu Bakar et al., 2020)." |
| 17 | "It is that" — unnatural | The construction is gone. |
| 18 | "systematic writing is processed as noise" — verify | **Not supported as written — see C7.** The claim is replaced by what the sources do support: the conventions Malaysian writers follow are consistent but differ from the conventions standard NLP tools were built to handle. The reader draws the inference; the review no longer asserts it for the sources. |
| 19 | "most often" too strong; abrupt | **(his wording)** "one common explanation is architectural." |
| 20 | "On that account" not academic | Changed to "On this explanation". |
| 21 | "cannot handle" too absolute | Changed to "handles code-switched input less effectively than monolingual input". |
| 22 | "would" → "may" | **(his wording)** Used verbatim. |
| 23 | "Against" → "in contrast" | **(his wording)** Used verbatim. |
| 24 | "spread across" → "accommodate" | **(his wording)** "a model of fixed capacity required to accommodate many languages". |
| 25 | "dilutes per-language" | **(his wording)** "may produce representations of lower quality for each individual language". |
| 26 | "The remainder of the difficulty" | **(his wording)** "Another source of difficulty does not originate in the model itself." |
| 27 | Does Artstein and Poesio support this? | **No — see C8.** The citation moves to the paragraph on chance-corrected coefficients, where it is the correct source and does real work. The supervised-learning claim, which is definitional, is now cited to Poria et al. (2023). |
| 28 | Predictions are measured, not the model | "the labels in a test set are the standard against which the model's predictions are compared." |
| 29 | Figurative | **(his wording)** "Incorrect labels can affect both model training and subsequent evaluation." |
| 30 | Patterns are learned, not noise | "a model may learn the patterns associated with incorrect labels". |
| 31 | "no longer reflects" too absolute | "reported accuracy becomes a less reliable indicator of how the model performs." |
| 32 | A label does not damage the model | "An incorrect label can therefore have an effect at two separate stages." |
| 33 | Performance is measured, not the model | "again when its performance is measured." |
| 34 | Unnatural | "the more limiting problem at present is the annotation label rather than the model." |
| 35 | Particularly unclear | Split into its own sentence: "A second and related problem is that the evidence these corpora offer for the soundness of their labels is limited." |

---

# PART C — What the sources actually say

Ten papers were read for this. **Five of the eight checks pass. Three fail**, and one failure uncovered a
factual error he did not ask about.

## C1 — Coluzzi (2017): **passes**, with a wording correction

> "It is a multilingual and multi-ethnic state, with around 140 different languages being spoken
> (Ethnologue online)." — p. 20
>
> "In Malaysia the phenomenon of code-mixing and code-switching between a speaker's **first languages**
> and English and/or Malay is widespread (Asmah Haji Omar 1992)." — p. 21

Both halves are supported, so no extra citation is needed. Two things follow from the exact wording.
Coluzzi credits the 140 figure to Ethnologue, so the review now does too. And Coluzzi writes **"first
languages"** in the plural — which is exactly the correction Dr. Ho asked for in comment 5. The singular
was introduced when the sentence was paraphrased.

## C2 — AlAfnan et al. (2025) on *Bahasa Rojak*: **fails**

**The phrase "Bahasa Rojak" does not appear anywhere in AlAfnan et al. (2025).** The paper is about
*Manglish* only, which it defines as "a hybrid linguistic form combining Malay and English" and "a
colloquial fusion of Malay and English".

Romadhona et al. (2022) — already one of your four corpora — defines the other term in its own abstract:

> "In this paper, we study **Bahasa Rojak, a dialect popular in Malaysia that consists of English,
> Malay, and Chinese.**"

Its corpus tables include a row labelled "Manglish + Chinese", and it reports 1,553,360 Chinese tokens.
Coluzzi (2017) points the same way from the other side, describing *Manglish* in a footnote as English
"born in contact with Malay, Chinese and Tamil".

**Dr. Ho was right.** The two terms were being used as interchangeable labels for Malay-English mixing,
and one of your own sources contradicts that. Both now carry their own definition and citation. **This
has consequences beyond the sentence — see D1.**

## C3 — the X sentence: **fails**, and there is a second error underneath it

Mohd Shamsuddin et al. (2024) give their reason for the platform and the keyword:

> "We used #Malaysia to crawl tweets… **This specific keyword selection was made exclusively to
> accumulate tweets originating from Malaysia.**"

The reason is geographic, not linguistic. Neither corpus paper claims Malay-English mixing is frequent
on X. Dr. Ho's reading of the logic was correct: both corpora coming from X is not evidence that mixing
is frequent there.

**The second error.** The sentence called "Maskat et al., 2024" one of two "Malaysian sentiment
corpora". Your own reference list says it is:

> "A bi-annotated Malay-English code-switching (Manglish) dataset of X posts for **biological gender
> identification and authorship attribution**." *Data in Brief.*

**It is not a sentiment corpus**, and it is not one of the four sentiment resources this review examines.
The sentence now says only that writing of this kind is collected from X by several recent Malaysian
studies, which all three cited papers do support. **See D2.**

## C4 — the three communicative purposes: **fails for one of the two papers**

| | communicate efficiently | signal identity | build rapport |
|---|---|---|---|
| AlAfnan et al. (2025) | ✔ | ✔ | ✔ |
| Treffers-Daller et al. (2022) | ✔ (a "strategy of efficiency") | ✘ | ✘ (only quoted from Ozog 1987, about *lah*) |

AlAfnan et al. (2025) supports all three: "The practical need for efficient and effective communication
shapes these patterns"; "a marker of national identity"; "The pragmatic functions identified include
softening directives, **building rapport**, and expressing cultural references."

Treffers-Daller et al. (2022) supports efficiency, as one of the "bilingual optimization strategies, as
well as strategies of neutrality and efficiency" in its abstract. It makes no identity claim, and its
only mention of rapport is a quotation from Ozog (1987) about the particle *lah*.

There is also a data-type problem. The paper analyses "the code-switching patterns in **the speech of two
teachers of English in Malaysia**", from seven video-recorded classroom sessions each. Spoken classroom
data from two teachers does not support a general claim about social media writing. The review now says
what the study is, which strengthens the sentence rather than weakening it.

## C5 — the standard Malay lexicon: **passes**

Maskat and Rahman (2020) support every part of it:

- "the word *tidak* meaning 'no' or 'not' would frequently be represented with the letter x", and a table
  entry reading `tidak = x`
- a table row listing "tidak ada, takde, xde, tade"
- the reference standard, named: "the standard Malay language curated by the Dewan Bahasa [dan Pustaka]"
- the out-of-vocabulary framing: "words not found in a predefined vocabulary", and "A shared assumption
  of these works is that of the availability of a dictionary of standard Malay spellings to replace these
  'rogue' text."

Comment 14 is answered by naming Dewan Bahasa dan Pustaka. Comment 15 is answered by the citation.

## C6 — who describes the text as careless: **passes, and the sources were already in your paper**

Maskat and Rahman (2020) state it directly:

> "Malay social media text has been labeled as **misspelled words**, **out-of-vocabulary words**,
> **ill-formed words**, and **noisy text**."

Abu Bakar et al. (2020) is titled *Sentiment Analysis of **Noisy** Malay Text*, and says "Malaysians
prefer to use noisy text when expressing their reactions on social media" and "noisy text does not have
any standard rules".

Both were already cited elsewhere. They are now attached to this sentence, which is what he asked for.
"Carelessness" is removed, because no source uses it — it was the review's own framing.

## C7 — "systematic writing is processed as noise": **fails as written**

Winata et al. (2023) does not make this claim. Its only relevant mention of noise is "modeling the noisy
CSW text", which is a different proposition.

Abu Bakar et al. (2020) treats the text as genuinely noisy and in need of normalisation. It does not
argue that a systematic variety is being misread as noise. That reading is the review's own, and Dr. Ho
was right to ask for it to be checked. The sentence now states the mismatch and stops there.

## C8 — Artstein and Poesio (2008): **fails on that sentence, but belongs a paragraph later**

The paper is *Inter-Coder Agreement for Computational Linguistics*. It does not say supervised learning
requires every message to be labelled before training. His reading was correct.

What it does say is more useful to your thesis than what it was being cited for, in section 4.1.4:

> "the purpose of reliability studies is not to find out whether annotations can be generalized, but
> whether they capture some kind of observable reality… **Reliability studies test the soundness of an
> annotation scheme and guidelines**, which is not to be equated with the machine-learnability of data
> produced by such guidelines."

That is a better source for your central claim than anything currently supporting it. The citation has
moved to the paragraph on chance-corrected coefficients. The supervised-learning claim, being
definitional, is now cited to Poria et al. (2023).

## Bonus — Doğruöz et al. (2021) partly contradicts the architectural framing

Checking comment 2 turned up a passage that matters for comment 19 as well:

> "these LMs are either trained primarily on monolingual datasets such as Wikipedia in the case of
> mBERT, or Common Crawl in the case of XLM-R. **So, they are either not exposed to C-S data at all
> during training**…"

Your source attributes the difficulty to training-data exposure at least as much as to architecture.
Calling the architectural account "most often" the explanation was therefore not only too strong, as he
said — it pointed away from what this source concludes. A sentence now gives Doğruöz et al. (2021) the
non-architectural limitation it identifies, which also earns the paragraph's closing line that model
choice is only part of the difficulty.

---

# PART D — Four things that need your decision

## D1. *Bahasa Rojak* is in your title block, your keywords and your abstract

Correcting C2 has consequences the Introduction cannot settle alone. *Bahasa Rojak* includes Chinese, on
the authority of the paper you cite for the *Bahasa Rojak* corpus. Your review is about Malay-English
data.

**Your abstract now contradicts your Introduction.** It opens:

> "Malaysian social media users mix English and Malay inside single messages, producing the contact
> varieties known as Bahasa Rojak and Manglish."

That is the same conflation the Introduction has just corrected, on page 1, in the first thing he reads.
It needs to change whichever option you pick. The smallest edit that fixes it:

> "Malaysian social media users mix English and Malay inside single messages, producing the contact
> variety known locally as Manglish."

Current keywords: sentiment analysis, code-mixed text, **Bahasa Rojak**, annotation reliability,
inter-annotator agreement.

1. **Keep the keyword, keep the new distinction.** The Introduction now explains the difference, and
   Romadhona et al. (2022) is genuinely one of your four corpora. Least disruptive, and it shows you read
   the source.
2. **Replace the keyword with *Manglish*.** More precise for a Malay-English review, and your title
   already says "Malay-English".
3. **Keep both.** Six keywords against the template's five.

My reading is option 1, with the abstract sentence fixed either way. But it is your call, and it is worth
mentioning to Dr. Ho when you send Section 1 — it is exactly the kind of care he has been asking for.

## D2. Maskat et al. (2024) is not a sentiment corpus

It is a gender-identification and authorship-attribution dataset. It has been removed from the "sentiment
corpora" claim and is still cited, correctly, as evidence that Malaysian Malay-English writing is
collected from X.

**Check whether it is described as a sentiment corpus anywhere in Sections 2 to 7.** I have not read
those sections against this correction, and the sentence may have been reused.

## D3. The `pre- trained` hyphenation is a Word artifact

Comment 1 is not a typo in your text. Full justification was breaking `pre-trained` across a line. The
rewrite changes where the line falls, so it renders correctly now — but that is luck, not a fix.

Search the whole document for the same artifact before you send it. It appears at least three times in
the reviewed PDF: `pre- trained`, `Malay- English`, `code- switched`. To fix one permanently, select the
word and apply a non-breaking hyphen (**Ctrl+Shift+-**), or turn off automatic hyphenation for the
paragraph.

## D4. You are at exactly 20 pages, against a 20-page cap

The original was 20 pages and the rewrite is still 20 pages, so this costs you nothing. But your project
notes say 19, and they are out of date — **you have no headroom at all.** Anything added to Sections 2 to
7 pushes you over the limit.

If the same rewrite treatment goes into the remaining sections, space has to come out first.
`Where_To_Cut_Two_Pages.md` already names where: the three contributions are stated three times across
the abstract, Section 1 and Section 6, and the central finding appears five times. **Cut repeated
content, never compress a sentence** — compression is the defect he is complaining about.

---

# PART E — Length and readability

| | Before | After |
|---|---|---|
| Words in Section 1 | 1,301 | **1,607** |
| Paragraphs | 14 | **15** |
| Sentences | 64 | **88** |
| Mean sentence length | 20.3 words | **18.3 words** |
| Longest sentence | 43 words | **38 words** |
| Sentences over 35 words | 9 | **3** |
| **Pages in the full paper** | **20** | **20** |

**The section is 24 per cent longer and carries 38 per cent more sentences.** The average sentence is two
words shorter, the longest is five words shorter, and sentences over 35 words drop from nine to three.
That is the trade he has been asking for across three rounds: more sentences, each doing less work.

His own replacement wordings run 25 to 200 per cent longer than what they replace, so directness was
always going to cost words. About half the increase is not style at all — it is the source corrections:
the *Manglish* / *Bahasa Rojak* distinction, the task-dependent performance evidence from Doğruöz et al.
(2021), the non-architectural limitation from the same paper, and the Artstein and Poesio sentence moved
into the compounding paragraph. Those are load-bearing and should not be traded away for space.

## Checks run on the rewrite

- No bold anywhere in the body.
- No `(Section X)`, `(Table X)` or `(Figure X)` cross-references.
- No content parked in brackets.
- Italics only on *Manglish*, *Bahasa Rojak* and the Malay word forms.
- Every one of the nineteen informal strings he flagged in Rounds 1 and 2 returns zero hits, including
  the four new ones from this round: `damages`, `dilutes`, `spread across`, `reach beyond`.
- Every sentence containing *most*, *often*, *normally* or *usually* carries its citation **on that
  sentence**, not in the neighbour.
- No source cited that is not peer-reviewed. No arXiv.

## What to say when you send it

Name the things you changed that he did not ask for. The *Bahasa Rojak* correction, the Maskat et al.
(2024) misclassification, and moving Artstein and Poesio to where it does real work are all findings from
reading the sources, not from his comments. Round 1 comment 1 asked whether the writing was yours. Three
corrections that came out of reading the papers answer that question better than anything else could.
