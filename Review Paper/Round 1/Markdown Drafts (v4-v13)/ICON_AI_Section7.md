# 7. Synthesis: How the Challenges Compound

Sections 3 to 6 examined linguistic structure, annotation practice, model capability and reliability
measurement in turn, which is how the literature itself is organised. Read separately they describe four
difficulties. Read together they describe one sequence, in which each difficulty creates the conditions for
the next and the sequence returns to its own starting point. Figure 1 sets it out. Establishing that this
structure exists is the contribution this review claims, and the directions in the second half of this section
are traced to points within it.

![Figure 1](fig/fig1.png)

**Figure 1.** The compounding chain in Malaysian code-mixed sentiment annotation

The first link runs from linguistic structure to systematic disagreement. Section 3 established three
properties of this text. Switching occurs inside the clause and offers little cue to where the opinion lies.
Affect is often carried by particles belonging to neither standard language. Phonetic spelling multiplies the
surface forms of a word. The consequence is not only that agreement is harder to reach. It is that
disagreement takes a particular form. Where one annotator reads *lah* as a softener and another reads it as a
marker of sarcasm, and each reading is stable, the disagreement recurs on the same construction in the same
direction. Random disagreement is reduced by recruiting more annotators, because independent errors average
out. Systematic disagreement is not, because additional annotators bring their own stable readings rather than
noise around a shared one (Pavlick and Kwiatkowski, 2019). The usual response to unreliable annotation is
therefore unsuited to the type of unreliability this text produces.

The second link runs from disagreement to automation. Competent annotation of this material requires a fluent
bilingual reader, and that requirement follows from the linguistic properties of the text rather than from any
general fact about annotation. The corpus papers give cost and annotator availability as their reason for
automating, and Mohd Shamsuddin et al. (2024) state that their tools "eliminated the need to find speakers
fluent in Malay and English to label the dataset". Automation on this material is therefore downstream of the
linguistic difficulty rather than an independent methodological preference.

The third link runs from automation to a shared blind spot. Annotators chosen under cost pressure are chosen
for availability, and the tools available are those built for well-resourced languages. Section 4.3 showed
what follows in the one regional case where the composition is documented. None of the three analysers used to
build MESocSentiment is described as covering Malay, each skewed neutral before any vote was taken, and the
most neutral-skewed of them was the transformer. Voting cancels error only to the extent that voters fail
independently. Where the property they share is the language none of them reads, the ensemble ratifies the
error instead of cancelling it, and unanimity produced that way is indistinguishable from confidence.

The fourth link runs from the shared blind spot to class skew. False neutrals accumulate rather than being
corrected, and the corpus acquires a class distribution that no participant intended. MESocSentiment reaches
78.23% neutral. Section 4.2 separated the two mechanisms that produce this, but one of them deserves restating
here, because it is the point at which the process turns on itself. Posts on which the three analysers could
not agree were removed, 512 of them, on the stated ground of retaining only "absolute categories". Those posts
are not a random sample. They are the contested, heavily code-switched cases that the first link identifies as
the source of the difficulty, and removing them raised both the neutral share and the measured agreement.

The fifth link runs from class skew to the reliability instrument, and it is where the two halves of this
review meet. The distribution produced at the fourth link is the specific condition under which a chance-
corrected coefficient stops returning interpretable values (Feinstein and Cicchetti, 1990; Byrt et al., 1993).
A researcher who suspects the labels are unsound and computes a coefficient obtains a low value, which is
consistent with poor annotation and equally consistent with competent annotation of a skewed corpus. Raw
agreement carries the same ambiguity in the opposite direction (Artstein and Poesio, 2008). The defect and the
inability to detect the defect have one cause. That is what separates an unresolved problem from a merely
difficult one: here the quality check is least informative exactly where quality is lowest.

The sixth link closes the cycle. Corpora whose reliability was never established are released, trained on and
evaluated against, so every downstream comparison inherits an error term that nobody has quantified. The more
consequential edge is the one that returns. The annotators used to build the next corpus are fine-tuned on the
last, and Section 5 showed that a fine-tuned encoder resolves only the variation it has been shown. The blind
spots of one generation of labels are transmitted to the instruments that produce the next, so the chain does
not merely persist. It reproduces itself.

Read as a whole, the chain explains a pattern that the individual studies cannot. Each reviewed work
intervenes at one link and does so competently. None addresses the chain as a chain, and an intervention at
one link is assessed with an instrument compromised at another, so the assessment cannot establish whether the
intervention worked. That is why effort in this area has been absorbed without accumulating.

