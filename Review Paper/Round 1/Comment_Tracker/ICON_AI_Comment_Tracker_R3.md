# Dr. Ho — Round 3 comment tracker

**Document reviewed:** `Template ICON AI 2026 - Section 1 to 7 (reviewed).pdf` (19 pages)
**Comments:** **35**, extracted from the PDF annotation layer, not retyped
**Pages annotated:** 1, 2 and 3 only — **all 35 are in Section 1, the Introduction**
**Date received:** 24 August 2026

He has stopped at page 3 of 19. Sections 2 to 7 have not been read this round.

---

# Part 0 — The covering email

> "I have reread your Introduction section but not finished yet. This round, it takes me **1 hour plus**
> to read and comment on it. I don't think the ideas are complicated. In fact, the introduction presents
> a **well-motivated and potentially valuable research problem**. But the same thing happens again, the
> language used for writing is **often more sophisticated than necessary**, which can potentially make
> the readers work very hard to extract those ideas.
>
> My only worry here is that, even if I can really read the whole paper, give you some comments for
> enhancement, and you did it but the contents are still written in the same style, there is a
> possibility that **reviewers may simply reject it for this reason**, or even if they can read it and
> understand it, based on my experience, most likely they will **recommend a substantial readability
> revision** before publication.
>
> In short, **don't do the writing in such a way that requires substantial inferential effort, but make
> everything stated more directly.**"

Two things in that paragraph are new and both matter.

**He separated the ideas from the writing, and praised the ideas.** "Well-motivated and potentially
valuable research problem" is the first unqualified positive statement across three rounds. The argument
is no longer in question. Only the prose is.

**He named a consequence.** Rounds 1 and 2 said the writing was hard to read. Round 3 says it may get the
paper rejected on that ground alone, or sent back for a substantial readability revision. That converts a
style preference into a submission risk.

---

# Part 1 — What changed between rounds

| | R1 | R2 | **R3** |
|---|---|---|---|
| Comments | 80 | 64 | **35** |
| Pages he reached | 4 of 26 | 5 of 7 | **3 of 19** |
| Formatting / cross-references | 33 | 0 | **0** |
| Missing citations | 14 | 11 | **8, all now "does your source actually say this?"** |
| Register | 4 | 19 | **7** |
| Overclaiming | 3 | 4 | **6** |
| Figurative language for technical relations | 0 | 0 | **4** |
| Imprecise technical relationships | 0 | 2 | **3** |

The count halved again, but read the bottom four rows. Two categories that did not exist in Round 1 —
figurative language and imprecise technical relationships — now account for 7 comments between them, and
overclaiming has gone up in absolute terms while everything else fell.

**The easy defects are gone. What is left is the voice.** Rounds 1 and 2 removed bold text, parenthetical
cross-references, bracketed content and conversational vocabulary. None of those came back. What Round 3
flags is not a list of bad words. It is a habit of sentence construction, and that is why he wrote a
covering email this time instead of relying on the annotations.

---

# Part 2 — The most useful thing in this round

**In 10 of the 35 comments he wrote the replacement wording himself.** That is 29 per cent. He has never
done this at anything like this rate before. Those 10 sentences are a specification of the register he
wants, written in his own hand.

| # | Your wording | His replacement |
|---|---|---|
| 7 | English and Malay are **the pair that combines most frequently** in Malaysian writing | English and Malay are **among the languages most frequently combined** in Malaysian written communication |
| 12 | the negator *tidak* **written** as x | the negator *tidak* **being written** as x |
| 13 | The same regularity holds at the level of spelling**:** Maskat and Rahman (2020) **record** the negator *tidak* | …at the level of spelling**, with** Maskat and Rahman (2020) **documenting** the Malay negator *tidak* being written as… |
| 19 | the explanation offered is **most often** architectural | **one common explanation** is architectural |
| 22 | a larger or more regionally adapted model **would** perform better | …**may** perform better |
| 23 | **Against** that, Winata et al. (2021) find… | **In contrast**, Winata et al. (2021) find… |
| 24 | finite model capacity, **spread across** many languages | finite model capacity, required to **accommodate** many languages |
| 25 | **dilutes per-language quality** | **potentially reducing the quality of representations for individual languages** |
| 26 | **The remainder of the difficulty** does not originate in the model | **Another source of difficulty** does not originate in the model **itself** |
| 29 | The consequences of incorrect labels **reach beyond the dataset** | **Incorrect labels can affect both model training and subsequent evaluation.** |

