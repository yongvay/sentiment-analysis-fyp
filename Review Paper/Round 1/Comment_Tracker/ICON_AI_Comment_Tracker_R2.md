# Dr. Ho — Round 2 comments on Sections 1 to 3.1 (64 comments)

Extracted from the PDF annotations in `Template ICON AI 2026 - Section 1 to 3.1 (reviewed).pdf`.
Numbered in document order: comments 1–21 on page 2, 22–44 on page 3, 45–54 on page 4, 55–64 on page 5.

**Round 1 had 80 comments on the v3 draft. Round 2 has 64 on a much shorter extract.** Do not read that as
regression. Round 1 was dominated by formatting (20 comments on bold alone) and structural problems, all of
which are gone. Round 2 is almost entirely sentence-level: register, ambiguous referents, and unsupported
claims. That is a different and later kind of problem, but there are enough of them that the same reading
would produce the same volume of comments on Sections 3.2 to 8 unless the rules below are applied there too.

---

# Part 1 — The twelve rules

This is the part to re-read before writing anything new. Each rule is followed by the comment numbers that
produced it, so you can see the evidence.

## Rule 1 — Citation format is author–date, and the author's name is never doubled

*Comments 1, 10.*

Dr. Ho wrote the format he wants, twice:

- Parenthetical: `(Poria et al., 2023)`
- Narrative: `Treffers-Daller et al. (2022)`

The placeholder form `Treffers-Daller et al. [Treffers-Daller et al. (2022)]` prints the name twice and must
never appear again. Multiple sources in one bracket are separated by semicolons: `(Poria et al., 2023; Nazir
et al., 2022)`, not `[Poria et al. (2023)], [Nazir et al. (2022)]`.

> **Flag for supervision.** The ICON AI template §11 says *"References should be numbered and cited within
> the square brackets in order of appearance in the text"*, and your v2 draft was converted to `[n]` on that
> basis. Dr. Ho has now told you author–date twice, in writing, while looking at the draft. The rewrite
> follows Dr. Ho. Confirm with him in one line so the decision is on record, because converting the finished
> paper either way is a mechanical but tedious pass.

## Rule 2 — Any statement about what other researchers do, find, or fail to do needs a citation

*Comments 2, 12, 15, 19, 20, 23, 40, 44, 62, 64 — ten comments, the second-largest group.*

The trigger words are the giveaway: *most*, *usually*, *commonly*, *the literature*, *the field*, *normally*,
*is often treated as*. Every one of these is an empirical claim about a body of work, and every one needs
either a survey or several primary studies behind it.

Two of the ten are worth singling out, because they show the standard is higher than "cite something nearby":

- **Comment 20** flagged *"Before a model can be trained or evaluated, every message must be read and given a
  sentiment label"* — a statement so basic it feels like it needs no source. It still needs one.
- **Comment 62** flagged *"The corpus consists of spoken data from two teachers"* — a fact taken straight out
  of Treffers-Daller et al. (2022), sitting two sentences after a citation to that same paper. The citation
  has to be **on the sentence making the claim**, not merely nearby.

## Rule 3 — Register: the informality rule, and the list of phrases that triggered it

*Comments 4, 18, 21, 22, 24, 28, 30, 31, 32, 33, 47, 50, 53, 57, 59, 60, 61, 63 — eighteen comments, the
largest single group.*

Eight of these say nothing but "Informal…" or "Slightly informal…". The pattern is consistent: **plain English
is not the same as conversational English.** Dr. Ho asked in Round 1 for simple, clear sentences; he did not
ask for spoken register. Short words are good. Phrasal verbs and physical metaphors for abstract relations
are not.

| Flagged | Use instead |
|---|---|
| This **carries over** to social media | On social media in particular / This extends to |
| A second part of the problem **sits earlier** | arises earlier / occurs earlier |
| a Malay noun phrase **sits inside** an English question | is embedded within |
| label errors do not **stay inside** the dataset | the consequences are not confined to the dataset |
| **judge how good the model is** | evaluate model performance *(his own suggested wording)* |
| the **limits of this route** | the limitations of this approach |
| pre-training **on its own** | pre-training alone |
| **giving up** the others / by **giving up** the other | at the expense of / at the cost of |
| the **same kind of text** | the same text type / comparable text |
| **how often they agree**, after subtracting chance | a chance-corrected agreement coefficient |
| this evidence is **thin** | this evidence is limited / sparse |
| which is **unsurprising** because | an omission that follows from, since |
| **It is also useful to state what this review does not do.** | The scope of this review also excludes several activities. *(his own wording)* |
| **simply occurring together** | merely co-occurring |
| a person **or a program** that has been asked to assign a label | the annotator, whether human or automatic |
| switching **happens mostly** inside the clause | occurs predominantly within the clause |
| with almost no grammatical **friction** | with minimal grammatical adjustment |
| **audits** what the corpora report | examines what the corpora report |

