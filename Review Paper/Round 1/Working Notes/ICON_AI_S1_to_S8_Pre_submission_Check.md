# Pre-submission check — Sections 1 to 8

**Checked:** `Template ICON AI 2026 - Section 1 to 8.pdf`, 22 pages, ~9,400 words, 37 references.
**Checked against:** `ICON AI Master Comment Tracker.md` (all 144 comments, 15 rules).
**Date:** 20 August 2026

---

## The short version

The paper is in good shape. Citation density is 128 in-text citations over 9,384 words, which is
about 13.6 per 1,000 words — higher than the ratio Dr. Ho accepted in Round 2. Three whole rule groups
are now clean:

| Rule | Round 1 + 2 comments | Status now |
|---|---|---|
| 11 — no bold in the body | 22 | Clean. No bold found. |
| 12 — no `(Section X)` or content in brackets | 11 | Clean. Every section reference is the subject of its sentence. |
| 13 — peer-reviewed sources only | 3 | Clean. No arXiv preprints in the reference list. |

**But there is one thing that would undo all of it.** The abstract was never revised after Round 2.
It still contains four phrases Dr. Ho highlighted and commented on individually, plus a fifth that
breaks a rule he stated twice. It is the first thing he reads. Fix A1 before anything else.

Below, **47 fixes** in three groups:

- **Group A — must fix (7).** Exact words he already flagged, still in the paper.
- **Group B — will draw new comments (29).** Same rules, applied to Sections 3.2 to 8, which he has
  never read closely.
- **Group C — errors and mechanics (11).** Typos, grammar, one missing reference, and your three
  comment bubbles.

Two things I did **not** treat as problems, for the record. Length: the paper is 22 pages against
the 20-page cap in your Direction doc, but you said you will handle the cuts, so I have only marked
the repeated passages (C7) that would give you about a page back for free. Citation style: you have
confirmed author–date with him, and author–date is applied correctly everywhere except three
ampersands (A3).

---

# GROUP A — Must fix. He already flagged these exact words.

## A1. The abstract was never updated after Round 2 — **highest priority**

In Round 2 his comments run from page 2 to page 5. The abstract sits on page 1, which he did not
annotate — so it never picked up the Round 2 fixes. Section 1 was rewritten around it and the
abstract still carries the old wording. Four of his comments land on it word for word.

This is also why it is dangerous. He has read this abstract once without commenting. If he reads it
again and finds the same four phrases he corrected inside the body, the reasonable conclusion is that
the corrections were applied mechanically rather than understood — which is close to R1 comment 1,
the question about whether the writing is your own.

| Line in the abstract | Comment it violates | Replace with |
|---|---|---|
| "each tier is shown to improve either label fidelity or scalability **by giving up the other**" | R2 50, "Informal" | "at the expense of the other" |
| "the four regional corpora **are audited against** what a reliability claim requires" | R2 52, "This sounds accounting-oriented" | "are examined against" |
| "the **class imbalance that affects the labels** is shown to be…" | R2 41, "Class imbalance affects the distribution of labels rather than the labels" | "the class imbalance in the label distribution is shown to be…" |
| "the same condition under which **the standard agreement statistic** becomes difficult to interpret" | R2 42, "Which statistic? Cohen's κ? But you never mentioned that explicitly" | "the same condition under which Cohen's kappa becomes difficult to interpret" |

One more line in the abstract, under Rule 9 (say who holds the position):

> "Sentiment analysis of this text **is usually treated as** a modelling problem."

He asked in R2 39: *"Who treat them as separate problems? You or existing studies?"* Rewrite as:

> "The studies reviewed here usually treat sentiment analysis of this text as a modelling problem."

**Corrected abstract, sentences 3 to 9** (the rest is fine):

> The studies reviewed here usually treat sentiment analysis of this text as a modelling problem.
> This review indicates that the more limiting problem lies earlier, in the sentiment labels
> themselves and in the evidence offered that those labels are sound. The review covers annotation
> practice and reliability evaluation for Malaysian Malay-English code-mixed sentiment data.
> Comparative benchmarking of sentiment classifiers is outside its scope. Three contributions
> follow. First, the annotation strategies used for low-resource code-mixed text are organised into
> three tiers, and each tier is shown to improve either label fidelity or scalability at the expense
> of the other. Second, the two causes of neutral-label skew are separated, and the four regional
> corpora are examined against what a reliability claim requires. […] Third, the class imbalance in
> the label distribution is shown to be the same condition under which Cohen's kappa becomes
> difficult to interpret.

