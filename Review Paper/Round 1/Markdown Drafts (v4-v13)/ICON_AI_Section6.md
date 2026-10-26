# 6. Evaluating Annotation Reliability

Sections 4 and 5 concerned how labels are produced. This section concerns how the labels that result are shown
to be sound. Reliability is normally demonstrated with a chance-corrected agreement coefficient, of which
Cohen's κ is the most widely used (Cohen, 1960). The coefficient measures how far the agreement two annotators
actually reach exceeds the agreement expected by chance. Magnitudes are then read against conventions. In
computational linguistics, values above 0.8 are generally treated as good reliability, and values between 0.67
and 0.8 as allowing tentative conclusions (Artstein and Poesio, 2008).

Those conventions assume that expected chance agreement is stable across datasets, and it is not. Feinstein
and Cicchetti (1990) show that an imbalance in the marginal totals of an agreement table can convert a high
observed agreement into a low coefficient. Their worked example is worth reproducing. Holding observed
agreement at 0.85, an expected chance agreement of 0.50 yields κ = 0.70, while an expected chance agreement of
0.78 yields κ = 0.32. The annotators agreed on the same 85% of items in both cases. Byrt et al. (1993)
formalise the effect, showing that κ reflects the distribution of data across categories as well as agreement,
and propose a prevalence-adjusted coefficient in response. Artstein and Poesio (2008) state the consequence
for annotation directly: when one category is very common, high agreement can result from indiscriminate
coding rather than from an ability to distinguish between categories.

That is the condition Malaysian code-mixed sentiment data is in. Section 4 established that the labelling
methods available for this text produce heavily skewed class distributions, the largest corpus standing at
78.23% neutral. A skew of that size raises expected chance agreement, which is the quantity the correction
depends on. The property that makes the labels unrepresentative is therefore the property that makes the
statistic used to check them difficult to read. The difficulty runs in both directions. A low coefficient may
indicate unreliable annotation, or a dominant class. A high one may indicate reliable annotation, or
indiscriminate coding. Neither reading can be ruled out from the coefficient alone. This is the sense in which
the annotation problem and the evaluation problem are one problem rather than two, and the reason correcting
either alone leaves the other in place.

What the four regional corpora report about their own reliability is set out in Table 3.

**Table 3.** Reliability evidence reported by the four Malay-English sentiment corpora

| Corpus | Annotators | Written guideline | Coefficient reported | What the coefficient measured |
|---|---|---|---|---|
| MESocSentiment (Mohd Shamsuddin et al., 2024) | None; three automatic analysers | Not applicable | None | — |
| MyCovid-Senti (Kong et al., 2023) | Three, independent | Yes | None | — |
| MY-EN-CS (Kasmuri and Basiron, 2019) | Two undergraduates proficient in Malay and English | Yes; the guideline is the paper's contribution | κ = 0.83 | Whether a sentence is opinionated or factual |
| SentiBahasaRojak (Romadhona et al., 2022) | Five native Bahasa Rojak experts | Not stated | "Kappa" = 0.77; the variant is not specified | Whether a stock-market post is bullish or bearish |

Three observations follow. Half of the regional corpora report no agreement coefficient at all, including one
annotated by three people working from a written guideline. The two coefficients that are reported were
obtained for binary judgements, and neither is the three-class polarity task the corpora are used to support.
Romadhona et al. (2022) report a kappa value without stating which coefficient it is. Their annotation used
five experts with the final label set by majority vote, and Cohen's κ is defined for two annotators.

No corpus in the regional literature therefore supplies what a reliability claim requires: a coefficient of a
stated type, computed for the task the labels are used for, over annotators whose number and qualification are
recorded. A corpus that did supply them would still face the interpretation problem above, because the class
distributions these methods produce are the distributions under which the coefficient becomes hard to read.
Establishing reliability for this data is not only unreported. With the instruments currently in use, it is
not clearly achievable.

---
---

# Part A — What Section 6 adds over the v3 draft

**A worked example instead of an assertion.** The v3 draft asserted that class imbalance makes κ hard to
interpret. Feinstein and Cicchetti (1990) demonstrate it numerically, and Section 6 now reproduces their
example: with observed agreement held at 0.85, an expected chance agreement of 0.50 gives κ = 0.70, while
0.78 gives κ = 0.32. Same 85% agreement, two very different coefficients. That is checkable arithmetic
rather than a claim, which is the right register for the paper's third contribution.

**A computational-linguistics source for the prevalence effect.** Artstein and Poesio (2008) — already cited
in the Introduction — state it for annotation specifically: when one category is very common, "high accuracy
and high agreement can also result from indiscriminate coding". That sentence does more work than the
biomedical sources alone, because it names the failure mode in the field Dr. Ho is reviewing for.

**A new audit finding on Romadhona et al. (2022).** Reading the paper turned up something the v3 draft
missed. They report "a Kappa value of 0.77" and never say which coefficient it is. Their annotation used
**five** native Bahasa Rojak experts with the final label set by majority vote — and Cohen's κ is defined for
two annotators. So the corpus reports a coefficient whose variant is unstated, for a design the most common
variant does not fit. That is now the third of the three observations under Table 3.

