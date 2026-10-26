# Fixes before this goes to Dr. Ho

Four blockers, two small ones, and the missing 3.2 / 3.3.

---

## BLOCKER 1 — The Abstract is still the old version

This is the most serious problem. Page 1 has not been touched. Dr. Ho reads the abstract first, and
it still contains every pattern he objected to in the body:

| Abstract still says | He flagged it as |
|---|---|
| "the binding constraint on progress" | comment 21 (bold) + the general density complaint |
| "the default return of a scoring function that recognises no sentiment-bearing token" | comment 65 — mechanism stated before it is introduced |
| "the class skew that **corrupts** the labels" | comment 66 — too strong, use "affect" |
| "annotators of different construction **fail** independently" | comment 39 — "fail" is too strong |
| "the annotation defect and the measurement instrument are coupled" | comment 73 — the clarity complaint |

If he opens the PDF and reads page 1, he will reasonably conclude nothing has changed.

### Paste-ready replacement (232 words, down from 300)

> Malaysian social media users mix English and Malay inside single messages, producing the contact
> varieties known as Bahasa Rojak and Manglish. Sentiment analysis of this text is usually treated as
> a modelling problem. This review indicates that the more limiting problem lies earlier, in the
> sentiment labels themselves and in the evidence offered that those labels are sound. The review
> covers annotation practice and reliability evaluation for Malaysian Malay-English code-mixed
> sentiment data. Comparative benchmarking of sentiment classifiers is outside its scope. Three
> contributions follow. First, the annotation strategies used for low-resource code-mixed text are
> organised into three tiers, and each tier is shown to improve either label fidelity or scalability
> by giving up the other. Second, the two causes of neutral-label skew are separated, and the four
> regional corpora are audited against what a reliability claim requires. No corpus reports the full
> set of elements, the highest reported coefficient measures a narrower task than the resource is
> used for, and one manually annotated corpus reports no agreement statistic at all. Third, the class
> imbalance that affects the labels is shown to be the same condition under which the standard
> agreement statistic becomes difficult to interpret. The review closes with a research agenda
> covering minimum reporting standards, agreement measurement under class imbalance, and the
> untested assumption that annotators of different types make different errors.

Keywords stay as they are.

---

## BLOCKER 2 — "bullish-versus-bearish" is still in the draft

Page 3, in the second observation paragraph. The fix from last time was not applied.

**Find:**

> and Romadhona et al. [Romadhona et al. (2022)] report κ = 0.77 for a bullish-versus-bearish
> decision on one subset only.

**Replace with:**

> and Romadhona et al. [Romadhona et al. (2022)] report κ = 0.77 for a two-way positive-or-negative
> judgement on stock-market posts, covering one subset of their corpus only.

---

## BLOCKER 3 — The AlAfnan claim does not hold. I checked the paper.

Current text on page 2:

> *Manglish* is often treated as a careless or broken form of English. Sociolinguistic work does not
> support that view.

I read AlAfnan et al. (2025) properly this time. **It never says Manglish is treated as careless or
broken.** Searching the full text for "broken", "substandard", "careless", "degraded", "inferior" and
"stigma" returns nothing. What the paper actually reports is a policy debate:

> "Ali (2015) expresses concerns that Manglish may dilute standard English and Malay, particularly
> among younger generations."

> "scholars like Albury (2021) view Manglish as a complementary linguistic resource rather than a
> threat"

> the paper calls for "recognizing Manglish as a legitimate linguistic phenomenon"

So the concern in the literature is about **language proficiency**, not about Manglish being sloppy.
Citing AlAfnan for "careless or broken" is the exact thing Dr. Ho warned about in comment 5 — a claim
the source does not support.

### Paste-ready replacement

> *Manglish* is sometimes described as a variety that weakens standard English and Malay rather than
> as a language form in its own right [AlAfnan et al. (2025)]. Its structure, however, is not random.
> Treffers-Daller et al. [Treffers-Daller et al. (2022)] and AlAfnan et al. [AlAfnan et al. (2025)]
> show that Malay-English switching follows describable syntactic and pragmatic patterns, and that
> speakers use it deliberately to communicate efficiently, signal identity and build rapport. The
> difficulty this text creates for natural language processing (NLP) is therefore not that it is
> written carelessly. It is that the rules Malaysian writers follow are not the rules that standard
> NLP tools were built to handle, so writing that is systematic is processed as noise
> [Winata et al. (2023)], [Abu Bakar et al. (2020)].