Abstract length after the change: about 225 words, still under the 300-word cap.

## A2. "This review argues" — page 3

R1 comment 13 on the word *argues*: *"You can soften the tone using more neutral words like
'highlight' or 'indicate'."*

Your abstract already says "This review **indicates**". Page 3 still says:

> "This review **argues** that for Malaysian Malay-English code-mixed sentiment data, the annotation
> label is at present the more limiting problem…"

**Change to:** "This review **indicates** that…"

This one matters more than its size. He will notice that the abstract took his correction and the
body did not.

## A3. Citation format — "&" in two places, "and" everywhere else

You confirmed he wants author–date. Author–date is applied correctly throughout. But the ampersand
is not consistent:

| Page | Now | Change to |
|---|---|---|
| 3 | (Artstein **&** Poesio, 2008) — twice | (Artstein **and** Poesio, 2008) |
| 3 | (Frénay **&** Verleysen, 2014) | (Frénay **and** Verleysen, 2014) |

Sections 4 to 7 already use "and": (Pavlick and Kwiatkowski, 2019), (Hutto and Gilbert, 2014),
(Artstein and Poesio, 2008). Your reference list also uses "and". So fix the three on page 3, not
the other way round.

## A4. "give up" — page 9

R2 50 flagged *"by giving up the other"* as informal. It is gone from Section 1 but has come back in
Section 4.1:

> "…but as different decisions about which of the two **to give up**."

**Change to:** "…but as different decisions about which of the two to sacrifice."

## A5. "the second-tier costs" — page 11

Same word family, R2 28 and 50. Also a grammar problem (see C4).

> "The clearest regional evidence of what the **second-tier costs**…"

**Change to:** "The clearest regional evidence of what the second tier concedes…"

## A6. "stays inside" — page 11

R2 22 flagged *"stay inside the dataset"* as informal.

> "Its score therefore **stays inside** the neutral band, and it is returned as neutral."

**Change to:** "Its score therefore **remains within** the neutral band, and it is returned as neutral."

## A7. "the intuitive remedy" with no citation — page 12

Two rules at once. Rule 3 (register) and Rule 2 (a claim about what researchers do, with no source).

> "Pooling several annotators is **the intuitive remedy** for an unreliable one, and MESocSentiment
> is evidence against the intuition…"

**Change to:**

> "Pooling several annotators is the response most often proposed when a single annotator is
> unreliable (Artstein and Poesio, 2008; Uma et al., 2021). MESocSentiment is evidence against that
> response, because it already was a consensus pipeline."

---

# GROUP B — Will draw new comments. Same rules, new sections.

Round 2 produced 64 comments on 4 pages. Sections 3.2 to 8 are 16 pages he has never read closely.
These 19 items are where the same three habits — conversational verbs, unnamed referents, and claims
with no citation — have come back.

## Rule 3 — Register (his largest group: 23 comments)

Physical metaphors for abstract ideas are what break the register. Short words are fine; verbs that
belong to bodies and machines are not.

| # | Page | Now | Change to |
|---|---|---|---|
| B1 | 9 | "label fidelity and scale **pull against each other**" | "label fidelity and scale are in tension" |
| B2 | 9 | "**Read that way** they fall into three tiers." | "On that reading, the strategies fall into three tiers." |
| B3 | 9 | "the two types of annotator therefore do not **break on** the same inputs, and they do not **break** at the same rate" | "the two types of annotator therefore do not fail on the same inputs, and they do not fail at the same rate" |
| B4 | 9, 17, 18 | "carries that type's **blind spot** throughout" / "a shared **blind spot**" / "The **blind spots** of one generation" | "carries that type's systematic weakness throughout" / "a shared limitation" / "The limitations of one generation" |
| B5 | 11 | "the mechanism **fires** on this data" | "the mechanism operates on this data" |
| B6 | 12 | "more damaging than the **headline percentage** suggests" | "more damaging than the aggregate percentage suggests" |
| B7 | 13 | "the **hard core** of the problem" | "the most difficult cases in the problem" |
| B8 | 14 | "where each family of model **breaks down** when used as an annotator" | "where each family of model is limited when used as an annotator" |
| B9 | 14 | "The direction is **worth stating plainly**." | "The direction of that result should be stated explicitly." |
| B10 | 15 | "Their worked example is **worth reproducing**." | "Their worked example illustrates the effect." |
| B11 | 18 | "one of them **deserves restating** here, because it is the point at which the process **turns on itself**" | "one of them should be restated here, because it is the point at which the process becomes self-reinforcing" |

