# Where to cut two pages — Sections 1 to 7

**Current:** 21 pages. Body runs to about one third down page 20; references occupy the
remaining 1.67 pages. Body ≈ 19.3 pages, 10,591 words in total, ~36 references.

**Target:** 19–19.5 pages with room for more references.

**The arithmetic.** Cut **2 pages of body** and you land on exactly **19.0 pages**. That leaves
**0.5 page of headroom** before 19.5 — enough for roughly **12 additional references** at this
type size. Getting from 36 to 40 costs only 0.18 page, so Dr. Ho's request is comfortably met.

A full text page in this template is **~550 words**. Two pages ≈ 1,100 words. The plan below
removes **~740 words of prose** and recovers **~0.55 page of white space**, which comes to
**~1.9–2.1 pages**.

---

## Before anything else: 11 broken cross-references

Deleting Section 2 (Review Methodology) shifted every section number down by one, and only some
of the references were updated. **Fix these first — they cost nothing and Dr. Ho will spot them
before he reads a sentence.**

| Page | Currently says | Should say |
|---|---|---|
| 4 | "and **Section 8** concludes the review" | Section 7 |
| 4 | "**The studies selected under these criteria** describe a body of text…" | criteria no longer exist — see below |
| 8 | "**Section 4** examines the annotation strategies used in response" | Section 3 |
| 9 | "no study meeting **the criteria in Section 2**" | see below |
| 11 | "As **Section 3.2** established, disagreement of this kind is not removed…" | Section 2.2 |
| 12 | "cases **Section 3** identified as the hardest to annotate" | Section 2 |
| 13 | "No study retrieved by **the search described in Section 2**" | see below |
| 13 | "returned to in **Section 7** as questions for future research" | Section 6 |
| 14 | "**Section 4.1** described the capability…" | Section 3.1 (there is no Section 4.1) |
| 15 | "**Section 4** established that the labelling methods… produce heavily skewed class distributions" | Section 3 |
| 16 | "**Section 3** established three properties of this text" | Section 2 |
| 18 | "**Section 5** showed that a fine-tuned encoder resolves only the variation it has been shown" | Section 4 |
| 18 | "which is precisely the ambiguity **Section 3.2** identified" | Section 2.2 |

### The three that need more than a number change

Pages 4, 9 and 13 point at a search protocol that no longer exists. Two options:

**Option A (recommended, ~40 words).** Dr. Ho objected to the *section*, not to the fact that
you searched. Add two sentences to the scope paragraph in Section 1:

> "The literature examined here was identified through searches of the ACL Anthology, IEEE
> Xplore, Scopus and arXiv, combining terms for the language variety, the sentiment task and
> annotation quality. Studies that only benchmark classifiers, with no annotation or reliability
> component, were not included."

That keeps your "no study…" claims checkable rather than asserted, and fixes all three at once.
Then change page 9 to "no study examined here evaluates generative annotation on Malaysian
code-mixed text" and page 13 to "No study examined here adjudicates annotator disagreement…".

**Option B (0 words).** Drop the grounding entirely: page 4 becomes "The text reviewed here has
linguistic properties that shape every later stage of the review…", and pages 9 and 13 become
"no study examined here…". Cheaper, but your three "no study exists" claims then rest on nothing
a reader can verify.

---

# The cuts, largest first

## Cut 1 — The three-findings preview in the Introduction ⟶ saves ~300 words (0.55 page)

**Pages 3–4, 542 words.** From *"This review indicates that for Malaysian Malay-English…"*
through *"…code-mixed Malay text (Selvaraju et al., 2024)."*

This is the single biggest redundancy in the paper. Every one of these four paragraphs is
delivered a second time, in full, later on:

- Finding 1 → Section 5 and Table 3
- Finding 2 → **Section 3.2 opens with the identical figures** (78.23% / 16.33% / 5.44%)
- Finding 3 → **Section 5 opens with the identical Cohen's κ definition**
- The prevalence paragraph → **Section 5 (pages 14–15) with the Feinstein worked example, and
  again as the fifth link in Section 6**

Replace all four paragraphs with:

> This review indicates that for Malaysian Malay-English code-mixed sentiment data, the
> annotation label is at present the more limiting problem, together with the evidence offered
> that the label is sound. Three findings support that reading, and each is developed in the
> sections that follow. First, none of the four existing Malay-English sentiment resources is
> simultaneously large, balanced across sentiment classes, drawn from casual social media and
> validated by human annotators; each secures some of these properties at the expense of the
> others. Second, the class imbalance in the largest of them originates in the labelling method
> rather than in Malaysian discourse. Third, annotation reliability is rarely reported, and where
> a coefficient is given it was obtained for a narrower task than the corpus is used to support.
>
> The second and third findings describe one condition rather than two. The skew the labelling
> methods produce is itself the condition under which a chance-corrected coefficient becomes
> difficult to interpret, so correcting either weakness alone leaves the other in place. A 2024
> review of the field still reports a lack of comprehensive datasets and annotated resources for
> code-mixed Malay text (Selvaraju et al., 2024).

**185 words. Saves 357.**

**Then repair Section 3.2 (page 10), which currently says "Section 1 gave two reasons…".** Move
the two reasons to where they belong (+60 words):

> …MESocSentiment is labelled 78.23% neutral, 16.33% positive and 5.44% negative across 19,714
> posts (Mohd Shamsuddin et al., 2024). **Two reasons support reading that distribution as an
> artefact of the labelling method rather than a property of Malaysian discourse. The corpus was
> collected under the "#Malaysia" keyword across sports, politics and the arts, which are not
> topics on which social media users are typically neutral. A comparable corpus of Malaysian
> tweets labelled by human annotators is only 23.6% neutral (Kong et al., 2023).** This section
> separates the two distinct causes at work in that skew…

**Net saving: ~297 words.**

---

## Cut 2 — The Conclusion restates the findings a third time ⟶ saves ~166 words (0.30 page)

**Pages 19–20.** The three findings now appear in the abstract, in the Introduction, and again
here. Two are enough.

**Delete the second paragraph entirely (116 words):** *"Three findings support that reading. The
review found no available Malay-English sentiment resource that is at once large… than the corpus
is used to support."*

The paragraph that follows it already carries the same content in the stronger, relational form
that is your actual contribution.

**Then trim that following paragraph from 160 to ~110 words.** It restates the six links of
Section 6 one by one. Compress to:

> The contribution this review claims is not any of those findings taken alone but the relation
> between them. The linguistic properties of the text produce disagreement that is systematic
> rather than random, which makes fluent bilingual annotation necessary and expensive, which is
> why labelling is automated. The tools available for that automation cover neither Malay nor
> Manglish, so pooling them ratifies a shared error instead of cancelling it. The class skew that
> results is the precise condition under which the standard agreement coefficient stops returning
> interpretable values, so the defect and the inability to detect it have one cause rather than
> two. Each corpus built this way then trains the annotators that build the next. An intervention
> at any single point is assessed by an instrument compromised at another, which is why competent
> work at each link has not accumulated into progress.

---

## Cut 3 — Two links in Section 6 re-narrate evidence already given ⟶ saves ~88 words (0.16 page)

The synthesis should assert the connection, not re-present the proof.

**Third link (page 17, 115 words → 65).** Three of its sentences are near-verbatim from page 12.

> The third link runs from automation to a shared limitation. The tools available for automation
> are those built for well-resourced languages. Section 3.3 documented the one regional case:
> none of the three analysers covers Malay, each skewed neutral before any vote was taken, and
> voting cancels error only to the extent that voters fail independently. Where the property they
> share is the language none of them reads, the ensemble ratifies the error instead of cancelling
> it.

**Fourth link (page 17, 123 words → 85).** Drop the sentence that announces it is repeating
itself — *"Section 3.2 separated the two mechanisms that produce this, but one of them should be
restated here, because it is the point at which the process becomes self-reinforcing"* — and go
straight to the 512 removed posts, which is the only part doing new work.

---

## Cuts 4–9 — Small duplications ⟶ saves ~186 words (0.34 page)

