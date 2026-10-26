# ICON AI — v19 → v20 readability rewrite

**Built:** 10 September 2026, from `Template ICON AI 2026 - Section 1 to 7 (v19).docx`. v19 is untouched and remains the backup.
**Output:** `Review Paper/Current/Template ICON AI 2026 - Section 1 to 7 (v20).docx` and a LibreOffice PDF preview beside it.
**Brief:** make the paper read like Poria et al. (2020), *Beneath the Tip of the Iceberg* — the review Dr. Ho gave as the example of good, easy reading. Clarity first, content second, page count last. Content may go; Section 1 stays.

## 1. Numbers

| | v19 | v20 |
|---|---|---|
| LibreOffice page count | 20 (references ended 6 lines into page 20) | **16** (references end about 60% down page 16) |
| Words, whole file | 9,948 | 8,198 |
| Body words, Sections 2–6 excluding tables | 6,044 | **4,307** (−29%) |
| Paragraphs in Sections 2–6 | 53 | 42 |
| Longest paragraph | 228 words | 158 words |
| Sentences over 30 words in Sections 2–6 | 17 | 11 |
| "Section N" back-references in Sections 2–6 | 13 | 9 |
| References | 38 | 38 — every one still cited, none orphaned |
| Section 1 and Abstract | — | byte-identical to v19 except six words in the roadmap |
| Tables and Figure 1 | — | unchanged |

Per subsection (body words, tables excluded): 2 opener 150→119 · 2.1 455→354 · 2.2 588→428 · 2.3 570→387 · 3 opener 104→70 · 3.1 557→439 · 3.2 678→546 · 3.3 619→469 · 3.4 228→deleted · 4 595→476 · 5 1,357→883 (opener 59, 5.1 371, 5.2 453) · 6 143→136.

**Dr. Ho's checker (`check_section.py`) over Sections 2–6:** 0 sentences over 35 words except the six-item numbered list in Direction 2 · 0 same-source-on-consecutive-sentences · 0 claim words without a citation · 0 previously flagged informal phrases · 0 parenthetical cross-references. The only pass-6 "bold" hits are headings and table header cells, as in every previous version. v19 had three live hits under passes 3 and 4 ("most", "the statistic used", "against that"); v20 has none.

**On the page count.** LibreOffice and Word have differed by 0–1 page on every version. Open v20 in Word and check. Either way the paper is now well under the 20-page limit and at or near the template's own "reviews no longer than 15 pages" line, which removes that question. There is room for the references Dr. Ho said he would ask you to add.

---

## 2. What the 2020 paper does that v19 did not

I read all thirty pages of Poria et al. with your question in mind — not what they say, but how. Nine habits carry their readability, and each one names a habit v19 had lost.

1. **A subsection opens with its point in one plain sentence.** "Sentiment on different aspects can be expressed implicitly." "Context is at the core of NLP research." The reader knows what the next three paragraphs are about before reading them. v19 opened subsections with the evidence ("Treffers-Daller et al. (2022) analysed 1,044 switched utterances…") and arrived at the point two paragraphs later.
2. **Paragraphs are 60–120 words and carry one idea.** Almost none exceed 150. v19's ran 100–230, and the long ones were long because they held a finding, a caveat about the finding, a definition, and the consequence, all at once.
3. **Terms are avoided rather than defined.** Where Poria et al. need a technical idea they say it in ordinary words ("words that sound neutral on the surface can bear sentiment when conjugated with other words") and reserve jargon for things the reader already knows. v19, following Rule 5 literally, kept the term and added a definition sentence after it: *inflectional morphology*, *span*, *encoder*, *marginal totals*, *BERT is a bidirectional transformer encoder*, "architecture, meaning that they are built in different ways". Each of those is a sentence the reader must process and then discard. v20 says the fact instead: "Malay words change little in form to mark features such as tense"; "the annotator first marks the words that express the opinion". Dr. Ho's rule is satisfied — there is no undefined term — and the reader never meets the term.
4. **One example per idea, and it is short.** A single italicised sentence ("*I hate the touchscreen as it freezes after 2-3 touches*"), then the implication. v19 stacked examples: five spellings of *macam mana*, then two vowel-less forms, then two regional forms of *besar*, then a combined form. v20 keeps the first two sets.
5. **Numbers appear when they are the finding, not as texture.** Poria et al. rarely give a count unless it is the point. v19 gave 33.0%, 30.7% and 24.8% for three named switching types when the argument needs only "most switches occurred within the clause"; 121 of 1,044 utterances when 11.6% carries the same information; 5,849 → 4,191 → 2,316 when Table 1 already holds the numbers.
6. **Sources are not caveated at length.** The 2020 paper cites and moves on. v19 had three caveat paragraphs in Section 2 alone ("Neither source measures…", "Two limits on this evidence should be noted…", "These proportions were measured on spoken classroom data…"). v20 keeps each as one to three sentences — enough that Dr. Ho's "does the source say this" check is answered, no more.
7. **Nothing is said twice.** The 2020 paper has no synthesis section that retells the survey; its conclusion is two short paragraphs. v19's Section 5 re-narrated Sections 2–4 as six "links" in 750 words, with new vocabulary (link, chain, arrow, cycle), and then the Conclusion told it a third time. Every reader hits the same content three times in different words. See Section 4 below for the full repetition table.
8. **The paper does not describe itself.** Poria et al. say "we discuss these applications next" once and otherwise just discuss them. v19 carried sentences whose only job was to comment on the paper's own reasoning: "this review states them as an inference rather than as a reported finding"; "Establishing that this structure exists is the contribution this review claims"; "since a direction that cannot be traced to a finding is a preference rather than a conclusion"; "That remains a suggestion rather than a measurement, and it is returned to in Section 5"; "These are directions rather than results. The claim of this review is not that they will succeed…". This is Dr. Ho's Rule 17 at paragraph scale. All of them are gone.
9. **No sentence is written to be admired.** This is the one that most produced the "read it twice" effect. v19 had a habit of closing paragraphs with a balanced or inverted sentence: "The property that makes the labels unrepresentative is therefore the property that makes the statistic used to check them difficult to interpret." "The evidence that would distinguish them is the affect the annotator could not read, and that is the evidence the annotator lacks." "It keeps the labels it is confident about and wrong about, and it deletes the labels it is uncertain about and would have learned from." "The chain does not merely persist. It reproduces itself." "unanimity produced this way is indistinguishable from confidence." Each is elegant and each costs a re-read. v20 states the same point once, in subject–verb–object order: "The same skew that makes the labels unrepresentative also makes the coefficient used to check them difficult to interpret."

