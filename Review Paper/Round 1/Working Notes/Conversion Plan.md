# Chapter 2 → Review Paper: Conversion Plan

**Scope decision:** narrowed review focused on *corpus construction and annotation* for Malaysian code-mixed sentiment, framed as **review + proposed framework**. RQ2 (multilingual vs. monolingual evaluation) is cut from the paper and stays in the thesis.

**Target venue format:** ICON AI 2026 template — A4, Times New Roman 12pt, single-spaced, margins 3.3 / 3.65 / 2.03 / 3.05 cm.

### Submission regulations — verified against the call for papers

Source: <https://fai.utm.my/iconai2026/paper-submission/>

| | |
|---|---|
| Maximum length | **20 pages for review papers, references included** (16 pages for all other types) |
| Minimum length | **8 pages** — shorter manuscripts are rejected immediately, without review |
| Accepted types | Full Papers, **Review Papers** |
| Submission system | Microsoft CMT — <https://cmt3.research.microsoft.com/ICONAI2026> |
| Peer review | At least 2 independent academic reviewers, to international standards |
| Publication | MyCite journal; selected papers to a Scopus-indexed journal for additional fees |
| Conference dates | 12–14 November 2026, UTM Kuala Lumpur (co-located with ICDSAI 2026) |
| Contact | icon-ai@utm.my |

**The template file's own "15 pages" line is wrong** — stale text carried over from a SERSC/OIJI journal template (the file metadata still names SERSC). The call for papers governs. Its *formatting* specifications remain authoritative.

**Submission deadline: 31 August 2026**, per Dr. Ho. Not published on the conference website, so this is the supervisor-sourced date and the schedule is built on it.

**Reference guidance from Dr. Ho (11 Aug):** aim to exceed 50 entries, but *after* revision is complete and only if time allows. Do not chase references during drafting.

**Verified budget:** a mock layout at the word counts, tables, figure, and 65 references (8pt) below renders to **19 pages** in the actual template — 1 page of margin under the cap.

---

## 1. Working title

> **Annotating Malaysian Code-Mixed Social Media Text for Sentiment Analysis: A Critical Review and a Heterogeneous Consensus Framework**

Alternatives if the above runs long:
- *From Discard to Adjudicate: A Critical Review of Annotation Strategies for Malaysian Code-Mixed Sentiment*
- *Beyond Majority Voting: Annotation Reliability for Bahasa Rojak Sentiment Corpora*

The title should name **annotation** explicitly. That is what distinguishes this from the many existing code-mixed sentiment surveys.

---

## 2. Page distribution (19.25 planned, 20 cap)

Uses Dr. Ho's original section headings unchanged.

| Section | Pages | Prose words | Table / figure |
|---|---|---|---|
| Title | 0.5 | — | — |
| Abstract + keywords | 0.5 | 300 (10pt) | — |
| Introduction *(incl. review methodology subsection)* | 1.75 | 800 | Table 1 — search strategy |
| Malaysian code-mixed language characteristics | 1.5 | 700 | — |
| **Corpus construction and annotation** | **5.5** | 2,850 | Table 2 — annotation taxonomy · Table 3 — voter composition |
| Evolution of sentiment analysis models | 1.25 | 600 | — |
| Evaluation practices | 1.25 | 600 | — |
| Critical discussion | 3.75 | 1,350 | Table 4 — synthesis matrix · Figure 1 — pipeline |
| Conclusion | 0.75 | 350 | — |
| References (8pt, ~65 entries) | 2.5 | — | — |
| **Total** | **19.25** | **~7,250** | 4 tables + 1 figure |

Verified: renders to **19 pages** in the template.

**Where the extra pages went.** Not spread evenly. The bulk went to *Corpus construction and annotation* (5.5 pages, up from 3.75 under the old 15-page assumption) — it is the paper's core under the narrowed scope. *Critical discussion* grew to 3.75 to carry a fuller synthesis matrix and the proposed framework. *Malaysian code-mixed characteristics* and *Evolution* were restored from the over-compressed state they were in at 15 pages.

**Release valves** if you run over: *Evolution* (cut to 0.75), *Evaluation practices* (cut to 0.75), *Malaysian code-mixed characteristics* (cut to 1.0). Do not cut *Corpus construction and annotation* — it is the paper.

### Measured layout constants

Established by rendering test documents in the actual template — use these instead of estimating:

- One full page holds **~537 words** of body prose (12pt, single-spaced)
- References at 8pt: **26 entries per page** (18 at 10pt, ~11 at 12pt)

### Reference font: 8pt — mandated by the template

The template's references section states: *"The references should be typed in single spacing, **8-font size**, Times New Roman."* This is not a choice, and it is more generous than assumed earlier in planning.