**A note on B4, "blind spot".** This one costs more than the others, because the phrase is also a box
label in Figure 1 and runs through six paragraphs on pages 17 and 18. It is not a phrase he has
flagged by name. I am flagging it because it is the same *kind* of word as *friction* and *audit* —
a physical or borrowed metaphor standing in for an abstract relation — and those are the two he
objected to most specifically. If you would rather not touch Figure 1, the safe middle option is to
keep the phrase but define it once at its first appearance on page 9: *"a systematic weakness, or
blind spot, in what that type of annotator can read."* After that the metaphor is your own defined
term rather than loose language.

## Rule 2 — Claims about other researchers need a citation on that sentence (25 comments)

He escalates on these. R1 36: *"Otherwise, you are simply making a baseless and unreasonable claim."*
Four sentences in Sections 4 to 7 make claims about the literature with no source attached.

**B12 — page 9, Section 4 opener**

> "…the practice of pooling several annotators is examined last, because it is **the remedy most
> often proposed**, and the one the regional evidence tests most directly."

"Most often proposed" is an empirical claim about a body of work. **Add a citation:**
(Artstein and Poesio, 2008; Uma et al., 2021). Both are already in your reference list.

**B13 — page 9, Section 4.1**

> "The strategies in **the literature** are best read not as competing solutions to one problem…"

R1 43: *"'elsewhere' refers to the existing literature, right? Then, a citation is needed."* Same
here. **Change to:**

> "The strategies reported by the studies reviewed here are best read not as competing solutions to
> one problem…"

That grounds it in your own Section 2 method instead of claiming something about all literature.
No citation needed once it is your own survey.

**B14 — page 16, Section 7 opener**

> "Sections 3 to 6 examined linguistic structure, annotation practice, model capability and
> reliability measurement in turn, **which is how the literature itself is organised**."

Same problem. **Change to:** "…in turn, which is how the studies reviewed here are organised."

**B15 — page 15, Section 6 opener**

> "Reliability is normally demonstrated with a chance-corrected agreement coefficient, of which
> Cohen's κ is the most widely used (Cohen, 1960)."

Cohen (1960) is the source for the coefficient, not for the claim that it is *normally* used or *most
widely* used. Page 3 gets this right with two sources. **Change to:**
"…(Cohen, 1960; Artstein and Poesio, 2008)."

**B16 — pages 10, 13, 16: three absolute claims about the whole literature**

These three sentences are the strongest in the paper and each has no citation, because none is
possible — they are negative claims:

- p.10: "**no published study** evaluates generative annotation on Malaysian code-mixed text"
- p.13: "**No published study** adjudicates annotator disagreement on Malaysian code-mixed sentiment text"
- p.16: "**No corpus in the regional literature** therefore supplies what a reliability claim requires"

You cannot cite the absence of a paper. What you *can* do is attribute the absence to your own search,
which Section 2 documents. This is Rule 9. **Change all three to the same pattern:**

- "**no study meeting the criteria in Section 2** evaluates generative annotation on Malaysian
  code-mixed text"
- "**No study retrieved by the search described in Section 2** adjudicates annotator disagreement…"
- "**None of the four corpora examined here** therefore supplies what a reliability claim requires…"

This turns three unsupportable claims into three findings of your review. It is a small change with
a large effect on how defensible the paper is.

## Rule 4 — Name what the word points at (15 comments)

**B17 — page 11**

> "This section separates the two distinct causes at work **in it**…"

"In it" points back two sentences to "that distribution". He asked "Which problem?" and "What
resources?" in exactly this situation. **Change to:** "…the two distinct causes at work in that
skew…"

**B18 — page 19**

> "…the premise that annotators of **different construction** fail independently…"

"Different construction" has not been used before and is unclear. The paper's own term, used in
Section 4.3, is *architectural difference*. **Change to:** "…the premise that annotators of
different architecture fail independently…"

## Rule 5 — Define every abbreviation and technical term at first use (3 comments so far)

He asked *"What is X?"* and *"What is ϰ?"*. Sections 4 to 6 introduce eight terms with no definition.
Your own comment L1 on page 10 spotted one of them already.

