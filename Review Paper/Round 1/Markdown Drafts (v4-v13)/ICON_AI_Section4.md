# 4. Annotation Practice and Its Failure Modes

Section 3 described what makes Malaysian code-mixed text hard to label. This section examines what has been
done about it. The strategies reported in the reviewed studies are set out first, arranged by the trade-off
each one accepts. The distribution of labels they produce is examined next, and the practice of pooling
several annotators is examined last, because it is the remedy most often proposed, and the one the regional
evidence tests most directly.

## 4.1 Annotation strategies and the fidelity-scalability trade-off

For low-resource code-mixed text, label fidelity and scale pull against each other. A corpus can be labelled
carefully or it can be labelled in volume. The strategies in the literature are best read not as competing
solutions to one problem, but as different decisions about which of the two to give up. Read that way they
fall into three tiers.

The first tier is manual annotation by people. Two of the four regional corpora were built this way, and they
are the only two whose labels come from human judgement. Kasmuri and Basiron (2019) drew 5,849 sentences from
23 personal blogs, selected 4,191 for annotation, and retained 2,316 in the finished corpus, reporting κ =
0.83 for the judgement of whether a sentence was opinionated or factual. Kong et al. (2023) collected 108,246
tweets and manually annotated 11,568 of them into three sentiment classes, using three independent annotators
working from a written guideline. What both illustrate is the cost of the decision rather than a defect in the
method. Kasmuri and Basiron kept 40% of the sentences they started with, and Kong et al. labelled 11% of what
they collected. The labour that produces reliable labels is the same labour that prevents either corpus from
reaching the scale a general-purpose Manglish resource would require.

The second tier is semi-automated annotation, which trades in the opposite direction by using existing tools
to label at volume and accepting the tools' limitations as the price. Mohd Shamsuddin et al. (2024) built
MESocSentiment this way. They collected 229,566 tweets carrying the "#Malaysia" keyword, reduced the set to
138,646 in pre-processing, applied the Malaya and Lingua libraries to identify code-switched posts, and
arrived at 20,226 tweets. Sentiment labels were then assigned by majority vote among three existing analysers.
The authors state the motivation plainly. The language identification libraries "reduced the need to find
fluent speakers in Malay and English to classify the tweets", and the sentiment analysers "eliminated the need
to find speakers fluent in Malay and English to label the dataset". The reasoning is defensible, and there is
evidence from other labelling tasks that automated annotators can match or exceed human crowd workers (Gilardi
et al., 2023). What the tier concedes is that the labels can be no more competent than the tools producing
them, and inherit whatever those tools cannot read.

The third tier replaces those tools with generative models used directly as annotators. Because a generative
model is not restricted to a fixed vocabulary, it can in principle interpret an unfamiliar spelling or an
unseen slang term from context, which is the capability the second tier lacks. In principle this dissolves the
trade-off. The peer-reviewed evidence does not yet support that reading. Jadhav et al. (2025) evaluated
generative annotators on Marathi across four tasks: sentiment analysis, two-class hate speech detection, four-
class hate speech detection, and news classification. They found GPT-4o and Llama 3.1 405B trailing a fine-
tuned BERT baseline by average accuracy margins of 10.2% and 14.1% respectively. They conclude that fine-tuned
transformers remain necessary where linguistic resources are scarce. Marathi is morphologically rich where
Malay is not, so the result bounds the tier's promise rather than measuring it in this setting. That it is the
only peer-reviewed study of the question available to this review is itself part of the finding. The third
tier is the least evidenced of the three, and no published study evaluates generative annotation on Malaysian
code-mixed text.

**Table 1.** Annotation strategies for Malaysian Malay-English code-mixed sentiment data

| Tier | Regional example | Scale achieved | Evidence of fidelity | What is conceded |
|---|---|---|---|---|
| Manual | Kasmuri and Basiron (2019) | 2,316 sentences retained from 5,849 candidates, drawn from 23 blogs | κ = 0.83, for a binary opinionated-or-factual judgement | Scale |
| Manual | Kong et al. (2023) | 11,568 tweets annotated from 108,246 collected | Three annotators and a written guideline; no coefficient reported | Scale |
| Semi-automated | Mohd Shamsuddin et al. (2024) | 19,714 posts from 229,566 collected | None reported; the pipeline has no human annotation stage | Demonstrable fidelity |
| Fully automated, generative | None published for Malay-English | — | — | Reliability precisely where linguistic resources are scarce (Jadhav et al., 2025) |

