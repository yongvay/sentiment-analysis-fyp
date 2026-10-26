# Project context

Final Year Project — **sentiment analysis of Malaysian code-mixed social media text** (Manglish / Bahasa Rojak).

- **Student:** Ng Yong Vay
- **Supervisor:** Dr. Ho

Two research questions drive the thesis:

- **RQ1** — corpus construction and annotation: how to build a large, polarity-balanced, human-validated Manglish sentiment corpus.
- **RQ2** — evaluation: how multilingual transformers compare with monolingual baselines on Malaysian code-mixed text.

## Folder map

| Path | Contents |
|---|---|
| `C1/` | Chapter 1 — refined draft plus Dr. Ho's commented PDF |
| `C2/` | Chapter 2 literature review — refined draft, reviewed PDF |
| `C3/` | Chapter 3 — methodology skeleton (early) |
| `Review Paper/` | ICON AI 2026 conversion — see below |
| `Proposal/` | Approved project proposal |
| `Direction Plan/` | Project direction planning documents |
| `References/` | Source PDFs, including `References/C2/` for Chapter 2 |
| `Training Datasets/`, `Target Dataset/` | Corpus data |
| `FYP1/` | University forms, rubrics, report templates, exemplar papers |
| `FYP 1.docx` | Main assembled report |

## Two active workstreams

1. **Thesis** — Chapters 1–3 (Chapter 3 methodology is the open one). Both RQs live here.
2. **Review paper** — converting Chapter 2 into a standalone paper for ICON AI 2026. Narrower scope than the thesis; see below.

Keep them separate. Decisions made for the paper do not automatically apply to the thesis — most notably, **RQ2 is cut from the paper but stays in the thesis**.

---

# Current workstream: Chapter 2 → ICON AI 2026 review paper

Working plan: **`Review Paper/Conversion Plan.md`** — read it before doing any work on the paper. This section is a summary; that file is authoritative.

*(This section is temporary. Once the paper is submitted, replace it with whatever the next workstream is.)*

## Key dates

- **Submission deadline: 31 August 2026** (per Dr. Ho; not published on the conference website)
- Conference: 12–14 November 2026

## Venue essentials

Source: <https://fai.utm.my/iconai2026/paper-submission/> (fetched 13 Aug 2026). Full regulations, formatting specs and measured layout constants are in the Conversion Plan.

- 2nd International Conference on Artificial Intelligence and Its Applications, Faculty of AI, Universiti Teknologi Malaysia, Kuala Lumpur
- **Page limit: 20 pages for review papers, references included.** Minimum 8 pages
- Submission via Microsoft CMT; peer review by ≥2 independent reviewers
- Template: `Review Paper/Template ICON AI 2026.docx`

**The template file contradicts itself and is partly stale.** Its body text says reviews are capped at 15 pages — that is wrong, carried over from a SERSC/OIJI journal template. The call for papers governs: 20 pages. Its *formatting* specs remain authoritative (notably: body 12pt, **references 8pt**, no "et al." in the reference list). When the template and the call for papers disagree, the call for papers wins.

## Decisions taken

- **Scope narrowed** to corpus construction and annotation. RQ2 is cut from the paper, retained in the thesis.
- **Framing:** review. Closes by proposing a heterogeneous tri-model consensus pipeline as the conclusion of the review — stated as *requirements*, not methodology. No model names, hyperparameters, or results.
- **Section headings follow Dr. Ho's original outline**; only the page weights changed.
- **References at 8pt** as the template mandates — at 26 entries per page, Dr. Ho's 50+ target costs only ~2 pages.
- **Dr. Ho's instruction (11 Aug):** proceed with drafting; expand the reference list past 50 *after* revision is complete, only if time allows. Do not chase references during drafting.