Read the right-hand column as a set. Three things are true of every single one of them.

**1. He adds a hedge.** *among*, *may*, *can*, *potentially*, *one common*. Not one of his replacements
states anything as flatly certain.

**2. He removes the metaphor and names the mechanism.** *Spread across* becomes *accommodate*. *Dilutes*
becomes *reducing the quality of representations*. *Reach beyond the dataset* becomes *affect both model
training and subsequent evaluation*. In every case a physical image is replaced by the literal technical
relationship it was standing in for.

**3. His versions are longer than yours.**

| | Your words | His words |
|---|---|---|
| #25 | 3 | 10 |
| #29 | 7 | 10 |
| #26 | 8 | 10 |
| #7 | 9 | 11 |
| #13 | 13 | 17 |

**This is the finding that should change how the rewrite is approached.** The Introduction has been
compressed hard — partly for the page budget, partly because compressed prose reads as sophisticated. Dr.
Ho is telling you, ten times over and without ever saying it directly, that he would rather read ten flat
words than four clever ones. Brevity is not what he is asking for. Directness is, and directness costs
words.

---

# Part 3 — The 35 comments, in document order

Highlighted text is reconstructed from the PDF annotation geometry, so on two-column reflow it sometimes
picks up part of the line beneath. Comment text is verbatim.

## Page 1 — 3 comments

| # | Highlighted | Dr. Ho's comment | Type |
|---|---|---|---|
| 1 | lexicons, **pre- trained** models | "pre-trained?" | Mechanics |
| 2 | **a persistent source of degraded performance** | "Clarity can be enhanced. By the way, one possible concern is that not all code-switched text necessarily causes degraded performance in every NLP system, especially models specifically trained for multilingual or code-switched data." | Overclaim |
| 3 | Malaysian social media text is **writing of exactly this kind** | "This part lacks clarity. In academic writing, clarity is important. Thus, in this case, what 'this kind' means should be stated clearly. Suppose you are referring to the idea of 'Malaysian social media text frequently exhibits code-switching, with users often alternating between languages within a single message', then one or two citations are needed, even though you are a Malaysian and you know that this is likely to be true but not all readers are Malaysian." | Referent + citation |

## Page 2 — 27 comments