Read across the rows, each tier resolves one constraint by giving up another, and the concession follows from
what the strategy is rather than from how carefully it was carried out. No strategy in the reviewed literature
secures fidelity and scale together for this data.

## 4.2 Two causes of neutral-label skew

The clearest regional evidence of what the second tier costs is the class distribution of the corpus it
produced. MESocSentiment is labelled 78.23% neutral, 16.33% positive and 5.44% negative across 19,714 posts
(Mohd Shamsuddin et al., 2024). Section 1 gave two reasons for reading that distribution as an artefact of the
labelling method rather than a property of Malaysian discourse. This section separates the two distinct causes
at work in it, because they produce identical labels and require opposite responses.

The first cause is the behaviour of a scoring function that finds nothing to score. Lexicon-based sentiment
tools work by matching each word or phrase in a text against a sentiment lexicon and aggregating the scores of
the matched words into an overall score (Selvaraju et al., 2024). That score is then divided into classes by
threshold. VADER, one of the three analysers used to build MESocSentiment, sets its classification thresholds
at −0.05 and +0.05 on a normalised score running from −1 to 1 (Hutto and Gilbert, 2014). Two consequences
follow from combining those two facts, and this review states them as an inference rather than as a reported
finding. A text whose affective tokens are absent from the lexicon contributes little or nothing to the
aggregate. Its score therefore stays inside the neutral band, and it is returned as neutral. On that reading,
neutral is not always a judgement that a text is affectively balanced. It can also be the default output when
nothing was recognised.

The corpus authors' own error analysis indicates that the mechanism fires on this data. Alongside the corpus,
Mohd Shamsuddin et al. (2024) present two small tables comparing the ensemble's label with the correct one.
All three of the misclassified examples they give are neutral labels that should have been positive, and in
all three the sentiment is carried by Malay: *memang cantik sangat*, *selamat deepavali* and *raih gelar
juara*. In the correctly classified negative example, the sentiment is carried by an English word,
*worthless*. Six author-selected examples are illustrative rather than statistical, and no error rate can be
computed from them. Their uniformity is nonetheless difficult to dismiss: where the ensemble succeeded, the
affect was in a language its tools covered, and in every case where it failed, the affect was not.

The second cause has nothing to do with tooling. Some posts are genuinely hard to judge, and the annotators of
the regional corpora say so. Kasmuri and Basiron (2019) note that low agreement in sentiment annotation arises
because sentiment texts are subjective, so evaluations differ from one annotator to another and are shaped by
each annotator's background. Kong et al. (2023) make the same point about their own task, observing that
tagging text with sentiment labels is highly subjective and influenced by personal beliefs, and that a clear
guideline is needed for this reason. As Section 3.2 established, disagreement of this kind is not removed by
collecting more judgements (Pavlick and Kwiatkowski, 2019).

Separating the two causes matters because the labels they produce are indistinguishable and the responses they
require are opposite. A genuinely neutral post is correctly labelled and belongs in the corpus. A falsely
neutral post is an error that a better-resourced annotator would not have made. A single-model pipeline is
structurally unable to tell them apart, because the evidence that would distinguish them, namely the affect
the annotator could not read, is exactly the evidence that annotator does not have.

The consequence is more damaging than the headline percentage suggests, because a false neutral does not only
inflate one class. It also depletes another. Every strongly polarised post absorbed into the neutral class is
a training example removed from a minority class that a downstream classifier needs most. At a 5.44% negative
share, the smallest class in the corpus is also the one most exposed to that erosion.

## 4.3 What consensus does with disagreement

Pooling several annotators is the intuitive remedy for an unreliable one, and MESocSentiment is evidence
against the intuition, because it already was a consensus pipeline. Three sentiment analysers labelled every
post and the majority label was assigned. The corpus skewed anyway.

