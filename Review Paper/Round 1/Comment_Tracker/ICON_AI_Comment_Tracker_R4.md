# Dr. Ho — Round 4 comment tracker

**Document reviewed:** `ICON AI 2026 - Section 1 (reviewed).pdf` (6 pages)
**Comments:** **60**, extracted from the PDF annotation layer, not retyped
**Pages annotated:** 1, 2, 3 and 4 — **all 60 are in Section 1, the Introduction**
**Date received:** 29 August 2026
**Revision produced:** `ICON AI 2026 - Section 1 (v15).docx` and
`Template ICON AI 2026 - Section 1 to 7 (v15 Section 1 revised).docx`

> **v14 was built first and did not survive its own check.** Part 3 records the eleven defects found in it
> and how v15 fixes them. Read Part 3 before Part 1.

---

# Part 0 — What this round actually says

## The count went up, but the Introduction got longer

| | R1 | R2 | R3 | **R4** |
|---|---|---|---|---|
| Comments | 80 | 64 | 35 | **60** |
| Words of Introduction reviewed | ~1,100 | ~1,000 | ~1,050 | **~1,770** |
| Comments per 100 words | — | — | ~3.3 | **~3.4** |

The rate is flat. Round 3's Introduction was rewritten into Round 4's, adding 700 words in the process —
which is exactly what Round 3 asked for, since his own replacement wordings ran longer than yours. More
words meant more surface for him to comment on, at the same density. **This is not a regression, but it is
not progress either.**

## He supplied the replacement wording twelve times

That is 20 per cent of the round, and it is the most useful thing in it. Every one has been used verbatim.

| # | Your wording | His replacement |
|---|---|---|
| 1 | Two sentences both citing Joshi et al. (2020) | "Joshi et al. (2020) **highlight** that only a small number of the world's languages are represented in current language technologies, **with** lexicons, pre-trained models and benchmark corpora concentrated in those few languages." |
| 5 | **Each** of these resources **is built for one language** | "**Many** of these resources **are developed primarily for individual languages**…" |
| 16 | *Manglish* **weakens** standard English and Malay | **"having a negative effect on"** |
| 18 | Its structure, however, is **not random** | "Its structure, however, is **systematic rather than random**." |
| 19 | The same **regularity** appears at the level of spelling | "The same **systematicity** appears at the level of spelling…" |
| 20 | …**which indicates that the variation is systematic rather than arbitrary** | "…**This categorization suggests that the variation follows recurring patterns rather than occurring arbitrarily**…" |
| 22 | Tools **therefore treat** them as OOV items | "…**may therefore**…" |
| 24 | **The conventions Malaysian writers follow** are consistent | "**These writing conventions are consistent within the observed variation**…" |
| 30 | Another source of difficulty **does not originate in the model itself. It originates one step earlier**, at the point where **the labels** are created | "Another source of difficulty **arises one step earlier**, at the point where **sentiment labels** are created." |
| 34 | …and Frénay and Verleysen (2014) **report that the accuracy of predictions may decrease as a result** | "…**which can reduce predictive accuracy** (Frénay & Verleysen, 2014)." |
| 41 | **validated by** human annotators | "**with annotation reliability assessed by** human annotators" |
| 42 | **secures some of these properties at the expense of the others** | "…**satisfies some of these criteria but not all of them**…" |
| 45 | The second and third findings **describe one condition rather than two** | "**The second and third findings are closely related rather than independent.**" |
| 48 | the statistic **stops being informative** | "…**can make the statistic used to assess the labels more difficult to interpret**." |
| 56 | …and shows that each tier **gains either label fidelity or scalability at the expense of the other** | "…and **examines the trade-off between label fidelity and scalability across them**." |

Read the right-hand column as a set. Every one **adds a hedge** (*many*, *may*, *suggests*, *can*), or
**replaces a metaphor with the literal relationship**, or **says what a thing is rather than what it is
not**. That is the register. It has not changed since Round 3; it has only been demonstrated more times.

## Four rules are new this round

| Rule | Comment | What it says |
|---|---|---|
| **16** | 1 | Do not cite the same source in two consecutive sentences. Merge them. |
| **17** | 13 | Do not tell the reader what the paper is doing inside a paragraph. |
| **18** | 40 | Give evaluative adjectives (*large*, *comprehensive*) an operational definition. |
| **19** | 58 | Use one term per concept for the whole paper. |