Measured in the template: **26 references fit on one full page at 8pt** (versus 18 at 10pt and ~11 at 12pt). Dr. Ho's 50+ target therefore costs only ~2 pages, and even 80 entries would fit in ~3.1 pages.

Since references are being added *after* revision per Dr. Ho, hold the 2.5-page reference budget from the first draft even while the list is still ~30 entries, so adding more later does not reflow the body.

### Other template rules worth noting

- **"No footnotes are allowed"** — stated in the references section. Note this contradicts §9, which describes footnote formatting at 9pt. Follow the stricter reading and avoid footnotes entirely, with the single exception of the corresponding-author asterisk, which the template explicitly requires at the footnote position on page 1 (10pt).
- Abstract: 10pt, italicised, fully justified, ≤300 words. The word "Abstract" is 10pt bold, centred.
- Main text: 12pt, single-spaced, fully justified, paragraphs indented 0.43 cm, no blank lines between paragraphs.
- First-order headings 13pt bold; second- and third-order 12pt bold. One blank line before and after.
- Table captions 12pt space above the table; figure captions 6pt below the figure.

---

## 3. Section-by-section mapping from Chapter 2

> **The job changed when the limit went from 15 to 20 pages.** Under the old assumption this was a compression exercise. It is not. Chapter 2's body is ~6,330 words; the paper needs ~7,250. The core section *expands* by roughly 1,200 words. Trim the periphery, but expect to write new material in Sections 3 and 6.

Headings below are Dr. Ho's.

### 1. Introduction — 800 w (600 + 200 subsection) + Table 1
Written fresh; only the ~257-word Chapter 2 preamble is reusable.

Must contain, in order: the Malaysian code-mixed sentiment problem; why annotation specifically is the bottleneck rather than model capacity; the scope of this review; an explicit statement of contributions.

State three contributions plainly:
1. A taxonomy of annotation strategies for low-resource code-mixed text along a fidelity–scalability axis.
2. A diagnostic account of neutral-label skew separating *structural* from *ambiguity-driven* causes.
3. A proposed heterogeneous consensus framework addressing the gaps identified.

**Subsection 1.1 — Review methodology (200 w + Table 1).** Does not exist in Chapter 2; write from scratch. Reviewers of review papers expect it, and its absence is a common desk-reject trigger. Table 1 covers databases searched (ACL Anthology, IEEE Xplore, Scopus, arXiv), search strings, date window (suggest 2019–2026), inclusion/exclusion criteria, and paper counts at each stage. Keep prose short — the table does the work.

### 2. Malaysian code-mixed language characteristics — from 2.1 (974 → 700 w)
Light trim, and **reframe**. Chapter 2 argues these features break *modelling*; the paper must argue they break *annotation*.

- **Keep:** intrasentential switching leaves no structural cue for segmentation; particles (*lah*, *kan*) carry affective weight but sit in neither lexicon; phonetic spelling generates OOV; the *institut kanser* example.
- **Trim:** the Muysken typology exposition and the SVO/inflectional-morphology explanation to a sentence each. At 20 pages these survive — they were only being cut for space.
- **Add** one sentence per feature connecting it to *annotator disagreement*, not just tokeniser failure.

### 3. Corpus construction and annotation — from 2.2 (1,628 → 2,850 w) + Tables 2, 3
**The core of the paper, and where the new writing goes.** Three subsections mirroring 2.2.1–2.2.3.

**3.1 Annotation strategies and trade-offs** (from 2.2.1, 495 → 950 w + Table 2)
- Three tiers preserved: manual → semi-automated → fully automated (generative).
- Table 2 formalises them: *Tier | Representative work | Fidelity | Scalability | Contextual robustness | Dominant failure mode*.
- Retain Kong et al. (11,568 tweets), Mohd Shamsuddin et al. (229,566 pool), Negi et al., Jadhav et al. (10.2% / 14.1%).
- **New material needed:** more works per tier. Chapter 2 carries one or two exemplars each, which is thin for a review. Add crowdsourcing quality-control literature to the manual tier and weak supervision / active learning to the semi-automated tier.
- Close on complementarity — this sets up 3.3 and Section 6.

**3.2 Neutral-label skew** (from 2.2.2, 489 → 900 w)
- The 78.23 / 16.33 / 5.44 distribution as headline evidence.
- The two-mechanism split (structural lexicon default vs. genuine ambiguity) is your most original analytical move — give it the room it now has.
- Minority-class erosion argument retained.
- **New material needed:** evidence of the same skew pattern from other low-resource or code-mixed corpora, to show it is a general failure mode rather than one corpus's accident.