**No new references.** Section 6 pays off groundwork already laid: Cohen (1960), Artstein and Poesio (2008),
Feinstein and Cicchetti (1990) and Byrt et al. (1993) were all introduced in the Introduction. The count
stays at **36**.

---

# Part B — What was verified

| Claim | Source | Verified |
|---|---|---|
| κ compares observed agreement against chance agreement computed from the marginals | Cohen (1960), read from your PDF | ✅ |
| CL convention: >0.8 good, 0.67–0.8 tentative | Artstein and Poesio (2008) | ✅ "content analysis researchers generally think of K > .8 as good reliability, with .67 < K < .8 allowing tentative conclusions" |
| po = 0.85 with pe = 0.50 → κ = 0.70; with pe = 0.78 → κ = 0.32 | Feinstein and Cicchetti (1990), read from your PDF | ✅ verbatim worked example |
| "a high value of po can be drastically lowered by a substantial imbalance in the table's marginal totals" | Feinstein and Cicchetti (1990), abstract | ✅ |
| κ is affected by bias between observers and by the distribution across categories ("prevalence"); PABAK proposed | Byrt et al. (1993), read from your PDF | ✅ abstract verbatim |
| "when one category is very common, high accuracy and high agreement can also result from indiscriminate coding" | Artstein and Poesio (2008) | ✅ |
| Kasmuri and Basiron used **two** annotators, undergraduates proficient in Malay and English | Kasmuri and Basiron (2019) | ✅ "two annotators were selected as candidate annotators. These candidates were undergraduate students who were proficient in written and spoken Malay and English" |
| The guideline is that paper's stated contribution | Kasmuri and Basiron (2019) | ✅ "This paper develops a guideline to build a code-switching subjectivity corpus" |
| Romadhona: five native experts, majority vote, bullish-versus-bearish, stock-market posts | Romadhona et al. (2022) | ✅ "hired five native Malaysian experts … Experts must be able to distinguish the difference between bullish (positive) and bearish (negative). These five experts first annotated all the posts, and then majority voting was carried out" |
| Romadhona do not state which kappa | Romadhona et al. (2022) | ✅ zero occurrences of "Cohen" or "Fleiss" in the paper |
| Kong et al. report no coefficient | Kong et al. (2023) | ✅ verified for Section 4 |
| MESocSentiment has no human annotation stage | Mohd Shamsuddin et al. (2024) | ✅ verified for Section 4 |

**A note on scope.** Feinstein and Cicchetti (1990) and Byrt et al. (1993) both work with fourfold, that is
binary, agreement tables. Both regional coefficients under audit are also binary judgements, so the results
apply directly rather than by extension. Worth knowing if Dr. Ho asks whether a clinical-epidemiology result
transfers to a three-class sentiment task — for the two coefficients actually reported, the tasks are binary
and the transfer is exact.

**Not used:** Landis and Koch (1977) and Gwet (2008), both of which appeared in the v3 reference plan. Neither
is needed. Artstein and Poesio (2008) supplies the interpretation thresholds in a computational-linguistics
setting, which is more appropriate here than the biomedical scale, and Byrt et al. (1993) supplies the
adjusted-coefficient alternative. Two fewer paywalled papers to chase.

---

# Part C — Page budget

Section 6 came in at **562 words (1.05 pp) plus Table 3 (~0.22 pp) = 1.27 pages**, against 1.20 suggested.
Over by 0.07, which is inside the noise of the estimate.

| Component | Pages |
|---|---|
| Title, abstract | 1.00 |
| 1 Introduction | 3.01 |
| 2 Review Methodology | 0.60 |
| 3 and subsections | 3.44 |
| 4 and subsections, 2 tables | 4.11 |
| 5 Models as Annotation Instruments | 0.93 |
| 6 Evaluating Annotation Reliability, 1 table | 1.27 |
| **Committed** | **14.36** |
| References, 45 entries at 8pt | 1.73 |
| **Left for Sections 7 and 8** | **3.91** |

The plan wanted 3.30 for Section 7 and 0.70 for Section 8, which is 4.00. There is 3.91 left, so the
two of them need to come in about 0.09 pages under plan. That is one sentence.

---

# Part D — What Section 7 inherits

Five open questions now, each one recorded in the section that raised it rather than invented at the end:

1. The independence premise behind consensus voting is asserted rather than measured on this material (4.3).
2. No peer-reviewed study adjudicates annotator disagreement on Malaysian code-mixed data (4.3).
3. No frequency measurement exists for particle use or phonetic spelling in Malaysian social media writing
   (3.2, 3.3).
4. Robustness to code-mixing is not predicted by pre-training volume, and nothing in the reviewed literature
   establishes what does predict it (5).
5. **New from Section 6:** no regional corpus reports a coefficient of a stated type for the task its labels
   are used for, and the class distributions these methods produce are the conditions under which any such
   coefficient is hardest to interpret. Minimum reporting standards and a coefficient appropriate to skewed
   data are both open.

Items 1, 2 and 5 are the research agenda promised in contribution 3. Items 3 and 4 are measurement gaps that
belong in the same section but under a separate heading, since they call for data collection rather than
methodological work.
