# ICON AI v3 Shortened — check against Dr. Ho's comments

**Checked on:** 11 Sept 2026
**File:** `ICON_AI v3 Shortened.docx`
**Size now:** 3,476 words of body text · 39 references · 3 tables · 11 pages
**Page limit:** 20 pages. Minimum 8. So you have lots of room.

---

## Short answer

The cut was good work. The English is the simplest it has ever been. That is what Dr. Ho has been asking for since Round 1.

I checked all 239 of his comments against the new text.

- **About 23 of his comments are now dead.** The text they pointed at is gone. You do not need to do anything.
- **9 of his comments are still broken.** These need fixing. All are small.
- **2 things need your decision.** They are about what the cut removed.

I did **not** ask you to paste back long text. That would undo his new instruction.

---

## Part 1 — Still broken. Small fixes.

### 1. You say the same thing twice, with the same source

This breaks Rule 16 (do not cite the same paper in two sentences in a row). It was the first comment he wrote in Round 4.

**Now — end of paragraph 1:**
> This issue is particularly relevant in Malaysia, where Malay-English code-mixing is common in social media and written communication (AlAfnan et al., 2025).

**Now — start of paragraph 2:**
> Malaysia's multilingual setting makes this problem especially relevant. Malay-English code-mixing is common in Malaysian written communication (AlAfnan et al., 2025).

Same claim. Same source. Back to back.

**Fix:** delete the last sentence of paragraph 1. Then start paragraph 2 like this:

> Malaysia is one setting in which this occurs frequently: Malay-English code-mixing is common in Malaysian social media and written communication (AlAfnan et al., 2025).

*("one setting in which…" is his own wording, from R4 8.)*

---

### 2. You use "code-switched" before you name it

This is R4 comment 7, word for word. He wrote:

> "you never named the phenomenon of 'two languages alternate within a single message' as 'code-switched'. In this case, readers will have to infer the relationship between them by themselves."

You added the naming words after Round 4. The cut deleted them again.

**Now:**
> This creates difficulties when two languages alternate within the same message because sentiment cues may occur in either language, while resources designed for monolingual text may not represent both languages equally well. Code-switched text therefore often produces lower performance…

**Change to:**
> This creates difficulties when two languages alternate within the same message, a pattern known as code-switching. Sentiment cues may then occur in either language, while resources designed for monolingual text may not represent both languages well.

This one change fixes three things at once:

- it names code-switching (R4 7)
- it drops the word **equally**, which he told you to delete (R1 44)
- it splits a 32-word sentence into two

---

### 3. The colon makes two studies look like proof

This is R4 comment 20. It is his sharpest comment in four rounds.

**Now:**
> Such mixing **is systematic rather than random:** Treffers-Daller et al. (2022) identify recurring syntactic patterns, while Maskat and Rahman (2020) document recurring non-standard spellings such as x for tidak… **These conventions** can differ from forms represented in standard language resources… (Abu Bakar et al., 2020; **Maskat and Rahman, 2020**).

Two problems here:

1. The colon says the two studies **prove** the mixing is systematic. He said they do not. His words: *"The fact that the authors categorize the variation and map two categories to standard forms does not necessarily prove that the variation is systematic."*
2. Maskat and Rahman (2020) appears in two sentences in a row. Rule 16 again. Your own checker script finds this one.

**Change to:**
> Treffers-Daller et al. (2022) identify recurring syntactic patterns in Malay-English switching, and Maskat and Rahman (2020) document recurring non-standard spellings such as *x* for *tidak*. This suggests that the mixing is systematic rather than random. Forms of this kind can differ from those represented in standard language resources, and may therefore obscure the words, negation or other cues that carry sentiment (Abu Bakar et al., 2020).

This keeps "systematic rather than random" (his wording, R4 18). But now it is a suggestion, not proof.

---

### 4. "sufficient scale" has no number

R4 40: *"What counts as large? You need an operational definition somewhere in the paper… For example, if you later define a threshold such as 10,000 messages, say so."*

"Sufficient scale" is the same problem as "large". Just a different word.

**Fix:** say **"a scale of at least ten thousand labelled messages"**.

---

### 5. His exact words were changed

R4 42 gave you the wording himself. You changed two parts of it.

| He wrote | Your paper now says |
|---|---|
| satisfies some of these **criteria** but not all **of them** | satisfies some of these **conditions** but not all |

He remembers his own wordings. Twenty-four of his 239 comments supply wording. Use them exactly.

**Change the two sentences to:**
> A general-purpose resource would need to meet four criteria: a scale of at least ten thousand labelled messages, a label distribution not dominated by one class, everyday social-media text, and direct evidence of annotation reliability. Each of the four satisfies some of these criteria but not all of them.

