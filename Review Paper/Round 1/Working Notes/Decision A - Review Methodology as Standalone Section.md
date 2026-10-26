# Decision A — move the review methodology out of Section 1

**Date:** 11 Sept 2026
**For:** `ICON_AI v3 Shortened.docx`

---

## Why do this

Right now your review methodology is two sentences sitting inside Section 1.

Moving it out does three things at once:

1. **Section 1 gets shorter.** That is Dr. Ho's new instruction.
2. **You answer a comment he made in Round 1 and you have never closed.** R1 68: *"It feels weird to have only 1 subsection within a section… perhaps you can make it a standalone section, 2. Review Methodology?"*
3. **You close ten more of his Round 1 comments** in one go. R1 68 to R1 78 all landed on this exact material. They are still open because the material was deleted, not fixed.

For a review paper this is also the part a reviewer looks for first. Without it, the paper reads like an essay.

You have room. The paper is 11 pages. The limit is 20.

---

## Step 1 — Delete this from Section 1

Delete the whole paragraph that sits between your three contributions and the roadmap:

> The literature examined here was identified through searches of the ACL Anthology, IEEE Xplore, and Scopus, combining terms for the language variety, the sentiment task and annotation quality. Studies that only benchmark classifiers, with no annotation or reliability component, were not included.

Section 1 now ends with the roadmap paragraph. That is the right place to end it.

---

## Step 2 — Add this as the new Section 2

Put it right after Section 1. Use **Heading 1** style, same as your other section headings.

Do **not** add any subsections. Rule 14: never one subsection alone.

---

### 2. Review Methodology

The studies reviewed here were found through structured searches of the ACL Anthology, IEEE Xplore and Scopus. Each search combined three groups of terms. The first group named the language variety, and included code-mixed, code-switching, Manglish, Bahasa Rojak and Malay-English. The second group named the task, and included sentiment analysis, polarity and opinion mining. The third group named the object of interest, and included corpus, annotation, inter-annotator agreement and label quality.

The search covered work published between 2019 and 2026. Earlier work was added by following citations from the papers retrieved. The date limit was not applied to work on inter-annotator agreement, because the agreement measures discussed in this review were published before 2019.

Four criteria were used to determine inclusion. A study had to (1) address Malaysian Malay-English code-mixed text, or provide annotation or reliability methods that can be applied to it; (2) describe how its labels were produced and checked; (3) appear in a peer-reviewed journal or conference; and (4) include an annotation or reliability component. Preprints without a peer-reviewed version were not used.

The fourth criterion sets the scope of this review. Studies that only measure classifier accuracy on an existing corpus were excluded. Those studies treat the existing labels as correct, while this review asks whether the labels can be shown to be reliable.

---

**That is 218 words.** About half a page.

---

## Step 3 — Renumber

Only three places in the whole paper mention a section number. I checked.

**a. The roadmap at the end of Section 1.** Replace it with:

> Section 2 describes how the literature was selected. Section 3 examines linguistic challenges for annotation. Section 4 compares labelling approaches and their limitations. Section 5 assesses reliability evidence. Section 6 explains how these challenges interact and proposes research priorities, and Section 7 concludes.

**b. The opening of Research Priorities.** Change:

> Section 5.1 first sets out how the challenges described in Sections 2 to 4 interact.

to:

> Section 6.1 first sets out how the challenges described in Sections 3 to 5 interact.

**c. Section 2.3 says "As discussed in Section 1".** No change needed. Section 1 stays Section 1.

**Then renumber the headings:**

| Old | New |
|---|---|
| 2. Linguistic Challenges for Annotation | **3.** |
| 2.1 / 2.2 / 2.3 | **3.1 / 3.2 / 3.3** |
| 3. Annotation Approaches and Their Limitations | **4.** |
| 3.1 / 3.2 / 3.3 | **4.1 / 4.2 / 4.3** |
| 4. Evaluating Annotation Reliability | **5.** |
| 5. Research Priorities | **6.** |
| 5.1 to 5.5 | **6.1 to 6.5** |
| 6. Conclusion | **7.** |

Table 1 and Table 2 keep their numbers.

---

## What this new section fixes

Eleven of his Round 1 comments. All were left open when the text was cut.

| Comment | What he asked | How the new section answers it |
|---|---|---|
| **R1 68** | One subsection alone is weird. Make it a standalone section. | It is now Section 2. No subsections. |
| **R1 69** | *"Avoid writing sentences by including contents in brackets."* | The search terms are written into full sentences. No bracket lists. |
| **R1 70** | arXiv preprints are risky. Use peer-reviewed sources. | Criterion 3 says peer-reviewed. One more sentence says preprints were not used. |
| **R1 71** | Fix the bracketed term list | Same as R1 69. |
| **R1 72** | Fix the bracketed term list | Same as R1 69. |
| **R1 73** | *"This part lacks clarity."* (the "apparatus Section 5 examines" sentence) | Rewritten in plain words: the measures were published before 2019. |
| **R1 74** | *"This part also lacks clarity."* ("cannot be cited from within it") | That clause is gone. |
| **R1 75** | Use **"Four criteria were used to determine inclusion."** | His exact sentence, word for word. |
| **R1 76** | The semicolon sentence is too dense. Use **"(1) …; (2) …; (3) …; and (4) …"** | His exact format. |
| **R1 77** | Remove this | Removed. |
| **R1 78** | *"the final part of 'it can be' feels incomplete"* | The sentence now finishes: *"…whether the labels can be shown to be reliable."* |
| **R2 54** | No arXiv preprints. Treat as absolute. | Stated directly. |

---

## Three things to watch

**1. You now have two lists called "four criteria".**

- Section 1: four criteria a good *resource* would need
- Section 2: four criteria for *including a study*

He warned about running two enumerations at once (R4 37) and about one name for two things (R4 58).

They sit in different sections and the word "inclusion" separates them. But to be safe, make Section 1 say:

> A general-purpose resource would need to meet **four criteria for a usable resource**: a scale of at least ten thousand labelled messages…

Do **not** change "satisfies some of these criteria but not all of them". Those are his exact words from R4 42.

**2. The criteria sentence is 47 words.** That is over his 35-word limit. It is fine here, because the numbered list format is what he asked for at R1 76. Your checker script says the same: *"a numbered list may legitimately run long."*

**3. Optional — add how many studies you kept.** Something like *"Twenty-eight studies met these criteria."* Only add this if you can state the real number. Do not guess. He checks.

---

## Honest note on balance

This helps, but it does not fix the balance on its own.

| | Now | After this change |
|---|---:|---:|
| Section 1 share of body | 31.6% | about 28.5% |
| Body words | 3,119 | about 3,290 |

Section 1 is still the longest section. Section 4 is still only 8.7%.

If Dr. Ho's real concern is balance, the bigger win is to grow the thin sections. Section 4 (Evaluating Annotation Reliability) is 271 words and carries your main argument. Section 2 (Linguistic Challenges) is 367 words.

Growing Section 4 also gives you somewhere to put the two or three extra references you still need. That solves Decision B at the same time.
