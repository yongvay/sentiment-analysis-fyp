# Dr. Ho — master comment tracker

**All 239 comments across four review rounds, in one file.**

| Round | Date | Document reviewed | Comments | Pages annotated |
|---|---|---|---|---|
| 1 | 14 Aug 2026 | `NgYongVay_ICON_AI_2026 (review).pdf` — full v3 paper | **80** | 2, 3, 4 of 26, plus References |
| 2 | 17 Aug 2026 | `Template ICON AI 2026 - Section 1 to 3.1 (reviewed).pdf` | **64** | 2, 3, 4, 5 of 7 |
| 3 | 24 Aug 2026 | `Template ICON AI 2026 - Section 1 to 7 (reviewed).pdf` | **35** | 1, 2, 3 of 19 |
| 4 | 29 Aug 2026 | `ICON AI 2026 - Section 1 (reviewed).pdf` | **60** | 1, 2, 3, 4 of 6 |

Every set was re-extracted directly from the PDF annotation layer, not retyped.

> **He has still never read past Section 3.1 in detail.** Rounds 3 and 4 were entirely Section 1. Everything
> below applies to Sections 2 through 8 as well — he simply has not got there yet, and those sections were
> written before most of these rules existed.

---

# Part 0 — Read this before writing anything

## The count is not falling. Read what he is counting.

| | R1 | R2 | R3 | **R4** |
|---|---|---|---|---|
| Comments | 80 | 64 | 35 | **60** |
| Words of Section 1 he was reading | ~1,100 | ~1,000 | ~1,050 | **~1,770** |
| Comments per 100 words of Introduction | — | — | ~3.3 | **~3.4** |
| Formatting / cross-references | 33 | 0 | 0 | **0** |
| Missing or unsupported citations | 14 | 11 | 8 | **6** |
| Register | 4 | 19 | 7 | **10** |
| Overclaiming | 3 | 4 | 6 | **7** |
| Unanchored referents and undefined terms | 4 | 11 | 2 | **15** |
| Imprecise technical relationships | 0 | 2 | 3 | **6** |

Round 4 has more comments than Round 3, but Round 3 covered a much shorter Introduction. Per hundred words
the rate is flat. **Three rounds of rewriting have not reduced the density of his objections.** What has
changed is which objections: the mechanical defects are gone for good, and what is left is one thing said
many ways.

## The one comment that matters most

Round 1, comment 73:

> **"This part lacks clarity. Maybe my command of English is not that good, I cannot really understand what
> you are trying to say in a few parts of your previous writing until I got help from ChatGPT. It is
> embarrassing to say so but if you want readers to read your entire paper, then in academic writing, you
> need to prioritize simple and clear English but not complex vocabulary and complicated sentences that
> sound impressive."**

## The second — his Round 3 covering email

> "…the language used for writing is **often more sophisticated than necessary**, which can potentially make
> the readers work very hard to extract those ideas. … even if I can really read the whole paper, give you
> some comments for enhancement, and you did it but the contents are still written in the same style, there
> is a possibility that **reviewers may simply reject it for this reason**. … In short, **don't do the
> writing in such a way that requires substantial inferential effort, but make everything stated more
> directly.**"

He also said, for the first time, that the Introduction "presents a **well-motivated and potentially
valuable research problem**." The argument is not in question. Only the prose is.

## The third — his Round 4 restatement, twice, in capitals

> **R4 6:** "As mentioned earlier, make EVERYTHING straightforward and clear."
> **R4 44:** "Remember? Don't increase the complexity of your writing unnecessarily. You want your readers
> to understand your ideas and messages 100%, right?"

Fifteen of the sixty Round 4 comments are one question in different clothes: **what does this word point
at?** *effect* of what. *one variety* of what. *in part* how. *regarded* how. *reading* of what. *the
problem*, which problem. *coefficient*, which one. *large*, how large. *regionally adapted*, adapted how.
That is the single largest category in the round, and it did not exist at this size before.

## The pre-submission checklist

Seven passes. Run every one over any section before it goes to him.

**Pass 1 — informal phrasing.** Grep for the exact strings he has flagged: `carries over`, `sits`,
`stay inside`, `how good`, `route`, `thin`, `unsurprising`, `kind of`, `simply`, `happens`, `friction`,
`audit`, `judge`, `on its own`, `giving up`, `bear on`, `stops there`, `equally`, `trustworthy`,
`settled practice`, `built to`, `an automatic one`, `at the expense of`, `stops being`, `diagnosis`,
`Against that`, `On that account`.

**Pass 2 — every word that points at something.** Not only sentence-initial `This`/`These`/`It`/`Both`.
**Every abstract noun standing in for something named earlier or not named at all**: *the effect*, *the
problem*, *the field*, *the argument*, *this material*, *this kind*, *one variety*, *the coefficient*,
*the resources*, *the reading*, *in part*. If a reader must look up or infer, name it in place.