*(You do not need the numbered "(1)…(2)…" format here. That format was R1 76, and it was about the study inclusion criteria, not this list.)*

---

### 6. The bridge into the model paragraph is gone

R4 26: *"it jumps quite quickly from the linguistic/resource mismatch to architecture."*

You wrote a bridge sentence after Round 4. The cut removed it.

Also, "is often attributed to" is a claim about other researchers. It has no citation on that sentence. That breaks Rule 2, his biggest rule.

**Now:**
> Poor performance on code-mixed text is often attributed to model architecture or limited exposure to code-switched data during pre-training.

**Change to:**
> This mismatch between writing conventions and tool design raises the question of where the difficulty actually lies. One answer points to the models.

Then keep your existing cited sentences after it.

**Checked against the PDF (11 Sept).** Do **not** cite Doğruöz et al. (2021) for "model architecture". The paper never says that. The word "architecture" appears only in the title of a reference. Their own summary names three causes: training data, evaluation benchmarks, and missing user-facing applications. Architecture is not one of them.

The paper **does** strongly support the training-data half, on page 1659:

> "these LMs are either trained primarily on monolingual datasets such as Wikipedia in the case of mBERT, or Common Crawl in the case of XLM-R. So, they are either not exposed to C-S data at all during training, or they miss out on several language pairs, types and functions of C-S."

So strengthen the Doğruöz sentence you already have later in the paragraph:

> Doğruöz et al. (2021) add that widely used multilingual models such as mBERT and XLM-R are trained mainly on monolingual corpora, so they may see little or no code-switched text during pre-training.

---

### 7. Two sentences are over 35 words

His limit is about 35 words.

**Sentence A — 37 words, §1 paragraph 4.** Split it at "while".

**Sentence B — 45 words, §3.3.** This one has a second problem too.

> The analyser with the highest neutral share, pysentimiento, is the only one of the three built on a pre-trained transformer model of the kind described by Devlin et al. (2019), so **a larger pre-trained model** did not, in this case, produce a smaller neutral share.

"Transformer-based" does not mean "larger". You never show the model sizes. This is the R4 20 problem again — the evidence is weaker than the claim.

**Change to two sentences:**
> Of the three analysers, only pysentimiento is built on a pre-trained transformer model of the kind described by Devlin et al. (2019). It also has the highest neutral share, so being built on a pre-trained transformer model did not, in this case, produce a smaller neutral share.

---

### 8. Two headings are not real headings

- `1. Introduction` is normal text with **bold** on it.
- `References` is the same.
- Sections 2 to 6 all use the proper Heading 1 style.

Two problems. The navigation pane breaks. And bold text in the body is R1 comment 5 — the comment he repeated 22 times.

**Fix in Word:** click each line, then apply **Heading 1**.

Also delete the empty paragraph between Table 2 and the text under it.

---

### 9. Table 2 lists the resources in a different order from Section 1

- Section 1 order: MY-EN-CS, SentiBahasaRojak, MyCovid-Senti, MESocSentiment
- Table 2 order: MY-EN-CS, MyCovid-Senti, SentiBahasaRojak, MESocSentiment

**Fix:** swap rows 2 and 3 of Table 2.

Also, Section 1 calls them "four **relevant** resources" but Contribution 2 calls them "four **Malay-English sentiment** resources". That is R4 58 (one name per thing). Use the second name in both places.

---

## Part 2 — Two things that need your decision

### Decision A — the review methodology

Section 1 now describes your search in two sentences only. These are missing:

- the four inclusion criteria (he gave you the sentence at R1 75 and the format at R1 76)
- the date range
- the "no preprints" policy (R2 54)

For a review paper, this is the part a reviewer looks for first. Without it, the paper reads like an essay, not a review.

**But putting it back into Section 1 makes Section 1 longer again.** That fights Dr. Ho's new instruction.

**My suggestion: make it a short standalone section instead.** About 120 words. Put it after the Introduction.

This is exactly what he asked for at R1 68:

> "It feels weird to have only 1 subsection within a section… perhaps you can make it a standalone section, 2. Review Methodology?"

This solves both instructions at once:

- Section 1 gets **shorter**, not longer
- the selection procedure comes back
- R1 68 is finally answered

Cost: you renumber Sections 2 to 6 as 3 to 7. The paper is 11 pages, so there is no page pressure.

If you are not sure, this is a good thing to ask Dr. Ho directly in one line.

---

### Decision B — the reference list

He asked for **at least 40** references (R1 80). You have **39**. Worse, **two are not cited anywhere in the paper**:

- **Coluzzi (2017)**
- **Joshi et al. (2020)**

An uncited reference looks like padding. He reads the reference list.

**Step 1 — free fix.** Put Joshi et al. (2020) back on this sentence, which currently has no citation at all:

> However, many language resources used for sentiment analysis are developed primarily for individual languages **(Joshi et al., 2020)**.

That fixes an orphan reference and a missing citation in one move. No extra words.

**Step 2 — decide on Coluzzi (2017).** The Malaysia-languages sentence it supported is gone. Either give it one short job, or remove it from the list. Removing it is honest. Then you are at 38 used.

**Step 3 — find two or three more that do real work.** Do not pad.

Good places to put them, because these sections are thin:

- **§2.3 spelling** — Dewan Bahasa dan Pustaka for standard Malay. He asked for this source by name at R4 21.
- **§4** — you write "Studies with more than two annotators should therefore name the coefficient used." A source for a multi-annotator measure (for example Fleiss' kappa) would fit naturally there.

Check each new source actually says what you use it for. Rounds 3 and 4 were mostly that question.

---

## Part 3 — Comments you can now ignore

These were real comments. The text they pointed at is gone. Nothing to do.

R4 2 (carry an assumption) · R4 8 (one variety) · R4 9 (Coluzzi / Ethnologue) · R4 11 (do not cover the same set) · R4 13 (states its position) · R4 14 (regarded) · R4 15 (technical difficulty) · R4 16 (weakens) · R4 17 · R4 19 (the same regularity) · R4 21 (dictionary sentence) · R4 23 (earlier work) · R4 24 (Malaysian writers) · R4 27 (On this explanation) · R4 28 (regionally adapted) · R4 31 (often limiting) · R4 38 (reading) · R4 45 (one condition) · R4 52 (author's) · R4 53 (diagnosis) · R4 55 and R4 56 (tiers and trade-off) · R1 41 (Scope heading) · R1 62–67 (bracket cross-references)

**And these of his wordings did survive the cut.** Keep them:

R4 3 (However) · R4 5 (developed primarily for individual languages) · R4 18 (systematic rather than random) · R4 22 (may therefore) · R4 25 (designed to) · R4 29 (no "capacity dilution") · R4 30 (arises earlier) · R4 32 (automatic methods) · R4 33 · R4 35 (label errors) · R4 36 (explains part of the difficulty, but not all) · R4 37 (one First/Second/Third spine) · R4 39 (identifies four) · R4 43 (inter-annotator agreement coefficient) · R4 44 (both tasks named) · R4 46 (assessed) · R4 47 (such as Cohen's kappa) · R4 48 (difficult to interpret) · R4 49 (Selvaraju link) · R4 50 · R4 51 (have not yet been established) · R4 54 · R4 57 · R4 59 (studies report, not corpora)

---

## Part 4 — Is Section 1 balanced now?

| Section | Words | Share of body |
|---|---:|---:|
| 1. Introduction | 963 | 31.1% |
| 2. Linguistic Challenges | 367 | 11.9% |
| 3. Annotation Approaches | 723 | 23.4% |
| 4. Evaluating Annotation Reliability | 271 | 8.8% |
| 5. Research Priorities | 636 | 20.6% |
| 6. Conclusion | 134 | 4.3% |

Section 1 is still the longest. It is about 2.6 times Section 2, and 3.5 times Section 4.

So cutting Section 1 alone did not fix the balance.

**Better idea: grow the thin sections instead of cutting Section 1 more.**

- Section 4 is only 271 words. That is very short for the section that carries your main point.
- Section 2 is only 367 words.
- Moving the review methodology out (Decision A) also lowers Section 1's share on its own.

The paper is 11 pages. The limit is 20. Nothing is forcing you to cut.

---

## Part 5 — Small things, low risk

- **"prerequisite for sound benchmark evaluation"** (§1 ¶4). "Prerequisite" is a strong word, and "sound" has no definition. Check Bowman and Dahl (2021) really says this. A safer version: *"Annotation reliability therefore affects how far benchmark results can be trusted."*
- **"pre-trained"** first appears in §1 ¶3 with no explanation. The definition was cut. Rule 5 says explain a technical term on first use. One short clause would cover it.
- **"the extent varies by task"** — extent of what? He asked this exact question at R4 6. Safer: *"although the size of this gap varies by task."*

---

## What to do first

1. Fixes 1 to 9 in Part 1. Maybe an hour in Word.
2. Then run your own checker: `python3 Comment_Tracker/check_section.py "ICON_AI v3 Shortened.docx"`. It should report **0** for passes 1, 2, 3, 4 and 7. Bold hits on table captions are fine.
3. Then decide on A and B.