| # | Highlighted | Dr. Ho's comment | Type |
|---|---|---|---|
| 4 | **Coluzzi (2017)** | "Does the citation to Coluzzi (2017) support approximately 140 languages in Malaysia only or including widespread code-mixing involving first languages, English, and Malay? If the second one is not supported, then a separate citation is needed." | **Citation check** |
| 5 | code-mixing between **a speaker's first language**, English and Malay | "Malaysia has many linguistic communities, therefore, in the case of Malaysia, individuals may be bilingual or multilingual from childhood. The use of 'first language' may oversimplify this linguistic situation." | Factual precision |
| 6 | The practice has **continued rather than** receded | "This implies a historical trend. Unless the cited studies explicitly examine this temporal development, this wording may be stronger than the evidence supports. Consider using a simpler and more defensible style." | Overclaim |
| 7 | **English and Malay are the pair that combines most frequently in Malaysian writing** | "The way it is written sounds a little awkward, perhaps express it like this 'English and Malay are among the languages most frequently combined in Malaysian written communication…'" | Register — **wording supplied** |
| 8 | **the mixed varieties they produce** are known locally as Bahasa Rojak and Manglish | "Bahasa Rojak and Manglish are not necessarily interchangeable labels for all Malay-English mixed writing. They could be the mix of more languages. Please double check the cited source again." | **Citation check** |
| 9 | **Malay-English mixed writing is frequent enough on X … that both of the Malaysian sentiment corpora examined in this review were collected from it** | "This sentence suggests a causal relationship where Malay-English mixing is frequent on X and therefore researchers collected both corpora from X. But the fact that both datasets were collected from X does not itself demonstrate that Malay-English mixed writing is frequent there. The researchers may have selected X for other reasons. Please double check on this and make sure the citation is used properly." | **Citation check** + logic |
| 10 | **How this mixed writing is regarded** matters for how it is processed | "How it is regarded introduces a new idea, which social or linguistic perception, which feels a little abrupt." | Bridge |
| 11 | **Treffers-Daller et al. (2022) and AlAfnan et al. (2025) show** that Malay-English switching follows describable syntactic and pragmatic patterns, and that speakers use it deliberately to communicate efficiently, signal identity and build rapport | "Do both papers support all three communicative purposes including communicate efficiently, signal identity, and build rapport?" | **Citation check** |
| 12 | the negator *tidak* **written** as x | "being written" | Grammar — **wording supplied** |
| 13 | at the level of **spelling: Maskat and Rahman (2020) record** the negator *tidak* | "'…spelling, with Maskat and Rahman (2020) documenting the Malay negator *tidak* being written as..'" | Register — **wording supplied** |
| 14 | but **a lexicon** compiled from standard Malay | "Which lexicon are you referring to?" | Referent |
| 15 | **but a lexicon compiled from standard Malay lists none of those forms.** | "Citation or assumption?" | **Citation check** |
| 16 | (NLP) is therefore not **carelessness** | "If any previous work explicitly characterizes code-mixed social media writing as noisy, erroneous or non-standard, then you should cite it here. Otherwise, readers may wonder who considers it 'carelessness'?" | **Citation check** |
| 17 | **It is that** the conventions Malaysian writers follow | "The opening of this sentence does not sound natural or smooth continuation from the previous sentence." | Register |
| 18 | so **writing that is systematic is processed as noise** | "This is a strong claim. You should verify that both citations genuinely support this interpretation." | **Citation check** + overclaim |
| 19 | the **explanation offered is most often architectural** | "This feels slightly abrupt because you have not explicitly framed architecture as an alternative explanation to the resource/input problem. 'Most often' sounds very strong. Perhaps you should be using 'one common explanation'?" | Overclaim + bridge — **wording supplied** |
| 20 | **On that account** the model cannot handle | "This is not so academic writing." | Register |
| 21 | the model **cannot handle** code-switched input | "This feels absolute because a model may not completely 'fail' to handle code-switched input, it may perform less effectively or struggle to process it." | Overclaim |
| 22 | a larger or more regionally adapted model **would** perform better | "Use 'may'?" | Overclaim — **wording supplied** |
| 23 | **Against** that, Winata et al. (2021) find | "Use 'in contrast' will sound better." | Register — **wording supplied** |
| 24 | finite model capacity, **spread across** many languages | "Capacity cannot spread across language, use 'accommodate'" | Figurative — **wording supplied** |
| 25 | **dilutes per-language** quality | "This sounds less academic, use 'potentially reducing the quality of representations for individual languages'." | Figurative — **wording supplied** |
| 26 | **The remainder of the difficulty does not originate in the** model | "This may sound better and slightly more academic 'another source of difficulty does not originate in the model itself.'" | Register — **wording supplied** |
| 27 | **Supervised sentiment analysis requires that every message be read and assigned a sentiment label … before any model can be trained or evaluated on it (Artstein and Poesio, 2008).** | "Artstein and Poesio (2008) is primarily about annotation and agreement methodology. So, please verify whether it directly supports the broader claim about supervised sentiment analysis requiring every message to be read and labelled before training/evaluation." | **Citation check** |
| 28 | the supervision signal **a model learns from and is measured** against | "This could be interpreted slightly awkwardly because the model's predictions are measured against the labels, rather than the model itself." | Technical precision |
| 29 | The consequences of incorrect labels **reach beyond the** dataset | "This is somewhat figurative. Make it more direct academic version like this 'Incorrect labels can affect both model training and subsequent evaluation.'" | Figurative — **wording supplied** |
| 30 | **Label noise is learned during training** | "Technically it is the patterns associated with noisy labels that can be learned by the model." | Technical precision |