What I did **not** copy from the 2020 paper: its first-person voice ("we believe"), its very long connected sentences, and its light hedging. Dr. Ho has asked for the opposite of all three (Rules 1, 3 and 6), and his instruction on the v17 Section 2 extract — that sentences were "written slightly densely where few ideas are compressed into one sentence" — still governs. So v20 keeps one idea per sentence and keeps the hedges (*may*, *can*, *suggests*, *is described as*). The mean sentence length rises from 16.7 to 18.8 words only because the choppiest v19 sentences ("A span is a marked stretch of text.") are gone; every sentence that joined two ideas with *so* or *and* was split again before the file was saved.

---

## 3. Section by section — what changed and why

### Section 1 and the Abstract — unchanged

Left exactly as Dr. Ho approved them, except the roadmap, which lost the six words "and the models used as annotators" because 3.4 no longer exists. That sentence was rewritten in v19 and he has never commented on it.

I looked hard for a strong reason to touch Section 1 and did not find one. Its length (1,925 words, now 29% of the body) is the only thing a reader would notice, and every candidate cut (C1–C8 in the old list) removes a sentence that exists because of one of his comments or carries his own wording. The one exception, the AlAfnan repeat in paragraph 2 (37 words), is not worth reopening an approved section. Recommendation: send Section 1 as it is.

### Section 2 — 1,763 → 1,288 words

*What the section is for:* three properties of the text, each with its consequence for the annotator. That is all v20 keeps.

- **Opener.** Kept the bridge from Section 1 and the named preview of the three properties (his R2 55 and R2 56). Cut the sentence that gave the first property's consequence early (the subsection gives it) and defined *affect* inline instead of in its own sentence.
- **2.1.** Cut the three named switching types with their percentages and definitions; kept "the majority of the switches occurred within the clause" and a plain description of the two main forms. Replaced "Malay also has very little inflectional morphology. Inflectional morphology refers to…" with "Malay words change little in form to mark features such as tense". Kept the spoken-data caveat in three split sentences, as he asked. Compressed the aspect-based sentiment detour from five sentences to two, both cited, and removed the word *span* rather than defining it.
- **2.2.** Dropped the formal definition of back-flagging (the construction is described in plain words, and Muysken still names it). Merged AlAfnan's two sentences into one. Cut the caveat paragraph from 81 to 40 words. Merged the two-readings example ("irritation, which is negative, or politeness, which is neutral") into one sentence. Kept the Pavlick and Kwiatkowski paragraph, shortened, because it is the evidence for "systematic rather than random" that Section 5 relies on.
- **2.3.** Cut the "Social Media Malay Language" label, the collection years, the regional *besar* example, the combined-category example, the "435 distinct words" detail, and the first of the two limits (Selangor slang), which only existed to point at the regional example. Kept the five categories, the *macam mana* set, the vowel-less examples, the 0.43 precision with its meaning stated inline, and the limit that matters (English removed before the experiment). The closing consequence paragraph is kept because Section 3.1 builds on it.

### Section 3 — 2,215 → 1,524 words

- **Opener.** Kept the bridge and the preview; removed the Artstein/Uma citations from it because 3.3 opens with the same sentence and the same citations, so the reader met them twice in a page.
- **3.1.** Table 1 now referenced from the text (it was not before). Manual tier: cut the "retained 40% / labelled 11%" sentence — the numbers already show it. Semi-automated tier: cut the library names and the pre-processing count. Generative tier: cut "Marathi is morphologically rich where Malay is not"; the closing sentence ("no study examined here evaluates generative annotation on Malaysian code-mixed text") already says the result does not transfer. BERT is tied to Section 1's definition of a pre-trained model instead of getting a new definition sentence.
- **3.2.** Kept in full the parts that are the paper's own analysis: the VADER threshold mechanism, the six-example error analysis, and the human-annotator comparison (23.6% neutral). Cut the sentence "this review states them as an inference rather than as a reported finding" and marked the inference with "It follows that" instead. Merged the "separating matters" and "depletion" paragraphs into one, removing the aphoristic closing sentence.
- **3.3.** Renamed "Two weaknesses of majority voting" so the heading says what the subsection shows. Merged the two opening paragraphs. Simplified the model-capacity point (pysentimiento is the only transformer-based tool and skewed hardest) to two sentences. Cut the "double effect" sentence. Folded the Uma et al. paragraph and the independence caveat into the arithmetic paragraph, so the subsection ends once, with the pointer to Section 5.
- **3.4 — deleted.** This is the largest single cut after Section 5. Its only content not already in the paper is the point that a fine-tuned annotator resolves only the variation it was trained on — which Section 5 needs for the arrow in Figure 1 that returns to automation, and now states there in two sentences with Manukonda and Kodali (2025) still cited. Adilazuarda et al. is already in Section 1 paragraph 5; Jadhav et al. is already in 3.1; "selecting an annotator selects which errors a corpus contains" already closes 2.3. The approved contribution statement names three challenges — linguistic, annotation, evaluation — and the paper's sections are now exactly those three.