| # | Page | What | Fix | Saves |
|---|---|---|---|---|
| 4 | 9 | **"Marathi is morphologically rich where Malay is not, so the result bounds the tier's promise" appears twice**, four sentences apart | Delete the first occurrence; keep the later one ("…rather than measuring it in this setting") | 25 |
| 5 | 8–9 | Two quotes saying the same thing: libraries *"reduced the need to find fluent speakers…"* and analysers *"eliminated the need to find speakers fluent…"*. The second is quoted **again** on page 17 | Keep one quote only | 28 |
| 6 | 5 & 6 | The Treffers-Daller **spoken-corpus caveat is given twice** — "recorded from two teachers" (§2.1) and "fifteen hours of recorded teaching by each of two university English lecturers" (§2.2) | Keep the fuller §2.2 version; reduce §2.1 to a clause: "…though the corpus is spoken classroom data, so the exact proportions should not be transferred to social media text." | 35 |
| 7 | 6 | The same 121 discourse markers counted **two ways**: 11.6% of utterances, then 9.9% of individual switches | Keep one. The utterance figure is the one the argument uses | 38 |
| 8 | 7 | The *tidak → x* and *tidak ada → takde/xde/tade* examples already appear on page 2 | Drop the repeated pair; keep *macam mana*, *besaq/beso*, *x suko* | 30 |
| 9 | 13 | The Uma et al. (2021) point ("models trained on the full distribution… can outperform models trained on aggregated labels") is repeated **verbatim** as Direction 4 on page 19 | Shorten the §3.3 version to one sentence; keep Direction 4 in full | 30 |

---

## Layout recovery ⟶ ~0.55 page, no words cut

**Page 9 is about 35% white.** Section 3.1 ends at 376 words and Table 1 is pushed to page 10.
Once Cut 1 pulls everything up by half a page, check whether Table 1 now fits on page 9 — if it
does, that gap closes for free. If it does not, tighten Table 1's cells so it fits: "2,316
retained of 5,849 candidates, 23 blogs" instead of the current full sentences, and "Reliability,
where linguistic resources are scarce (Jadhav et al., 2025)" for the last cell.

**Tables 1 and 3 have narrow columns that force tall wrapped cells.** In Table 3 the
SentiBahasaRojak row alone is five lines deep because "Whether a stock-market post is positive or
negative; reported for the stock review subset only" is wrapping in a narrow column. Widen the
last column, narrow "Written guideline" (its entries are one or two words), and the row height
drops by half.

**Figure 1** and its caption take about 40% of page 16, which holds only 366 words. Reducing the
figure height by 20% is invisible to the reader and buys a few lines.

---

## If you still need more

1. **The numbered contributions list in the Introduction (111 words, page 4)** is near-verbatim
   with the abstract's "Three contributions follow. First… Second… Third…". Reducing it to one
   sentence saves ~70 words. Listed last because the numbered form is easier for a reviewer to
   scan than the abstract's prose, so this is a real trade.
2. **The scope-exclusion paragraph (48 words, page 4)** — *"The scope of this review also excludes
   several activities…"* — partly repeats the paragraph immediately above it, which already places
   benchmarking and general sentiment analysis outside the scope. Merging the two saves ~30 words.

---

## What not to cut

- **The four "Two limits on this evidence should be noted" paragraphs.** These are the clearest
  evidence in the paper that you read the sources critically rather than summarising them. Cut 6
  above removes only the duplication *between* two of them, not the paragraphs.
- **The Feinstein and Cicchetti worked example (page 14)** — κ = 0.70 versus κ = 0.32 at the same
  85% observed agreement. It is the paper's single best concrete demonstration, and the fifth link
  and Section 7 both depend on the reader having seen it.
- **Section 4 (Models as Annotation Instruments)** is already the shortest section at ~750 words.
- **Table 2** — it is the only place the analyser-by-analyser neutral rates appear, and the third
  link, Section 3.3 and the conclusion all rest on them.

---

## Order of work

1. The 13 cross-references (15 minutes, zero risk)
2. Cut 1 — Introduction preview, plus the Section 3.2 repair
3. Cut 2 — Conclusion
4. Cuts 4–9 — the small duplications, by Ctrl+F
5. Cut 3 — Section 6 links
6. Re-check page 9 and the two tables **after** the text has reflowed
7. Read the page count. If it is 19.0, add references until 19.5.