| # | Page | Term | Suggested first-use wording |
|---|---|---|---|
| B19 | 10 | **Marathi** (your comment L1) | "Marathi, an Indo-Aryan language of western India, is morphologically rich where Malay is not…" |
| B20 | 10 | **BERT** | "a fine-tuned BERT baseline, where BERT is a bidirectional transformer encoder pre-trained on unlabelled text" |
| B21 | 10, 14 | **GPT-4o**, **Llama 3.1 405B** | "two generative large language models, GPT-4o and Llama 3.1 405B" |
| B22 | 14 | **XLM-RoBERTa** and **masked language modelling** | "XLM-RoBERTa, a multilingual encoder model, using masked language modelling, a training method in which the model predicts words hidden from the input" |
| B23 | 14 | **macro F1** | "a macro F1 of 0.90, where macro F1 is the mean of the per-class F1 scores and F1 is the harmonic mean of precision and recall" |
| B24 | 13, 14 | **transformer**, **encoder** | Define *transformer* once at its first appearance on p.13, and say plainly that an *encoder* here means a model that reads text and produces representations rather than generating text. |

Do not add a long explanation for each. One clause is enough, and one clause is what he asked for
with κ.

## Rule 10 — Preview enumerated things by name (8 comments)

**B25 — page 14, Section 5 opener**

R2 56 is the exact template for this: *"Reader has to continue reading to discover what the three
properties are."* Section 5 says:

> "This section asks where each family of model breaks down when used as an annotator."

The reader then has to read two pages to find out there are two families. **Add one sentence after
it:**

> "Two families are examined: fine-tuned multilingual encoders, and generative models used directly
> as annotators."

**B26 — page 9, Section 4.1**

> "…they fall into three tiers. The first-tier is manual annotation by people."

**Change to:** "…they fall into three tiers: manual annotation, semi-automated annotation, and fully
automated generative annotation. The first tier is manual annotation by people."

## Rule 1 — Split the long sentences (9 comments)

He flagged a 47-word sentence in Round 2 as *"long and relatively difficult to digest."* Five
sentences are still over 40 words. Four of them are on pages 2 and 3 — the two pages he reads hardest.

**B27 — page 3, 48 words**

> "Label noise is learned during training and degrades the resulting classifier (Frénay and
> Verleysen, 2014), and incorrect labels in a test set distort the evaluation of model performance,
> so that reported accuracy no longer reflects how the model actually behaves (Northcutt et al.,
> 2021; Bowman and Dahl, 2021)."

**Split at the "and":**

> "Label noise is learned during training and degrades the resulting classifier (Frénay and
> Verleysen, 2014). Incorrect labels in a test set also distort the evaluation of model performance,
> so that reported accuracy no longer reflects how the model actually behaves (Northcutt et al.,
> 2021; Bowman and Dahl, 2021)."

**B28 — page 2, 42 words.** "Against that, Winata et al. (2021) find that multilingual pre-training
alone does not guarantee good representations of code-switched text, and Conneau et al. (2020)
describe a 'curse of multilinguality'…" — split before "and Conneau et al. (2020)".

**B29 — page 2, 41 words.** "Khanuja et al. (2020) report that multilingual models fine-tuned on
code-switched data achieve the strongest scores…, and Adilazuarda et al. (2022) show that robustness
depends on…" — split before "and Adilazuarda et al. (2022)".

Both have the same shape: two findings from two different studies joined by "and". Each becomes two
clear sentences with no rewording at all.

The 42-word sentence on page 2 about lexicons and benchmark corpora uses a colon, which carries the
length, so it can stay. The 53-word sentence on page 19 is the numbered list of five reporting
elements — a list reads fine at that length. Leave it.

---

# GROUP C — Errors and mechanics

## C1. Grammar error — page 18

> "The fifth link runs from extreme class skew to **the reliability hard to established**…"

This is not grammatical. **Change to:** "The fifth link runs from extreme class skew to the
difficulty of establishing reliability…"

## C2. Missing word — page 19

> "Publishing that distribution would preserve **the cases present pipelines delete**."

A word is missing and the sentence is hard to parse. **Change to:** "Publishing that distribution
would preserve the cases that current pipelines delete."

## C3. Typo in Figure 1 — page 17

The fourth box reads "**Share** Blind Spot". The text calls it "a **shared** blind spot".
**Change the box label.** If you apply B4 and drop "blind spot" entirely, the box should read
"Shared Limitation" and the six link paragraphs on pages 17 to 18 should use the same words as
the boxes.

## C4. "first-tier / second-tier / third-tier" — pages 9, 10, 11

When these are the subject of a sentence they are nouns and take no hyphen. Five places:

| Page | Now | Change to |
|---|---|---|
| 9 | "The **first-tier** is manual annotation" | "The first tier is manual annotation" |
| 9 | "The **second-tier** is semi-automated annotation" | "The second tier is semi-automated annotation" |
| 10 | "The **third-tier** replaces those tools" | "The third tier replaces those tools" |
| 10 | "the capability the **second-tier** lacks" | "the capability the second tier lacks" |
| 11 | "what the **second-tier** costs" | see A5 |

Page 10's "The third tier is the least evidenced of the three" is already correct — that is the one
to match.

## C5. Tay et al. (2016) is cited but is not in the reference list — page 7

> "Treffers-Daller et al. (2022), citing Tay et al. (2016), describe the effect more precisely…"

Every other name in the paper has an entry. Two options:

1. **Preferred:** rewrite as a secondary citation so no entry is needed —
   "Treffers-Daller et al. (2022) describe the effect more precisely, drawing on earlier work on
   Malaysian discourse particles: *lah* shifts an utterance…"
2. Find the Tay et al. (2016) paper and add a full entry.

Option 1 is safer. You have not read Tay et al. (2016) yourself, and R1 comment 3 was exactly about
not extending a source beyond what you can verify.

## C6. Table 3, SentiBahasaRojak row — page 16 (your comment L3)

I checked the source. The row is correct but incomplete in a way that weakens your own argument.
Romadhona et al. (2022) built SentiBahasaRojak from three sub-sets: product reviews and movie reviews
(both generated by data augmentation) and stock reviews (manually crawled). **The κ = 0.77 covers the
stock review subset only.** The other two sub-sets have no agreement figure at all, because they were
not manually annotated.

**Change the "What the coefficient measured" cell to:**

> "Whether a stock-market post is positive or negative; reported for the stock review subset only"

*Bullish* and *bearish* are finance words that many readers will not know, and they are the only
specialist vocabulary in that column. The row above it reads "Whether a sentence is opinionated or
factual" — plain words, same sentence shape. "Positive or negative" matches it, and it is exactly
what the source means: Romadhona et al. (2022) define bullish as positive and bearish as negative.

It also makes your own argument easier to see. The point of that column is that the two reported
coefficients measure **two-class** judgements, not the three-class polarity task the corpora are used
for. "Positive or negative" shows the two classes on the page. "Bullish or bearish" hides them behind
jargon.

Then add one sentence to the three observations below the table:

> "The coefficient Romadhona et al. (2022) report covers the stock review subset alone. The product
> and movie review subsets were produced by data augmentation and carry no agreement figure."

This makes your point stronger, not weaker: the reported number covers part of a resource that is
cited as a whole.

**One thing to verify yourself.** The paper says Romadhona et al. "report a kappa value without
stating which coefficient it is". Their text describes it as substantial agreement among five
experts. Open the paper and check whether they name Cohen's kappa explicitly. If they do, soften your
sentence to: "report a kappa value for five annotators, although Cohen's κ is defined for two."

## C7. Repeated sentence — pages 10 and 14 (your comment L2)

You are right, and it is the clearest repetition in the paper.

- Page 10: "Because a generative model is not restricted to a fixed vocabulary, it can in principle
  interpret an unfamiliar spelling or an unseen slang term from context, which is the capability the
  second tier lacks."
- Page 14: "Because they are not restricted to a task-specific vocabulary, they can in principle
  interpret an unfamiliar spelling or an unseen slang term from context. This is the capability the
  encoder lacks."

**Keep page 10** (it belongs to the tier argument) and **cut the explanation on page 14**, replacing
it with a back-reference:

> "Generative models locate their competence differently. Section 4.1 described the capability that
> follows from not being restricted to a fixed vocabulary. It is the capability the encoder lacks,
> and it is why generative annotation is attractive for a variety that changes faster than its
> resources."

Two smaller repeats you may want to trim if you need space:

- Uma et al. (2021)'s finding is stated in full on page 13 and again on page 19.
- The MESocSentiment percentages (78.23 / 16.33 / 5.44) appear on pages 3, 11, 15 and 18.
  Pages 15 and 18 could give the neutral share alone.

## C8. Title block is still template placeholder text — page 1

The first page shows "Author(s) Name(s)", "*Author Affiliation(s)*", "*E-mail*", the four "xx xxx
2023" dates, and "xyz @utm.my" as the corresponding author. Your `Revision Alignment Check` note says
the corresponding author address should be yongvay@gmail.com.