**3.3 Consensus and disagreement** (from 2.2.3, 644 → 1,000 w + Table 3)
- Keep the **discard → stabilise → adjudicate** axis. It is the paper's best organising device; signpost it in the abstract and introduction.
- Table 3 = existing Table 2.2.3 (voter composition), unchanged.
- Keep the 1-1-1 tie / dataset attrition argument in full — the sharpest critique in the chapter.
- Keep Niimi (2024), Negi et al. (2026), Ahtisham et al. (2026).
- **New material needed:** ensemble and adjudication literature from outside the regional context to give the axis more than three data points.

### 4. Evolution of sentiment analysis models — from 2.3 (1,427 → 600 w)
Demoted to context, but less brutally than the 15-page plan required.

- **Cut:** 2.3.1 classical ML baselines.
- **Keep, compressed:** encoders are reliable but cannot reason about unseen slang; LLMs reason but trail fine-tuned transformers on low-resource languages; the Jadhav et al. figures; one line on multilingual pretraining under-representing Malay (this saves Conneau and Adilazuarda).
- Frame as "what the candidate annotators can and cannot do," not a history of NLP.

### 5. Evaluation practices — from 2.4 (923 → 600 w)
More survives than under the 15-page plan.

- **Keep:** inter-rater reliability — Cohen's / Fleiss' Kappa, Landis & Koch thresholds, and the prevalence paradox (Feinstein & Cicchetti; Gwet's AC1). This is annotation reliability measurement and is directly on-topic.
- **Keep, condensed:** 2.4.2's evidence that no existing regional corpus is simultaneously large-scale, polarity-balanced, casually authentic, and human-validated.
- **Cut:** Macro-F1 and the accuracy paradox (Sokolova & Lapalme) — RQ2 material.

### 6. Critical discussion — from 2.5 (902 → 1,350 w) + Table 4 + Figure 1
Absorbs both the synthesis and the proposed framework.

- Table 4 = existing Table 2.5.1 synthesis matrix. **Add rows** — at 20 pages there is room, and a six-row matrix is thin for a review.
- Keep **Gap 1** (fidelity–scalability) and **Gap 2** (architectural silos). **Cut Gap 3** — RQ2 material.
- **Proposed framework** (~650 w of the 1,350), from 2.2.3's closing plus 2.5.2's "Addressing the gaps":
  - Figure 1: fine-tuned multilingual encoder + generative LLM → consensus → adjudication → human-in-the-loop validation. Budget half a page.
  - State the three jointly-necessary properties (complementary voters, reasoning-based adjudication, human anchoring) and show the figure satisfies each.
  - **Present it as a proposed framework motivated by the review, not as validated work.** No model names, hyperparameters, or results.

### 7. Conclusion — from 2.6 (218 → 350 w)
Rewrite for a standalone paper — remove all "Chapter 3 details…" thesis scaffolding. End on open problems for the field, not on your project plan.

### Cut entirely
- 2.3.1 classical ML baselines (400 w)
- 2.4.1 Macro-F1 / accuracy paradox (~370 w of 491)
- 2.5.2 Gap 3 (~150 w)
- All RQ1/RQ2 cross-references and thesis-internal section pointers

### Word budget summary

| | Words |
|---|---|
| Chapter 2 body available | ~6,330 |
| Paper prose target | ~7,250 |
| Cut from Chapter 2 | ~1,800 |
| Genuinely new writing required | **~2,350** |

The new writing concentrates in the Introduction (800), Section 3 (~1,200) and Section 6 (~450).

---

## 4. References

Chapter 2 list: **33**. Not all of them carry over — the narrowing kills references that appear only in cut sections. Citation-traced audit below.

### Carry over — 22

**Core (17):** Lim et al. (2021) · Maskat et al. (2024) · AlAfnan et al. (2025) · Treffers-Daller et al. (2022) · Mohd Shamsuddin et al. (2024) · Kong et al. (2023) · Gilardi et al. (2023) · Negi et al. (2026) · Jadhav et al. (2025) · Raees & Fazilat (2024) · Selvaraju et al. (2024) · Chakravarthi et al. (2022) · Ahtisham et al. (2026) · Niimi (2024) · Manukonda & Kodali (2025) · Romadhona et al. (2022) · Kasmuri & Basiron (2019)

**Annotation reliability (5)** — the surviving half of 2.4.1: Cohen (1960) · Fleiss (1971) · Landis & Koch (1977) · Feinstein & Cicchetti (1990) · Gwet (2008)

### Drop — 5

| Reference | Sole location | Why it goes |
|---|---|---|
| Mulianingrum (2025) | 2.3.1 only | 2.3.1 cut entirely |
| Wadhawan (2021) | 2.3.1 only | 2.3.1 cut entirely |
| Devlin et al. (2019) | 2.3.2 only | Generic BERT citation; encoder discussion compressed to one claim |
| Brown et al. (2020) | 2.3.3 only | Generic GPT-3 citation |
| Sokolova & Lapalme (2009) | 2.4.1 only | Supports Macro-F1 / accuracy paradox = RQ2 material |

### Judgment calls — 6

| Reference | Location | Decision hinges on |
|---|---|---|
| Conneau et al. (2020) | 2.3.2 + Gap 3 | Whether you keep one line on multilingual pretraining limits |
| Adilazuarda et al. (2022) | 2.3.2 + Gap 3 | Same line — Malay under-representation in pretraining |
| Muysken (2013) | 2.1.1 only | Whether the typology exposition survives the cut to 1.0 page |
| Mamta et al. (2023) | 2.1.2 only | How hard 2.1.2 is condensed |
| Maskat et al. (2020) | 2.1.2 only | How hard 2.1.2 is condensed |
| Khalip (2025) | 2.1.2 + 2.3.3 | Both locations compressed |

**Recommendation:** keep one sentence noting that multilingual pretraining under-represents Malay. It saves Conneau and Adilazuarda, and it belongs in the narrowed paper anyway — models used *as annotators* inherit that weakness, which is an annotation argument, not an evaluation one.

### Net position

**Revised upward now that the limit is 20 pages.** At 15 pages the judgment-call references were going to die of compression. With *Malaysian code-mixed characteristics* restored to 1.5 pages and *Evolution* to 1.25, five of the six survive — Conneau, Adilazuarda, Muysken, Mamta, Maskat (2020) and Khalip all have room again. Devlin may also return if the encoder discussion is written out properly.

Realistic carry-over: **~29–31 of 33**. Only the drops tied to genuinely cut material stay out: Mulianingrum, Wadhawan (2.3.1, cut entirely) and Sokolova & Lapalme (Macro-F1, RQ2 material).

To exceed Dr. Ho's target of 50, you need **~20 new references** — but per his instruction, that happens after revision, not during drafting.

Note the drops cluster almost entirely in the model-architecture literature — which is exactly what the narrowing demoted. That is a good coherence signal, but it also means your surviving base is thin in the one area the paper is now about. The additions must be annotation-specific:

- Crowdsourcing and annotation quality control
- LLM-as-annotator literature beyond Negi et al. and Gilardi et al.
- Weak supervision / programmatic labelling (e.g. Snorkel-style approaches)
- Active learning for low-resource annotation
- Annotation guideline design and inter-annotator agreement methodology
- Additional Southeast Asian code-mixed corpus papers

Template requirements: numbered, cited as `[n]` in order of appearance, **all author names spelled out** — no "et al." in the reference list. This makes entries long; the 10pt setting compensates.

**Space check on the carry-over set:** even the reduced ~24 references occupy ~2.2 pages at 12pt, still well above the 1.5 originally allocated. The case for enlarging the reference budget holds regardless of how the judgment calls go.

---

## 5. Revised timeline (11 → 31 August)

Your original schedule had Introduction due 8 Aug and Evolution+Evaluation due 11 Aug with nothing started, so it was three tasks behind on day one. It also assumed 1-day supervisor turnaround across four review rounds. This version assumes 2-day turnaround and three rounds.

| Dates | Task |
|---|---|
| 11–12 Aug | Finalise outline; run and **document** the literature search; collect ~15 new references |
| 13–14 Aug | Draft Sections 3 and 4 + Table 2 |
| 15–16 Aug | Draft Sections 5 and 6 + Table 3 |
| 17 Aug | Draft Sections 7 and 8 + Table 4 |
| 18 Aug | Draft Section 9 + Figure 1 |
| 19 Aug | Draft Sections 1, 2, 10 + abstract and keywords |
| 20 Aug | Self-review; format into template; **check page count** |
| 21 Aug | Send to Dr. Ho — Round 1 |
| 22–24 Aug | Revision |
| 25 Aug | Send — Round 2 |
| 26–28 Aug | Revision |
| 29 Aug | Send — Round 3 (light pass) |
| 30 Aug | Final revision, proofread, reference check, copyright form |
| 31 Aug | Submit |

**Act on this now:** message Dr. Ho with the three review dates (21, 25, 29 Aug) so the turnaround is agreed in advance. The schedule fails if a round slips.

---

## 6. Open items to confirm

1. **Verify the template against the actual ICON AI 2026 call for papers.** The file's metadata says SERSC and the body text refers to *OIJI*, which suggests a reused journal template. Confirm the page limit, the review category, and the deadline.
2. **Confirm 10pt references are acceptable.** The budget depends on it; at 12pt you lose roughly a page.
3. **Confirm with Dr. Ho that publishing the proposed pipeline before results is acceptable**, and check authorship order.
4. **Copyright release form** — the template requires a completed, signed form at submission. Obtain it early.
