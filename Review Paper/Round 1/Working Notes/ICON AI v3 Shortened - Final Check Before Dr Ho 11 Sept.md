# ICON AI v3 Shortened — final check before sending to Dr. Ho

**Date:** 11 Sept 2026
**File:** `ICON_AI v3 Shortened.docx`
**Verdict: fix two things, then send.** Both are small. About five minutes.

---

## The numbers

| | Result |
|---|---|
| Pages | 11 (limit 20, minimum 8) |
| Body words | 3,307 |
| References | **38** (he asked for at least 40) |
| References not cited anywhere | **0** |
| arXiv preprints | **0** |
| Rule 16 breaches (same source, two sentences in a row) | **0** — I checked all 223 sentences, including across paragraph breaks |
| Sentences over 35 words | 2, and both are numbered lists (allowed) |
| Mean sentence length | 15.3 words |
| Bold in body prose | 0 (the 11 checker hits are all table captions and table headers) |
| Parenthetical cross-references | 0 |

---

## Must fix before sending

### 1. A section number was missed during renumbering

In the opening of Section 6 (Research Priorities):

> The reviewed studies leave uncertainty about how labels were produced and checked. Section 6.1 first sets out how the challenges described in **Sections 2 to 4** interact.

"6.1" was updated, but "Sections 2 to 4" was not. The three challenges now live in Sections 3, 4 and 5.

**Find:** `described in Sections 2 to 4 interact`
**Replace:** `described in Sections 3 to 5 interact`

### 2. Reword the criteria sentence in Section 1 — my mistake

I gave you a bad guard phrase. It repeats "resource" three times in one sentence.

**Now:**
> A general-purpose **resource** would need to meet four criteria for a usable **resource**: a scale of at least ten thousand labelled messages…

**Change to:**
> A usable general-purpose resource would need to meet four criteria: a scale of at least ten thousand labelled messages; a label distribution not dominated by one class; everyday social-media text; and direct evidence of annotation reliability.

Keep the next sentence exactly as it is. "Each of the four satisfies some of these criteria but not all of them" is his own wording from R4 42.

The semicolons also separate this list clearly from the inclusion criteria in Section 2.

---

## Worth fixing, but not a blocker

### 3. You are at 38 references. He asked for at least 40 (R1 80)

Removing Coluzzi was the right call — every reference now does a job, and an uncited reference looks worse than a missing one.

But you are two short of what he asked for.

**Do not pad.** Two options:

- Add two sources that do real work. The natural slot is Section 5, which is only 271 words and carries your main argument. You write there: *"Studies with more than two annotators should therefore name the coefficient used."* A source for a multi-annotator agreement measure would fit naturally.
- Or tell him plainly in your email: *"I am at 38 references. I removed one that was no longer cited. I am working towards 40."* Being open about a known gap is a stronger position than padding the list.

### 4. Two blank paragraphs before the Section 3 heading

Every other section has one. Delete one of them.

---

## Leave these alone

The checker will keep flagging them. Each one is fine.

- **"the statistic used"** (pass 4) — these are Dr. Ho's own words from R4 48.
- **11 bold hits** (pass 6) — all table captions and table header cells. His bold comments were about body prose, not tables.
- **Three "claim word" hits** (pass 3) — I checked each one. All false alarms:
  - *"Section 2 describes how the literature was selected"* — this means your own review, not the field.
  - *"how often this occurs"* — part of a question, not a claim.
  - *"most retained posts"* — the numbers are right there in Table 1.
- **Two sentences over 35 words** — both are numbered or semicolon lists. R1 76 is where he asked you to use that format.

---

## Section balance

| Section | Words | Share |
|---|---:|---:|
| 1. Introduction | 956 | 28.9% |
| 2. Review Methodology | 218 | 6.6% |
| 3. Linguistic Challenges | 367 | 11.1% |
| 4. Annotation Approaches | 725 | 21.9% |
| 5. Evaluating Annotation Reliability | 271 | 8.2% |
| 6. Research Priorities | 636 | 19.2% |
| 7. Conclusion | 134 | 4.1% |

Section 1 has come down from 31.6% to 28.9%. That is real progress.

Section 5 is still the thin one at 8.2%. It carries your central argument about Cohen's κ, so it is the section a reviewer will weigh most. Growing it is the next thing to do after this round, and it solves the reference count at the same time.

---

## What has been closed

Over the two rounds of edits today, this draft closed:

- **All nine** conflicts found in the first check
- **Eleven** Round 1 comments that reopened when Section 1 was cut (R1 68 to R1 78), through the new Review Methodology section
- **R2 54** — no preprints, stated directly
- **One wrong citation** — Doğruöz et al. (2021) was being used for "model architecture", which that paper never claims

Your reference list is now clean: 38 sources, all cited, all peer-reviewed.