Fill in your name, your affiliation and your e-mail before you send it. Leave the "Article history"
dates as they are — those are filled in by the journal.

## C9. Table and figure captions are sentence case; the template asks for title case

Your `Direction` doc records Template §7.1 as: caption **above** the table, 12pt bold, centred,
**title-case**. Placement, weight and centring are all correct. The case is not:

| Now | Title case |
|---|---|
| "Table 1. Annotation strategies for Malaysian Malay-English code-mixed sentiment data" | "Table 1. Annotation Strategies for Malaysian Malay-English Code-Mixed Sentiment Data" |
| "Table 2. The three annotators used to build MESocSentiment, and the labels each assigned" | "Table 2. The Three Annotators Used to Build MESocSentiment, and the Labels Each Assigned" |
| "Table 3. Reliability evidence reported by the four Malay-English sentiment corpora" | "Table 3. Reliability Evidence Reported by the Four Malay-English Sentiment Corpora" |
| "Figure 1. The compounding chain in Malaysian code-mixed sentiment annotation" | "Figure 1. The Compounding Chain in Malaysian Code-Mixed Sentiment Annotation" |

Your section headings are already title case, so this also makes the document internally consistent.

## C10. Two tables break across a page

Table 1 splits between pages 10 and 11, and Table 2 splits between pages 12 and 13 in the middle of
the pysentimiento row. In Word: select the table, **Table Properties → Row → untick "Allow row to
break across pages"**, and set **Repeat Header Rows** on the top row. If Table 1 still splits after
that, it is short enough to move whole onto page 11.

This is cosmetic, but he reads the tables closely — Table 3 is where two of your three findings live.

## C11. Reference count: 37, and he asked for at least 40

R1 comment 80: *"If possible, try increase the volume of references to at least 40."* You have gone
from 24 to 37, which is real progress, but you are three short of the number he named, and he
will count.

Three places where a source is missing anyway, so the additions do real work rather than padding:

1. **B12** needs a source for "the remedy most often proposed" — you can cite something already in
   the list, or add one on annotator aggregation.
2. **Section 4.2's VADER argument** rests on Hutto and Gilbert (2014) plus your own inference. One
   more study on lexicon coverage and out-of-vocabulary behaviour would support it.
3. **Section 5's encoder paragraph** rests on one shared-task system description (Manukonda and
   Kodali, 2025), and the paper says so honestly. A second study on fine-tuned multilingual encoders
   for code-mixed text would make the paragraph stand on two legs.

Do this **after** the wording fixes, not during — that is his own instruction from 11 August.

---

# Before you send

Run these five checks over the file after making the edits. About twenty minutes.

1. **Ctrl+F for:** `giving up`, `give up`, `audit`, `blind spot`, `break`, `fires`, `sits`,
   `stays inside`, `carries over`, `thin`, `unsurprising`, `hard core`, `headline`, `worth`,
   `argues`, `&`.
2. **Ctrl+F for:** `the literature`, `most often`, `usually`, `commonly`, `normally`, `no published`,
   `no corpus`, `no study`. Each needs either a citation on the same sentence, or the words
   "the studies reviewed here" / "Section 2".
3. **Read the first paragraph of Sections 5, 6, 7 and 8 on their own.** Does each one connect back
   and name what is coming?
4. **Check every abbreviation** the first time it appears: NLP ✔, SVO ✔, κ ✔, BERT ✘, GPT-4o ✘,
   XLM-RoBERTa ✘, macro F1 ✘, transformer ✘, encoder ✘.
5. **No bold anywhere in the body.** Italics only for *Bahasa Rojak*, *Manglish*, *lah*, *tidak* and
   the Malay examples, κ, and journal titles in the reference list.

## One line to put in your message to him

Author–date is now settled, so the only thing left to say is what you changed. Something like:

> "I have revised the abstract and Sections 3.2 to 8 using the same rules from your comments on
> Sections 1 to 3.1 — plainer register, a citation on every claim about other studies, and every
> abbreviation defined at first use. The reference list is now at 37 and I am still adding to reach
> 40."

---

## Sources

- [Romadhona, N. P., Lu, S.-E., Lu, B.-H., and Tsai, R. T.-H. (2022). BRCC and SentiBahasaRojak: The First Bahasa Rojak Corpus for Pretraining and Sentiment Analysis Dataset. COLING 2022](https://aclanthology.org/2022.coling-1.389/)
- [BRCC and SentiBahasaRojak — full PDF](https://aclanthology.org/2022.coling-1.389.pdf)