The reason is visible in the corpus authors' own reporting, and it is not the one that might be expected.
Voting cancels error only to the extent that voters fail independently, and the usual guarantee of
independence is architectural difference. Table 2 shows that architectural difference was present and did not
help.

**Table 2.** The three annotators used to build MESocSentiment, and the labels each assigned (Mohd Shamsuddin et al., 2024)

| Analyser | How the corpus authors describe it | Languages it is described as covering | Neutral labels assigned, of 19,714 |
|---|---|---|---|
| TextBlob | "a Python library used to process textual data" | Not stated | 14,305 (72.6%) |
| VADER | "a rule-based model … made to focus on social media texts" | Not stated | 13,115 (66.5%) |
| pysentimiento | A toolkit "trained for sentiment analysis in English, Spanish, Portugeuse, and Italian" | English, Spanish, Portuguese, Italian | 16,916 (85.8%) |
| Majority vote | — | — | 15,422 (78.2%) |

Two things follow. The first is that every analyser skewed neutral before any vote was taken, so the skew was
not produced by the voting rule. The second is that the analyser skewing hardest, at 85.8%, is pysentimiento,
which is the transformer-based tool of the three. The shared weakness is therefore not shallow processing,
since the deepest model performed worst. None of the three is described by the corpus authors as covering
Malay, and one is explicitly described as trained on four other languages. The property the three voters share
is the language they cannot read, and a Malay affective token invisible to one is invisible to all. The
ensemble does not cancel that error. It ratifies it, and unanimity produced this way is indistinguishable from
confidence.

The second weakness concerns the posts the ensemble cannot agree on. Where all three analysers returned
different labels there was no majority, and the authors state their response directly: ambiguous cases "were
removed to ensure the corpus only contains tweets from absolute categories". This affected 512 posts, or 2.53%
of the 20,226 labelled. The difficulty is not the proportion but the composition. A post on which three
analysers disagree is one where the signal is contested, or is carried by material none of them reads
confidently. That description fits the heavily code-switched and particle-laden cases Section 3 identified as
the hard core of the problem. The rule therefore removes the examples a robust classifier would most need, and
removes them systematically rather than at random.

The effect on the corpus can be computed from the paper's own tables, and it runs in the wrong direction.
Removing the contested posts left the neutral count unchanged at 15,422 while reducing the total from 20,226
to 19,714, so the neutral share rose by roughly two percentage points. Taken with the first weakness, static
voting has a double effect: it keeps the labels it is confident about and wrong about, and deletes the ones it
is uncertain about and would have learned from.

The methodological literature on annotation supports treating that deletion as a loss rather than a cleanup.
Uma et al. (2021) survey learning from disagreement and question the assumption that a single correct
interpretation exists for every item. They report that models trained on the full distribution of annotator
judgements can outperform models trained on aggregated or even gold labels. On that view, the 512 discarded
posts were not noise removed from the corpus but signal removed from it.

What the reviewed literature does not contain is any evaluation of a better procedure on this data. No
published study adjudicates annotator disagreement on Malaysian code-mixed sentiment text, and the premise
that annotators of different types fail independently, which is what licenses aggregation in the first place,
is asserted rather than measured on this material. The evidence assembled above suggests that independence
fails when the annotators share a language gap, but a suggestion is not a measurement and this review does not
treat it as one. Both points are recorded here and returned to in Section 7 as questions for future research.

---
---

# Part A — Three corrections to the v3 Section 4 material

Everything below came out of reading the PDFs. All three would have been visible to Dr. Ho.

## Correction 1 — the ensemble argument was wrong, and the right one is better

The v3 draft said the three voters fail together because they "all resolve sentiment through surface lexical
matching". **Table 8 of Mohd Shamsuddin et al. (2024), which the draft never used, contradicts that.** It
reports each analyser's own output before voting:

| | TextBlob | VADER | pysentimiento | Majority vote |
|---|---|---|---|---|
| Neutral labels, of 19,714 | 14,305 | 13,115 | 16,916 | 15,422 |
| Share | 72.6% | 66.5% | **85.8%** | 78.2% |