Rule 16 is the interesting one, because it is a defect *caused by* following Rule 2 for three rounds. He
asked for citations 39 times; the draft answered by citing everything; now the citations themselves impede
reading.

## The single largest category: fifteen comments asking what a word points at

*effect* of what · *one variety* of what · *such mixed writing*, which writing · *in part*, how ·
*regarded*, how · *technical difficulty*, which · *the same regularity*, which · *they*, who ·
*that reading*, of what · *the problem*, which · *coefficient*, which · *large*, how large ·
*regionally adapted*, how · *carry an assumption*, which assumption · *code-switched*, never named

This is the habit to watch in Sections 2 to 7. It is not vocabulary and it is not sentence length. **It is
writing a noun phrase that stands in for something the reader has to reconstruct**, and doing it once every
hundred words or so.

---

# Part 1 — All 60 comments and what changed

Comment text is verbatim. Highlighted text is reconstructed from the PDF annotation geometry.

> **The "What changed" column records the v14 fix.** Fifteen of these sentences were revised again in v15,
> for reasons given in Part 3 — the v14 wording had introduced fresh breaches of his own rules. Where the
> two differ, **the shipped wording is v15**, and the .docx is the authority.

## Page 1 — the opening paragraph (comments 1–7)

| # | His point | What changed |
|---|---|---|
| 1 | Same source cited in two consecutive sentences. He supplied the merged sentence. | **(his wording, verbatim)** The two Joshi et al. (2020) sentences are now one. The same fix was applied unprompted to the two Doğruöz et al. (2021) sentences, the two Coluzzi (2017) sentences and the two Maskat and Rahman (2020) sentences. |
| 2 | "carry an assumption" — a reader may ask what assumption | Named in place: "the tools used for this task **assume that their input is written in one standard language**." |
| 3 | Add "However" to signal the move from usefulness to limitation | Added. |
| 4 | The definition of *pre-trained model* needs a citation, and arrives abruptly | Cited to **Devlin et al. (2019)**, a new reference. Linked back to the resource list with "Among these resources, a pre-trained model is…" so it reads as a continuation rather than a new topic. |
| 5 | "Each of these resources is built for one language" is too absolute | **(his wording)** "Many of these resources are developed primarily for individual languages." |
| 6 | "the effect" — effect of what? | "the effect **of code-switching on model performance** varies by task." |
| 7 | The phenomenon is described but never named "code-switching" before the term is used | Named at first description: "text in which two languages alternate within a single message, **a pattern known as code-switching**." |

## Page 2 — terminology, attitudes, spelling (comments 8–25)

| # | His point | What changed |
|---|---|---|
| 8 | "one variety" — of what? And text is not itself a variety | "Malaysian social media text is **one setting in which such code-switching is common**." |
| 9 | "Coluzzi (2017), citing Ethnologue, records…" feels awkward | Recast, and merged with the second Coluzzi sentence per comment 1: "**Drawing on Ethnologue figures, Coluzzi (2017) records** around 140 languages in use in the country, **and reports that** code-mixing…" |
| 10 | "such mixed writing" is vague — all multilingual writing, or code-mixed? | "Two local terms are used for **this code-mixed writing**." |
| 11 | "they do not cover the same set of languages" is informal | "they **refer to different combinations of languages**." |
| 12 | "in part" — what do you mean? | Spelled out: "*Manglish* refers to that combination directly, **whereas *Bahasa Rojak* refers to a wider combination that also includes Chinese**." |
| 13 | "so this review states its position before turning to…" — you don't have to tell the reader what the paper is doing | Clause deleted. **New Rule 17.** |
| 14 | "regarded" — imprecise | Sentence recast: "**Descriptions of *Manglish* in the literature are not uniform.**" |
| 15 | "technical difficulty" is ambiguous | Gone with the deleted clause. |
| 16 | "weakens" — does the source use that word? | **(his wording)** "**having a negative effect on** standard English and Malay." |
| 17 | "How this mixed writing is regarded affects how it is processed" is a claim needing a citation | Sentence removed rather than propped up with a citation the sources do not support. The paragraph now opens on what the literature says, not on a claim about it. |
| 18 | "is not random" | **(his wording)** "is **systematic rather than random**." |
| 19 | "The same regularity" — reader must infer you mean systematicity | **(his wording)** "The same **systematicity** appears at the level of spelling." |
| 20 | Logical over-reach: categorising variation does not prove it is systematic | **(his wording)** "…and **this categorisation suggests that the variation follows recurring patterns rather than occurring arbitrarily**." |
| 21 | The Dewan Bahasa dan Pustaka claim needs a citation | Cited: "such as *Kamus Dewan*, does not list these non-standard forms **(Dewan Bahasa dan Pustaka, 2005)**." New reference. |
| 22 | "tools therefore treat them as OOV" assumes all tools behave the same way | **(his wording)** "**may therefore** treat them as out-of-vocabulary items." |
| 23 | Ambiguous attribution: do the sources *report* that earlier work said this, or *say* it themselves? | The latter, so the source is now the subject: "**Abu Bakar et al. (2020) accordingly describe** Malay social media text as misspelled, out-of-vocabulary, ill-formed and noisy." |
| 24 | "The conventions Malaysian writers follow" is a claim about all Malaysian writers | **(his wording)** "**These writing conventions are consistent within the observed variation**." |
| 25 | "built to" | "**designed to** handle." |