**Pass 3 — claims about other people's work.** `most`, `usually`, `commonly`, `normally`, `often`, `the
literature`, `elsewhere`, `is treated as`, `well described`, `the most widely used`. Each needs a citation
**on the same sentence** — and the source must actually say it.

**Pass 4 — the same source cited twice in a row.** New in Round 4. If two consecutive sentences carry the
same citation, merge them into one sentence. See Rule 16. **This is the pass that is broken most often and
noticed least** — run the script, do not do it by eye.

**Pass 5 — evaluative adjectives.** `large`, `small`, `high`, `low`, `strong`, `comprehensive`, `limited`.
Each needs an operational definition somewhere in the paper. See Rule 18.

**Pass 6 — one term per concept.** Search for every name you have given the same object. Round 4 caught
*four Malay-English sentiment resources* and *four regional corpora* in the same section. See Rule 19.

**Pass 7 — read each section's first paragraph alone.** Does it connect to the previous section and name
what is coming? Are enumerated items previewed by name?

Then: no bold anywhere; no `(Section X)` in parentheses; nothing parked in brackets; nothing cited that is
not peer-reviewed; no sentence over about 35 words; **no sentence that tells the reader what the paper is
doing** (Rule 17).

## Run the checker first

`Comment_Tracker/check_section.py` automates passes 1, 3, 4, 5 and 6 plus the bold and cross-reference
checks over any .docx:

```
python3 Comment_Tracker/check_section.py "ICON AI 2026 - Section 1 (v15).docx"
python3 Comment_Tracker/check_section.py paper.docx --from "2. Why Malaysian" --to "References"
```

It reports a count of hard failures, which should be zero or explained. It cannot judge meaning, so the
evaluative-adjective and demonstrative passes still need a human read. **Nothing goes to Dr. Ho until this
runs clean.** It was written after the first Round 4 revision shipped with five Rule 16 breaches, a claim
that contradicted Section 5.2, and a source cited for something it does not say.

---

# Part 1 — The rules, with the evidence

Comment numbers are prefixed **R1**, **R2**, **R3** or **R4**.

## Rule 1 — Write simply. This is the whole game.

*R1 1, 2, 39, 73, 74, 78 · R2 5, 34, 45 · R3 35 · R4 9, 18, 31, 33, 44 — **15 comments***

Not "write short". Write so that a reader who is not inside your head follows it on one pass.

- **R1 73** — quoted in full above.
- **R2 45** — a 47-word scope sentence: "long and relatively difficult to digest."
- **R3 35** — *"the annotation label is at present the more limiting problem, together with the evidence
  offered that the label is sound"* — "particularly unclear."
- **R4 44** — *"a narrower task than the corpus is used to support"*: "What exactly is narrower? This part
  can be difficult to understand." Fixed by naming both tasks: a two-way judgement rather than three-way
  positive, negative and neutral labelling.
- **R4 33** — *"The labels it produces form the supervision signal"*: "Removing this can make the message
  clearer." Two words deleted. He notices two words.
- **R4 18** — *"Its structure, however, is not random"* → **"is systematic rather than random"** *(his
  wording)*. Say what a thing is, not only what it is not.

> **His replacements are longer than yours.** Round 3 measured it: across ten supplied rewordings his
> versions ran 25 to 200 per cent longer. **Directness costs words. Pay for it by deleting repeated
> content, never by compressing a sentence** — compression is the defect he is complaining about.

## Rule 2 — Any claim about what other researchers do, find, or fail to do needs a citation on that sentence, and the source must actually say it

*R1 3, 8, 11, 14, 19, 24, 26, 29, 30, 33, 34, 36, 43, 79 · R2 2, 3, 12, 15, 19, 20, 23, 40, 44, 62, 64 ·
R3 4, 8, 9, 11, 15, 16, 18, 27 · R4 4, 17, 20, 21, 36, 47 — **39 comments. The largest category across all
four rounds.***

> **R1 8:** "Citation? Or else this is just your assumption. Writing research paper directly forces you to
> double check everything you said and claim."

> **R1 36:** "A citation is needed, ideally to specific studies and an explanation of why their conditions
> are problematic. Otherwise, you are simply making a baseless and unreasonable claim."

Four sub-rules:

1. **Trigger words.** *most, usually, commonly, normally, often, the literature, elsewhere, is treated as,
   well described, the most widely used.* Each is an empirical claim about a body of work. **R4 47**: *"the
   most widely used of which is Cohen's kappa"* — "If Artstein and Poesio (2008) explicitly support it,
   fine. Otherwise, avoid an unnecessary claim by simply saying 'such as Cohen's kappa'."
2. **The citation goes on the claim sentence.** R2 62 flagged a fact sitting two sentences after its source.
3. **Definitions need sources too.** **R4 4**: the definition of *pre-trained model* — "Citation is needed."
   A sentence that teaches the reader something is still a claim.
4. **An inference is not a finding.** **R4 20** is the sharpest example in four rounds: *"Maskat and Rahman
   (2020) sort this variation into five categories and map two of them back to their standard forms, which
   indicates that the variation is systematic rather than arbitrary."* — "There is a logical issue here.
   The fact that the authors categorize the variation and map two categories to standard forms does not
   necessarily prove that the variation is systematic." He supplied the fix: **"This categorisation suggests
   that the variation follows recurring patterns rather than occurring arbitrarily."** Same evidence, honest
   verb. Compare R1 29 and R1 30, which are the same objection about neutral-label skew.

**R4 36** extends this to your own conclusions: *"the more limiting problem"* — "Your previous paragraph
establishes that label errors can affect training and evaluation, but it does not by itself establish that
labels are more limiting than models for Malaysian Malay-English sentiment data." A conclusion must be
attached to the evidence that carries it, not to the paragraph it happens to follow.

## Rule 3 — Register: plain is not the same as conversational

*R1 37, 44, 47, 75 · R2 18, 21, 22, 24, 28, 30, 31, 32, 33, 46, 47, 50, 52, 53, 57, 60, 61, 63, 4 ·
R3 7, 13, 17, 20, 23, 26, 34 · R4 11, 25, 27, 30, 32, 34, 42, 53, 56, 60 — **40 comments***

He asks for simple words and formal register at the same time. Phrasal verbs, physical metaphors and
casual constructions are what break it.

| Flagged | Use instead | Where |
|---|---|---|
| This **carries over** to social media | On social media in particular | R2 4 |
| the problem **sits earlier** | originates one step earlier | R2 21 |
| errors do not **stay inside** the dataset | the consequences are not confined to the dataset | R2 22 |
| **judge how good the model is** | evaluate model performance *(his wording)* | R2 24 |
| the **limits of this route** | the limitations of this approach | R2 18 |
| **giving up** the others | at the expense of the others | R2 28, 50 |
| this evidence is **thin** | limited / sparse | R2 32 |
| **audits** what the corpora report | examines what the corpora report | R2 52 |
| **Against** that, Winata et al. find | **In contrast**, Winata et al. find *(his wording)* | R3 23 |
| **On that account** the model cannot | Under this view the model | R3 20 |
| **The remainder of the difficulty** | **Another source of difficulty** *(his wording)* | R3 26 |
| they **do not cover the same set of languages** | they refer to different combinations of languages | R4 11 |
| tools were **built to** handle | tools were **designed to** handle *(his wording)* | R4 25 |
| **On this explanation** the model | **Under this view** *(his wording)* | R4 27 |
| **does not originate in the model itself. It originates one step earlier** | **arises one step earlier** *(his wording)* | R4 30 |
| assigned by a human annotator or by **an automatic one** | by an automatic labelling method | R4 32 |
| and Frénay and Verleysen (2014) **report that the accuracy of predictions may decrease as a result** | **which can reduce predictive accuracy** (Frénay and Verleysen, 2014) *(his wording)* | R4 34 |
| secures some of these properties **at the expense of the others** | **satisfies some of these criteria but not all of them** *(his wording)* | R4 42 |
| Its contribution is a **diagnosis** | an analysis / synthesis / examination *(his wording)* | R4 53 |
| each tier **gains either label fidelity or scalability at the expense of the other** | **examines the trade-off between label fidelity and scalability across them** *(his wording)* | R4 56 |
| the linguistic, annotation and **measurement** challenges | **evaluation** challenges | R4 60 |
| **trustworthy** labels … **settled practice** | reliable annotations … established practice *(his wording)* | R1 37 |
| **Four criteria governed inclusion.** | Four criteria were used to determine inclusion. *(his wording)* | R1 75 |

**Twenty-four of his 239 comments supply the replacement wording outright.** Ten in Round 3, twelve in
Round 4. Use his words verbatim wherever he gave them. He remembers.

## Rule 4 — Never make the reader work out what a word points at

*R1 12, 17, 18, 20 · R2 6, 11, 13, 14, 17, 29, 35, 37, 38, 43, 58 · R3 3, 14 ·
R4 2, 6, 7, 8, 10, 12, 14, 15, 19, 35, 38, 54 — **29 comments***

Round 4 made this the largest single category of the round. It is no longer only about demonstratives — it
is about **any word standing in for something the reader has to reconstruct.**

| Flagged | What he asked | Fix |
|---|---|---|
| The tools **carry an assumption** | "A reader may ask what assumption are you referring to" | assume that their input is written in one standard language |
| The **effect** on performance varies by task | "Effect of what exactly?" | the effect of code-switching on model performance |
| two languages **alternate within a single message** … then "code-switched" | "you never named the phenomenon as 'code-switched'" | …a pattern known as code-switching |
| Malaysian social media text is **one variety** | "One variety of what? … 'text' is not necessarily a 'variety'" | one setting in which such code-switching is common |
| Two local terms for **such mixed writing** | "could refer to all multilingual Malaysian writing" | this code-mixed writing |
| *Bahasa Rojak* only **in part** | "What do you mean by 'in part'?" | refers to a wider combination that also includes Chinese |
| How this mixed writing is **regarded** | "What does 'regarded' mean?" | Descriptions of *Manglish* in the literature are not uniform |
| before turning to the **technical difficulty** | "If you mean the difficulty of processing Manglish with NLP models, say so" | *(clause deleted — see Rule 17)* |
| The same **regularity** | "the reader has to infer that you mean systematicity" | The same systematicity *(his wording)* |
| Northcutt et al. show that **they** can change | "Make it clearer using 'label errors'" | label errors |
| Three findings support that **reading** | "Reading of what?" | *(recast — findings point to a conclusion)* |
| why **the problem** remains unresolved | "'the problem' could refer to several things" | why reliable annotation and evaluation remain difficult to establish |
| **This kind of writing** is common on X | "What do you mean by this kind of writing?" | Malay-English mixed writing | 
| **The field** therefore lacks | "What do you mean by the field?" | Research on Malaysian code-mixed sentiment |
| **labelling practice** appears from nowhere | R1 12: introduce a concept before using it | define at first mention |

R1 12, R1 17 and R4 7 are the same rule applied to concepts rather than pronouns: **a term must be
introduced before it is used** — and if you describe a phenomenon and then start using its technical name,
you must join the two explicitly.

## Rule 5 — Introduce every abbreviation, symbol, statistic, platform and technical term on first use

*R2 7, 36, 42 · R4 28, 29, 43 — **6 comments***

- **X** — "What is X? For those who are not familiar with it, it is better to introduce it once."
- **κ** — "What is ϰ? Not everyone knows that this is Cohen's kappa."
- **R4 28 — "regionally adapted"** — "Does it mean trained on Malaysian data, fine-tuned on Malay-English
  data, trained on Southeast Asian languages, or adapted to local linguistic patterns? You should specify
  what you mean."
- **R4 29 — "capacity dilution"** — "Perhaps you can define this to enhance its clarity."
- **R4 43 — "coefficient"** — "A reader may not immediately know whether you mean Cohen's kappa, Fleiss'
  kappa, or any other agreement coefficient. Alternatively, use a general term like 'inter-annotator
  agreement coefficient'."

A term you borrowed from a source counts as a technical term. If you had to look it up, so does he.

## Rule 6 — Do not overstate

*R1 13, 40, 60 · R2 9, 16, 48, 59 · R3 2, 6, 19, 21, 22, 31 · R4 5, 16, 22, 24, 39, 48, 57 — **20 comments***

| Word | His objection | Replace with |
|---|---|---|
| **fail** | R1 40: "the word 'fail' is too strong" | problematic, limited, weakness |
| **corrupts** | R1 60: "too strong and negative" | affect |
| **the best results** | R2 16: "if it is the best … there will be no room for improvement" | the strongest scores among the systems evaluated |
| **cannot handle** | R3 21: "a model may not completely fail to handle it" | handles it less effectively |
| **would** perform better | R3 22 | **may** perform better *(his wording)* |
| **no longer reflects** how the model behaves | R3 31: "too absolute" | becomes a less reliable indicator |
| **Each** of these resources is built for one language | R4 5: "This is too absolute. How do you know not every modern language resource is strictly monolingual?" | **Many of these resources are developed primarily for individual languages** *(his wording)* |
| **weakens** standard English and Malay | R4 16: "Does the cited source make this claim using 'weakens'?" | **having a negative effect on** *(his wording)* |
| tools **therefore treat** them as OOV | R4 22: "A dictionary not containing a word does not automatically mean all tools will treat it as OOV. It depends on how the tool is designed." | **may therefore** treat *(his wording)* |
| **The conventions Malaysian writers follow** are consistent | R4 24: "a very broad claim about all Malaysian writers" | **These writing conventions are consistent within the observed variation** *(his wording)* |
| **four Malay-English sentiment resources currently exist** | R4 39: "otherwise readers may ask whether you are really certain there are only four" | **four resources are identified in this review** *(his wording)* |
| κ **stops being informative** | R4 48: "Cohen's κ does not simply stop being informative" | **can make the statistic more difficult to interpret** *(his wording)* |
| the two **causes** of neutral-label skew | R4 57: "to indicate that there might be more than two" | two **sources** *(his wording)* |

**The pattern in his own replacements: he always adds a hedge.** *among*, *may*, *can*, *potentially*,
*many*, *one common*, *suggests*. Not one of his 24 supplied rewordings states anything flatly.

## Rule 7 — Every change of topic or scale needs an explicit bridge

*R1 6, 10, 15, 41 · R2 8, 26, 55 · R3 10, 19 · R4 3, 26, 49, 50 — **13 comments***

> **R1 10:** "…the 'difficulty' is introduced implicitly. If the readers get it, then it is fine, otherwise,
> they will find the transition unsmooth as if something is missing."

- **R4 3** — one word. "Adding 'However' to the front of this sentence will signal that you are moving from
  the usefulness of sentiment analysis to one of its limitations."
- **R4 26** — "it jumps quite quickly from the linguistic/resource mismatch to architecture." Fixed with a
  sentence naming the jump: *This mismatch between writing conventions and tool design raises the question
  of where the difficulty in processing such text actually lies.*
- **R4 49** — a paragraph on reliability, imbalance and κ ends with a 2024 review of dataset scarcity. "The
  connection is not explicit, the reader has to infer it." Fixed by writing the link as its own sentence.
- **R4 50** — even a good transition can be improved: "perhaps you can enhance the transition a little?"

Write the bridge as its own sentence. Every scale is represented: sentence to sentence, paragraph to
paragraph, general to specific, section to section.

## Rule 8 — State technical relationships exactly

*R2 25, 41 · R3 28, 30, 32, 33 · R4 41, 45, 46, 51, 55, 59 — **12 comments***

Ask of every sentence: **is the thing you named actually the thing that changes?**

| Wrong | Right | Where |
|---|---|---|
| label errors distort **the test set** | incorrect labels distort **the evaluation of model performance** | R2 25 |
| class imbalance affects **the labels** | affects **the distribution of** labels | R2 41 |
| the supervision signal a model **is measured against** | the standard against which the model's **predictions** are compared | R3 28 |
| **label noise** is learned during training | the **patterns associated with** incorrect labels are learned | R3 30 |
| a label **damages the model** twice | affects training, and affects the measurement of performance | R3 32 |
| again when **it** is measured | again when **its performance** is measured | R3 33 |
| **validated by** human annotators | **with annotation reliability assessed by** human annotators *(his wording)* | R4 41 |
| the findings describe one **condition** rather than two | **The second and third findings are closely related rather than independent** *(his wording)* | R4 45 |
| reliability is **demonstrated** by κ | reliability is **assessed** — "it is not always demonstrated specifically through Cohen's kappa" | R4 46 |
| annotation and evaluation **remain unresolved** | "a question is unresolved, but annotation and evaluation themselves are not usually described as unresolved" | R4 51 |
| each tier **gains** fidelity or scalability | a tier does not gain either; there is a **trade-off** | R4 55 |
| what each **corpus reports** about its own reliability | what the **studies that introduce** each resource report | R4 59 |

**R4 59 is the subtlest comment in four rounds:** "This is understandable, but it also sounds like a corpus
will literally report something." A dataset is not an author.

## Rule 9 — Attribute positions to whoever holds them

*R1 22 · R2 27, 39 · R4 23 — **4 comments***

> **R2 39:** "Who treat them as separate problems? You or existing studies?"

**R4 23** is the precise form of the problem: *"Malay social media text has accordingly been described in
earlier work as misspelled … (Maskat and Rahman, 2020; Abu Bakar et al., 2020)."* — "There are two
different ways to interpret this sentence. First, the two cited sources mentioned that **earlier work**
described it that way. Or second, **these two cited sources** make such claim? If it is the latter case,
then you should have shifted the cited source to right after 'earlier work'."

When the cited authors are themselves the ones making the claim, name them as the subject: *Abu Bakar et
al. (2020) describe Malay social media text as…*

## Rule 10 — One spine per section. Preview enumerated items by name.

*R1 32, 48, 52, 59, 76 · R2 49, 51, 56 · R4 37 — **9 comments***

- **R4 37** — *"A second and related problem is…"* — "What is the first problem? Make it clearer and avoid
  making the reader wonder what 'second' refers to." The paragraph already had a *First / Second / Third*
  spine for the three findings; a separate *second problem* was running alongside it. **Do not run two
  enumerations at once.** The fix was to fold the second problem into the same sentence as the first, so
  only one numbered spine remains.
- **R1 76** — he supplied the format: *"Studies were included if they met four criteria: (1) …; (2) …;
  (3) …; and (4)…"*
- **R2 56** — name all items up front, before the reader has to keep reading to find them.

## Rule 11 — Formatting: no bold in the body, ever

*R1 5, 7, 9, 16, 21, 23, 25, 28, 31, 35, 45, 46, 49, 50, 53, 54, 55, 56, 58, 61, 71, 72 — **22 comments,
all Round 1, none since***

Italics only for: non-English words on first use (*Manglish*, *Bahasa Rojak*, *tidak*, *takde*), titles of
works, statistical symbols (*κ*), and words discussed as words.

## Rule 12 — No cross-references in parentheses, no content parked in brackets

*R1 27, 38, 51, 57, 62, 63, 64, 65, 66, 67, 69 — **11 comments, all Round 1, none since***

> **R1 69:** "Avoid writing sentences by including contents in brackets. Express it in a proper and complete
> sentence."

## Rule 13 — Sources: peer-reviewed only, and enough of them

*R1 70, 80 · R2 54 — **3 comments***

> **R2 54:** "If possible, try your best to not consider using any preprints from arXiv." Treat as absolute.

> **R1 80:** "If possible, try increase the volume of references to at least 40."

**Status after Round 4: 38 references.** Two short. Round 4 added two that do real work — Devlin et al.
(2019) for the definition of a pre-trained model (R4 4) and Dewan Bahasa dan Pustaka (2005) for the
standard Malay dictionary (R4 21). That is the right kind of addition: a source he asked for, doing a job.
Find two more the same way rather than padding.

## Rule 14 — Never one subsection alone under a heading

*R1 68 — **1 comment***

Either two or more subsections, or promote it.

## Rule 15 — Small mechanics

*R1 4, 42, 77 · R2 1, 10 · R3 1, 12 · R4 52 — **8 comments***

- **R4 52** — *"it does not report the author's own experimental work"* → **authors'**. "Use authors'
  because this is a multi-author paper." The paper has one named author and a supervisor; he still reads
  the possessive as plural. Follow him.
- **R1 42** — compound subject joined by *and* takes a plural verb: *remain*, not *remains*.
- **R2 1 and R2 10** — citation style. Parenthetical `(Poria et al., 2023)`; narrative
  `Treffers-Daller et al. (2022)`. Never `Author et al. [Author et al. (year)]`.

> **Still open with Dr. Ho.** Template §11 requires numbered `[n]` citations. He has now written author–date
> **four times** while looking at your draft, and Round 4 comment 34 supplies a replacement in author–date
> form. The paper follows him. Get one line from him confirming it before submission.

## Rule 16 — NEW in Round 4. Do not cite the same source in consecutive sentences

*R4 1 — **1 comment, and it is the first one he wrote this round***

> **"Reading can be made difficult if the same source is cited in few sentences right after another. For
> instance, you can remove the second citation by revising it as: 'Joshi et al. (2020) highlight that only
> a small number of the world's languages are represented in current language technologies, with lexicons,
> pre-trained models and benchmark corpora concentrated in those few languages.'"**

He is describing a habit that came from Rule 2. Three rounds of "citation?" produced a draft where the same
reference appears on two or three sentences in a row. **The fix is to merge the sentences, not to drop the
citation.** Search every paragraph for a source name appearing twice within three sentences and join them
with a subordinate clause.

Round 4's revision applied this in three further places he had not flagged: the two Doğruöz et al. (2021)
sentences, the two Coluzzi (2017) sentences, and the two Maskat and Rahman (2020) sentences.

> **It then broke the rule five more times.** The first revision (v14) reintroduced Doğruöz et al. (2021) on
> consecutive sentences in paragraph 1, **AlAfnan et al. (2025) on four consecutive sentences** in
> paragraph 2, and Kong et al. (2023) with Mohd Shamsuddin et al. (2024) in paragraph 7. This is the easiest
> rule in the file to break, because every citation added under Rule 2 is a candidate. **It is also the
> easiest to check mechanically — pass 2 of `Comment_Tracker/check_section.py` finds every instance.**
>
> The fix is never to delete the citation. Merge the sentences, or carry the attribution forward with a
> phrase that does not repeat the reference: *In their survey…*, *The same study describes…*, *They add
> that…*

## Rule 17 — NEW in Round 4. Do not tell the reader what the paper is doing

*R4 13 — **1 comment***

On *"…so this review states its position before turning to the technical difficulty"*:

> **"You don't have to explicitly tell what the paper is doing like this."**

Narrating the structure of your own argument inside a paragraph is scaffolding left in the finished
building. A well-organised paragraph does not need to announce itself. This is the same instinct as R1 27
("Remove this. If the outline is logically organized, readers can link them together") and R1 41 ("'Scope'
is not an actual section heading"), now applied to a whole clause.

**The exception he accepts:** the formal scope paragraph — *This review does not propose, implement or
evaluate a system* — is standard and he approved its wording at R2 47. The rule bites on mid-paragraph
narration, not on the scope statement.

## Rule 18 — NEW in Round 4. Give evaluative adjectives an operational definition

*R4 40 — **1 comment***

> **"What counts as large? You need an operational definition somewhere in the paper, or this claim could
> appear subjective. For example, if you later define a threshold such as 10,000 messages, say so."**

Applied: *"large, meaning at least ten thousand labelled messages."* That threshold now has to hold
everywhere in the paper — MY-EN-CS at 2,316 is not large; MyCovid-Senti at 11,568 and MESocSentiment at
19,714 are.

Check the same way: *comprehensive*, *limited*, *high agreement*, *strong*, *small*, *casual*.

## Rule 19 — NEW in Round 4. One term per concept, for the whole paper

*R4 58 — **1 comment***

> **"This term is unclear. Earlier, you used 'four Malay-English sentiment resources'. Now you say 'four
> regional corpora.' 'Regional corpora' is broader and potentially ambiguous. Does 'regional' mean
> Malaysian, Southeast Asian, Malay-English, or locally developed?"**

Section 1 now uses **four Malay-English sentiment resources** throughout. **Sections 2 to 7 still say
"regional corpora" in several places and must be aligned before he reads them.** Same for *causes* versus
*sources* of neutral-label skew, which is also the heading of Section 3.2.

---

# Part 2 — Where the comments fall

Every comment is assigned to exactly one rule, so the columns sum to 239.

| Rule | | R1 | R2 | R3 | R4 | Total |
|---|---|---|---|---|---|---|
| 3 | Formal register, not conversational | 4 | 19 | 7 | 10 | **40** |
| 2 | Citation on every claim, and the source must say it | 14 | 11 | 8 | 6 | **39** |
| 4 | Never make the reader work out what a word points at | 4 | 11 | 2 | 12 | **29** |
| 11 | No bold in the body | 22 | 0 | 0 | 0 | **22** |
| 6 | Do not overstate | 3 | 4 | 6 | 7 | **20** |
| 1 | Write simply | 6 | 3 | 1 | 5 | **15** |
| 7 | Explicit bridges between topics | 4 | 3 | 2 | 4 | **13** |
| 8 | State technical relationships exactly | 0 | 2 | 4 | 6 | **12** |
| 12 | No parenthetical cross-references or bracketed content | 11 | 0 | 0 | 0 | **11** |
| 10 | One spine per section; preview enumerations | 5 | 3 | 0 | 1 | **9** |
| 15 | Citation format and small mechanics | 3 | 2 | 2 | 1 | **8** |
| 5 | Define every symbol, abbreviation and technical term | 0 | 3 | 0 | 3 | **6** |
| 9 | Attribute positions to who holds them | 1 | 2 | 0 | 1 | **4** |
| 13 | Peer-reviewed sources only, and enough of them | 2 | 1 | 0 | 0 | **3** |
| 14 | Never one subsection alone | 1 | 0 | 0 | 0 | **1** |
| 16 | No same source on consecutive sentences | 0 | 0 | 0 | 1 | **1** |
| 17 | Do not narrate what the paper is doing | 0 | 0 | 0 | 1 | **1** |
| 18 | Operational definitions for evaluative adjectives | 0 | 0 | 0 | 1 | **1** |
| 19 | One term per concept | 0 | 0 | 0 | 1 | **1** |
| | **Total** | **80** | **64** | **35** | **60** | **239** |

*(Round 3 counts are re-mapped from that round's own categories: its "figurative language" group is folded
into Rule 8, its "factual oversimplification" into Rule 15, its "sentence not interpretable" into Rule 1.)*

## What the four rounds show

**Mechanical defects were solved once and never came back.** Formatting (22) and cross-references (11) are
Round 1 only. Thirty-three comments eliminated permanently by a find-and-replace.

**Register is now the largest category and it is not falling.** 4 → 19 → 7 → 10. Round 2 overshot into
conversational English; Rounds 3 and 4 have been pulling back from that without landing.

**Citation comments changed character rather than volume.** Rounds 1 and 2 asked *where is the citation.*
Rounds 3 and 4 ask *does the source actually say this* — a harder question, and the only category that can
damage the paper's credibility rather than its readability.

**Round 4 opened a front that did not exist before: precision of reference.** Twelve comments asking what a
word points at, six asking whether a technical relationship is stated correctly, three asking for a
definition. Twenty-one of sixty. **That is the category to watch in Sections 2 to 7**, because those
sections were written in the same compressed style and have never been read.

---

# Part 3 — Appendix: Round 1, all 80 comments in document order

Extracted from `NgYongVay_ICON_AI_2026 (review).pdf`. The "Highlighted" column is reconstructed from the PDF
annotation geometry, so on two-column reflow it sometimes interleaves the marked text with the line beneath
it. Comment text is verbatim.

| # | Page | Highlighted | Dr. Ho's comment |
|---|---|---|---|
| 1 | 2 | 1. Introduction | Is the content written by generative AI or you only use it for polishing and proofreading? This is a good chance for you to enhance your writing. If the writing is mostly done by generative AI, you will learn little in doing academic writing at the end of the day. Too little cited sources are used in this section. Usually many claims are made in the introduction section and hence many citation wil… |
| 2 | 2 | On een | The second sentence is overly long. Avoid writing long sentences that might be difficult to digest. |
| 3 | 2 | X, Facebook and WhatsApp, y within a single utterance to | Is this supported by the cited source? If not, you need another citation(s) ya. |
| 4 | 2 | bilingual users manage efficien | I think Chinese are mostly multilingual users. However, if you refer to Malay or Indian or Malaysian of other races, then maybe majority of them are bilingual users. Perhaps you can enhance the clarity of this? It would be great if citation can also be provided specifically to this part. |
| 5 | 2 | Bahasa ore any Rojak compu | If this is not the requirement stated in the template, then do not highlight words in bold,. Please fix all of these occurrences in your writing. Anyway, italics is still accepted, but do not over use it, apply it only when needed. For instance, to scientific terms, variables and mathematical symbols, statistical symbols, words being discussed as words, emphasis (for good reason) and titles of boo… |
| 6 | 2 | This use th | It feels slightly abrupt when reading this sentence from the previous one because it suddenly shifts from describing multilingual discourse to discussing computational mischaracterisation. Transition between sentences has to be smooth so that readers can enjoy reading your writing. |
| 7 | 2 | Manglish al claim is m | Fix this |
| 8 | 2 | routinely mischaracterised. ned contact varieties with | Citation? Or else this is just your assumption. Writing research paper directly forces you to double check everything you said and claim. Once you are used to it, you won't simply say anything based on assumptions which can create lots of unnecessary trouble for you. |
| 9 | 2 | rule-governed contact varieties ventions, in which switching fol | Fix this |
| 10 | 2 | The it is difficulty careless w | The previous sentences establish what the varieties are, but they do not explicitly establish the "difficulty" they create for NLP. So, the "difficulty" is introduced implicitly. If the readers get it, then it is fine, otherwise, they will find the transition unsmooth as if something is missing. You can enhance the transition by making it explicit, such as "This systematic variation creates partic… |
| 11 | 2 | the writing is systematic in ways current tooling was not review argues, in ways current labelling practice is not built to read, built to recor | This is a broad claim about NLP and annotation limitations, so it should be supported by relevant NLP literature if it is presented as established facts. |
| 12 | 2 | labelling practice | If you notice, "labelling practices" has not been introduced earlier. The earlier sentences establish only a few points including Malaysian multilingual discourse, its linguistic structure, and the challenge it poses to NLP. Therefore, "labelling practices" appears quite suddenly in the last sentence. Usually, a new concept is introduced first before it is used or mentioned later. |
| 13 | 2 | argues, | You can soften the tone using more neutral words like "highlight" or "indicate". |
| 14 | 2 | the diagnosis offered is represent code-switched almost always architectural. input; a larger, better pre-train | This needs citation because this is a claim about how prior studies explain poor performance. |
| 15 | 2 | When sentiment systems most always architectura | The first paragraph ends by introducing labeling, and then the second paragraph immediately shifts to sentiment systems. However, sentiment analysis has not been introduced earlier like the case of "labeling practice", resulting in the shift feels slightly sudden. Either you reorganize the points. Alternatively, you can consider adding a connector which can help address this issue. For instance, "… |
| 16 | 2 | architectural. better pre-train | Fix this |
| 17 | 2 | model, r more | Again, the word "model" appears somewhat suddenly because the first paragraph discusses NLP tooling and labelling, and the previous sentence talks about sentiment systems but none explicitly introduce machine-learning/sentiment models... |
| 18 | 2 | represent d model sh | The use of "represent" can be ambiguous, because when it is used for both the model's capability and the input, it can mislead readers to think that you are trying to equate the model with the input. The word "handle" might be a better option in this case. |
| 19 | 2 | a larger, better pre-trained or more regionally adapted model should therefore ent it better. That reasoning is intuitive, and it is not so much wrong… | Citation? Otherwise, this is just your assumption. |
| 20 | 2 | represent it better. premature. This re | Replace the use of "represent" with other words, for instance, "perform better on such data." |
| 21 | 2 | binding constraint is lies upstream of | Fix this |
| 22 | 2 | It is the ained and annotation label, the quality of the supervision signal a model is trained and evaluated on, together with the credibility of the … | If you present these as established findings from previous research. You should cite literature supporting the importance of annotation quality, label reliability, and supervision quality in sentiment analysis or NLP. But if this is your review's central argument, the sentence itself does not necessarily need a citation immediately after it. However, you need to support the claim using any evidenc… |
| 23 | 2 | annotation label, evaluated on, toge | Fix this |
| 24 | 2 | No existing Malay-English polarity-balanced, casually sentiment authentic corpus and hum is an- simultaneously validated; each large-scale, vailable r… | Citation? Otherwise, this is just your assumption. |
| 25 | 2 | corpora themselves. ously large-scale, p | Fix this |
| 26 | 2 | each available resource secures some of these thers (Section 5.2). The largest general-domain properties only by conceding others resource, MESocSenti… | Citation? Otherwise, this is just your assumption. |
| 27 | 2 | (Section 5.2). the cost of tha | Remove this. If the outline is logically organized, readers can link them together. |
| 28 | 2 | 78.23% neutral, 16.33% positive and 5.44% agnitude is not a property of Malaysian discourse. It negative is an arte | Fix this. |
| 29 | 2 | It at is an artefact of the labelling method, produces it. | This is a causal claim and cannot be safely inferred from the previous claim about class distribution because class imbalance alone does not prove that the imbalance was caused by the labeling method. Therefore, a citation is also needed. |
| 30 | 2 | A skew of that magnitude is not a property of Malaysian discourse. t of the labelling method, and Section 3.2 traces the mechanism th | This is a strong claim about the underlying population rather than the dataset itself. Therefore, a citation is needed. |
| 31 | 2 | artefact of the labelling method, uces it. | Fix this. |
| 32 | 2 | The second observation concerns what alf of the problem that has received leas | This assumes that all readers understand what the second observation is all about, maybe you are right, but to play safe, perhaps you can state it explicitly. For instance, like this "The second observation concerns gaps in the reporting of annotation reliability..." |
| 33 | 2 | the literature does not report, st attention. For the automate | A citation needed, because this is a claim about the literature. |
| 34 | 2 | For the automated and semi- most in doubt, reliability is automated corpora, precisely those whose labels are most in doubt, reliability is largely un… | Citation, especially to the relevant corpus studies? Otherwise, this is just your assumption. |
| 35 | 2 | reliability is easured under largely unreported, conditions that make | Fix this |
| 36 | 2 | where an agreement statistic is given, it is measured under resulting number difficult to interpret (Section 5). The field conditions that make the re… | A citation is needed, ideally to specific studies and an explanation of why their conditions are problematic. Otherwise, you are simply making a baseless and unreasonable claim. |
| 37 | 2 | The field onstrating therefore lacks not only trustworthy labels but a settled practice for demonstrating that any given set of labels is trustworthy.… | The word "trustworthy" appears 2 times in the same sentence. Besides, "trustworthy" and "settled practice" sounds informal in academic writing. Try express it in a more academic style such as "The field therefore lacks not only reliable annotations but also established practices for validating their reliability". |
| 38 | 2 | (Section 5). ice for demo | Remove this. |
| 39 | 2 | Annotation and evaluation fail an either deficiency alone, which together, and it is that conjunction, rather than either deficiency alone, which expl… | The last sentence is only valid if your previous claims are supported (via citation). But the way it is expressed is a little dense, making it potentially unclear. Do you think "The combined weakness of annotation and evaluation" is clearer? |
| 40 | 2 | fail hich | Unless you can prove this after reading many papers, otherwise. the word "fail" is too strong. Consider using a neutral word as a replacement to soften the claim. For instance, "problematic", "limited" or "weakness". |
| 41 | 2 | Scope. valuation | "Scope" is not an actual section heading, writing a paragraph that begins like this can feel slightly abrupt. Perhaps you can remove it. |
| 42 | 2 | remains domain | remain |
| 43 | 3 | both are well surveyed elsewhere. | "elsewhere" refers to the existing literature, right? Then, a citation is needed. |
| 44 | 3 | equally ment or | Remove "equally" to make the sentence sounds more and academic. |
| 45 | 3 | It does not propose, author's own work. implement or evaluate a system, and it does not report the author's own work. Its contribution is diagnosis an… | Fix this |
| 46 | 3 | diagnosis and direction: and of what the field wou | Fix this |
| 47 | 3 | Where the analysis identifies a vacancy in the literature, tops there. it names the vacancy and stops there. | Revise the last sentence as it sounds informal and less suitable to an academic paper. |
| 48 | 3 | Three contributions follow from that analysis. | Keep the three contributions concise without making it carries the technical mechanisms. |
| 49 | 3 | taxonomy of annotation strategies ranged along a fidelity-scalability | Fix this |
| 50 | 3 | fidelity-scalability axis, traint by conceding anoth | Fix this. |
| 51 | 3 | (Section 3.1, Table 1). | Remove this. Citation will be required in the Table. |
| 52 | 3 | that separates its structural e-based scoring under out-of- cause, the near-zero default of lexicon and rule-based scoring under out-of- vocabulary (O… | This is a new concept or mechanism that has not been introduced earlier, and readers will be confused with this term as in why you suddenly talk about something they have not read before. Maybe you should remove the near-zero/OOV mechanism from the contribution statement, only explain the mechanism later where you can introduce and support it properly. |
| 53 | 3 | diagnostic account of neutral-label skew use, the near-zero default of lexicon and rule | Fix this |
| 54 | 3 | structural nder out-of- | Fix this |
| 55 | 3 | ambiguity-driven ora actually repor | Fix this |
| 56 | 3 | audit of what regional corpora actually report about their own iability (Section 3.2; Section 5.2, Table 3). reliability | Fix this |
| 57 | 3 | (Section 3.2; Section 5.2, Table 3). | Remove this. |
| 58 | 3 | compound rather than merely coexist, class skew which corrupts the labels is t | Fix this |
| 59 | 3 | the same condition under which the be interpretable, and the research standard agreement statistic ceases to be interpretable, agenda that follows fro… | This is a new concept or mechanism that has not been introduced earlier, and readers will be confused with this term as in why you suddenly talk about something they have not read before. Maybe you should remove the mechanism from the contribution statement, only explain it later where you can introduce and support it properly. |
| 60 | 3 | corrupts ent statist | This sounds too strong and negative, perhaps you can go with a neutral tone first. For instance, "affect"? |
| 61 | 3 | research agenda | Fix this |
| 62 | 3 | (Section 6.2, Figure 1; Section 6.3). | Remove this. |
| 63 | 3 | (Section 2), models emp | Remove this. |
| 64 | 3 | (Section 3), n of annota | Remove this. |
| 65 | 3 | (Section 4) hesis that tr | Remove this. |
| 66 | 3 | (Section 5), system and | Remove this. |
| 67 | 3 | (Sections 6 and 7). | Remove this. |
| 68 | 3 | 1.1. Review Methodology | It feels weird to have only 1 subsection within a section. Besides, it is weird to have content presented right after the paragraph "The remainder of the paper..." because that already indicates the end of the section. Since your section 2 is about review, perhaps you can make it a standalone section, 2. Review Methodology? Unlike technical paper that talks about empirical study that involves expe… |
| 69 | 3 | (code- e task mixed, (sentim code-switching, ent analysis, pola Manglish, ity, opinio Bahasa mining Rojak, and th Malay-English), object of intere | Avoid writing sentences by including contents in brackets. Express it in a proper and complete sentence. If you read your introduction section again, you did this quite many times. |
| 70 | 3 | arXiv, Mangl | The use of papers from arXiv can be a little risky and they are pre-print papers, not equivalent to peer-reviewed journal/conference literature. So, if possible, consider only peer-reviewed publications and preprints with traceable publication or submission records. |
| 71 | 3 | (sentiment analysis, polarity, opinion mining) annotation, inter-annotator agreement, label q | Fix this |
| 72 | 3 | (corpus, 2019 to annotation, inter-annotator agreement, label quality). 2026, extended backwards by citation chaining from | Fix this |
| 73 | 3 | e n apparatus Section 5 examines it. | This part lacks clarity. Maybe my command of English is not that good, I cannot really understand what you are trying to say in a few parts of your previous writing until I got help from ChatGPT. It is embarrassing to say so but if you want readers to read your entire paper, then in academic writing, you need to prioritize simple and clear English but not complex vocabulary and complicated sentenc… |
| 74 | 3 | cannot be cited from within it. | This part also lacks clarity. |
| 75 | 3 | Four criteria governed inclusion. omparable Malay-English code-m | Make it more formal, such as "Four criteria were used to determine inclusion." |
| 76 | 4 | Open International Journal of Informatics (OIJI) (2019) Vol. 7 No. 2 (2019) evaluation practice to be assessed; be peer-reviewed or a preprint with a … | The second sentence is too dense. The semicolon structure makes the reader work too hard. Listing the four criteria in your paragraph can enhance readability and comprehension. For instance, "Studies were included if they met four criteria: (1) ...; (2) ...; (3) ...; and (4)". |
| 77 | 4 | is an what existi | Remove this. |
| 78 | 4 | because they take label quality as given and this her it can be. review is concerned with whether it can be. | The final part of "it can be" feels incomplete and hence lacks clarity in meaning. The reader has to infer whether label quality can be established or demonstrated. |
| 79 | 4 | All three are well described in the sociolinguistic literature; t the description but the consequence each carries for a perso | Citation? |
| 80 | 25 | References [1] Treffers-Daller, J | If possible, try increase the volume of references to at least 40. 24 references can be a little low for a review paper because a review paper systematically examines, synthesizes and critically evaluates existing research on a specific topic to identify key findings, gaps and future research directions. To be able to do so, it usually requires authors to read many recent related papers. |

---

# Part 4 — Appendix: Round 2, all 64 comments in document order

Extracted from `Template ICON AI 2026 - Section 1 to 3.1 (reviewed).pdf`. Same reconstruction caveat.
The fix applied to each of these is recorded in Part B of `ICON_AI_S1_to_S3.1_v5.md`.

| # | Page | Highlighted | Dr. Ho's comment |
|---|---|---|---|
| 1 | 2 | [Poria et al. (2023)]. applications that rang | You can consider to use this style: (Poria et al., 2023) |
| 2 | 2 | Most of these applications were built and tested uage. Malaysian social media text does not meet on text written in one standard language. Malaysian s… | The first sentence is a broad empirical claim about the application literature. Unfortunately, it is not self-evident and needs evidence. You can consider supporting it with a review/survey or multiple studies. In fact, the second sentence requires citation too. Otherwise, how do you know it doesn't meet that condition? Transition between these two sentences is not smooth. The last sentence create… |
| 3 | 2 | [Coluzzi (2017)] languages insid | Since your research concerns Malaysian social-media/Manglish sentiment analysis, it is perfectly acceptable to cite a 2017 paper for this sentence. But since there is almost a 10 years gap between 2017 and 2026. Many things can change within 10 years, for instance, is 140 remains a valid number. Has it increased or decreased? Therefore, I would prefer to add a more recent source on Malaysian code-… |
| 4 | 2 | This carries over a single message | This feels informal as "carries over” sounds conversational. |
| 5 | 2 | English and Malay are the pair that meets most often in written form, mixed varieties that result are known locally as Bahasa | Rewrite the highlighted part as it sounds weird and a little unnatural. |
| 6 | 2 | This kind of writing ent corpora examined in | What do you meant by this kind of writing? |
| 7 | 2 | X cte | What is X? For those who are not familiar with it, it is better to introduce it once. |
| 8 | 2 | Manglish alay rather | Transition from the previous sentence to this one can be enhanced. |
| 9 | 2 | language form not random. T | legitimate language variety? |
| 10 | 2 | Treffers-Daller et al. [Treffers-Daller et al. nan et al. (2025)] show that Malay-English (2022)] switchin | Use this style: Treffers-Daller et al. (2022) |
| 11 | 2 | this text written ca | What do you meant by text? Language or text? |
| 12 | 2 | When a sentiment model performs poorly on this material, the explanation ually given is architectural. The argument is that the model cannot handle co… | Citation? |
| 13 | 2 | this material, the model can | What do you meant by this material? |
| 14 | 2 | The argument ger or more reg | Is this argument referring to the previous sentence? Is this argument the same as the next "argument" in the following sentence? This writing style is a little informal and more importantly, it can result in unnecessary confusion. Perhaps you can consider changing the way of expressing the same idea? |
| 15 | 2 | part of the literature multilingual models fi | Citation? |
| 16 | 2 | the best 22)] sho | The best is not suitable because if it is the best, then it means that it is perfect, and there will be no room for improvement. But it is almost impossible to create something that is perfect. |
| 17 | 2 | The same inata et al. literature, (2021)] fi | If you are referring to Adilazuarda et al. (2022), perhaps you can consider changing the way you refer to it. |
| 18 | 2 | limits of this route. -training on its ow | Informal and less academic |
| 19 | 2 | Model choice is therefore part of the problem, but it is not all of it. | Citation? If available... |
| 20 | 2 | Before a model can be a sentiment label, either trained or evaluated, every message must be read and given a sentiment label, either | Citation? |
| 21 | 2 | sits earlier in the process. ge must be read and given | Informal... |
| 22 | 3 | label errors do not training [Frénay & stay inside the dataset. Verleysen (2014)], and | Informal... |
| 23 | 3 | Annotation quality matters because label errors do not y are learned by the model during training [Frénay & stay inside the dataset. Verleysen (2014)]… | Citation? |
| 24 | 3 | judge how good 1)]. This review the model is indicates that | Informal... At least use "evaluate model performance" |
| 25 | 3 | distort the test set 2021)], [Bowman | Test set itself is not necessarily distorted, but incorrect labels in the test set can distort the evaluation of model performance. |
| 26 | 3 | This review ata, the more indicates that for Malaysian Malay-English code-mixed sentiment data, the more limiting problem at present is the annotation… | The conclusion is understandable, but "This review indicates" jumps from general evidence to a specific claim about Malaysian Malay-English data suddenly... |
| 27 | 3 | Two observations he first concerns the | Two observations from the existing literature? |
| 28 | 3 | Each resource obtains some of these largest general-domain resource, properties MESocSen by ime giving t, show up the others. ost most | This is understandable but slightly informal... |
| 29 | 3 | cost m d 5.44 | This is ambiguous. Cost of what? |
| 30 | 3 | same kind of text. | Slightly informal... |
| 31 | 3 | how often they agree, after subtracting the agreement that duce [Artstein & Poesio (2008)]. Among the four regional chance alone would produce resourc… | This is a little informal... |
| 32 | 3 | this evidence is thin. nsurprising because it | Informal... |
| 33 | 3 | which is unsurprising et al. (2024)]. MyCov | Informal... |
| 34 | 3 | The two resources than the three-class that do report a coefficient measured a binary judgement rather than the three-class polarity task for which th… | Do you think this sentence feels incomplete? |
| 35 | 3 | the resources are actually used. 019)] report κ = 0.83 for an opi | What resources are you referring to? |
| 36 | 3 | κ = 0.83 ona et al. | What is ϰ? Not everyone knows that this is Cohen's kappa. |
| 37 | 3 | The field es for vali | What do you meant by the field? |
| 38 | 3 | These two weaknesses onnected. The class imba | If "two weaknesses" refers to the two observations established immediately before it, then this is understood. But the previous paragraph focused mainly on annotation reliability, while the class-imbalance issue was discussed in the paragraph before that, and this can result in a slight ambiguity. |
| 39 | 3 | are usually treated as separate problems, alance that affects the labels is also the co | Who treat them as separate problems? You or existing studies? |
| 40 | 3 | The class imbalance that affects the labels is also the condition under standard agreement statistic becomes difficult to interpret. It is this which … | Citation? |
| 41 | 3 | class imbalance that affects the labels dard agreement statistic becomes diffi | Class imbalance affects the distribution of labels rather than the labels. |
| 42 | 3 | standard agreement statistic weakness of annotation and ev | The "standard agreement statistic" is ambiguous. Which statistic? Cohen's κ? But you never mentioned that explicitly. |
| 43 | 3 | the problem | What do you meant the problem? Which problem? |
| 44 | 3 | has proved persistent. | Any support for this? |
| 45 | 4 | Comparative benchmarking of sentiment classifiers is ntiment analysis as a general field, because both have outside the scope, as is sentiment analysi… | This sentence is a little long and relatively difficult to digest. "Both" is a little ambiguous here. What are the two things? Comparative benchmarking of sentiment classifiers and sentiment analysis as a general field? |
| 46 | 4 | bear on de the s | Is "are relevant to" a better option? |
| 47 | 4 | It is also useful to state what this review does not do. mplement or evaluate a system, and it does not report the auth | Does this "The scope of this review also excludes several activities" sound less informal? |
| 48 | 4 | problem has resisted solution, Where the analysis finds that a | This sounds a little strong. |
| 49 | 4 | each tier improves either label fidelity or r. scalability | Can you enhance the clarity of this part? |
| 50 | 4 | by giving up the other. | Informal |
| 51 | 4 | two different causes of neutral-label skew, al corpora report about their own reliability. | Perhaps you can make this explicit to enhance its clarity. |
| 52 | 4 | audits | This sounds accounting-oriented... |
| 53 | 4 | simply occurring together, m that interaction. | Informal... |
| 54 | 4 | Preprints were treated with caution. A paper from arXiv was included only when o peer-reviewed version could be found and the preprint had a traceable… | If possible, try your best to not consider using any preprints frm arXiv. |
| 55 | 5 | Why Malaysian Code-Mixed Text Is Difficult to Annotate | A short bridging sentence added to the front of the first paragraph of this section would make the progression smoother because the previous section is still describing selection criteria but then the reader suddenly moves from how studies were selected directly to why the linguistic data are difficult to annotate. |
| 56 | 5 | Three properties rectly. All three h | Reader has to continue reading to discover what the three properties are. If this paragraph is intended to introduce the structure of Section 3, it is clearer to preview them. |
| 57 | 5 | a person or a program that has been asked to assign a rty is therefore followed by a short statement of that sentiment label. consequence, an | Informal... |
| 58 | 5 | is not developed further. | What is not developed further? |
| 59 | 5 | gives no structural cue | This is too strong and yet informal... |
| 60 | 5 | happens mostly . [Treffers-Daller | Informal... |
| 61 | 5 | with almost no grammatical friction 013)]. | Less formal... |
| 62 | 5 | The corpus consists of spoken data ld not be transferred to social media from two teachers, text. However, the | Citation? |
| 63 | 5 | sits inside | Informal... |
| 64 | 5 | In monolingual fied before it is annotation, the phrase carrying the opinion can usually be identified before it is judged. Here, identifying it is al… | Citation? |

---

# Part 5 — Appendix: Round 3, all 35 comments in document order

Extracted from `Template ICON AI 2026 - Section 1 to 7 (reviewed).pdf`, 24 August 2026. Comment text is verbatim.

## Page 1 — 3 comments

| # | Highlighted | Dr. Ho's comment | Type |
|---|---|---|---|
| 1 | lexicons, **pre- trained** models | "pre-trained?" | Mechanics |
| 2 | **a persistent source of degraded performance** | "Clarity can be enhanced. By the way, one possible concern is that not all code-switched text necessarily causes degraded performance in every NLP system, especially models specifically trained for multilingual or code-switched data." | Overclaim |
| 3 | Malaysian social media text is **writing of exactly this kind** | "This part lacks clarity. In academic writing, clarity is important. Thus, in this case, what 'this kind' means should be stated clearly. Suppose you are referring to the idea of 'Malaysian social media text frequently exhibits code-switching, with users often alternating between languages within a single message', then one or two citations are needed, even though you are a Malaysian and you know that this is likely to be true but not all readers are Malaysian." | Referent + citation |

## Page 2 — 27 comments

| # | Highlighted | Dr. Ho's comment | Type |
|---|---|---|---|
| 4 | **Coluzzi (2017)** | "Does the citation to Coluzzi (2017) support approximately 140 languages in Malaysia only or including widespread code-mixing involving first languages, English, and Malay? If the second one is not supported, then a separate citation is needed." | **Citation check** |
| 5 | code-mixing between **a speaker's first language**, English and Malay | "Malaysia has many linguistic communities, therefore, in the case of Malaysia, individuals may be bilingual or multilingual from childhood. The use of 'first language' may oversimplify this linguistic situation." | Factual precision |
| 6 | The practice has **continued rather than** receded | "This implies a historical trend. Unless the cited studies explicitly examine this temporal development, this wording may be stronger than the evidence supports. Consider using a simpler and more defensible style." | Overclaim |
| 7 | **English and Malay are the pair that combines most frequently in Malaysian writing** | "The way it is written sounds a little awkward, perhaps express it like this 'English and Malay are among the languages most frequently combined in Malaysian written communication…'" | Register — **wording supplied** |
| 8 | **the mixed varieties they produce** are known locally as Bahasa Rojak and Manglish | "Bahasa Rojak and Manglish are not necessarily interchangeable labels for all Malay-English mixed writing. They could be the mix of more languages. Please double check the cited source again." | **Citation check** |
| 9 | **Malay-English mixed writing is frequent enough on X … that both of the Malaysian sentiment corpora examined in this review were collected from it** | "This sentence suggests a causal relationship where Malay-English mixing is frequent on X and therefore researchers collected both corpora from X. But the fact that both datasets were collected from X does not itself demonstrate that Malay-English mixed writing is frequent there. The researchers may have selected X for other reasons. Please double check on this and make sure the citation is used properly." | **Citation check** + logic |
| 10 | **How this mixed writing is regarded** matters for how it is processed | "How it is regarded introduces a new idea, which social or linguistic perception, which feels a little abrupt." | Bridge |
| 11 | **Treffers-Daller et al. (2022) and AlAfnan et al. (2025) show** that Malay-English switching follows describable syntactic and pragmatic patterns, and that speakers use it deliberately to communicate efficiently, signal identity and build rapport | "Do both papers support all three communicative purposes including communicate efficiently, signal identity, and build rapport?" | **Citation check** |
| 12 | the negator *tidak* **written** as x | "being written" | Grammar — **wording supplied** |
| 13 | at the level of **spelling: Maskat and Rahman (2020) record** the negator *tidak* | "'…spelling, with Maskat and Rahman (2020) documenting the Malay negator *tidak* being written as..'" | Register — **wording supplied** |
| 14 | but **a lexicon** compiled from standard Malay | "Which lexicon are you referring to?" | Referent |
| 15 | **but a lexicon compiled from standard Malay lists none of those forms.** | "Citation or assumption?" | **Citation check** |
| 16 | (NLP) is therefore not **carelessness** | "If any previous work explicitly characterizes code-mixed social media writing as noisy, erroneous or non-standard, then you should cite it here. Otherwise, readers may wonder who considers it 'carelessness'?" | **Citation check** |
| 17 | **It is that** the conventions Malaysian writers follow | "The opening of this sentence does not sound natural or smooth continuation from the previous sentence." | Register |
| 18 | so **writing that is systematic is processed as noise** | "This is a strong claim. You should verify that both citations genuinely support this interpretation." | **Citation check** + overclaim |
| 19 | the **explanation offered is most often architectural** | "This feels slightly abrupt because you have not explicitly framed architecture as an alternative explanation to the resource/input problem. 'Most often' sounds very strong. Perhaps you should be using 'one common explanation'?" | Overclaim + bridge — **wording supplied** |
| 20 | **On that account** the model cannot handle | "This is not so academic writing." | Register |
| 21 | the model **cannot handle** code-switched input | "This feels absolute because a model may not completely 'fail' to handle code-switched input, it may perform less effectively or struggle to process it." | Overclaim |
| 22 | a larger or more regionally adapted model **would** perform better | "Use 'may'?" | Overclaim — **wording supplied** |
| 23 | **Against** that, Winata et al. (2021) find | "Use 'in contrast' will sound better." | Register — **wording supplied** |
| 24 | finite model capacity, **spread across** many languages | "Capacity cannot spread across language, use 'accommodate'" | Figurative — **wording supplied** |
| 25 | **dilutes per-language** quality | "This sounds less academic, use 'potentially reducing the quality of representations for individual languages'." | Figurative — **wording supplied** |
| 26 | **The remainder of the difficulty does not originate in the** model | "This may sound better and slightly more academic 'another source of difficulty does not originate in the model itself.'" | Register — **wording supplied** |
| 27 | **Supervised sentiment analysis requires that every message be read and assigned a sentiment label … before any model can be trained or evaluated on it (Artstein and Poesio, 2008).** | "Artstein and Poesio (2008) is primarily about annotation and agreement methodology. So, please verify whether it directly supports the broader claim about supervised sentiment analysis requiring every message to be read and labelled before training/evaluation." | **Citation check** |
| 28 | the supervision signal **a model learns from and is measured** against | "This could be interpreted slightly awkwardly because the model's predictions are measured against the labels, rather than the model itself." | Technical precision |
| 29 | The consequences of incorrect labels **reach beyond the** dataset | "This is somewhat figurative. Make it more direct academic version like this 'Incorrect labels can affect both model training and subsequent evaluation.'" | Figurative — **wording supplied** |
| 30 | **Label noise is learned during training** | "Technically it is the patterns associated with noisy labels that can be learned by the model." | Technical precision |

## Page 3 — 5 comments

| # | Highlighted | Dr. Ho's comment | Type |
|---|---|---|---|
| 31 | **so that reported accuracy no longer reflects how the model actually behaves** | "This is too absolute. Even with some incorrect labels, accuracy can still provide information about performance, it is simply biased or less reliable." | Overclaim |
| 32 | **An unsound label therefore damages the model** twice | "This is technically imprecise because a label does not necessarily 'damage the model' itself. But it can affect the model during training, and affect the measurement of the model during evaluation." | Figurative + precision |
| 33 | once when it is trained and again **when it is** measured | "This could imply that the model is being physically measured. In fact, it is its performance being measured." | Technical precision |
| 34 | **the annotation label is at present the more limiting** problem | "This might be grammatically understandable but definitely unnatural." | Register |
| 35 | **together with the evidence offered that the label is sound.** | "This is particularly unclear. It sounds as though the annotation label is a problem together with evidence that it is sound" | Clarity |

---

# Part 6 — Appendix: Round 4, all 60 comments in document order

Extracted from `ICON AI 2026 - Section 1 (reviewed).pdf`, 29 August 2026. Highlighted text is
reconstructed from the PDF annotation geometry, so it sometimes picks up part of the line beneath.
Comment text is verbatim. **What changed for each is recorded in `ICON_AI_Comment_Tracker_R4.md`.**

| # | Page | Highlighted | Dr. Ho's comment |
|---|---|---|---|
| 1 | 1 | Joshi et al. (2020) show that only a small number of the world's languages are represented in current language technologies. Lexicons, pre-trained mod | Reading can be made difficult if the same source is cited in few sentences right after another. For instance, you can remove the second citation by revising it as: "Joshi et al. (2020) highlight that only a small number of the world's languages are represented in current language technologies, with lexicons, pre-trained models and benchmark corpora concentrated in those few languages." |
| 2 | 1 | carry an assumption | Even though the next sentence explains a little about this part, but you can actually enhance its clarity here to make the connection to the next sentence more explicit. Because a reader may ask what assumption are you referring to when first read about this. |
| 3 | 1 | The | Adding "However" to the front of this sentence will signal that you are moving from the usefulness of sentiment analysis to one of its limitations. |
| 4 | 1 | pre-trained model is one that has already learned general patterns from a large body of text, and is then adapted to a particular task such as sentime | Citation is needed. But if you read beginning from the previous sentence again, do you feel that it feels a little abrupt to talk about pre-trained model here. The reason is that even though lexicons, pre-trained models and benchmark corpora are mentioned in the previous sentence, but you talk about them 3 again in the next sentence... |
| 5 | 1 | Each of these resources is built for one language | This is too absolute because how do you know not every modern language resource is strictly monolingual? This can become more convincing if you can get a strong citation. Otherwise, you can soften it like this "Many of these resources are developed primarily for individual languages..." |
| 6 | 1 | effect | This can be slightly ambiguous because readers may ask effect of what exactly? As mentioned earlier, make EVERYTHING straightforward and clear. If you are referring to effect of code-switching on model performance, then you can just say it explicitly |
| 7 | 1 | two languages alternate within a single message | In the next sentence, "code-switched language" is used, but you never named the phenomenon of "two languages alternate within a single message" as "code-switched". In this case, readers will have to infer the relationship between them by themselves. This is another example where clarity must be enhanced, to make everything clear and stated explicitly. |
| 8 | 2 | one variety | One variety of what? Do you mean a variety of code-switched text? By the way, "Malaysian social media text" itself is not necessarily a "variety" because one is text and another is a mixed of two languages... |
| 9 | 2 | Coluzzi (2017), citing Ethnologue, records around 140 languages in use | This part feels slightly awkward. |
| 10 | 2 | for such mixed writing, | This is slightly vague. It could refer to all multilingual Malaysian writing rather than specifically to code-mixed or code-switched writing. So, which one are you referring to? |
| 11 | 2 | they do not cover the same set of languages | This feels less formal... |
| 12 | 2 | in part. | What do you meant by "in part"? |
| 13 | 2 | so this review states its position b | You don't have to explicitly tell what the paper is doing like this. |
| 14 | 2 | How this mixed writing is regarded | What does "regarded" mean? This is what readers feel when they read this. Even though this is explained in the next sentence, you can make it more precise here. |
| 15 | 2 | technical difficulty | This also ambiguous. If you are referring to the difficulty of processing Manglish using NLP models, then just say so, don't make it more complex unnecessarily. |
| 16 | 2 | weakens | Does the cited source make this claim using "weakens" because it sounds strong. If not, then better use the softer version "having a negative effect on" |
| 17 | 2 | How this mixed writing is regarded affects how it is processed, | This sounds like a claim, so a citation is needed. |
| 18 | 2 | Its structure, however, is not random | You can be more precise like this "Its structure, however, is systematic rather than random." |
| 19 | 2 | The same regularity | "The same regularity" could be slightly clearer because the reader has to infer that you mean systematicity. Perhaps you can write "The same systematicity appears at the level of spelling..." to create an explicit link |
| 20 | 2 | Maskat and Rahman (2020) sort this variation into five categories and map two of them back to their standard forms, which indicates that the variation | There is a logical issue here. The fact that the authors categorize the variation and map two categories to standard forms does not necessarily prove that the variation is systematic., indicating that the inference might be over strong. A softer version can be like this "...This categorization suggests that the variation follows recurring patterns rather than occurring arbitrarily..." |
| 21 | 2 | A dictionary of standard Malay, such as the one curated by Dewan Bahasa dan Pustaka, does not list the non- standard forms | This needs citation, and better cite Dewan Bahasa dan Pustaka. |
| 22 | 2 | Tools that rely on such a dictionary therefore treat them as out-of- vocabulary items | This sounds logical in general but a small assumption might have been made incorrectly here. A dictionary not containing a word does not automatically mean that all tools relying on it will treat the word as an OOV item. It depends on how the tool is designed. Consider use the softer version of "...may therefore..." |
| 23 | 2 | Malay social media text has accordingly been described in earlier work as misspelled, out-of-vocabulary, ill- formed and noisy (Maskat and Rahman, 202 | There are two different ways to interpret this sentence. First, the two cited sources mentioned that earlier work described Malay social media text as ill-formed and noisy. Or second, these two cited sources make such claim? If it is the latter case, then you should have shifted the cited source to right after "earlier work". |
| 24 | 2 | The conventions Malaysian writers follow are consistent, | This is very a broad claim about all Malaysian writers generally. if your evidence concerns particular forms of Manglish social media writing. It would be safer to narrow the subject: "These writing conventions are consistent within the observed variation..." |
| 25 | 2 | were built to | "designed to" is used more often in academic writing |
| 26 | 3 | When a sentiment model performs poorly on Malay-English mixed text, one common explanation is architectural | The transition from the end of the previous paragraph to the beginning of this paragraph is a little abrupt because it jumps quite quickly from the linguistic/resource mismatch to architecture. By the way, do you think it reads better when the second part of the sentence is revised as "...one common explanation concerns the model architecture." |
| 27 | 3 | On this explanation | Reading this doesn't feel natural... "Under this explanation" or "Under this view" may sound better. |
| 28 | 3 | regionally adapted | What do you meant by "regionally adapted"? Does it mean trained on Malaysian data, fine-tuned on Malay-English data, trained on Southeast Asian languages, or adapted to local linguistic patterns? You should specify what you mean. |
| 29 | 3 | capacity dilution | Perhaps you can define this to enhance its clarity. |
| 30 | 3 | Another source of difficulty does not originate in the model itself. It originates one step earlier, at the point where the labels are created | This feels more academic and straight to the point "Another source of difficulty arises one step earlier, at the point where sentiment labels are created." |
| 31 | 3 | often limiting | This lacks clarity. Limiting in what way? |
| 32 | 3 | an automatic one | "Automatic one" is understandable but it doesn't sound natural |
| 33 | 3 | it produces | Removing this can make the message clearer. |
| 34 | 3 | and Frénay and Verleysen (2014) report that the accuracy of predictions may decrease as a result. | This sounds a little awkward, try this "...which can reduce predictive accuracy (Frénay & Verleysen, 2014)." |
| 35 | 3 | they | Make it clearer using "label errors" |
| 36 | 3 | more limiting problem | Your previous paragraph establishes that label errors can affect training and evaluation, but it does not by itself establish that labels are more limiting than models for Malaysian Malay-English sentiment data. |
| 37 | 3 | second | What is the first problem? Make it clearer and avoid making the reader wonder what "second" refers to. |
| 38 | 3 | reading | Reading of what? |
| 39 | 3 | four Malay-English sentiment resources | It is safer to say "four resources are identified in this review", otherwise readers may ask whether you are really certain there are only four? |
| 40 | 3 | large | What counts as large? You need an operational definition somewhere in the paper, or this claim could appear subjective. For example, if you later define a threshold such as 10,000 messages, say so. |
| 41 | 3 | validated by human annotators | This can be ambiguous. Does it mean the labels were assigned by humans, the labels were checked by humans, multiple human annotators independently labelled the data, inter-annotator agreement was measured, and a subset was manually validated? if you specifically mean agreement/reliability, then perhaps it is better to use "with annotation reliability assessed by human annotators" |
| 42 | 3 | secures some of these properties at the expense of the others | This part feels informal in academic writing. This style is more commonly used "...satisfies some of these criteria but not all of them..." |
| 43 | 4 | coefficient | What coefficient? A reader may not immediately know whether you mean Cohen's kappa, Fleiss' kappa, or any other agreement coefficient. Alternatively, use a general term like "inter-annotator agreement coefficient" to refer to it |
| 44 | 4 | narrower task than the corpus is used to support | What exactly is narrower? This part can be difficult to understand. Remember? Don't increase the complexity of your writing unnecessarily. You want your readers to understand your ideas and messages 100%, right? |
| 45 | 4 | describe one condition rather than two | You are describing two related problems or limitations but not necessarily one "condition", right? So, "condition" is not quite the right word to be used here. Which one is easier to understand? The one you wrote here or "The second and third findings are closely related rather than independent."? |
| 46 | 4 | demonstrated | Reliability is not always "demonstrated" specifically through Cohen's kappa. It is safer to use "assessed" |
| 47 | 4 | the most widely used of which is Cohen's kappa (κ) | If Artstein and Poesio (2008) explicitly support it, fine. Otherwise, avoids an unnecessary claim by simply saying "such as Cohen's kappa (κ)" |
| 48 | 4 | stops being informative | This is too strong. Cohen's κ does not simply "stop being informative." Its interpretation can become problematic or misleading under prevalence imbalance. It is safer to use a softer tone like this "...can make the statistic used to assess the labels more difficult to interpret." |
| 49 | 4 | A 2024 review of the field still reports a lack of comprehensive datasets and annotated resources for code- mixed Malay text (Selvaraju et al., 2024). | The paragraph has been discussing 1) annotation reliability, 2) class imbalance, and 3) Cohen's κ. Then suddenly, you talk about this. The connection is not explicit, the reader has to infer it. Try explicitly connect the review to your argument. |
| 50 | 4 | This review examines one question | Since this sentence connects the previous paragraph's discussion of class imbalance, annotation reliability, and limited resources directly to the central question, perhaps you can enhance the transition a little? |
| 51 | 4 | remain unresolved | This part can be ambiguous because a question is unresolved, but annotation and evaluation themselves are not usually described as unresolved. |
| 52 | 4 | author's | Use authors' because this is a multi-author paper |
| 53 | 4 | diagnosis | Diagnosis is less academic, perhaps you can consider to use either "analysis", "synthesis" or "examination" |
| 54 | 4 | the problem | This is slightly ambiguous because "the problem" could refer to several things. Make it explicit. |
| 55 | 4 | gains either label fidelity or scalability at the expense of the other | A tier does not necessarily "gain either label fidelity or scalability". Most probably you are referring to the fact that there is a trade-off. |
| 56 | 4 | and shows that each tier gains either label fidelity or scalability at the expense of the other. | Perhaps you can say "...and examines the trade-off between label fidelity and scalability across them." |
| 57 | 4 | two causes of neutral-label skew | Use "two sources of neutral-label skew" to indicate that there might be more than two causes. |
| 58 | 4 | four regional corpora | This term is unclear. Earlier, you used "four Malay-English sentiment resources". Now you say "four regional corpora." "Regional corpora" is broader and potentially ambiguous. Does "regional" mean Malaysian, Southeast Asian, Malay-English, or locally developed? |
| 59 | 4 | what each of the four regional corpora reports about its own reliability | This is understandable, but it also sounds like a corpus will literally report something. |
| 60 | 4 | measurement c | I think "evaluation" may be clearer than "measurement" unless you want to distinguish the measurement of annotation reliability from model evaluation. |