## Page 3 — 5 comments

| # | Highlighted | Dr. Ho's comment | Type |
|---|---|---|---|
| 31 | **so that reported accuracy no longer reflects how the model actually behaves** | "This is too absolute. Even with some incorrect labels, accuracy can still provide information about performance, it is simply biased or less reliable." | Overclaim |
| 32 | **An unsound label therefore damages the model** twice | "This is technically imprecise because a label does not necessarily 'damage the model' itself. But it can affect the model during training, and affect the measurement of the model during evaluation." | Figurative + precision |
| 33 | once when it is trained and again **when it is** measured | "This could imply that the model is being physically measured. In fact, it is its performance being measured." | Technical precision |
| 34 | **the annotation label is at present the more limiting** problem | "This might be grammatically understandable but definitely unnatural." | Register |
| 35 | **together with the evidence offered that the label is sound.** | "This is particularly unclear. It sounds as though the annotation label is a problem together with evidence that it is sound" | Clarity |

---

# Part 4 — The 35 grouped by cause

| Cause | Count | Comments |
|---|---|---|
| **Does your source actually support this?** | **8** | 4, 8, 9, 11, 15, 16, 18, 27 |
| **Register — awkward or not academic** | **7** | 7, 13, 17, 20, 23, 26, 34 |
| **Overclaiming — stated too absolutely** | **6** | 2, 6, 19, 21, 22, 31 |
| **Figurative language for a technical relation** | **4** | 24, 25, 29, 32 |
| **Technical relationship stated imprecisely** | **3** | 28, 30, 33 |
| **Unanchored referent** | **2** | 3, 14 |
| **Mechanics and grammar** | **2** | 1, 12 |
| **Factual oversimplification** | **1** | 5 |
| **Abrupt topic shift** | **1** | 10 |
| **Sentence not interpretable** | **1** | 35 |
| | **35** | |

## The three habits behind 13 of them

Groups 3, 4 and 5 — overclaiming, figurative language and imprecise relationships — are 13 comments and
they are the same underlying move made three different ways: **a compressed sentence that asks the reader
to reconstruct what was meant.**

**Habit one — the physical metaphor for an abstract relation.** Capacity *spread across* languages. Quality
*diluted*. Consequences that *reach beyond* the dataset. A label that *damages* the model. A model that is
*measured*. Each one is a picture the reader has to translate back into a technical statement before they
can check whether it is true. He flagged six.

**Habit two — one sentence carrying two or three propositions.** The clearest case is #32: *"An unsound
label therefore damages the model twice, once when it is trained and again when it is measured."* That
sentence is doing four jobs at once, and he needed three separate comments (32, 33, and 29 upstream) to
unpick it. Same with #35: *"the annotation label is at present the more limiting problem, together with the
evidence offered that the label is sound"* — two different things joined by *together with*, and he could
not tell whether both were being called problems. His verdict: "particularly unclear."

**Habit three — the unhedged absolute.** *Cannot handle. No longer reflects. Is processed as noise. Most
often. Would perform better.* Six comments, all saying the same thing: the claim is stronger than the
evidence, and a reviewer will notice.

---

# Part 5 — The 8 citation checks, for you to verify

These are the ones he asked you to go back to the source on. For each: what the sentence currently claims,
and what the source must contain for the sentence to stand as written.