The chain identifies where intervention would matter, not which intervention would succeed. The five
directions below are framed as work that remains to be done rather than as a programme any particular study
should adopt. Each is traced to a link, since a direction that cannot be traced to a finding is a preference
rather than a conclusion.

The first direction is agreement measurement under class skew, and it follows from the fifth link. Prevalence-
adjusted coefficients exist (Byrt et al., 1993) but have not been evaluated on code-mixed sentiment data, so
it is not known which behaves best under the distributions these corpora actually exhibit. The study requires
no new data collection, only an existing annotated corpus, a set of candidate coefficients, and a comparison
of how they behave as skew increases. It is a precondition for the others, because until reliability can be
measured under prevailing conditions, no corpus built hereafter can be shown to improve on the ones described
here.

The second direction is a minimum reporting standard, and it follows from Table 3. A minimum set for any newly
released corpus would comprise five elements: (1) the number of annotators and their stated qualification; (2)
the availability of the annotation guideline; (3) the variant of the coefficient and the task it was computed
for; (4) per-class rather than aggregate agreement; and (5) the full class distribution. Per-class agreement
deserves particular emphasis, since an aggregate figure on a skewed corpus is dominated by the majority class
and can conceal near-total disagreement on the minority polarities that matter most.

The third direction is a shared annotation convention for affect-bearing particles, and it follows from the
first link. Because the disagreement these particles generate is systematic rather than random, the
appropriate remedy is a shared convention rather than additional annotators, and no such convention exists for
*lah*, *kan* and their equivalents. A model is available. Mohammad (2016) proposes a questionnaire that
separates the speaker's emotional state, the target of the opinion and the attitude taken toward it. It also
treats sarcasm, ridicule and mockery as a distinct response rather than folding them into polarity, which is
precisely the ambiguity Section 3.2 identified. Kong et al. (2023) adapt this scheme into a four-question
guideline for Malaysian tweets. What is absent is not the design but its adaptation to Malaysian particles and
its adoption across projects.

The fourth direction is to publish label distributions rather than only resolved labels, and it follows from
the fourth link. Current practice resolves disagreement by majority rule or removes it, discarding the
information that the case was contested. Uma et al. (2021) report that models trained on the full distribution
of annotator judgements can outperform models trained on aggregated labels. Publishing that distribution would
preserve the cases present pipelines delete. It would also make the fourth link visible, since a corpus that
reports what it discarded allows a reader to judge whether its reported reliability was earned or obtained by
attrition.

The fifth direction is to test the independence premise, and it follows from the third link. Every consensus
mechanism in this literature depends on the premise that annotators of different construction fail
independently, and on this material the premise is asserted throughout and measured nowhere. The study is a
direct one: label a common sample with annotators of deliberately different competence, and measure the
correlation of their errors rather than their individual accuracies. Low correlation would justify the
aggregation strategies already in use. High correlation would indicate that consensus on this material adds
confidence without adding evidence.

These are directions rather than results. The claim of this review is not that they will succeed. It is that
the chain in Figure 1 identifies where effort in this area is currently absorbed without accumulating, and
that the first direction is a precondition for knowing whether any of the others have worked.

---
---

# Part A — Scope decision, recorded

You chose to follow the Introduction: **no system is proposed.** Section 7 ends on five research directions
and nothing else. The heterogeneous tri-model consensus pipeline described in `CLAUDE.md` and the Conversion
Plan does not appear, and no requirements paragraph stands in for it.

That is now consistent across the paper. The Introduction says the review "does not propose, implement or
evaluate a system", contribution 3 promises "a research agenda that follows from that interaction", and
Section 7 delivers exactly that. Dr. Ho commented approvingly on the wording of that Introduction paragraph
in Round 2 (comments 47 and 48), so the consistency is with text he has already accepted.

**Worth updating `CLAUDE.md`** — its "Decisions taken" section still says the framing is "review + proposed
framework" and that the paper "closes by proposing a heterogeneous tri-model consensus pipeline". That is no
longer true of the paper. The framework stays in the thesis, where RQ1 is exactly that question, and the
fifth research direction in this section — testing whether annotators of different construction fail
independently — is the question your thesis then answers. The paper sets it up without claiming it.

---

# Part B — Figure 1

Delivered as `fig/fig1.svg` and `fig/fig1.png`. Insert the **PNG** into Word at full text width; the SVG is
the editable master if you need to change wording later.

The v1 pre-submission check flagged four problems with the old Figure 1. All four are addressed:

| Old problem | Now |
|---|---|
| "Reads as a screenshot"; bitmap | Vector SVG, rendered at 3.5× for a crisp PNG |
| US spelling "labeling" in a paper that writes "labelling" | "labelling" throughout; British spelling checked against the body text |
| "Perpetuates and obscures" edge label floating unanchored | Every label is either inside a box, beside a numbered arrow, or in the annotation block |
| Possibly under the template's 6 cm minimum width | 900 units wide; at full text width in the template it renders about 14.6 cm |

Two further choices worth knowing. The figure is greyscale-safe, so it survives a black-and-white print of
the proceedings. And the node labels are deliberately hedged to match the prose — the reliability node reads
"Reliability hard to establish", not "unmeasurable", because Section 6 concludes that establishing
reliability is "not clearly achievable" with current instruments rather than impossible.

---

# Part C — What was verified for the research directions

| Claim | Source | Verified |
|---|---|---|
| Prevalence-adjusted coefficients exist | Byrt et al. (1993) | ✅ PABAK, read from your PDF |
| Models trained on full annotator distributions can beat models trained on aggregated labels | Uma et al. (2021) | ✅ verified for Section 4 |
| A questionnaire separating speaker's emotional state, target of opinion and attitude toward it | Mohammad (2016) | ✅ "a sentiment questionnaire that includes questions about the target of opinion, as well as additional questions such as those that address the speaker's emotional state" |
| Sarcasm, ridicule and mockery treated as a distinct response option | Mohammad (2016) | ✅ "Sarcasm, ridicule, and mockery are included as a separate option" |
| Kong et al. adapted that scheme into a four-question guideline | Kong et al. (2023) | ✅ "Our approach to manual sentiment annotation took the intuition from the proposed semantic role-based sentiment questionnaire by [40], that is, to determine the speakers' emotional state and identify the Primary Target of Opinion (PTO) using four questions" — and their [40] is Mohammad (2016) |
| Systematic disagreement is not reduced by more annotators | Pavlick and Kwiatkowski (2019) | ✅ verified for Section 3.2 |
| Chance-corrected coefficients become uninterpretable under skew | Feinstein and Cicchetti (1990); Byrt et al. (1993); Artstein and Poesio (2008) | ✅ verified for Section 6 |

**Dropped from the v3 material:** the two trends that rested on Niimi (2024) and Negi et al. (2026), both
arXiv preprints. Trend 1 ("flexibility trades against reliability") depended on Niimi for output instability
and Negi for unfaithful relational structure, and neither claim now has a peer-reviewed source. Trend 2's
point — that every consensus mechanism aggregates voters of one competence class — survives, and it is
carried in the third link by the MESocSentiment evidence alone, which is stronger anyway because it is
regional and documented.

**Also dropped:** the seventh v3 direction, a shared evaluation benchmark, and the sixth, targeted human
validation. Both are defensible but neither traces to a link in the chain, and the section's own rule is that
a direction which cannot be traced to a finding is a preference rather than a conclusion. Cutting them
enforces that rule rather than merely stating it.

---

# Part D — New reference

One added. Sections 1 to 7 now cite **37 sources**, all peer-reviewed.

Mohammad, S. M. (2016). A practical guide to sentiment annotation: Challenges and solutions. *Proceedings of the 7th Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis (WASSA)*, 174–179.

---

# Part E — Page budget

Section 7 came in at **1,515 words (2.82 pp) plus Figure 1 (~0.38 pp) = 3.20 pages**, against 3.21 suggested.

| Component | Pages |
|---|---|
| Title, abstract | 1.00 |
| 1 Introduction | 3.01 |
| 2 Review Methodology | 0.60 |
| 3 and subsections | 3.44 |
| 4 and subsections, 2 tables | 4.11 |
| 5 Models as Annotation Instruments | 0.93 |
| 6 Evaluating Annotation Reliability, 1 table | 1.27 |
| 7 Synthesis, 1 figure | 3.20 |
| **Committed** | **17.56** |
| References, 45 entries at 8pt | 1.73 |
| **Left for Section 8** | **0.71** |

The plan wanted 0.70 for the conclusion. There is 0.71 left. **The paper lands inside the 20-page cap
without further trimming**, which is the first time that has been true since the budget was first measured
after Section 3.2, when the projection was 22.65.

One caveat on the reference line: 1.73 pages assumes 45 entries at the template's 8pt. You currently have 37.
If chasing Dr. Ho's 40+ target pushes the list to 50, references cost 1.92 pages and the total rises by 0.19,
which the 0.71 pages remaining after Section 8 absorbs comfortably.