Note the last one. Comment 52 says *"This sounds accounting-oriented"* — "audit" is a real term of art in
data-quality work, but he does not read it that way, and arguing the point in a supervisor draft is not worth
the ground.

## Rule 4 — Never let a demonstrative point backwards on its own

*Comments 6, 11, 13, 14, 35, 37, 38, 43, 45, 58 — ten comments.*

"This", "these", "the argument", "the problem", "the field", "the resources", "both" — each one made him stop
and ask what it referred to.

| Flagged | The question he asked | Fix |
|---|---|---|
| **This kind of writing** is common on X | "What do you meant by this kind of writing?" | Malay-English mixed writing |
| the difficulty **this text** creates | "Language or text?" | Malay-English mixed writing |
| performs poorly on **this material** | "What do you meant by this material?" | on Malay-English mixed text |
| **The argument** is that the model cannot… | Is this the same argument as the next one? | On that account, the model cannot… |
| the task **the resources** are actually used for | "What resources are you referring to?" | those two resources |
| **The field** therefore lacks | "What do you meant by the field?" | Research on Malaysian code-mixed sentiment |
| **These two weaknesses** are connected | The two are two paragraphs apart | Name both in the sentence |
| why **the problem** has proved persistent | "Which problem?" | why reliable annotation … remains unachieved |
| because **both** have already been surveyed | "Both" = which two things? | Name the two, then say "Both" |
| and **is not developed further** | "What is not developed further?" | the linguistic description itself |

The rule that covers all ten: **if a reader has to look up to find the referent, name it instead.** In a paper
this dense, that is roughly every demonstrative.

## Rule 5 — Introduce every abbreviation, symbol, statistic and platform on first use

*Comments 7, 36.*

- **X** — "What is X? For those who are not familiar with it, it is better to introduce it once." → *X, the
  platform formerly known as Twitter*.
- **κ** — "What is ϰ? Not everyone knows that this is Cohen's kappa." → define Cohen's kappa (κ) before the
  first numeric value, and cite Cohen (1960).

Applies equally to NLP, SVO, OOV, LLM, ABSA and anything else in Sections 3.2 to 8.

## Rule 6 — Do not overstate

*Comments 9, 16, 48, 59.*

- **"the best results"** → *"the strongest scores among the systems evaluated"*. His reasoning is worth
  keeping: *"if it is the best, then it means that it is perfect, and there will be no room for improvement."*
- **"a problem has resisted solution"** → *"remains unresolved"*.
- **"the switch point gives no structural cue"** → *"offers little reliable structural cue"*. Absolute
  negatives are claims, and claims need evidence.
- **"a language form"** → he offered *"legitimate language variety"*, which is stronger and also more precise.

## Rule 7 — Every change of topic or scale needs an explicit bridge

*Comments 2, 8, 13, 26, 38, 55.*

Six comments about transitions, at every scale:

- **General → Malaysian** (comment 2): "The last sentence creates a slightly abrupt jump from the general
  discussion of sentiment analysis to the Malaysian context."
- **Sentence → sentence** (comment 8): "Transition from the previous sentence to this one can be enhanced."
- **Evidence → conclusion** (comment 26): *"This review indicates"* jumps from general evidence about label
  noise to a specific claim about Malaysian data.
- **Section → section** (comment 55): Section 2 ends on selection criteria and Section 3 opens on linguistic
  difficulty, with nothing joining them.

Write the bridge as its own sentence. It costs fifteen words and removes the complaint.

## Rule 8 — State technical relationships exactly

*Comments 25, 41.*

Two places where the sentence was nearly right and therefore wrong:

- *"label errors distort the test set"* → **incorrect labels in a test set distort the evaluation of model
  performance.** The test set is not distorted; the measurement taken from it is.