### Section 4 — 626 → 476 words

Kept the bridge (R2 55), the κ definition, the conventions, the prevalence mechanism, Table 3 and the three observations. Cut Feinstein and Cicchetti's three-sentence worked example (0.85 observed → κ 0.70 or 0.32) and kept Di Eugenio and Glass's one-sentence one (90 of 100 agreed → κ from −0.048 to 0.80), which is shorter and more memorable; Feinstein and Cicchetti and Byrt et al. remain the citation for the mechanism. Cut the definition of *marginal totals* by not using the term. The key sentence is now stated directly: "The same skew that makes the labels unrepresentative also makes the coefficient used to check them difficult to interpret." The closing paragraph is kept — it is the paper's thesis and the only place it needs to be argued.

### Section 5 — 1,367 → 883 words, now 5.1 and 5.2

This is where readers were reading everything a second time. The six numbered "links" walked back through Sections 2–4 in 750 words, re-citing the evidence and adding vocabulary (link, chain, cycle, arrow). Figure 1 already numbers the six connections. v20 tells the chain **once**, in two paragraphs (371 words), stating only the connections and citing only what is new at that point: the random-versus-systematic contrast (Pavlick and Kwiatkowski), the interpretation problem (Feinstein and Cicchetti; Byrt et al.), and the fine-tuning inheritance (Manukonda and Kodali). Everything else the reader has just read is not repeated. A third paragraph keeps the paper's most important claim — that an intervention at one point is assessed with a statistic compromised at another — in plain words.

The opener lost "Establishing that this structure exists is the contribution this review claims" (the contributions are in Section 1). The directions lost their "and it follows from the Nth link" scaffolding and the closing hedge paragraph. All four directions survive, each 60–140 words; Direction 2's six-element list is kept intact. The section is split into **5.1 The compounding chain** and **5.2 Directions for future research** so a reader can find either.

### Section 6 — 143 → 136 words

Kept; the 40-word final sentence split in two.

---

## 4. Where each repeated point now lives

| Point | v19 said it in | v20 says it in |
|---|---|---|
| Disagreement from more than one justifiable reading is not removed by adding annotators (Pavlick and Kwiatkowski) | 2.2, 3.2, 5 link 1, 5 D3 | 2.2 (evidence), 3.2 (one-line pointer), 5.1 (one sentence) |
| Annotators of different types may not fail independently | 3.3 ¶2, 3.3 last ¶, 5 link 3, 5 D4 | 3.3 (once, closing), 5.2 D4 |
| 78.23% neutral | 1, 3.2, 4, 5 link 4, Table 2 | 1, 3.2, 4, Table 2 |
| The prevalence problem | 1, 4, 5 link 5, 5 D1, 6 | 1, 4 (full treatment), 5.1 (one sentence), 6 (one clause) |
| Choice of annotator determines which errors a corpus contains | 2.3, 3.4 | 2.3 |
| Mohd Shamsuddin's reason for automating | 3.1 (one quote), 5 link 2 (a second quote) | 3.1 (quote), 5.1 (paraphrase) |
| The 512 removed posts | 3.3 (twice), 5 link 4 | 3.3 |
| "Absorbed without accumulating" | 5 ¶8, 5 last ¶ | 5.1, once, in plain words |
| Annotation and evaluation problems have one cause | 1, 4, 5 link 5, 6 | 4 (thesis), 5.1, 6 (one sentence each) |
| Fine-tuned annotators inherit their training data's limits | 3.4, 5 link 6 | 5.1 |

---

## 5. Verdict on the v18 cut list, under the new priority

The list you asked me to verify was written to preserve every finding and lose only repetition; the verified version was more conservative still. Your brief changes the yardstick, so several DO-NOT-CUT verdicts flip. "v19" below means the cut was already applied in the v19 build.