## Page 3 — architecture and annotation (comments 26–42)

| # | His point | What changed |
|---|---|---|
| 26 | Abrupt jump from linguistic mismatch to architecture; and "one common explanation **concerns the model architecture**" | Bridge sentence added: "**This mismatch between writing conventions and tool design raises the question of where the difficulty in processing such text actually lies.**" His phrasing adopted. |
| 27 | "On this explanation" does not read naturally | "**Under this view**." |
| 28 | "regionally adapted" — adapted how? | "a larger model, or one **further trained on Malay-English or other Southeast Asian data**." |
| 29 | "capacity dilution" needs defining | Defined in its own sentence: "**Capacity dilution refers to the reduction in the modelling capacity available to each individual language as more languages are added to a model of fixed size.**" |
| 30 | More academic and direct | **(his wording)** "Another source of difficulty **arises one step earlier**, at the point where **sentiment labels** are created." |
| 31 | "often limiting" — limiting in what way? | Made concrete and kept faithful to Poria et al. (2023), who write that heavy reliance on annotated data "is often limiting" and that this has driven renewed use of external knowledge: "…is a limitation, **and that it has renewed interest in supplying models with external knowledge such as sentiment lexicons**." |
| 32 | "an automatic one" is unnatural | "by **an automatic labelling method**." |
| 33 | "it produces" — remove | Removed: "**The labels form** the supervision signal." |
| 34 | The Frénay and Verleysen sentence is awkward | **(his wording)** "…**which can reduce predictive accuracy** (Frénay and Verleysen, 2014)." *(Kept as "and" rather than "&" to match the citation style used throughout the paper.)* |
| 35 | "they" | "**label errors** can change which of two models a benchmark ranks higher." |
| 36 | The preceding paragraph does not establish that labels are *more* limiting than models | The conclusion is now attached to the evidence that carries it: "**Three findings, each developed in the sections that follow, point to** the annotation label rather than the model as the more limiting constraint…" |
| 37 | "A second and related problem" — what was the first? | The parallel enumeration is gone. The second problem is folded into the same sentence as the first, leaving one *First / Second / Third* spine for the three findings. |
| 38 | "that reading" — reading of what? | Recast; "reading" removed. |
| 39 | "four Malay-English sentiment resources currently exist" — are you certain there are only four? | **(his wording)** "**this review identifies** four Malay-English sentiment resources." |
| 40 | "large" needs an operational definition | "large, **meaning at least ten thousand labelled messages**." Consistent with the corpus sizes reported in Sections 3 and 5: MY-EN-CS 2,316; MyCovid-Senti 11,568; MESocSentiment 19,714. |
| 41 | "validated by human annotators" is ambiguous | **(his wording)** "**accompanied by an assessment of annotation reliability by human annotators**." |
| 42 | "at the expense of the others" is informal | **(his wording)** "**satisfies some of these criteria but not all of them**." |

## Page 4 — reliability, scope, contributions (comments 43–60)