**The second half of the sentence is fully supported.** AlAfnan et al. state that "the pragmatic
functions identified include softening directives, building rapport, and expressing cultural
references", that "the practical need for efficient and effective communication shapes these
patterns", and that "Manglish operates as a dynamic linguistic system". Efficiency, identity and
rapport are all there.

**One caveat to remember for later.** AlAfnan et al.'s examples come from Malaysian television and
film — *KL Gangster*, *Phua Chu Kang*, *Oh My English!*, *Kopitiam*. That is scripted dialogue, not
social media writing. It is fine evidence for what the particles *do*, but not for how often they
appear in written text. Worth stating explicitly when you write Section 3.2, which is where the
particles live.

---

## BLOCKER 4 — Section 3 promises three properties and delivers one

The section opener says:

> "Three properties of Malaysian code-mixed writing affect the annotation task directly."

Then only 3.1 appears. This is exactly the problem Dr. Ho raised in comment 68 about §1.1 — a section
with a single subsection. He will notice it immediately, and this time the text itself announces the
gap.

**The two missing subsections, from your v2 paper:**

- **3.2 — Affect is carried by function words that no standard lexicon contains.** Sentence-final
  particles (*lah*, *kan*) attach to otherwise-English clauses and carry pragmatic weight rather than
  propositional meaning. Annotation consequence: the reading of a particle is underdetermined, so
  disagreement is *systematic* rather than random — which means adding more annotators reproduces it
  instead of averaging it away. Sources: Treffers-Daller et al. (2022) for the switched-function-word
  frequencies (pronouns 10.4%, discourse markers 9.9%), AlAfnan et al. (2025) for the pragmatic
  functions.
- **3.3 — Phonetic spelling multiplies the surface forms of one word.** *tidak* → *tak*, *tk*, *x*.
  Maskat and Rahman (2020) sort this into five categories and report normalising only two of them.
  Annotation consequence: human and machine annotators fail on *different* inputs — a person reads
  *x* as *tidak* without effort, a lexicon returns out-of-vocabulary and no signal at all.
  Sources: Maskat & Rahman (2020), Abu Bakar et al. (2020).

Two options: either write 3.2 and 3.3 before sending, or send now with a line telling Dr. Ho that
Section 3 is partial and 3.2 and 3.3 are in progress. Sending a section that contradicts its own
opening sentence is the worse of the two.

---

## SMALL FIX 1 — Stray space inside two brackets

Two places have `[ ` with a space after the bracket:

- Page 2: `...brand monitoring to political and policy analysis [ Poria et al. (2023)]`
- Page 4: `...surveyed in detail by Poria et al. [ Poria et al. (2023)]`

Delete the space in both.

---

## SMALL FIX 2 — Add a note explaining the placeholder citations

Ten places read like this:

> Treffers-Daller et al. [Treffers-Daller et al. (2022)]
> Khanuja et al. [Khanuja et al. (2020)]
> Kasmuri and Basiron [Kasmuri & Basiron (2019)]

The author name appears twice. That is a side effect of using `[Author (year)]` as a stand-in for the
number — once the numbers go in it becomes `Treffers-Daller et al. [4]`, which is correct. But Dr. Ho
does not know that yet, and doubled names look like a mistake.

Add one line under the title, or in your email to him:

> **Note on citations.** In-text citations are shown as [Author (year)] as a temporary placeholder.
> They will be converted to the numbered [n] format required by the template, in order of first
> appearance, once the full paper is complete.

This also shows him you know the template rule rather than having ignored it.

---

## What is already correct

- Section numbering — 1 Introduction, 2 Review Methodology, 3 Why Malaysian Code-Mixed Text Is
  Difficult to Annotate. Comment 68 is answered.
- No bold anywhere in the body. Italics only on *Bahasa Rojak*, *Manglish*, κ. Comments 1, 9, 11 and
  the whole "Fix this" group are answered.
- No `(Section X)` cross-references in the Introduction. Comments 26, 36, 56–63 are answered.
- The roadmap paragraph puts section numbers as sentence subjects, matching the pattern in both
  papers Dr. Ho sent you.
- The four inclusion criteria are a numbered list. Comments 75, 76 are answered.
- The three contributions are one clause each with no mechanisms. Comments 64, 65, 67 are answered.
- The neutral-skew argument now gives two pieces of evidence rather than asserting causation.
  Comments 30, 31 are answered.
- Sentence length. The longest sentence in the rewritten body is 38 words; the old Introduction
  opened with 43.