Every voter already skewed neutral before any vote was taken, and **pysentimiento — the transformer-based
tool, the deepest of the three — skewed hardest.** "Shallow lexical processing" cannot explain that.

What can: none of the three is described by the corpus authors as covering Malay. Their own words — VADER is
"a rule-based model … made to focus on social media texts", pysentimiento is "trained for sentiment analysis
in English, Spanish, Portugeuse, and Italian". The shared blind spot is **language coverage, not
architecture.** That is a sharper claim, it is sourced entirely from the corpus paper, and it explains the
one figure the old argument could not.

## Correction 2 — three sources were arXiv preprints

Negi et al. (2026) is arXiv:2601.16800 with no published version. Niimi (2024) is arXiv:2407.13069 and the
PDF is stamped "A PREPRINT". Ahtisham et al. (2026) could not be verified at all. Section 2 tells Dr. Ho
that every source cited is peer-reviewed, so citing them would have made that sentence false.

All three are out. The disagreement argument in 4.3 now rests on **Uma et al. (2021), "Learning from
Disagreement: A Survey", JAIR 72, 1385–1470** — peer-reviewed, and a source Negi himself cites. It is
stronger scaffolding than a single preprint: it establishes that discarding disagreement discards signal,
which is exactly what the 512 deleted posts represent.

The cost is real and 4.3 states it rather than hiding it: with the preprints gone, **no peer-reviewed study
adjudicates annotator disagreement on Malaysian code-mixed data.** That absence is now reported as a finding
and handed to Section 7.

## Correction 3 — VADER does not say what the draft claimed

The v3 draft cited Hutto and Gilbert (2014) for the claim that a post containing no recognised sentiment
token "scores exactly zero, and zero falls inside the neutral band by construction". **The paper does not
say this.** It states the thresholds — "classification thresholds set at –0.05 and +0.05 for all normalized
sentiment scores between -1 and 1" — but it never describes how the compound score is computed, and never
addresses what happens when no lexicon words are found.

Section 4.2 now builds the mechanism from two cited premises and labels the join as the review's own
inference: lexicon tools aggregate only the scores of *matched* words (Selvaraju et al., 2024), and VADER
thresholds at ±0.05 (Hutto and Gilbert, 2014). The conclusion follows, and the text says "this review states
them as an inference rather than as a reported finding". That phrasing is the honest answer to a "Citation?"
in the margin.

---

# Part B — What was verified, and where

| Claim | Source | Verified |
|---|---|---|
| 229,566 collected → 138,646 after pre-processing → 20,226 after language ID → 19,714 final | Mohd Shamsuddin et al. (2024) | ✅ all four figures verbatim |
| 78.23 / 16.33 / 5.44 over 19,714 | Table 4 | ✅ |
| 512 contested posts, 2.53% | Table 3 | ✅ |
| Neutral count 15,422 unchanged; total falls 20,226 → 19,714 | Tables 3 and 4 | ✅ computed from the paper's own counts, avoids the 76.23 vs 76.25 discrepancy in their Table 3 |
| "Ambiguous cases were removed to ensure the corpus only contains tweets from absolute categories" | | ✅ verbatim |
| "reduced the need to find fluent speakers…" / "eliminated the need to find speakers fluent…" | | ✅ both verbatim |
| Three misclassified examples all false neutrals, all carrying polarity in Malay | Table 7: *memang cantik sangat*, *selamat deepavali*, *raih gelar juara* | ✅ — the draft was right, it was just pointing at Table 5 |
| Correctly classified negative carries polarity in English | Table 6: *worthless* | ✅ |
| Per-analyser neutral counts | Table 8 | ✅ (new — see Correction 1) |
| κ = 0.83, binary opinionated-or-factual | Kasmuri and Basiron (2019) | ✅ |
| 5,849 → 4,191 selected → 2,316 retained, from 23 personal blogs | Kasmuri and Basiron (2019) | ✅ — note the source is blogs, not social media |
| 108,246 collected, 11,568 annotated, three independent annotators, written guideline | Kong et al. (2023) | ✅ |
| Kong et al. report no agreement coefficient | | ✅ zero hits for kappa / inter-annotator / inter-rater in the paper |
| Neutral 2,728 of 11,568 = 23.6% | Kong et al., MyCovid-Senti class table | ✅ — this confirms the 23.6% used in the Introduction, which was computed rather than printed |
| Sentiment annotation is subjective and varies by annotator background | Kasmuri and Basiron (2019); Kong et al. (2023) | ✅ both state it about their own task |
| Lexicon tools aggregate scores of *matched* words | Selvaraju et al. (2024) | ✅ verbatim |
| ±0.05 thresholds | Hutto and Gilbert (2014) | ✅ verbatim |
| GPT-4o −10.2%, Llama 3.1 405B −14.1% vs fine-tuned BERT, Marathi, four tasks | Jadhav et al. (2025) | ✅ |
| Disagreement is signal; soft labels can beat aggregated or gold labels | Uma et al. (2021) | ✅ |

