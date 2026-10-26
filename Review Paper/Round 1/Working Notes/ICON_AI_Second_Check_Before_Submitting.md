# Second check — Sections 1 to 8, revised version

**Checked:** the revised `Template ICON AI 2026 - Section 1 to 8.pdf` (22 pages, 9,443 words, 37 references)
against the 47 fixes in the first check and against all 144 comments in the Master Comment Tracker.
**Date:** 20 August 2026

---

## Where you stand

**36 of the 47 fixes are done correctly.** The abstract's four flagged phrases are gone. All the
ampersands are now "and". "This review argues" is now "indicates". The three absolute claims about the
literature are now grounded in your own Section 2 search. Every long sentence on pages 2 and 3 is
split. Table 3 reads "positive or negative". All four captions are title case, and Table 1 and Table 3
now fit on one page each.

**But do not send it yet.** The editing pass introduced **8 new errors**, and 3 of them are broken
sentences that read worse than what they replaced. Six of the original fixes were not done.

The 8 new errors all come from one habit, so it is worth naming: **the new wording was pasted into the
middle of an existing sentence instead of being given a sentence of its own.** Every definition you
inserted broke the sentence it was inserted into. The rule to use instead: *add a new full stop, then
the new sentence.*

---

# PART 1 — New errors. Fix these first.

## N1. The abstract now says the same thing twice — **most urgent**

Sentences 2 and 3 of the abstract:

> "Sentiment analysis of this text is usually treated as a modelling problem. **The studies reviewed
> here usually treat sentiment analysis of this text as a modelling problem.**"

The new sentence was added but the old one was not deleted. **Delete the first sentence.** Keep the
second.

This is the first paragraph Dr. Ho reads. A repeated sentence there is more damaging than the phrase
it was meant to replace.

## N2. Page 10 — the Marathi definition broke the sentence

Current:

> "Jadhav et al. (2025) evaluated generative annotators on Marathi, an Indo-Aryan language of western
> India, **is morphologically rich where Malay is not** across four tasks: sentiment analysis, …"

The clause "is morphologically rich where Malay is not" was pulled forward into this sentence, but it
was also left in place four sentences later. So it appears twice, and here it has no subject.

**Replace the sentence with:**

> "Jadhav et al. (2025) evaluated generative annotators on Marathi, an Indo-Aryan language of western
> India, across four tasks: sentiment analysis, two-class hate speech detection, four-class hate
> speech detection, and news classification."