| Cut | Old list said | Verified list said | **v20** |
|---|---|---|---|
| C1–C8 (Section 1) | reserve | do not cut | **Not applied.** Not a readability problem; each removes his wording or a cited sentence he asked for |
| C9 roadmap | keep | keep | Applied in v19; six more words removed now for 3.4 |
| C10 S2 opener | replace with 40 words | keep bridge and preview | **Middle path**: bridge and named preview kept (R2 55/56), 150→119 |
| C11 2.1 definitions | trim 20 | trim 4 | **Went further**: percentages and named switch types cut; *inflectional morphology* removed by saying the fact |
| C12 2.1 caveat | rejoin into one sentence | do not (his density comment) | **Verified list was right**: kept split, trimmed 102→75 |
| C13 2.1 aspect-based detour | compress to one sentence | keep the definitions | **Went further than either**: two cited sentences, *span* removed rather than defined |
| C14 back-flagging definition | fold | do not | **Cut** the formal definition; Muysken still names it, the construction is described plainly |
| C15 | delete "distinguish" sentence | merge | Merged (v19) |
| C16 2.2 caveat | one 43-word sentence | four sentences | **Three short sentences, 40 words** |
| C17, C18 | delete | delete | v19 |
| C19 regional slang pair | delete | do not (caveat points at it) | **Cut**, together with the Selangor caveat that pointed at it, so nothing dangles |
| C20 normalisation trims | trim | trim | **Went further**: SMML label, years, 435-word figure cut; every definition kept inline |
| C21 2.3 "two limits" | compress | do not | **Cut to the one limit that matters** (English removed); the Selangor limit went with C19 |
| C22, C23 | delete | delete | v19 |
| C24 S3 opener | replace | keep bridge, add 3.4 | Bridge and preview kept; duplicate citations moved to 3.3; 3.4 removed from preview |
| C25 Jadhav list | trim | trim | v19; also cut the Marathi-morphology caveat and the library names |
| C26 | trim | trim | v19; paragraph then merged into the one before it |
| C27 3.3 closing | delete 68 words | keep the hedge | **One sentence** of hedge kept, folded into the arithmetic paragraph |
| C28 Section 4 → 3.4 | fold to 120 words | fold to 233 words | **Deleted 3.4 entirely**; its one necessary point moved to 5.1 (two sentences, citation kept) |
| C29 S4 bridge | delete | keep | Kept (R2 55) |
| C30 Di Eugenio example | delete | do not — the strongest number | **Reversed**: kept Di Eugenio's one sentence, cut Feinstein and Cicchetti's three-sentence example instead |
| C31 "one problem not two" | delete | delete | v19 |
| C32 S5 opener | trim | trim | Trimmed further; contribution-claim sentence removed |
| Six links | keep all | keep all | **Retold once in two paragraphs**; Figure 1 carries the numbering |
| C33 five directions → three | cut D3, D4 | fold D4 into D2, keep D3 | Verified version kept (four directions); each trimmed; link scaffolding removed |
| C34 Conclusion | replace | replace, fix two phrases | v19; final sentence split |
| A1–A3, A5 | — | new | v19 |
| A4 closing hedge | — | optional | **Cut** |

Cuts neither list found, which did most of the work: the Section 5 re-narration (item 7 in Section 2 above); the meta-commentary sentences (item 8); the inverted closing sentences (item 9); the definitional asides (item 3); the duplicated citations at the top of Section 3; and the second Mohd Shamsuddin quotation in Section 5.

---

## 6. Alignment with Dr. Ho