**Still unverified:** Gilardi et al. (2023). PNAS and the Zurich repository both block automated access. It
supports one clause — that automated annotators can match crowd workers on other tasks — which is the claim
in the paper's own title, so the risk is low. Worth downloading anyway.

**Not needed after all:** Chakravarthi et al. (2022). The second cause of neutral-label skew is now carried
by Kasmuri and Basiron (2019) and Kong et al. (2023), who both say it about their own annotation task. Those
are regional and verified, which is better for a Malaysian review than a Dravidian dataset paper. Add
Chakravarthi later if you want the sharper "neutral and mixed-feelings are the hardest categories" claim.

---

# Part C — New references

Four added. Sections 1 to 4 now cite **35 sources**, all peer-reviewed.

Gilardi, F., Alizadeh, M., and Kubli, M. (2023). ChatGPT outperforms crowd workers for text-annotation tasks. *Proceedings of the National Academy of Sciences*, 120(30), e2305016120. https://doi.org/10.1073/pnas.2305016120

Hutto, C. J., and Gilbert, E. (2014). VADER: A parsimonious rule-based model for sentiment analysis of social media text. *Proceedings of the International AAAI Conference on Web and Social Media*, 8(1), 216–225.

Jadhav, S., Shanbhag, A., Thakurdesai, A., Sinare, R., and Joshi, R. (2025). On limitations of LLM as annotator for low resource languages. *Proceedings of the 8th International Conference on Natural Language and Speech Processing (ICNLSP-2025)*, 277–282.

Uma, A. N., Fornaciari, T., Hovy, D., Paun, S., Plank, B., and Poesio, M. (2021). Learning from disagreement: A survey. *Journal of Artificial Intelligence Research*, 72, 1385–1470. https://doi.org/10.1613/jair.1.12752

---

# Part D — Page budget

Section 4 came in at **1,939 prose words (3.61 pp) plus two tables (~0.50 pp) = 4.11 pages**,
against the 4.5 allocated.

| Component | Pages |
|---|---|
| Title block | 0.50 |
| Abstract + keywords | 0.50 |
| 1 Introduction | 3.01 |
| 2 Review Methodology | 0.60 |
| 3 + 3.1 + 3.2 + 3.3 | 3.44 |
| 4 + 4.1 + 4.2 + 4.3, incl. 2 tables | 4.11 |
| **Committed so far** | **12.16** |
| References, 45 entries at 8pt | 1.73 |
| **Left for Sections 5 to 8** | **6.11** |

The plan wanted 7.00 pages for Sections 5 to 8, so they need to come in about 0.9 pages under it — a 13%
compression, against the 18% the arithmetic demanded before Section 4 was written. The gap is closing rather
than widening.

Suggested split for what remains: Section 5 (models as annotators) 0.90, Section 6 (evaluating reliability)
1.20, Section 7 (synthesis and research agenda) 3.30, Section 8 (conclusion) 0.70. Section 7 keeps the most
because it carries contribution 3, the synthesis matrix and the research agenda, and because three separate
threads now hand it open questions: the untested independence premise from 4.3, the absent adjudication
evidence from 4.3, and the missing frequency measurement for particles and spelling from 3.2 and 3.3.