- *"class imbalance that affects the labels"* → **class imbalance affects the distribution of labels**, not
  the labels themselves.

Check every causal sentence for the same slippage: is the thing you named actually the thing that changes?

## Rule 9 — Attribute positions to whoever holds them

*Comment 39.* "Who treat them as separate problems? You or existing studies?"

Never write *"X is usually treated as…"* without saying by whom. Either *"the studies reviewed here address
them separately"* or *"this review treats them as connected"* — but the sentence has to say which.

## Rule 10 — Split dense sentences; preview enumerated things by name

*Comments 34, 45, 49, 51, 56.*

- **Comment 45** — the scope sentence ran 47 words with an ambiguous "both". Split into three.
- **Comment 34** — *"The two resources that do report a coefficient measured a binary judgement rather than
  the three-class polarity task for which the resources are actually used."* He asked: "Do you think this
  sentence feels incomplete?" It is grammatical, but the contrast has no landing point.
- **Comment 56** — *"Three properties … affect the annotation task directly"* and then the reader has to keep
  reading to discover what they are. **Name all three in the opening paragraph.**
- **Comments 49, 51** — the contribution statements were too compressed to be clear.

> **Tension with Round 1 worth knowing about.** Round 1 comment 65 said the contribution statements must
> *not* carry technical mechanisms. Round 2 comment 51 says make the two causes of neutral-label skew
> explicit. These pull in opposite directions. The resolution used in the rewrite: name the two causes in
> ordinary language ("one produced by the labelling tools themselves, the other by genuine uncertainty among
> annotators") without naming the mechanism. Explicit, but no machinery.

## Rule 11 — Cite peer-reviewed work only

*Comment 54.* "If possible, try your best to not consider using any preprints from arXiv."

Sharper than Round 1 comment 69, which allowed preprints with traceable records. Treat it as absolute.
Searching arXiv is still legitimate and worth saying — it is where code-switching work appears first — but
nothing cited should stop there. All 29 sources now in Sections 1 to 3.1 are peer-reviewed.

## Rule 12 — A section opener bridges backwards and previews forwards

*Comments 55, 56.* Both land on the same paragraph. The template for every section opener from here on:

1. one sentence connecting to what the previous section established;
2. one sentence naming what this section covers, listing the items if there are enumerable ones;
3. one sentence saying what the section contributes beyond description.

---

# Part 2 — All 64 comments in document order

| # | Page | Highlighted | Dr. Ho's comment | Rule |
|---|---|---|---|---|
| 1 | 2 | `[Poria et al. (2023)]` | "You can consider to use this style: (Poria et al., 2023)" | 1 |
| 2 | 2 | "Most of these applications were built and tested on text written in one standard language. Malaysian social media text does not meet that condition." | Broad empirical claim, not self-evident, needs a review/survey or multiple studies. Second sentence needs a citation too. Transition not smooth; abrupt jump to the Malaysian context. | 2, 7 |
| 3 | 2 | `[Coluzzi (2017)]` | Fine to cite a 2017 paper, but there is a ten-year gap. Is 140 still valid? Add a more recent source on Malaysian code-mixing, but keep Coluzzi. | 2 |
| 4 | 2 | "This carries over" | "Feels informal as 'carries over' sounds conversational." | 3 |
| 5 | 2 | "English and Malay are the pair that meets most often in written form, mixed varieties that result are known locally as Bahasa…" | "Rewrite the highlighted part as it sounds weird and a little unnatural." | 3 |
| 6 | 2 | "This kind of writing" | "What do you meant by this kind of writing?" | 4 |
| 7 | 2 | "X" | "What is X? For those who are not familiar with it, it is better to introduce it once." | 5 |
| 8 | 2 | "Manglish … rather" | "Transition from the previous sentence to this one can be enhanced." | 7 |
| 9 | 2 | "language form … not random" | "legitimate language variety?" | 6 |
| 10 | 2 | `Treffers-Daller et al. [Treffers-Daller et al. (2022)]` | "Use this style: Treffers-Daller et al. (2022)" | 1 |
| 11 | 2 | "this text" | "What do you meant by text? Language or text?" | 4 |
| 12 | 2 | "the explanation usually given is architectural…" | "Citation?" | 2 |
| 13 | 2 | "this material" | "What do you meant by this material?" | 4 |
| 14 | 2 | "The argument" | Is this the previous sentence's argument? The same as the next one? Informal, and causes unnecessary confusion. Change how the idea is expressed. | 4 |
| 15 | 2 | "part of the literature … multilingual models" | "Citation?" | 2 |
| 16 | 2 | "the best" | "The best is not suitable because if it is the best, then it means that it is perfect, and there will be no room for improvement." | 6 |
| 17 | 2 | "The same literature" | "If you are referring to Adilazuarda et al. (2022), perhaps you can consider changing the way you refer to it." | 4 |
| 18 | 2 | "limits of this route", "pre-training on its own" | "Informal and less academic" | 3 |
| 19 | 2 | "Model choice is therefore part of the problem, but it is not all of it." | "Citation? If available…" | 2 |
| 20 | 2 | "Before a model can be trained or evaluated, every message must be read and given a sentiment label" | "Citation?" | 2 |
| 21 | 2 | "sits earlier in the process" | "Informal…" | 3 |
| 22 | 3 | "label errors do not stay inside the dataset" | "Informal…" | 3 |
| 23 | 3 | "Annotation quality matters because label errors … are learned by the model during training" | "Citation?" | 2 |
| 24 | 3 | "judge how good the model is" | "Informal… At least use 'evaluate model performance'" | 3 |
| 25 | 3 | "distort the test set" | "Test set itself is not necessarily distorted, but incorrect labels in the test set can distort the evaluation of model performance." | 8 |
| 26 | 3 | "This review indicates that for Malaysian Malay-English code-mixed sentiment data…" | Conclusion is understandable, but jumps from general evidence to a specific claim about Malaysian data suddenly. | 7 |
| 27 | 3 | "Two observations" | "Two observations from the existing literature?" | 9 |
| 28 | 3 | "Each resource obtains some of these properties by giving up the others" | "Understandable but slightly informal…" | 3 |
| 29 | 3 | "shows the cost most clearly" | "This is ambiguous. Cost of what?" | 4 |
| 30 | 3 | "same kind of text" | "Slightly informal…" | 3 |
| 31 | 3 | "how often they agree, after subtracting the agreement that chance alone would produce" | "This is a little informal…" | 3 |
| 32 | 3 | "this evidence is thin" | "Informal…" | 3 |
| 33 | 3 | "which is unsurprising" | "Informal…" | 3 |
| 34 | 3 | "The two resources that do report a coefficient measured a binary judgement rather than the three-class polarity task for which the resources are actually used." | "Do you think this sentence feels incomplete?" | 10 |
| 35 | 3 | "the resources are actually used" | "What resources are you referring to?" | 4 |
| 36 | 3 | "κ = 0.83" | "What is ϰ? Not everyone knows that this is Cohen's kappa." | 5 |
| 37 | 3 | "The field" | "What do you meant by the field?" | 4 |
| 38 | 3 | "These two weaknesses" | If it refers to the two observations immediately before, understood — but the previous paragraph was about annotation reliability and class imbalance was a paragraph earlier. Slight ambiguity. | 4, 7 |
| 39 | 3 | "are usually treated as separate problems" | "Who treat them as separate problems? You or existing studies?" | 9 |
| 40 | 3 | "The class imbalance that affects the labels is also the condition under which the standard agreement statistic becomes difficult to interpret." | "Citation?" | 2 |
| 41 | 3 | "class imbalance that affects the labels" | "Class imbalance affects the distribution of labels rather than the labels." | 8 |
| 42 | 3 | "standard agreement statistic" | "Ambiguous. Which statistic? Cohen's κ? But you never mentioned that explicitly." | 4, 5 |
| 43 | 3 | "the problem" | "What do you meant the problem? Which problem?" | 4 |
| 44 | 3 | "has proved persistent" | "Any support for this?" | 2 |
| 45 | 4 | "Comparative benchmarking … outside the scope, as is sentiment analysis as a general field, because both have already been surveyed…" | Sentence is long and difficult to digest. "Both" is ambiguous. | 10, 4 |
| 46 | 4 | "bear on" | "Is 'are relevant to' a better option?" | 3 |
| 47 | 4 | "It is also useful to state what this review does not do." | "Does this 'The scope of this review also excludes several activities' sound less informal?" | 3 |
| 48 | 4 | "problem has resisted solution" | "This sounds a little strong." | 6 |
| 49 | 4 | "each tier improves either label fidelity or scalability" | "Can you enhance the clarity of this part?" | 10 |
| 50 | 4 | "by giving up the other" | "Informal" | 3 |
| 51 | 4 | "two different causes of neutral-label skew … what the four regional corpora report about their own reliability" | "Perhaps you can make this explicit to enhance its clarity." | 10 |
| 52 | 4 | "audits" | "This sounds accounting-oriented…" | 3 |
| 53 | 4 | "simply occurring together" | "Informal…" | 3 |
| 54 | 4 | "Preprints were treated with caution. A paper from arXiv was included only when…" | "If possible, try your best to not consider using any preprints from arXiv." | 11 |
| 55 | 5 | Heading "3. Why Malaysian Code-Mixed Text Is Difficult to Annotate" | A short bridging sentence at the front of the first paragraph would make the progression smoother — the previous section is still describing selection criteria and the reader moves suddenly to why the data are difficult to annotate. | 7, 12 |
| 56 | 5 | "Three properties … All three have…" | Reader has to keep reading to discover what the three properties are. If this paragraph introduces the structure of Section 3, preview them. | 10, 12 |
| 57 | 5 | "a person or a program that has been asked to assign a sentiment label" | "Informal…" | 3 |
| 58 | 5 | "is not developed further" | "What is not developed further?" | 4 |
| 59 | 5 | "gives no structural cue" | "This is too strong and yet informal…" | 6, 3 |
| 60 | 5 | "happens mostly" | "Informal…" | 3 |
| 61 | 5 | "with almost no grammatical friction" | "Less formal…" | 3 |
| 62 | 5 | "The corpus consists of spoken data from two teachers" | "Citation?" | 2 |
| 63 | 5 | "sits inside" | "Informal…" | 3 |
| 64 | 5 | "In monolingual annotation, the phrase carrying the opinion can usually be identified before it is judged. Here, identifying it is already an act of interpretation." | "Citation?" | 2 |

---

# Part 3 — Where the comments land, and what that predicts for Sections 3.2 to 8

| Group | Count | Share |
|---|---|---|
| Rule 3 — informal register | 18 | 28% |
| Rule 4 — ambiguous referents | 10 | 16% |
| Rule 2 — missing citations | 10 | 16% |
| Rule 7 — transitions | 6 | 9% |
| Rule 10 — density / previewing | 5 | 8% |
| Rule 6 — overstatement | 4 | 6% |
| Rule 8 — imprecise technical claims | 2 | 3% |
| Rules 1, 5, 9, 11, 12 | 9 | 14% |

Two-thirds of the comments come from three habits: conversational verbs, backward-pointing demonstratives,
and claims about other people's work with no source attached. **A self-check pass on Sections 3.2 to 8 that
does nothing but grep for those three would remove most of the next round's comments before he sees them.**

Practical checklist before any section goes to Dr. Ho:

1. Search for: *carries over, sits, stay inside, gives up, how good, route, thin, unsurprising, kind of,
   simply, happens, friction, audit, judge, on its own*.
2. Search for every sentence-initial *This*, *These*, *The argument*, *The problem*, *The field*, *Both*.
3. Search for *most*, *usually*, *commonly*, *normally*, *often*, *the literature* — each needs a citation on
   the same sentence.
4. Read each section's first paragraph on its own. Does it connect backwards and name what is coming?
5. Any number, symbol, abbreviation or platform: is it defined at its first appearance?

---

# Part 4 — Round 1 rules that still hold

Round 2 raised no new complaints about these, which means they were fixed. Do not let them return in 3.2 to 8.

- **No bold anywhere in the body.** Italics only for non-English words on first use, statistical symbols, and
  titles in the reference list.
- **No parenthetical cross-references** such as `(Section 4)` or `(see Table 3)`. Where a section must be
  referred to, make the section number the subject: *"Section 4 examines…"*.
- **No content in brackets** as a substitute for a sentence — Round 1 comment 70/71/72.
- **Sentence length under about 35 words.** Round 2 still flagged one at 47.
- **The reference list needs to reach 40+**, per Round 1 comment 80. Sections 1 to 3.1 now carry 29.
- **Round 1 comment 17 — the generative-AI question.** He asked directly whether the writing was AI-produced,
  and tied it to the thin citation count. The volume of citations is now the evidence that answers it. Keep
  the density up in every remaining section.