### C1 — Coluzzi (2017) — comment 4

**Sentence:** "Malaysia is a multilingual and multi-ethnic country in which Coluzzi (2017) recorded around
140 languages in use, with code-mixing between a speaker's first language, English and Malay already
widespread in everyday communication."

**Check:** does Coluzzi (2017) support **both** halves, or only the 140-languages figure?

- [ ] Coluzzi (2017) gives the ~140 figure — almost certainly yes
- [ ] Coluzzi (2017) **also** states that code-mixing between first language, English and Malay is
      widespread in everyday communication

If the second box is empty, that half needs its own citation. Note that comment 5 hits the same sentence
from another angle: "first language" oversimplifies a country where many people are multilingual from
childhood, so this sentence likely needs rewriting regardless of what the source says.

### C2 — AlAfnan et al. (2025) on Bahasa Rojak and Manglish — comment 8

**Sentence:** "English and Malay are the pair that combines most frequently in Malaysian writing, and the
mixed varieties they produce are known locally as Bahasa Rojak and Manglish (AlAfnan et al., 2025)."

**Check:** does AlAfnan et al. (2025) actually equate the two terms with **Malay-English** mixing
specifically?

- [ ] The source defines Bahasa Rojak
- [ ] The source defines Manglish
- [ ] The source treats both as covering Malay-English mixing **only**, not mixing that also involves
      Chinese dialects, Tamil or others

His point is that Bahasa Rojak in particular is usually described as involving more than two languages. If
the source is broader than your sentence, the sentence has to narrow. This matters more than it looks —
Bahasa Rojak is in your title and your keywords.

### C3 — the X / Twitter sentence — comment 9

**Sentence:** "Malay-English mixed writing is frequent enough on X, the platform formerly known as Twitter,
that both of the Malaysian sentiment corpora examined in this review were collected from it (Maskat et al.,
2024; Mohd Shamsuddin et al., 2024)."

**Check:** this is a logical problem more than a sourcing one. The sentence uses *"both corpora came from
X"* as evidence for *"mixing is frequent on X"*. It is not evidence for it — the researchers may have
chosen X for API access, cost, or convention.

- [ ] Does either paper state that Malay-English mixing is frequent on X?
- [ ] Does either paper give a reason for choosing X?

If neither states the frequency claim, the honest sentence is the plain one: both corpora were collected
from X. Drop the causal framing.

### C4 — the three communicative purposes — comment 11

**Sentence:** "Treffers-Daller et al. (2022) and AlAfnan et al. (2025) show that Malay-English switching
follows describable syntactic and pragmatic patterns, and that speakers use it deliberately to communicate
efficiently, signal identity and build rapport."

**Check:** he is asking whether **both** papers support **all three** purposes. Fill this in:

| | communicate efficiently | signal identity | build rapport |
|---|---|---|---|
| Treffers-Daller et al. (2022) | ☐ | ☐ | ☐ |
| AlAfnan et al. (2025) | ☐ | ☐ | ☐ |

Note that Treffers-Daller et al. (2022) is a study of **spoken** data from two teachers — the pre-submission
check already flagged that. A spoken classroom corpus is unlikely to support all three claims about social
media writing. Split the citation so each paper is credited only with what it found.

### C5 — the standard Malay lexicon — comment 15

**Sentence:** "A reader who knows the convention recovers the word without effort, but a lexicon compiled
from standard Malay lists none of those forms."

**Check:** he asks straight out, "Citation or assumption?" Two separate problems here:

- [ ] Is there a source for a standard Malay lexicon not containing *x*, *takde*, *xde*, *tade*?
- [ ] **Which lexicon?** (comment 14) — the sentence says "a lexicon" with no antecedent

If you have no source, the defensible version drops the lexicon and describes the coverage problem
generally, or cites out-of-vocabulary behaviour in Malay NLP from work you already have in Section 4.2.

### C6 — who calls it carelessness? — comment 16