- **Section 1**: unchanged except the roadmap, so everything he approved is still there, including all 24 of his supplied wordings.
- **His Section 2 comments (R2 55–64)** are all still honoured: the bridge sentence, the named preview, the citation on the monolingual-annotation claim (Pontiki; Nazir), the spoken-data caveat with its reasoning, no "structural cue" overclaim.
- **His v17 comment on density**: one idea per sentence throughout; every *so*/*and* sentence that joined a premise to a conclusion was split.
- **Rules 2, 6, 16, 19**: checker-clean (Section 1 of this note). Hedges kept: *may*, *can*, *is described as*, *suggests*, *cannot be expected to*. One term per concept: "four Malay-English sentiment resources", "sources of neutral-label skew".
- **Rule 5 (define terms)**: satisfied by removal rather than definition — there is no term in Sections 2–6 that a reader of Section 1 has not met.
- **Rule 17**: no sentence in Sections 2–6 tells the reader what the paper is doing, apart from the one-sentence section bridges he asked for.
- **Things he will see for the first time and might remark on**: 3.4 is gone (he never saw it); three subsection headings are shorter; 3.3 is renamed; Section 5 now has 5.1 and 5.2; the paper is about four pages shorter. None of these touches anything he has commented on.
- **Reference count**: still 38. He said he would tell you which references to add after this revision, so nothing was padded.

## 7. Before it goes to him

1. Open in Word and note the page count (LibreOffice says 16).
2. The title block is still template placeholder text (Author(s) Name(s), Affiliation, xyz@utm.my, and the footer). Same as every version since v2.
3. Read Section 5.1 once yourself. It is the paragraph pair that replaces 750 words, so it is where a reader's understanding of the argument now rests. If any sentence there needs a second read, tell me which.
4. Run your own `check_section.py` over the file (the run above used your script, unmodified).

---

## Appendix — v20 text of Sections 2–6

Reproduced from the v20 file so the prose can be read here without opening Word. Tables are omitted (unchanged from v19).

### 2. Why Malaysian Code-Mixed Text Is Difficult to Annotate

Section 1 identified the sentiment labels, rather than the model, as the greater constraint on sentiment analysis of Malaysian Malay-English text. Three properties of the text explain why those labels are difficult to produce. First, switching between Malay and English occurs inside the sentence. Second, the affect of a message, meaning the attitude it conveys, can be carried by Malay particles that no standard sentiment lexicon lists. Third, phonetic spelling gives a single word many written forms. All three properties are described in the sociolinguistic literature on Malay-English contact (Muysken, 2013; Treffers-Daller et al., 2022; AlAfnan et al., 2025). Each is presented below with its consequence for the annotator, who may be a person or an automatic labelling method.

#### 2.1 Switching occurs within the sentence

Treffers-Daller et al. (2022) analysed 1,044 switched utterances from the classroom speech of two Malaysian teachers of English. In their data, the majority of the switches occurred within the clause rather than between clauses. Within-clause switches took two main forms: a Malay word or phrase inserted into an English stretch, or words from both languages combined in a single shared word order. The authors attribute this pattern to the structure of the two languages rather than to the style of the speakers. English and Malay both place the subject before the verb and the verb before the object, and Malay words change little in form to mark features such as tense. A speaker can therefore move from one language to the other in the middle of a clause with little grammatical adjustment (Treffers-Daller et al., 2022; Muysken, 2013).

These proportions were measured on spoken classroom data and should not be taken as the proportions in social media text. The explanation given by the authors, however, concerns the structure of the two languages and not the medium in which they are used. The same type of switching can therefore be expected in writing. Mohd Shamsuddin et al. (2024) give a written example in the post "Does institut kanser offer free medication cheap chemotherapy", where the Malay noun phrase institut kanser is placed inside an English question.

The consequence for annotation is that the boundary between the two languages does not show where the sentiment in a message is located. In monolingual annotation, locating the words that express an opinion is a separate step from judging their polarity. Aspect-based sentiment analysis is one example, in which a sentiment label is assigned to each entity mentioned in a text rather than to the text as a whole (Nazir et al., 2022). The annotator first marks the words that express the opinion and then assigns a polarity to them (Pontiki et al., 2016). In Malay-English mixed text, deciding which words to judge already requires interpretation. Two annotators may therefore assign different labels because they are judging different parts of the message, not because they judge the sentiment differently.

#### 2.2 Affect is carried by particles that belong to neither language

A second difficulty arises once the opinion has been located. The word that carries the affect may be a Malay particle attached to a clause that is otherwise entirely English, a construction Muysken (2013) terms back-flagging. In the data of Treffers-Daller et al. (2022), back-flagging accounts for 11.6% of the switched utterances, and the particle involved most frequently is lah. The same study reports that lah can attach to a clause that is entirely English, entirely Malay or mixed. Two examples it reproduces from earlier descriptive work are "Buy this lah" and "you understand lah kan".

These particles change the tone of a sentence rather than its factual content. AlAfnan et al. (2025) classify particles as a lexical feature that distinguishes Manglish from standard English and standard Malay. In their account, particles add emphasis, signal politeness or informality, and soften instructions. Their example is "Don't disturb la, he's busy", in which the particle makes the instruction less direct. Treffers-Daller et al. (2022) report the same effect for lah, which can shift an utterance from a highly assertive tone to a polite request or a friendly encouragement. In both accounts, the particle leaves what the sentence states unchanged and alters only the attitude it conveys. That attitude is what a sentiment label is meant to record.

Neither source measures how frequently these particles occur in Malaysian social media writing. Treffers-Daller et al. (2022) analyse recorded classroom teaching, and AlAfnan et al. (2025) analyse scripted television dialogue. Both establish that the construction recurs and that it carries affect.

The consequence for annotation is that the particle shows the tone of a message but does not determine its polarity. "Don't disturb la, he's busy" can be read as irritation, which is negative, or as politeness, which is neutral. Treffers-Daller et al. (2022) note the same difficulty for discourse markers in general, whose specific meanings are often difficult to capture even where their pragmatic functions can be evaluated. Two annotators may read the same particle differently, and both may be reading it competently.

Disagreement that arises from more than one justifiable reading is not removed by adding annotators. Pavlick and Kwiatkowski (2019) find that where an item can be read in more than one justifiable way, the disagreement is reproducible. Further annotators divide in the same way rather than converging on one label. A corpus built by majority vote over such items records the majority reading as though it were the only justifiable one. An agreement coefficient computed over such items therefore reflects genuine differences in interpretation rather than annotator error alone.

#### 2.3 Phonetic spelling gives a single word many written forms

The third property concerns whether the words that carry the sentiment can be recognised at all. Maskat and Rahman (2020) document Malay social media users spelling words as they are pronounced rather than as a dictionary lists them. A single word therefore appears in many written forms. From a corpus of 6,241 Twitter posts, they sort this variation into five categories: spelling variants, Malay-English mixed sentences, loan words spelled according to Malay pronunciation, slang-based spellings, and vowel-less words. Among the spelling variants, macam mana appears as mcmana, camne, camner, mcmner and cane. In the vowel-less category, a word is reduced to its consonants or to a single character, so that jangan is written jgn and pada is written pd.

Whether this variation can be reversed automatically was tested by Maskat and Rahman (2020) for two of the five categories, spelling variants and vowel-less words. They used two measures of how closely two spellings resemble one another, n-gram similarity and Levenshtein distance, to map each non-standard form to its standard spelling. The benchmark was a set of 1,176 word pairs identified by hand by a native Malay speaker. The highest precision reported for any configuration was 0.43, meaning that fewer than half of the matches proposed were correct. The authors conclude that similarity matching can detect the two categories but that a more sophisticated technique is needed, and they leave the remaining three categories to future research.

One limit on this evidence matters for this review. English words were removed before the experiment and code-mixed posts were excluded from the evaluation subsets. The reported precision was therefore measured on Malay text with the English taken out, not on Malay-English mixed text. No equivalent measurement for mixed text was found among the studies reviewed here.

The consequence for annotation is that human and automatic annotators differ in what they can recognise. In the study just described, a single native speaker identified the 1,176 word pairs reliably enough for them to serve as the ground truth. Automatic matching on the same ground truth reached a precision of 0.43. A human reader recognises x as tidak; the automatic procedure largely did not. The two types of annotator therefore make errors on different inputs, and the choice of annotator determines not only cost and speed but which errors a corpus will contain.

### 3. Annotation Practice and Its Failure Modes

Section 2 described what makes Malaysian code-mixed text difficult to label. This section examines what has been done about it. The annotation strategies reported in the reviewed studies are set out first, with the trade-off each one accepts. The skew towards the neutral label that those strategies produce is examined next. The section closes with the practice of pooling several annotators, on which the largest Malaysian corpus provides direct evidence.

#### 3.1 Annotation strategies and the fidelity-scalability trade-off

For low-resource code-mixed text, label fidelity and scale are in tension: a corpus can be labelled carefully or it can be labelled in volume. The strategies reported in the reviewed studies differ in which of the two they sacrifice, and they fall into the three tiers summarised in Table 1.

The first tier is manual annotation. Two of the four Malay-English sentiment resources were built this way, and they are the only two whose labels come from human judgement. Kasmuri and Basiron (2019) retained 2,316 sentences from 5,849 drawn from personal blogs, and report κ = 0.83 for the judgement of whether a sentence was opinionated or factual. Kong et al. (2023) annotated 11,568 of the 108,246 tweets they collected into three sentiment classes, using three independent annotators and a written guideline. Both resources illustrate the cost of choosing fidelity rather than a defect in the method. The labour that produces reliable labels is also what limits how far a manually annotated corpus can grow.

The second tier is semi-automated annotation, which makes the opposite choice: existing tools label at volume, and the limitations of those tools are accepted as the price. Mohd Shamsuddin et al. (2024) built MESocSentiment this way. They collected 229,566 tweets carrying the "#Malaysia" keyword, and after pre-processing and automatic language identification 20,226 code-switched posts remained. Sentiment labels were then assigned by majority vote among three existing sentiment analysers. The authors state that the language identification libraries "reduced the need to find fluent speakers in Malay and English to classify the tweets". The reasoning is justifiable, and on other labelling tasks automated annotators have matched or exceeded human crowd workers (Gilardi et al., 2023). What the tier concedes is that the labels can be no more competent than the tools that produce them.

The third tier replaces those tools with generative language models used directly as annotators. A generative model is not restricted to a fixed vocabulary. It can therefore, in principle, interpret an unfamiliar spelling or slang term from its context, which is the capability the second tier lacks. The peer-reviewed evidence does not yet support that promise. Jadhav et al. (2025) evaluated GPT-4o and Llama 3.1 405B as annotators for Marathi, a low-resource Indian language, across four classification tasks including sentiment analysis. Both scored below a smaller pre-trained model, BERT (Devlin et al., 2019), that had been fine-tuned on each task, by average accuracy margins of 10.2% and 14.1%. The authors conclude that fine-tuned models remain necessary where linguistic resources are scarce. No study examined here evaluates generative annotation on Malaysian code-mixed text, so this tier is the least evidenced of the three.

*Table 1. Annotation Strategies for Malaysian Malay-English Code-Mixed Sentiment Data*

#### 3.2 Two sources of neutral-label skew

The clearest evidence of what the second tier costs is the class distribution of the corpus it produced. MESocSentiment is labelled 78.23% neutral, 16.33% positive and 5.44% negative across 19,714 posts (Mohd Shamsuddin et al., 2024). Two reasons support interpreting that distribution as an artefact of the labelling method rather than as a property of Malaysian discourse. The first is that the corpus was collected under the "#Malaysia" keyword across sports, politics and the arts, topics that would be expected to attract opinion rather than neutral comment. The second is that a comparable corpus of Malaysian tweets labelled by human annotators is only 23.6% neutral (Kong et al., 2023). Two sources contribute to the skew.

The first source is a scoring function that finds nothing to score. Lexicon-based sentiment tools match each word or phrase in a text against a sentiment lexicon and add the scores of the matched words into an overall score (Selvaraju et al., 2024). That score is then divided into classes by threshold. VADER, one of the three analysers used to build MESocSentiment, returns neutral for any score between −0.05 and +0.05 on a scale from −1 to 1 (Hutto and Gilbert, 2014). It follows that a text whose affect-bearing words are absent from the lexicon contributes little or nothing to the score and is returned as neutral. Under this view, neutral is not always a judgement that a text is affectively balanced. It can also be the default output when nothing was recognised.

The corpus authors' own error analysis indicates that this default output occurs in their data. Mohd Shamsuddin et al. (2024) present six examples comparing the ensemble's label with the correct label. All three misclassified examples are neutral labels that should have been positive, and in all three the sentiment is carried by Malay: memang cantik sangat, selamat deepavali and raih gelar juara. In the correctly classified negative example, the sentiment is carried by an English word, worthless. Six author-selected examples give no error rate, but their pattern is consistent. Where the ensemble succeeded, the affect was in a language its tools covered; where it failed, the affect was not.

The second source is genuine uncertainty among annotators, and it has nothing to do with the tools. Kasmuri and Basiron (2019) note that low agreement in sentiment annotation arises because sentiment is subjective, so judgements differ from one annotator to another and are shaped by each annotator's background. Kong et al. (2023) make the same point about their own task and give it as the reason a clear guideline is needed. As Section 2.2 showed, disagreement that arises from subjectivity is not removed by collecting more judgements.

Separating the two sources matters because they produce the same label and require opposite responses. A genuinely neutral post belongs in the corpus, whereas a falsely neutral post is an error that a better-resourced annotator would not have made. A pipeline built from tools that do not recognise the affect has no way to tell the two apart. A false neutral also does more than inflate one class. Every strongly polarised post assigned to the neutral class is a training example removed from a minority class. At a 5.44% negative share, the smallest class is the one that this depletion reduces further.

#### 3.3 Two weaknesses of majority voting

Pooling several annotators is a commonly proposed response when a single annotator is unreliable (Artstein and Poesio, 2008; Uma et al., 2021). The construction of MESocSentiment provides a direct test of that response: three sentiment analysers labelled every post and the majority label was assigned. The corpus skewed towards the neutral label anyway. Voting cancels error only to the extent that the voters make different errors, and the corpus authors' own reporting, summarised in Table 2, shows why that condition was not met.

*Table 2. The Three Annotators Used to Build MESocSentiment, and the Labels Each Assigned (Mohd Shamsuddin et al., 2024)*

Two observations follow from Table 2. First, every analyser skewed neutral before any vote was taken, so the voting rule did not produce the skew. Second, the analyser that skewed hardest, pysentimiento at 85.8%, is the only one of the three built on a pre-trained transformer model (Devlin et al., 2019). Greater model capacity therefore did not help. None of the three analysers is described by the corpus authors as covering Malay, and one is explicitly described as trained on four other languages. What the three voters share is the language they do not cover. A Malay affect-bearing word that one analyser does not recognise is therefore unlikely to be recognised by the others, and the vote confirms the error instead of cancelling it. This shared language gap is the first weakness of the pipeline.

The second weakness concerns the posts on which the three analysers could not agree. Where all three returned different labels there was no majority, and the authors removed those posts "to ensure the corpus only contains tweets from absolute categories". This affected 512 posts, or 2.53% of the 20,226 labelled. The difficulty is not the proportion but the composition. A post on which three analysers disagree is one where the sentiment is contested or is carried by words that none of them recognises confidently. That description fits the heavily code-switched and particle-laden posts that Section 2 identified as the hardest to annotate. The rule therefore removes the examples that a robust classifier particularly needs, and it removes them systematically rather than at random.

The effect on the corpus can be computed from the paper's own tables. Removing the contested posts left the neutral count unchanged at 15,422 while reducing the total from 20,226 to 19,714, so the neutral share rose by about two percentage points. Uma et al. (2021) question the assumption that a single correct interpretation exists for every item. Under that view, the 512 discarded posts were signal removed from the corpus rather than noise. No study examined here measures whether annotators of different types fail independently on Malaysian code-mixed text, which is the premise on which majority voting rests. The evidence above suggests that they do not fail independently when they share a language gap, and Section 5 returns to this point as a direction for future research.

### 4. Evaluating Annotation Reliability

Section 3 concerned how labels are produced. This section concerns how the reliability of those labels is evaluated. Reliability is normally assessed with a chance-corrected agreement coefficient, such as Cohen's κ (Cohen, 1960; Artstein and Poesio, 2008). The coefficient measures how far the agreement two annotators reach exceeds the agreement expected by chance. In computational linguistics, values above 0.8 are generally treated as good reliability, and values between 0.67 and 0.8 as allowing tentative conclusions (Artstein and Poesio, 2008).

Those conventions assume that expected chance agreement is stable across datasets, and it is not. When one category dominates the label distribution, the agreement expected by chance rises, and the same observed agreement yields a lower coefficient (Feinstein and Cicchetti, 1990; Byrt et al., 1993). Di Eugenio and Glass (2004) call this the prevalence problem. They report a case in which two coders agreeing on 90 of 100 items obtain κ values ranging from −0.048 to 0.80, depending only on how the two categories are distributed. Artstein and Poesio (2008) state the consequence for annotation directly: when one category is very common, high agreement can result from indiscriminate coding rather than from an ability to distinguish between categories.

That is the condition Malaysian code-mixed sentiment data is in. The labelling methods described in Section 3 produce heavily skewed class distributions, with the largest corpus at 78.23% neutral. The same skew that makes the labels unrepresentative also makes the coefficient used to check them difficult to interpret, because it raises the chance agreement on which the correction depends. The difficulty runs in both directions. A low coefficient may indicate unreliable annotation, or it may indicate a dominant class. A high coefficient may indicate reliable annotation, or it may indicate indiscriminate coding. Neither interpretation can be ruled out from the coefficient alone.

Table 3 sets out what the studies introducing the four Malay-English sentiment resources report about the reliability of their annotation.

*Table 3. Reliability Evidence Reported by the Four Malay-English Sentiment Corpora*

Three observations follow. First, two of the four studies report no agreement coefficient at all, including one whose corpus was annotated by three people working from a written guideline. Second, the two coefficients that are reported were obtained for binary judgements, and neither concerns the three-class polarity task for which the resources are used. Third, Romadhona et al. (2022) report a kappa value without stating which coefficient it is. Their annotation used five experts with the final label set by majority vote, whereas Cohen's κ is defined for two annotators.

None of the four studies therefore supplies what a reliability claim requires: a coefficient of a stated type, computed for the task the labels are used for, over annotators whose number and qualification are recorded. A study that did supply them would still face the interpretation problem described above, because the class distributions these labelling methods produce are the ones that make the coefficient difficult to interpret. Reliability for this data is therefore not only unreported. With the instruments currently in use, it is not clearly achievable.

### 5. Synthesis: How the Challenges Compound

Sections 2 to 4 examined linguistic structure, annotation practice and reliability evaluation as three separate difficulties. Read together, they form one sequence in which each difficulty creates the conditions for the next, and the sequence returns to its own starting point. Figure 1 sets out that sequence, and the directions for future research in Section 5.2 follow from it.

#### 5.1 The compounding chain

*Figure 1. The Compounding Chain in Malaysian Code-Mixed Sentiment Annotation*

The chain begins with the text. Because the particles that carry sentiment in Malaysian code-mixed writing can be read in more than one justifiable way, annotators may disagree systematically rather than randomly. Adding annotators reduces random disagreement, because independent errors average out. It does not reduce systematic disagreement, because each new annotator brings a stable reading of their own (Pavlick and Kwiatkowski, 2019). Competent annotation therefore requires fluent bilingual readers, and their cost and scarcity is the reason Mohd Shamsuddin et al. (2024) give for automating. The tools used for automation were designed for other languages and do not recognise Malay spellings or particles. In MESocSentiment, none of the three analysers is described as covering Malay, so pooling them confirmed a shared error instead of cancelling it. False neutrals accumulated, and the corpus acquired a class distribution that no participant intended.

That skew then undermines the check that would reveal it. A distribution skewed in that way is the condition under which a chance-corrected coefficient becomes difficult to interpret (Feinstein and Cicchetti, 1990; Byrt et al., 1993). A researcher who suspects the labels are unsound and computes a coefficient therefore cannot distinguish poor annotation from competent annotation of a skewed corpus. The defect and the inability to detect it have the same cause, so the quality check is least informative where quality is lowest. Corpora whose reliability was never established are then released, trained on and evaluated against. Manukonda and Kodali (2025) show a fine-tuned model handling the spelling variants it was shown in training. By the same reasoning, such a model cannot be expected to resolve variants it was not shown. An annotator fine-tuned on one generation of labels therefore carries their limitations into the next. That is the arrow in Figure 1 that returns to automation.

Read as a whole, the chain explains a pattern that the individual studies cannot. Each reviewed study intervenes at one point in the chain and does so competently, but none addresses the chain as a whole. An intervention at any one point is assessed with an agreement statistic compromised at another, so the assessment cannot show whether the intervention worked. That is why competent work at each point has not accumulated into progress.

#### 5.2 Directions for future research

The chain shows where intervention would matter, not which intervention would succeed. Four directions follow from it.

The first is agreement measurement under class skew. Prevalence-adjusted coefficients exist (Byrt et al., 1993), but no study examined here evaluates them on code-mixed sentiment data. It is therefore not known which behaves best under the distributions these corpora exhibit. The study requires no new data collection, only an existing annotated corpus, a set of candidate coefficients, and a comparison of how they behave as skew increases. It is a precondition for the other three directions.

The second is a minimum reporting standard, which follows from Table 3. Any newly released corpus should report six elements: (1) the number of annotators and their qualification; (2) the availability of the annotation guideline; (3) the variant of the coefficient and the task it was computed for; (4) per-class as well as aggregate agreement; (5) the full class distribution; and (6) the distribution of annotator judgements for each item, together with any items discarded. Per-class agreement matters because an aggregate figure on a skewed corpus is dominated by the majority class and can conceal near-total disagreement on the minority polarities. The sixth element preserves the contested cases that current pipelines delete. Uma et al. (2021) report that models trained on the full distribution of annotator judgements can outperform models trained on aggregated labels. A corpus that reports what it discarded also lets a reader judge whether its reliability was earned or obtained by removing the contested items.

The third is a shared annotation convention for affect-bearing particles such as lah and kan. Because the disagreement these particles generate is systematic, the remedy is a shared convention rather than additional annotators, and none was found among the studies reviewed here. Mohammad (2016) proposes a questionnaire that separates the speaker's emotional state, the target of the opinion and the attitude taken toward it. The questionnaire also treats sarcasm and mockery as a distinct response rather than folding them into polarity, which is the ambiguity Section 2.2 identified. Kong et al. (2023) adapt this scheme into a four-question guideline for Malaysian tweets. What is missing is its adaptation to Malaysian particles and its adoption across projects.

The fourth is to test the independence premise. Every consensus mechanism in the reviewed studies assumes that annotators of different types fail independently, and on Malaysian code-mixed text that assumption has been asserted but not measured. The study is direct: label a common sample with annotators of deliberately different competence, and measure the correlation of their errors rather than their individual accuracies. Low correlation would justify the aggregation strategies already in use. High correlation would show that consensus on this text adds confidence without adding evidence.

### 6. Conclusion

This review examined why reliable annotation and evaluation of Malaysian Malay-English code-mixed sentiment data have not yet been established. One common explanation concerns the model architecture, and the evidence assembled here indicates that it is incomplete. Model choice accounts for part of the difficulty, and the rest arises earlier, in the sentiment labels themselves and in the evidence offered that those labels are sound. The contribution of this review is the relation between these findings, set out in Figure 1 as a chain in which each difficulty creates the conditions for the next. An intervention at any one point in that chain is assessed by an agreement statistic compromised at another. Until reliability can be measured under the class distributions these corpora produce, no new corpus can be shown to improve on the ones examined here.