| # | His point | What changed |
|---|---|---|
| 43 | "coefficient" — which coefficient? | "where an **inter-annotator agreement coefficient** is reported" — his own suggested general term. |
| 44 | "a narrower task than the corpus is used to support" is hard to understand | Both tasks named: "it was **measured on a two-way judgement rather than on the three-way positive, negative and neutral labelling** for which the resource is used." |
| 45 | "describe one condition rather than two" — they are two problems, not one condition | **(his wording)** "**The second and third findings are closely related rather than independent.**" |
| 46 | Reliability is not always "demonstrated" through Cohen's κ | "Reliability is normally **assessed** by…" |
| 47 | "the most widely used of which is Cohen's kappa" is a claim Artstein and Poesio may not make | **(his wording)** "a chance-corrected agreement coefficient, **such as** Cohen's kappa (κ)." |
| 48 | "stops being informative" is too strong | **(his wording)** "the condition that **can make the statistic used to assess the labels more difficult to interpret**." |
| 49 | The Selvaraju et al. (2024) sentence arrives with no explicit connection | Link written as its own sentence: "**This shortage of reliably labelled data is not confined to the four resources examined here.** Selvaraju et al. (2024) report that…" |
| 50 | The transition into the research question could be stronger | "**These three findings lead to the question this review examines:**…" |
| 51 | Annotation and evaluation are not themselves "unresolved" | "why reliable annotation and evaluation … **have not yet been established**." |
| 52 | "author's" | "**authors'**." |
| 53 | "diagnosis" is less academic | "Its contribution is **an analysis** of…" |
| 54 | "the problem" is ambiguous | Named: "an analysis of **why reliable annotation and evaluation remain difficult to establish for this data**." |
| 55 | A tier does not "gain" fidelity or scalability; it is a trade-off | See 56. |
| 56 | Suggested wording for contribution 1 | **(his wording)** "…and **examines the trade-off between label fidelity and scalability across them**." |
| 57 | "two causes" implies there are exactly two | "two **sources** of neutral-label skew." |
| 58 | "four regional corpora" contradicts "four Malay-English sentiment resources" used earlier | One term throughout: **four Malay-English sentiment resources**. **New Rule 19.** |
| 59 | "what each of the four corpora reports" — a corpus does not literally report | "what **the studies introducing** the four Malay-English sentiment resources report about the reliability of their annotation." |
| 60 | "measurement" versus "evaluation" | "the linguistic, annotation and **evaluation** challenges." |

---

# Part 2 — Changes made beyond the 60 comments

Five, all consequences of the comments rather than new decisions.

1. **Three further same-source pairs merged** under comment 1 — Doğruöz et al. (2021), Coluzzi (2017) and
   Maskat and Rahman (2020) each appeared on two consecutive sentences.
2. **Two new references**, both requested by a comment and both doing real work: **Devlin et al. (2019)**
   for the definition of a pre-trained model (comment 4) and **Dewan Bahasa dan Pustaka (2005), *Kamus
   Dewan*** for the standard Malay dictionary (comment 21). The reference list is now **38**; his Round 1
   target was 40.
3. **The Abstract was aligned** with the terminology fixes in comments 55–58 and 60, since it repeated the
   exact wording he flagged in the contributions list. Nothing else in the Abstract changed.
4. **Six sentences over 35 words were split**, following the standing rule from R1 2 and R2 45. Two remain
   at 36 words, both simple lists.
5. **A stray manual page break** before the References in the standalone Section 1 file was removed; with
   the slightly longer body it would have produced a blank page.

## What is still open

- **Sections 2 to 7 still use "four regional corpora" and "two causes of neutral-label skew"**, including
  the heading of Section 3.2. Rule 19 says these must be aligned with Section 1 before he reads them.
- **The reference list is 38 against his target of 40.** Two more, added the way these two were, would close
  it.
- **Citation style.** He has now written author–date four times while looking at your draft, and comment 34
  supplies a replacement in author–date form. Template §11 asks for numbered `[n]`. Get one line from him.
- **Page count is unchanged**: 21 pages in LibreOffice for both v13 and v14, so the Word count of 20 holds.

---

# Part 3 — The v15 self-check, and why v14 was not ready

After v14 was built, the Introduction was re-read against all 19 rules as if Dr. Ho were reading it —
mechanically, with a script, and adversarially by a second reader. **Eleven real defects were found in the
draft that had just been produced.** None came from a Round 4 comment. All came from the rules those
comments established.