Leave the later sentence ("Marathi is morphologically rich where Malay is not, so the result bounds
the tier's promise…") exactly as it is. It is doing real work there.

## N3. Page 10 — "a a", and the BERT definition broke the next sentence

Current:

> "They found two generative large language models, GPT-4o and Llama 3.1 405B trailing **a a**
> fine-tuned BERT baseline, where BERT is a bidirectional transformer encoder pre-trained on
> unlabelled text **by average accuracy margins of 10.2% and 14.1% respectively.**"

Two problems. "a a" is a typo. And the definition sits between "trailing a … baseline" and "by average
accuracy margins", so the reader loses the thread of the main clause.

**Replace with two sentences:**

> "They found two generative large language models, GPT-4o and Llama 3.1 405B, trailing a fine-tuned
> BERT baseline by average accuracy margins of 10.2% and 14.1% respectively. BERT is a bidirectional
> transformer encoder pre-trained on unlabelled text."

## N4. Page 14 — the XLM-RoBERTa sentence is now 69 words

This is the longest sentence in the paper. Dr. Ho flagged a **47-word** one in Round 2 as *"long and
relatively difficult to digest."* Two definitions were inserted into one sentence and it has doubled
in length. It also now reads as though the model "predicts words hidden from the input **over**
original, fully transliterated and partially transliterated versions" — which is not what happened.

Current:

> "They fine-tuned XLMRoBERTa, a multilingual encoder model, using masked language modelling, a
> training method in which the model predicts words hidden from the input over original, fully
> transliterated and partially transliterated versions of the same text, and report a macro F1 of
> 0.90, where macro F1 is the mean of the per-class F1 scores and F1 is the harmonic mean of precision
> and recall on the shared-task test set."

**Replace with three sentences:**

> "They fine-tuned XLM-RoBERTa, a multilingual encoder model, over original, fully transliterated and
> partially transliterated versions of the same text, and report a macro F1 of 0.90 on the shared-task
> test set. The training method was masked language modelling, in which the model predicts words
> hidden from the input. Macro F1 is the mean of the per-class F1 scores, and F1 is the harmonic mean
> of precision and recall."

25 words, 17 words, 20 words. All three are readable on one pass.

## N5. Page 11 — subject–verb agreement

> "Its score therefore **remain** within the neutral band…"

**Change to:** "Its score therefore **remains** within the neutral band…"

## N6. Page 18 — "the shared limitation spot"

> "The fourth link runs from the shared **limitation spot** to extreme class skew."

"blind" was replaced with "limitation" and "spot" was left behind.

**Change to:** "The fourth link runs from the shared limitation to extreme class skew."

## N7. Page 9 — half of the "break" fix was applied

Three sentences apart, on the same page:

> "The two types of annotator therefore do not **fail** on the same inputs, and they do not **fail** at
> the same rate." ✔ fixed
>
> "Because they **break** on different inputs, the choice determines which errors a corpus will
> contain…" ✘ not fixed

**Change the second to:** "Because they fail on different inputs, the choice determines…"

## N8. Page 13 — "cases … cases"

> "That description fits the heavily code-switched and particle-laden **cases** Section 3 identified as
> the most difficult **cases** in the problem."

My suggested wording was clumsy — this one is my fault. **Use instead:**

> "That description fits the heavily code-switched and particle-laden cases Section 3 identified as the
> hardest to annotate."

---

# PART 2 — Six fixes that were not done

## O1. Figure 1 still says "Share Blind Spot" — page 17

This is now worse than before the edit. The body text on pages 17 and 18 says "a shared **limitation**"
and "The **limitations** of one generation", but the figure box still says "**Share** Blind Spot" —
which is also a typo for "Shared".

The figure and the text must use the same words. **Change the box label to "Shared Limitation".**

While you are in the figure, the box "Reliability Hard To Establish" would read better as
"Reliability Hard to Establish" (lower-case "to"), to match the other boxes.

## O2. "transformer" and "encoder" are still undefined — pages 13 and 14

You defined BERT, macro F1, XLM-RoBERTa, masked language modelling and Marathi. These two were missed,
and they carry the argument of Section 5.

- **Page 13**, first use of *transformer*: "…is pysentimiento, which is the transformer-based tool of
  the three." Add one clause: "…which is the transformer-based tool of the three, built on the neural
  architecture that underlies most current language models."
- **Page 14**, first use of *encoder*: "Fine-tuned multilingual encoders acquire their competence from
  exposure." Add a second sentence: "An encoder here is a model that reads text and produces
  representations of it, rather than generating new text."

Give each its own sentence or its own clause after a comma. Do not paste them into the middle — that
is what caused N2, N3 and N4.

## O3. Section 5 still does not say there are two families — page 14

The opener says "This section asks where each family of model is limited when used as an annotator",
and the reader has to get two pages in to discover there are two. R2 comment 56 is the exact complaint,
about the three properties in Section 3.

**Add one sentence after "…is limited when used as an annotator":**

> "Two families are examined: fine-tuned multilingual encoders, and generative models used directly as
> annotators."

## O4. The three tiers are still not named up front — page 9

> "On that reading, the strategies fall into three tiers. The first tier is manual annotation by
> people."

**Change to:**

> "On that reading, the strategies fall into three tiers: manual annotation, semi-automated annotation,
> and fully automated generative annotation. The first tier is manual annotation by people."

Six extra words, and it removes the same complaint he made about Section 3.

## O5. Tay et al. (2016) is still cited with no reference entry — page 7

> "Treffers-Daller et al. (2022), citing Tay et al. (2016), describe the effect more precisely: *lah*
> shifts an utterance…"

Every other name in the paper has an entry in the reference list. This one does not.

**Simplest fix — remove the secondary citation:**

> "Treffers-Daller et al. (2022) describe the effect more precisely: *lah* shifts an utterance from a
> highly assertive tone to a polite request or a friendly encouragement."

You have read Treffers-Daller et al. (2022). You have not read Tay et al. (2016). R1 comment 3 was
exactly about not extending a source beyond what you can check yourself.

## O6. The title block is still template placeholder text — page 1

The first page still shows "Author(s) Name(s)", "*Author Affiliation(s)*", "*E-mail*", and at the
bottom "* Corresponding author. **masaini@abc.xxx.xxx**".

Fill in:

- **Author:** Ng Yong Vay
- **Affiliation:** your faculty and university
- **E-mail** and **corresponding author line:** yongvay@gmail.com

Leave the four "xx xxx 2023" dates under "Article history" — the journal fills those in.

He will see this before he reads a single sentence.

---

# PART 3 — Still open, but not blocking

**Reference count is still 37.** He asked for at least 40. His own instruction of 11 August was to
expand the list *after* revision, so this is correctly last — but it is the one number he will check,
and you are three short. The three places from the first check where a source would do real work rather
than pad are still open: annotator aggregation (Section 4.3), lexicon coverage and out-of-vocabulary
behaviour (Section 4.2), and a second study on fine-tuned multilingual encoders for code-mixed text
(Section 5).

**Two sentences are still over 40 words**, and both are fine as they are:

- Page 5, 37 words on the date filter — under the limit, no action.
- Page 19, 53 words listing the five reporting elements — it is a numbered list, so it reads easily.

**Optional, from the first check.** You did not add the sentence noting that Romadhona et al.'s
κ = 0.77 covers only the stock review subset, and that the product and movie subsets were produced by
data augmentation and carry no agreement figure. Table 3 now says "reported for the stock review subset
only", so the point is made. Adding the sentence below the table would strengthen it, but the table
carries it.

---

# Before you send

Fourteen edits: N1 to N8, then O1 to O6. About forty minutes.

Then three final checks:

1. **Ctrl+F `a a`** — should return nothing.
2. **Read the abstract out loud.** If any idea appears twice, one of them is left over from the old
   version.
3. **Read the four Figure 1 box labels against pages 17 and 18.** Every box label should use the same
   words as the paragraph that explains it.

One thing worth saying in your message to him, because it answers R1 comment 1 better than anything
else could: name the two or three changes you made that he did *not* ask for. The Marathi and BERT
definitions, grounding the "no published study" claims in your own Section 2 search, and the Table 3
subset correction are all yours. Those show the reading was done by you.