**Sentence:** "The difficulty that Malay-English mixed writing creates for natural language processing
(NLP) is therefore not carelessness."

**Check:** the sentence rebuts a position nobody in the paper has been shown to hold.

- [ ] Find a source that explicitly characterises code-mixed social media text as noisy, erroneous or
      non-standard

Winata et al. (2023) or Doğruöz et al. (2021) may well do this — they are already in your list. If one
does, cite it on this sentence and the rebuttal has something to push against. If none does, cut the
sentence: you cannot rebut a claim you cannot attribute.

### C7 — "systematic writing is processed as noise" — comment 18

**Sentence:** "…so writing that is systematic is processed as noise (Winata et al., 2023; Abu Bakar et al.,
2020)."

**Check:** he wants both citations verified against this specific interpretation.

- [ ] Winata et al. (2023) supports it
- [ ] Abu Bakar et al. (2020) supports it

This is also an overclaim (see #21, #31 — same pattern). Even if both sources support the direction of the
claim, "is processed as noise" is absolute where the sources are likely to be qualified.

### C8 — Artstein and Poesio (2008) — comment 27

**Sentence:** "Supervised sentiment analysis requires that every message be read and assigned a sentiment
label, by a human annotator or by an automatic one, before any model can be trained or evaluated on it
(Artstein and Poesio, 2008)."

**Check:** Artstein and Poesio (2008) is *Inter-Coder Agreement for Computational Linguistics* — an
agreement-methodology paper. It is the right source for what agreement coefficients mean. It is the wrong
source for a claim about the requirements of supervised learning.

- [ ] Does it state that supervised models require labelled data before training or evaluation?

Almost certainly not in those terms. This is the weakest of the eight. The claim itself is uncontroversial
and any supervised-learning or annotation reference covers it — keep Artstein and Poesio for the agreement
discussion, where it genuinely belongs, and support this sentence from somewhere else or leave it
uncited as a definitional statement.

## Why these eight matter more than the other 27

The other 27 are style. A reviewer who dislikes your style recommends revision. **A reviewer who checks one
citation and finds it does not support the sentence stops trusting the other 40.** These eight are the only
comments in the round that can damage the paper's credibility rather than its readability, and three of
them — C2, C3 and C8 — look likely to fail the check on the evidence available.

---

# Part 6 — What this means for the rewrite

## The page budget problem

| | |
|---|---|
| Hard cap | **20 pages** (confirmed with the author, 15 Aug) |
| Current | **19 pages** |
| Headroom | **~1 page** |

Dr. Ho's own replacement wordings run 25 to 200 per cent longer than what they replace. Applying his
register to the whole Introduction will add words, not remove them. The Introduction currently runs about
1,050 words over roughly 2.5 pages; converting every compressed sentence at his ratio adds perhaps 120 to
180 words, which is a third to a half of a page.

**That fits inside the headroom, but only just, and only if nothing else grows.** If the same treatment is
later applied to Sections 2 to 7 there is no headroom at all, and the space has to come from cutting whole
sentences rather than tightening existing ones. `Where_To_Cut_Two_Pages.md` and the two cut plans in the
project already identify where: the three contributions are stated three times, and the central finding
appears five times.

The rule that follows: **pay for directness by deleting repeated content, never by compressing a
sentence.** Compression is the defect he is complaining about.

## The reference count

Still open from R1 comment 80: he asked for at least 40, and the paper has 37. Three of the eight citation
checks above (C5, C6, C8) may require a source the paper does not currently have. Those additions would
count toward the 40 and would be doing real work rather than padding — which is the best kind of reference
to add.

## What he has not seen

Sections 2 to 7 have never been read at this level of detail. The habits flagged here — metaphor for
technical relations, compressed multi-proposition sentences, unhedged absolutes — were not introduced in
the Introduction. They are how the whole paper is written. Whatever is decided for Section 1 will have to
be applied to roughly 8,400 more words.