The most serious was a repeat of Rule 16, the rule his very first Round 4 comment created.

## The five Rule 16 violations in v14

| Where | Source repeated on consecutive sentences |
|---|---|
| Paragraph 1 | Doğruöz et al. (2021), twice in a row |
| Paragraph 2 | **AlAfnan et al. (2025), four sentences in a row** |
| Paragraph 7 | Kong et al. (2023) and Mohd Shamsuddin et al. (2024), twice in a row |

Fixing Rule 2 in Rounds 1 to 3 by adding a citation to every claim produced exactly the pattern Rule 16
forbids. The fix is never to delete the citation. It is to merge the sentences, or to carry the attribution
forward with a phrase that does not repeat the reference: **"In their survey…"**, **"The same study
describes…"**, **"They add that…"**.

## The other six

| # | Defect | Rule | Fix |
|---|---|---|---|
| 1 | *"Descriptions of Manglish in the literature are not uniform."* | 2 | "The literature" is a trigger phrase carrying no citation. Rewritten as "*Manglish* is not always described in the same terms", which the next two sentences then evidence. |
| 2 | Treffers-Daller et al. (2022) cited for a claim about **social media writing** | 2 | That paper analyses the **classroom speech of two teachers**, as the paper itself says two paragraphs later. He flagged this misuse at R2 62 and R3 11. The social-media claims now go to AlAfnan et al. (2025) alone, and the Treffers-Daller finding is bounded with "there". |
| 3 | *"annotation reliability is rarely reported across these four resources"* | 2, 8 | **Factually wrong and inconsistent with Section 5.2**, which says "Half of the regional corpora report no agreement coefficient at all." Two of four report one. Rewritten as "the studies introducing two of the four resources report no inter-annotator agreement coefficient at all". |
| 4 | *"…large, meaning at least ten thousand labelled messages, balanced across sentiment classes, drawn from casual social media…"* | 18 | "Large" was operationalised and **"balanced" and "casual" were left undefined in the same sentence** — the exact objection of comment 40, one clause later. All four criteria are now set out in the numbered format he supplied at R1 76. |
| 5 | *"the statistic used to assess the labels"* and *"Correcting either weakness alone"* | 4 | He asked "Which statistic?" at R2 42 and objected to "These two weaknesses" at R2 38. Both constructions had come back. Now: "makes Cohen's *κ* more difficult to interpret in the third" and "Neither correction would be sufficient without the other." |
| 6 | *"Poria et al. (2023) note that this heavy reliance on annotated data is a limitation"* | 2, 4 | The source says the heavy reliance **of deep learning models** is often limiting. The paraphrase widened it to supervised learning generally, and "this heavy reliance" pointed at nothing. Both corrected against the source text. |

Also fixed: "positive transfer" was left undefined beside a newly defined "capacity dilution" (Rule 5);
"resources" meant two different things in paragraphs 1 and 7 (Rule 19); no bridge carried the reader from
the general account of annotation into the review's own three findings (Rule 7); "such text" and "actually"
had crept into the new bridge sentence (Rules 3, 4); "which of two models a benchmark ranks higher" made a
benchmark the actor (Rule 8); the unfulfilled "one of four conditions" was reduced to "one of the
conditions" (Rule 10); and Selvaraju et al. (2024) was dropped from the list of surveys said to cover
comparative benchmarking, which it does not.

## The checker

`Comment_Tracker/check_section.py` runs the mechanical passes over any .docx:

```
python3 Comment_Tracker/check_section.py "ICON AI 2026 - Section 1 (v15).docx"
python3 Comment_Tracker/check_section.py paper.docx --from "2. Why Malaysian" --to "References"
```

It catches long sentences, repeated citations on consecutive sentences, trigger words without a citation,
previously flagged wording, bold in the body, and parenthetical cross-references. It cannot judge meaning,
so passes 5 and 8 always need a human read. **Run it before anything goes to him.**

## v15 status

| Pass | Result |
|---|---|
| Sentences over 35 words | 2 — one is the numbered criteria list in his own R1 76 format, one is 36 words |
| Same source on consecutive sentences | **0** |
| Trigger words without a citation | 1 false positive (the checker splits at a colon; the citation is on the sentence) |
| Previously flagged informal wording | none |
| Bold in the body | 0 |
| Parenthetical cross-references | 0 |
| Page count | 21 in LibreOffice, unchanged from v13 and v14 |
| Sections 2 to 7 | byte-identical to v14 |

---

# Part 4 — The author's own review of v15, and v16

Six Word comments, 30 August 2026, on `Template ICON AI 2026 - Section 1.pdf`. Four of the six were
correct. The file also contained two grammar errors introduced while hand-editing v15.

| # | The comment | Verdict | What changed in v16 |
|---|---|---|---|
| L1 | Dr. Ho's comment 23 (ambiguous attribution of "described in earlier work") | **Closed already.** The sentence he objected to no longer exists; *Abu Bakar et al. (2020)* is now the grammatical subject, so neither of his two readings is available. | A leftover pointer was removed all the same: "describe Malay social media text **in those terms, as** misspelled" → "describe Malay social media text **as** misspelled". "Those terms" pointed at nothing definite (Rule 4). |
| L2 | Comment 31, "limiting in what way?" | **Correct — not solved.** v15 said what the limitation *led to*, not what it *is*. | A plain statement of the constraint now precedes the citation: "The amount of labelled data available therefore sets a bound on what can be trained and on what can be tested." Poria et al. (2023) keep only what they actually say. |
| L3 | Comment 36, "does not establish that labels are more limiting than models" | **Correct — only partly solved.** v15 grounded the claim in the three findings, but still asserted the comparison, and none of the three findings compares labels with models. | The comparison is now the question the findings answer: "the question is whether the model or the sentiment labels are the greater constraint at present. Three findings point to the labels." |
| L4a | Comment 48, "stops being informative" too strong | **Correct — his hedge had been dropped.** He wrote "**can** make … more difficult to interpret"; v15 wrote "makes". | "can therefore make Cohen's *κ* … more difficult to interpret". His "can" restored. |
| L4b | Comment 49, the Selvaraju sentence is not explicitly connected | **Correct — not solved, and v15 made it worse.** "Selvaraju et al. (2024) find **the same shortage**" — no shortage had been named. | The link is written out: "These four resources are therefore limited both in what they contain and in what is known about the reliability of their labels. That shortage is not confined to them, since Selvaraju et al. (2024) report…" |
| L5 | Comment 58, use "Malay-English sentiment resources" not "four regional corpora" | **Done in Section 1 since v14** — but **still live in Sections 2 to 7**, which he has not reached. | All five occurrences replaced, plus the Section 3.2 heading "Two **causes**" → "Two **sources**" and the three "cause" references beneath it, per comment 57. |
| L6 | Comment 59, "sounds like a corpus will literally report something" | **Closed in Section 1** — contribution 2 makes *the studies* the subject, and he uses "existing studies" as an agent himself (R2 39). | But the defect was still live in Section 5.2: "What the four regional corpora report about their own reliability" and "Half of the regional corpora report no agreement coefficient". Both rewritten with the studies as subject. |

## Two grammar errors introduced by hand-editing

| In the file | Problem | v16 |
|---|---|---|
| "report that **effect of code-switching** on model performance varies by task" | Missing article. The sentence also names code-switching six words earlier, so the noun is repeated. | "report that **its** effect on model performance varies by task" |
| "the modelling capacity available to any individual language falls, **which called** capacity dilution" | Not grammatical. | "…falls, **an effect they call** capacity dilution" (and "an effect **they call** positive transfer" restored above it, for parallelism and to keep the attribution to Conneau et al.) |

**The lesson is procedural, not linguistic.** Both errors came from editing a finished paragraph by hand in
Word. `check_section.py` cannot catch a missing article. Either make edits in the source and rebuild, or
read the changed sentence aloud once before saving.

## Left for the author to decide

- **The author block is still template placeholder text** — "Author(s) Name(s)", "Author Affiliation(s)",
  "xyz @utm.my", and the footer "masaini@abc.xxx.xxx". These must be filled in before submission.
- **The keyword list says *Bahasa Rojak*, but the paper's subject is *Manglish*.** Since R3 comment 8, the
  paper distinguishes the two and states that it examines Malay-English mixing, which *Manglish* names
  directly. A keyword naming the broader variety contradicts the scope statement (Rule 19).
- Reference count is 38 against his target of 40.
- Citation style is still unconfirmed with him: template §11 asks for numbered `[n]`, he has written
  author–date five times while reading the draft.
