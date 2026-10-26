# ICON AI — v18 → v19 change log

**Built:** 10 September 2026, from `Template ICON AI 2026 Section 1 to 7 v18.docx` (8 Sept). v18 is untouched and remains the backup.
**Output:** `Template ICON AI 2026 - Section 1 to 7 (v19).docx` and a LibreOffice PDF preview.
**Basis:** `ICON AI Cut List v18 - Verified.md` — every KEEP and MODIFY item, the five additional cuts A1–A3 and A5, the fixes list, and the readability pass on Sections 3–6 in one pass per section. Nothing marked DO NOT CUT was touched. Section 1 was changed in exactly two places, both forced by the Section 4 fold: the roadmap (C9) and the Abstract's agenda clause (your choice).

## Numbers

| | v18 | v19 |
|---|---|---|
| Words, whole file (python count; Word shows ~100 fewer) | 10,656 | 9,876 |
| Body words, Sections 1–6 excluding references | 9,141 | 8,263 |
| LibreOffice page count | 21 | **20, with 6 lines of references on page 20** (≈19.1 pages) |
| Sentences over 35 words in Sections 2–6 | 15 | **0** |
| Same source cited in consecutive sentences | — | **0** |
| References | 38 | 38 (none orphaned; Devlin et al. 2019 now also cited in 3.1, 3.3 and 3.4) |

Section word counts: S1 1,931 → 1,925 · S2 2,068 → 1,763 · S3 1,981 → 2,215 (including the new 3.4 at 228) · S4 (old) 564 → folded · Evaluating reliability 630 → 626 · Synthesis 1,389 → 1,367 · Conclusion 269 → 143.

The readability pass added only about 150 words to Sections 3–6, not the 420–500 the budget allowed for, because splitting and cutting framing were done together.

**On the page count.** LibreOffice and Word have differed by 0–1 page on every version so far (v13/v14: LO 21, Word 20; v18: both 21). v19 is 19 full pages plus six lines of references in LibreOffice, so Word will show either 19 or 20. **Open it in Word and check.** If Word shows 20, apply the first retreat item below (one paragraph, 32 words) and it will almost certainly drop to 19; the second is ready if not. Neither removes a citation.

## What to check in Word before it goes to Dr. Ho

1. **Page count** (see above).
2. **Tables.** All three are now 10pt, left-aligned inside cells (they were justified, which produced large gaps in the narrow columns), with the header row set to repeat if a table breaks across a page, rows set not to split, and each caption kept with its table. In LibreOffice this leaves a short gap at the foot of page 9 before Table 1; Word will place it differently. If a table lands badly, the caption and header-row "keep with next" settings are the ones to loosen.
3. **Headings** now have "keep with next", so no heading can sit alone at the foot of a page (the new 3.4 heading did, before this was set).
4. **Figure 1** — the box label now reads "Shared Limitation" (was "Share Limitation"). The figure was patched in place with a metric-compatible serif; if you have the original drawing, re-export from there for a perfect match. Size unchanged (14.0 × 5.8 cm).
5. **The title block is still template placeholder text** (Author(s) Name(s), Affiliation, xyz@utm.my, and the footer). Not touched — it needs your details.
6. **Section 1 and the Abstract** are byte-identical to v18 except the roadmap paragraph and the eight-word Abstract clause.

## Retreat items, ready to apply (only if Word shows 20 pages)

1. **A4 — delete the last paragraph of Section 5 (Synthesis), 32 words:** *"These are directions rather than results. The claim of this review is not that they will succeed, but that Figure 1 identifies where effort in this area is currently absorbed without accumulating."* — the paragraph before the directions already makes the "absorbed without accumulating" point.
2. **C30 — in Section 4, second paragraph, 31 words:** replace *"Di Eugenio and Glass (2004) name the effect the prevalence problem. They report a case in which two coders agreeing on 90 of 100 items yield κ values ranging from −0.048 to 0.80, depending only on how the two categories are distributed."* with *"Di Eugenio and Glass (2004) name the effect the prevalence problem."*

Do not go further than these two without deciding deliberately: the next items are C2 (Section 1) and dropping Direction 3 (which orphans Mohammad 2016).

## What was applied, by section

**Section 1 / Abstract.** Roadmap rewritten for six sections (C9). Abstract's closing sentence now lists four agenda items, matching Section 5.

**Section 2 (2,068 → 1,763).** Deletions only, in v18's sentence shape: C10 (opener trimmed, bridge and three-property preview kept), C11 (unused SVO abbreviation removed and the ungrammatical clause fixed), stray comma in 2.1, C13 tail (two restating sentences), C15 (the "distinguish" sentence merged, not deleted), C16 (caveat rewritten in four sentences, longest 30 words), C17, C18 (mini-summary deleted), C20 (two trims, citation moved onto the 0.43 figure), C22 (merged with the preceding sentence), C23 (closing summary deleted). C14 was **not** applied: the citation on "The particle involved most frequently is lah" is there because `check_section.py` reads "most" as a claim word, as the v18 note records.

**Section 3 (1,981 → 2,215 incl. 3.4).** C24 (opener keeps its bridge and now previews 3.4), C25, C26, C27, A1, A2, A3 (and "causes" → "sources" throughout 3.2), plus the readability pass on every paragraph. Two substantive corrections made while rewriting: (a) 3.1 no longer says the manual tier "prevents either corpus from reaching the scale a general-purpose resource would require" — Kong et al.'s 11,568 meets the ten-thousand threshold Section 1 defines, so the sentence now says the labour is what limits how far a manually annotated corpus can grow; (b) 3.3's "a Malay affective token invisible to one is invisible to all" is now hedged ("is therefore unlikely to be recognised by the others"), matching the caveat at the end of 3.3 that this is a suggestion, not a measurement. 3.3 now names its two weaknesses on one spine (R4 37). **New 3.4** replaces Section 4 with the corollary stated as the review's own inference, the encoder defined and cited, Adilazuarda's direction-of-result kept, and "carry the signature" replaced by "reflect".

**Section 4, Evaluating Annotation Reliability (630 → 626).** Bridge kept and renumbered (C29 edit). The sentence he corrected twice in Section 1 is now corrected here too: "assessed" not "demonstrated", "such as Cohen's κ" not "the most widely used" (R4 46, 47). C31 deleted. "actually" removed. "None of the four corpora … supplies" → "None of the studies introducing the four corpora" (R4 59). Marginal totals defined. κ italicised as in Section 1.

**Section 5, Synthesis (1,389 → 1,367).** C32 (opener; the uncited "which is how the studies reviewed here are organised" is gone; "reliability evaluation" per R4 60). All six links kept and rewritten: "stops returning interpretable values" → "makes a chance-corrected coefficient more difficult to interpret" (R4 48); "this material" named; "The corpus papers give…" → Mohd Shamsuddin et al. as the subject; "raised … the measured agreement" → "and, by construction, the agreement among the three analysers" (MESocSentiment reports no coefficient); "edge" → "arrow in Figure 1"; "Section 4 showed" → "Section 3.4 showed"; "The usual response" → "Pooling annotators, the response examined in Section 3.3". Directions: four, not five — D4 folded into D2 as element (6) with the Uma et al. finding kept; D3 kept with "A model is available" and "precisely" removed; D5 renumbered fourth; A5 applied to D1.

**Section 6, Conclusion (269 → 143).** C34 with the two flagged phrases corrected ("have not yet been established", R4 51; "One common explanation concerns the model architecture", R3 19 / R4 26), Figure 1 named, longest sentence 32 words. Heading size corrected to 13pt like the other first-order headings.

## Checker output on v19

Passes replicate the master tracker's checklist (sentence length, same-source repeats, claim words without a citation, previously flagged wording, bold and parenthetical cross-references, evaluative adjectives for a human read, cross-reference validity, citation–reference integrity, term consistency). The remaining hits under pass 3 and pass 4 are false positives ("soften/softener" contains "often"; "in particular" contains "in part"; "evidence against that response" is not the flagged "Against that,"). Run your own `check_section.py` over the file as well before sending.

```
== 1. Sentences over 35 words (Sections 2-6) ==
  total: 0
== 2. Same source cited in consecutive sentences (Sections 2-6) ==
  total: 0
== 3. Claim words without a citation on the sentence (Sections 2-6) ==
  P33 ['often']: According to the same study, one function of these particles is to soften an instruction.…
  P35 ['often']: A reader of "Don't disturb la, he's busy" can see that the particle softens the instruction.…
  P35 ['often']: A softened instruction can still be read in two ways.…
  P85 ['often']: Where one annotator reads lah as a softener and another reads it as a marker of sarcasm, and each reading is stable, the…
  total: 4
== 4. Previously flagged informal / figurative wording (whole body) ==
  P13 "in part": …malaysian malay-english code-mixed sentiment data in particular, the question is whether the model or the s…
  P36 "this kind": …disagreement of this kind is not necessarily reduced by adding annotators.…
  P61 "against that": …08; uma et al., 2021). mesocsentiment is evidence against that response, because it was already built as a conse…
  total: 3
== 5. Bold in body / parenthetical cross-references ==
  P4 bold: Keywords: sentiment analysis, code-mixed text, Manglish, ann
  total: 1
== 6. Evaluative adjectives to read by eye (Sections 2-6) ==
  P43 ['large']
  P51 ['large']
  P56 ['small']
  P57 ['low']
  P59 ['strong']
  P65 ['heavily']
  P70 ['limited']
  P74 ['high', 'low']
  P75 ['large', 'high', 'low', 'heavily']
  P88 ['heavily', 'extreme']
  P89 ['low', 'extreme']
  P96 ['high', 'low']
== 7. Cross-references ==
  headings: ['1', '2', '2.1', '2.2', '2.3', '3', '3.1', '3.2', '3.3', '3.4', '4', '5', '6']
  dangling section refs: none
  tables referenced: ['2', '3'] | figures referenced: ['1'] | tables in file: 3
== 8. Citations vs reference list ==
  references: 38
  cited but not in list: [('Bakar', '2020'), ('Eugenio', '2004'), ('Pustaka', '2005'), ('Shamsuddin', '2024')]
  in list but never cited: [('Abu', '2020'), ('Dewan', '2005'), ('Di', '2004'), ('Mohd', '2024')]
== 9. Term consistency ==
  'causes of': 0
  'two causes': 0
  'first cause': 0
  'second cause': 0
  'regional corpora': 0
  'regional resources': 0
  'reliability measurement': 0
  'sources of neutral': 2
  'Malay-English sentiment resources': 5
== 10. Section word counts ==
    224  Abstract
   1925  1. Introduction
    150  2. Why Malaysian Code-Mixed Text Is Difficult to Annotate
    455  2.1 Switching occurs within the sentence and offers little reliable structural cue
    588  2.2 Affective meaning is carried by particles that belong to neither standard language
    570  2.3 Phonetic spelling multiplies the surface forms of a single word
    104  3. Annotation Practice and Its Failure Modes
    567  3.1 Annotation strategies and the fidelity-scalability trade-off
    678  3.2 Two sources of neutral-label skew
    638  3.3 What consensus does with disagreement
    228  3.4 Where each family of model is limited as an annotator
    626  4. Evaluating Annotation Reliability
   1367  5. Synthesis: How the Challenges Compound
    143  6. Conclusion
   1199  References
```

## Content integrity, v18 Sections 2–7 against v19 Sections 2–6

Every citation, every quoted string and every number in v18 Sections 2–7 is present in v19, with these intended exceptions: the Manukonda and Kodali macro-F1 of 0.90 and the XLM-RoBERTa / masked-language-modelling / Malayalam detail (dropped with the Section 4 fold, as the verified list proposed); the television series names Kopitiam and KL Gangster (C16); Direction 4's standalone text (its two substantive sentences moved into Direction 2); and the Conclusion's re-walk of the six links. Italic forms (lah, kan, x, tidak, institut kanser, the Maskat and Rahman spellings, the three Malay examples in 3.2, worthless, κ) are preserved.

---

## Appendix — every changed paragraph, old and new

Indices are v18 paragraph positions. "(deleted)" means the paragraph was removed without replacement.

### P3 Abstract (D3 clause)

**v18:** Malaysian social media users mix English and Malay inside single messages, producing the contact variety known locally as Manglish. The studies reviewed here usually treat sentiment analysis of Malay-English mixed writing as a modelling problem. This review indicates that the more limiting constraint is earlier in the process, in the quality of the sentiment labels and in the evidence offered that those labels are sound. The review covers annotation practice and reliability evaluation for Malaysian Malay-English code-mixed sentiment data. Comparative benchmarking of sentiment classifiers is outside its scope. Three contributions follow. First, the annotation strategies used for low-resource code-mixed text are organised into three tiers, and the trade-off between label fidelity and scalability is examined across them. Second, two sources of neutral-label skew are separated, one produced by the labelling tools and the other by genuine uncertainty among annotators. The four Malay-English sentiment resources are then examined against what a reliability claim requires, and none supplies it. Third, the class imbalance in the label distribution is shown to be the condition that makes Cohen's kappa more difficult to interpret. The review closes with a research agenda covering minimum reporting standards, agreement measurement under class imbalance, and the untested assumption that annotators of different types make different errors.

**v19:** Malaysian social media users mix English and Malay inside single messages, producing the contact variety known locally as Manglish. The studies reviewed here usually treat sentiment analysis of Malay-English mixed writing as a modelling problem. This review indicates that the more limiting constraint is earlier in the process, in the quality of the sentiment labels and in the evidence offered that those labels are sound. The review covers annotation practice and reliability evaluation for Malaysian Malay-English code-mixed sentiment data. Comparative benchmarking of sentiment classifiers is outside its scope. Three contributions follow. First, the annotation strategies used for low-resource code-mixed text are organised into three tiers, and the trade-off between label fidelity and scalability is examined across them. Second, two sources of neutral-label skew are separated, one produced by the labelling tools and the other by genuine uncertainty among annotators. The four Malay-English sentiment resources are then examined against what a reliability claim requires, and none supplies it. Third, the class imbalance in the label distribution is shown to be the condition that makes Cohen's kappa more difficult to interpret. The review closes with a research agenda covering minimum reporting standards, agreement measurement under class imbalance, a shared annotation convention for affect-bearing particles, and the untested assumption that annotators of different types make different errors.

### P21 C9 roadmap

**v18:** The rest of this paper is organised as follows. Section 2 explains why Malaysian code-mixed writing is difficult to annotate. Section 3 examines annotation practice and its failure modes, and Section 4 examines the models that are used as annotators. Section 5 discusses how annotation reliability is evaluated. Section 6 brings these findings together and sets out directions for future research, and Section 7 concludes the review.

**v19:** The rest of this paper is organised as follows. Section 2 explains why Malaysian code-mixed writing is difficult to annotate. Section 3 examines annotation practice, its failure modes and the models used as annotators. Section 4 discusses how annotation reliability is evaluated. Section 5 brings these findings together and sets out directions for future research, and Section 6 concludes the review.

### P24 C10

**v18:** Section 1 identified the sentiment labels as the greater constraint on sentiment analysis of Malaysian Malay-English text, rather than the model. Annotation practice is examined in Section 3. The text being annotated is described first, because three of its linguistic properties affect the annotation task directly. The first property is that switching between Malay and English occurs inside the sentence. The boundary between the two languages therefore does not show where the opinion in a message is located. The second property concerns the affect of a message, meaning the emotional attitude it expresses. That affect can be carried by Malay particles, and these particles appear in no standard sentiment lexicon. The third property is that phonetic spelling gives a single word many written forms. All three properties are described in the sociolinguistic literature on Malay-English contact (Muysken, 2013; Treffers-Daller et al., 2022; AlAfnan et al., 2025). Each property is presented below together with its consequence for the annotator. The annotator may be a human or an automatic labelling method.

**v19:** Section 1 identified the sentiment labels, rather than the model, as the greater constraint on sentiment analysis of Malaysian Malay-English text. Annotation practice is examined in Section 3. The text being annotated is described first, because three of its linguistic properties affect the annotation task directly. The first property is that switching between Malay and English occurs inside the sentence. The second property concerns the affect of a message, meaning the emotional attitude it expresses. That affect can be carried by Malay particles, and these particles appear in no standard sentiment lexicon. The third property is that phonetic spelling gives a single word many written forms. All three properties are described in the sociolinguistic literature on Malay-English contact (Muysken, 2013; Treffers-Daller et al., 2022; AlAfnan et al., 2025). Each property is presented below together with its consequence for the annotator, who may be a human or an automatic labelling method.

### P27 C11

**v18:** Treffers-Daller et al. (2022) analysed 1,044 switched utterances from the classroom speech of two Malaysian teachers of English. In their data, the majority of the switches occurred within the clause rather than between clauses. Insertion accounted for 33.0% of the switches. In insertion, a word or phrase from one language is placed inside a stretch of the other. Congruent lexicalisation accounted for a further 30.7%. In congruent lexicalisation, words from both languages are combined within a single shared word order. Alternation between whole clauses accounted for 24.8%. The authors attribute this distribution to the structure of the two languages rather than to the style of the speakers. English and Malay share the same basic word order. In both languages, the subject comes before the verb and the verb before the object known as Subject-Verb-Object (SVO). Malay also has very little inflectional morphology. Inflectional morphology refers to changes in the form of a word that mark grammatical features such as tense. A speaker can therefore move from one language to the other in the middle of a clause with little grammatical adjustment (Treffers-Daller et al., 2022; Muysken, 2013).

**v19:** Treffers-Daller et al. (2022) analysed 1,044 switched utterances from the classroom speech of two Malaysian teachers of English. In their data, the majority of the switches occurred within the clause rather than between clauses. Insertion accounted for 33.0% of the switches. In insertion, a word or phrase from one language is placed inside a stretch of the other. Congruent lexicalisation accounted for a further 30.7%. In congruent lexicalisation, words from both languages are combined within a single shared word order. Alternation between whole clauses accounted for 24.8%. The authors attribute this distribution to the structure of the two languages rather than to the style of the speakers. English and Malay share the same basic word order. In both languages, the subject comes before the verb and the verb before the object. Malay also has very little inflectional morphology. Inflectional morphology refers to changes in the form of a word that mark grammatical features such as tense. A speaker can therefore move from one language to the other in the middle of a clause with little grammatical adjustment (Treffers-Daller et al., 2022; Muysken, 2013).

### P28 stray comma

**v18:** These proportions were measured on spoken classroom data. They should therefore not be taken as the proportions in social media text. However, the explanation given by the authors, concerns the structure of the two languages and not the medium in which they are used. The same type of switching can therefore be expected in writing. Mohd Shamsuddin et al. (2024) give a written example in the post "Does institut kanser offer free medication cheap chemotherapy". Here the Malay noun phrase institut kanser is placed inside an English question. The phrase follows Malay word order, in which the noun comes before its modifier.

**v19:** These proportions were measured on spoken classroom data. They should therefore not be taken as the proportions in social media text. However, the explanation given by the authors concerns the structure of the two languages and not the medium in which they are used. The same type of switching can therefore be expected in writing. Mohd Shamsuddin et al. (2024) give a written example in the post "Does institut kanser offer free medication cheap chemotherapy". Here the Malay noun phrase institut kanser is placed inside an English question. The phrase follows Malay word order, in which the noun comes before its modifier.

### P29 C13 tail

**v18:** The consequence for annotation is that the annotator cannot use the boundary between the two languages to locate the part of the message that carries the sentiment. In monolingual annotation, locating that part is a separate step from judging its polarity. Aspect-based sentiment analysis is one task in which the two steps are separate. In that task, a sentiment label is assigned to each entity or attribute mentioned in a text rather than to the text as a whole (Nazir et al., 2022). In the annotation scheme described by Pontiki et al. (2016), the annotator first marks the words that express the opinion as a span. A span is a marked stretch of text. The annotator then assigns a polarity label to that span. In Malay-English mixed text, the annotator has no language boundary to guide the first step. Deciding which span to judge already requires interpretation. Two annotators may therefore assign different labels because they are judging different parts of the message, not because they judge the sentiment differently. Disagreement about which part of a message to judge is therefore separate from disagreement about its polarity. The first of these two disagreements also arises before the second.

**v19:** The consequence for annotation is that the annotator cannot use the boundary between the two languages to locate the part of the message that carries the sentiment. In monolingual annotation, locating that part is a separate step from judging its polarity. Aspect-based sentiment analysis is one task in which the two steps are separate. In that task, a sentiment label is assigned to each entity or attribute mentioned in a text rather than to the text as a whole (Nazir et al., 2022). In the annotation scheme described by Pontiki et al. (2016), the annotator first marks the words that express the opinion as a span. A span is a marked stretch of text. The annotator then assigns a polarity label to that span. In Malay-English mixed text, the annotator has no language boundary to guide the first step. Deciding which span to judge already requires interpretation. Two annotators may therefore assign different labels because they are judging different parts of the message, not because they judge the sentiment differently.

### P32 C14 not applied: citation kept for the checker (see log)

**v18:** Locating the part of the message that carries the opinion is the first difficulty. A second difficulty arises once that part has been located. The word that carries the affect may be a Malay particle. That particle may be attached to a clause that is otherwise entirely English. Muysken (2013) terms this construction back-flagging. Treffers-Daller et al. (2022) define back-flagging as the attachment of a discourse marker or a coordinating conjunction from a speaker's first language to a stretch of speech in the second language. In their data, back-flagging accounts for 121 of the 1,044 switched utterances, or 11.6%. The particle involved most frequently is lah (Treffers-Daller et al., 2022). The same study reports that lah can attach to a clause that is entirely English, entirely Malay or mixed. Two examples that the study reproduces from earlier descriptive work are "Buy this lah" and "you understand lah kan".

**v19:** Locating the part of the message that carries the opinion is the first difficulty. A second difficulty arises once that part has been located. The word that carries the affect may be a Malay particle. That particle may be attached to a clause that is otherwise entirely English. Muysken (2013) terms this construction back-flagging. Treffers-Daller et al. (2022) define back-flagging as the attachment of a discourse marker or a coordinating conjunction from a speaker's first language to a stretch of speech in the second language. In their data, back-flagging accounts for 121 of the 1,044 switched utterances, or 11.6%. The particle involved most frequently is lah (Treffers-Daller et al., 2022). The same study reports that lah can attach to a clause that is entirely English, entirely Malay or mixed. Two examples that the study reproduces from earlier descriptive work are "Buy this lah" and "you understand lah kan".

### P33 C15

**v18:** These particles contribute to the tone of a sentence rather than to its factual content. AlAfnan et al. (2025) classify particles as a lexical feature of Manglish. In their account, particles add emphasis or tone and signal politeness or informality. They also list particles among the features that distinguish Manglish from standard English and standard Malay. According to the same study, one function of these particles is to soften an instruction. The example given is "Don't disturb la, he's busy", in which the particle makes the instruction less direct. Treffers-Daller et al. (2022) describe the same effect for lah. They report that lah can shift an utterance from a highly assertive tone to a polite request or a friendly encouragement. In both accounts, the particle leaves what the sentence states unchanged. What the particle alters is the attitude the sentence conveys. That attitude is the property a sentiment label is intended to record.

**v19:** These particles contribute to the tone of a sentence rather than to its factual content. AlAfnan et al. (2025) classify particles as a lexical feature that distinguishes Manglish from standard English and standard Malay. In their account, particles add emphasis or tone and signal politeness or informality. According to the same study, one function of these particles is to soften an instruction. The example given is "Don't disturb la, he's busy", in which the particle makes the instruction less direct. Treffers-Daller et al. (2022) describe the same effect for lah. They report that lah can shift an utterance from a highly assertive tone to a polite request or a friendly encouragement. In both accounts, the particle leaves what the sentence states unchanged. What the particle alters is the attitude the sentence conveys. That attitude is the property a sentiment label is intended to record.

### P34 C16

**v18:** Two limits on this evidence should be noted. Treffers-Daller et al. (2022) supply frequencies. However, their corpus is fifteen hours of recorded classroom teaching by each of two university English lecturers. Their frequencies should therefore not be read as frequencies for social media writing. AlAfnan et al. (2025) describe Malaysian usage more broadly. However, their data are scripted dialogue from Malaysian television series such as Kopitiam and KL Gangster. Those data were examined through qualitative content analysis. That study therefore reports what the particles do, not how frequently they occur. Neither source establishes how frequently particles are used in Malaysian social media posts. What both sources do establish is that the construction recurs and that it carries affect.

**v19:** Neither source measures how frequently these particles occur in Malaysian social media writing. Treffers-Daller et al. (2022) report frequencies, but their corpus is fifteen hours of recorded classroom teaching by each of two university English lecturers. AlAfnan et al. (2025) describe Malaysian usage more broadly, but their data are scripted television dialogue examined through qualitative content analysis, which reports what the particles do rather than how frequently they occur. Both sources establish that the construction recurs and that it carries affect.

### P35 C17

**v18:** The consequence for annotation is that the particle indicates the tone of a message but does not determine its polarity. A reader of "Don't disturb la, he's busy" can see that the particle softens the instruction. A softened instruction can still be read in two ways. Under a negative reading, the writer is irritated. Under a neutral reading, the writer is being polite. Treffers-Daller et al. (2022) note the same difficulty for discourse markers as a whole, whose specific meanings are often difficult to capture even where their pragmatic functions can be evaluated. The particle therefore carries affect without showing which polarity that affect has. Two annotators may read the same particle differently, and both may be reading it competently.

**v19:** The consequence for annotation is that the particle indicates the tone of a message but does not determine its polarity. A reader of "Don't disturb la, he's busy" can see that the particle softens the instruction. A softened instruction can still be read in two ways. Under a negative reading, the writer is irritated. Under a neutral reading, the writer is being polite. Treffers-Daller et al. (2022) note the same difficulty for discourse markers as a whole, whose specific meanings are often difficult to capture even where their pragmatic functions can be evaluated. Two annotators may read the same particle differently, and both may be reading it competently.

### P37 C18 mini-summary

**v18:** The first property examined in this section produces disagreement about which part of a message to judge. The second property produces disagreement about how to judge that part once it has been located. That disagreement arises because more than one reading of the part is justifiable.

**v19:** (deleted)

### P42 C20

**v18:** The question that matters for annotation is whether this variation can be reversed automatically. Maskat and Rahman (2020) tested this question directly. They attempted to normalise two of the five categories, which are spelling variants and vowel-less words. To normalise a form means to map it automatically to its standard spelling. Two measures of string similarity were used, n-gram similarity and Levenshtein distance. Each measure scores how closely two spellings resemble one another. The benchmark was a set of 1,176 pairs of similar words covering 435 distinct words. A native Malay speaker identified these pairs by hand. Precision here is the proportion of the matches proposed by a method that were correct. On that benchmark, the highest precision reported for any configuration was 0.43. Most of the configurations reported were lower than that (Maskat and Rahman, 2020). The authors conclude that similarity matching can detect the two categories but that a more sophisticated technique is needed. They also state that normalisation of the remaining three categories is left for future research.

**v19:** The question that matters for annotation is whether this variation can be reversed automatically. Maskat and Rahman (2020) tested this directly by attempting to normalise two of the five categories, spelling variants and vowel-less words. To normalise a form means to map it automatically to its standard spelling. Two measures of string similarity were used, n-gram similarity and Levenshtein distance. Each measure scores how closely two spellings resemble one another. The benchmark was a set of 1,176 pairs of similar words covering 435 distinct words. A native Malay speaker identified these pairs by hand. Precision here is the proportion of the matches proposed by a method that were correct. On that benchmark, the highest precision reported for any configuration was 0.43 (Maskat and Rahman, 2020). The authors conclude that similarity matching can detect the two categories but that a more sophisticated technique is needed. They also state that normalisation of the remaining three categories is left for future research.

### P44 C22

**v18:** The consequence for annotation is that human and automatic annotators differ in what they can recognise. The difference can be seen in the study just described. A single native speaker identified 1,176 word pairs by hand. That identification was reliable enough for the result to serve as the ground truth. Automatic matching on the same ground truth reached a highest precision of 0.43. A human reader recognises x as tidak. The automatic procedure largely did not. The two types of annotator therefore make errors on different inputs and at different rates.

**v19:** The consequence for annotation is that human and automatic annotators differ in what they can recognise. The difference can be seen in the study just described. A single native speaker identified 1,176 word pairs by hand. That identification was reliable enough for the result to serve as the ground truth. Automatic matching on the same ground truth reached a highest precision of 0.43. A human reader recognises x as tidak. The automatic procedure largely did not. The two types of annotator therefore make errors on different inputs and at different rates. The choice of annotator consequently determines not only cost and speed but which errors a corpus will contain.

### P45 C22 counterfactual paragraph

**v18:** This difference changes what the choice of annotator means. If human and automatic annotation differed only in cost and speed, the choice between them would be a matter of budget. Because the two types make errors on different inputs, the choice also determines which errors a corpus will contain. A corpus labelled entirely by one type of annotator therefore carries that type's systematic errors throughout.

**v19:** (deleted)

### P46 C23 closing summary

**v18:** The three properties examined in this section therefore create three separate difficulties for annotation. The first property makes the part of the message that carries the opinion difficult to locate. The second property leaves the reading of that part open once it has been located. The third property makes the words themselves difficult for an automatic annotator to recognise. A human annotator recognises the same words readily. Section 3 examines the annotation strategies that have been used in response to these difficulties. It also examines the trade-off that each strategy accepts.

**v19:** (deleted)

### P49 C24

**v18:** Section 2 described what makes Malaysian code-mixed text hard to label. This section examines what has been done about it. The strategies reported in the reviewed studies are set out first, arranged by the trade-off each one accepts. The distribution of labels they produce is examined next, and the practice of pooling several annotators is examined last, because it is the remedy most often proposed, and the one the regional evidence tests most directly (Artstein and Poesio, 2008; Uma et al., 2021).

**v19:** Section 2 described what makes Malaysian code-mixed text difficult to label. This section examines what has been done about it. The annotation strategies reported in the reviewed studies are set out first, arranged by the trade-off each one accepts. The distribution of labels they produce is examined next. The practice of pooling several annotators is examined after that. It is a commonly proposed remedy for unreliable annotation (Artstein and Poesio, 2008; Uma et al., 2021), and it is the one that the Malaysian corpus evidence tests most directly. The section closes with the limits of each family of model when used as an annotator.

### P51 A1 + readability

**v18:** For low-resource code-mixed text, label fidelity and scale are in tension. A corpus can be labelled carefully or it can be labelled in volume. The strategies reported by the studies reviewed here are best read not as competing solutions to one problem, but as different decisions about which of the two to sacrifice. On that reading, the strategies fall into three tiers: manual annotation, semi-automated annotation, and fully automated generative annotation. 

**v19:** For low-resource code-mixed text, label fidelity and scale are in tension. A corpus can be labelled carefully or it can be labelled in volume. The strategies reported by the studies reviewed here differ in which of the two they sacrifice. They fall into three tiers: manual annotation, semi-automated annotation, and fully automated generative annotation.

### P52 readability

**v18:** The first tier is manual annotation by people. Two of the four Malay-English sentiment resources were built this way, and they are the only two whose labels come from human judgement. Kasmuri and Basiron (2019) drew 5,849 sentences from 23 personal blogs, selected 4,191 for annotation, and retained 2,316 in the finished corpus, reporting κ = 0.83 for the judgement of whether a sentence was opinionated or factual. Kong et al. (2023) collected 108,246 tweets and manually annotated 11,568 of them into three sentiment classes, using three independent annotators working from a written guideline. What both illustrate is the cost of the decision rather than a defect in the method. Kasmuri and Basiron kept 40% of the sentences they started with, and Kong et al. labelled 11% of what they collected. The labour that produces reliable labels is the same labour that prevents either corpus from reaching the scale a general-purpose Manglish resource would require.

**v19:** The first tier is manual annotation by people. Two of the four Malay-English sentiment resources were built this way, and they are the only two whose labels come from human judgement. Kasmuri and Basiron (2019) drew 5,849 sentences from 23 personal blogs, selected 4,191 for annotation, and retained 2,316 in the finished corpus. They report κ = 0.83 for the judgement of whether a sentence was opinionated or factual. Kong et al. (2023) collected 108,246 tweets and manually annotated 11,568 of them into three sentiment classes, using three independent annotators working from a written guideline. What both resources illustrate is the cost of choosing fidelity rather than a defect in the method. The labour that produces reliable labels is also what limits how far a manually annotated corpus can grow. Kasmuri and Basiron retained 40% of the sentences they started with, and Kong et al. labelled 11% of the tweets they collected.

### P53 readability

**v18:** The second tier is semi-automated annotation, which trades in the opposite direction by using existing tools to label at volume and accepting the tools' limitations as the price. Mohd Shamsuddin et al. (2024) built MESocSentiment this way. They collected 229,566 tweets carrying the "#Malaysia" keyword, reduced the set to 138,646 in pre-processing, applied the Malaya and Lingua libraries to identify code-switched posts, and arrived at 20,226 tweets. Sentiment labels were then assigned by majority vote among three existing analysers. The authors state the motivation plainly. The language identification libraries "reduced the need to find fluent speakers in Malay and English to classify the tweets". The reasoning is defensible, and there is evidence from other labelling tasks that automated annotators can match or exceed human crowd workers (Gilardi et al., 2023). What the tier concedes is that the labels can be no more competent than the tools producing them, and inherit whatever those tools cannot read.

**v19:** The second tier is semi-automated annotation. It makes the opposite choice, using existing tools to label at volume and accepting the limitations of those tools as the price. Mohd Shamsuddin et al. (2024) built MESocSentiment this way. They collected 229,566 tweets carrying the "#Malaysia" keyword and reduced the set to 138,646 in pre-processing. They then applied the Malaya and Lingua libraries to identify code-switched posts, which left 20,226 tweets. Sentiment labels were assigned by majority vote among three existing sentiment analysers. The authors state their motivation directly: the language identification libraries "reduced the need to find fluent speakers in Malay and English to classify the tweets". The reasoning is justifiable, and there is evidence from other labelling tasks that automated annotators can match or exceed human crowd workers (Gilardi et al., 2023). What the tier concedes is that the labels can be no more competent than the tools that produce them. Whatever those tools do not recognise, the labels do not record.

### P54 C25 + A2 + readability

**v18:** The third tier replaces those tools with generative models used directly as annotators. Because a generative model is not restricted to a fixed vocabulary, it can in principle interpret an unfamiliar spelling or an unseen slang term from context, which is the capability the second tier lacks. In principle this dissolves the trade-off. The peer-reviewed evidence does not yet support that reading. Jadhav et al. (2025) evaluated generative annotators on Marathi, an Indo-Aryan language of western India, across four tasks: sentiment analysis, two-class hate speech detection, four-class hate speech detection, and news classification. They found two generative large language models, GPT-4o and Llama 3.1 405B, trailing a fine-tuned BERT baseline by average accuracy margins of 10.2% and 14.1% respectively. BERT is a bidirectional transformer encoder pre-trained on unlabelled text. They conclude that fine-tuned transformers remain necessary where linguistic resources are scarce. Marathi is morphologically rich where Malay is not, so the result bounds the tier's promise rather than measuring it in this setting. That it is the only peer-reviewed study of the question available to this review is itself part of the finding. The third tier is the least evidenced of the three, and no study examined here evaluates generative annotation on Malaysian code-mixed text.

**v19:** The third tier replaces those tools with generative models used directly as annotators. A generative model is not restricted to a fixed vocabulary. It can therefore, in principle, interpret an unfamiliar spelling or an unseen slang term from its context, which is the capability the second tier lacks. In principle, this removes the trade-off. The peer-reviewed evidence does not yet support that conclusion. Jadhav et al. (2025) evaluated generative annotators on Marathi, an Indo-Aryan language of western India, across four classification tasks including sentiment analysis. They found that two generative large language models, GPT-4o and Llama 3.1 405B, scored below a fine-tuned BERT baseline by average accuracy margins of 10.2% and 14.1% respectively. BERT is a bidirectional transformer encoder pre-trained on unlabelled text (Devlin et al., 2019). The authors conclude that fine-tuned transformers remain necessary where linguistic resources are scarce. Marathi is morphologically rich where Malay is not, so the result limits what can be expected of the tier rather than measuring its performance on Malay-English text. The third tier is the least evidenced of the three, and no study examined here evaluates generative annotation on Malaysian code-mixed text.

### P57 A3 + readability

**v18:** The clearest regional evidence of what the second tier costs is the class distribution of the corpus it produced. MESocSentiment is labelled 78.23% neutral, 16.33% positive and 5.44% negative across 19,714 posts (Mohd Shamsuddin et al., 2024). Two reasons support reading that distribution as an artefact of the labelling method rather than a property of Malaysian discourse. The corpus was collected under the "#Malaysia" keyword across sports, politics and the arts, which are not topics on which social media users are typically neutral. A comparable corpus of Malaysian tweets labelled by human annotators is only 23.6% neutral (Kong et al., 2023). This section separates the two distinct causes at work in that skew, because they produce identical labels and require opposite responses.

**v19:** The clearest Malaysian evidence of what the second tier costs is the class distribution of the corpus it produced. MESocSentiment is labelled 78.23% neutral, 16.33% positive and 5.44% negative across 19,714 posts (Mohd Shamsuddin et al., 2024). Two reasons support interpreting that distribution as an artefact of the labelling method rather than as a property of Malaysian discourse. The first is that the corpus was collected under the "#Malaysia" keyword across sports, politics and the arts, topics that would be expected to attract opinion rather than neutral comment. The second is that a comparable corpus of Malaysian tweets labelled by human annotators is only 23.6% neutral (Kong et al., 2023). This section separates the two sources at work in that skew.

### P58 readability

**v18:** The first cause is the behaviour of a scoring function that finds nothing to score. Lexicon-based sentiment tools work by matching each word or phrase in a text against a sentiment lexicon and aggregating the scores of the matched words into an overall score (Selvaraju et al., 2024). That score is then divided into classes by threshold. VADER, one of the three analysers used to build MESocSentiment, sets its classification thresholds at −0.05 and +0.05 on a normalised score running from −1 to 1 (Hutto and Gilbert, 2014). Two consequences follow from combining those two facts, and this review states them as an inference rather than as a reported finding. A text whose affective tokens are absent from the lexicon contributes little or nothing to the aggregate. Its score therefore remains within the neutral band, and it is returned as neutral. On that reading, neutral is not always a judgement that a text is affectively balanced. It can also be the default output when nothing was recognised.

**v19:** The first source is the behaviour of a scoring function that finds nothing to score. Lexicon-based sentiment tools work by matching each word or phrase in a text against a sentiment lexicon and aggregating the scores of the matched words into an overall score (Selvaraju et al., 2024). That score is then divided into classes by threshold. VADER, one of the three analysers used to build MESocSentiment, sets its classification thresholds at −0.05 and +0.05 on a normalised score running from −1 to 1 (Hutto and Gilbert, 2014). Two consequences follow from combining those two facts, and this review states them as an inference rather than as a reported finding. A text whose affect-bearing words are absent from the lexicon contributes little or nothing to the aggregate score. Its score therefore remains within the neutral band, and it is returned as neutral. Under this view, neutral is not always a judgement that a text is affectively balanced. It can also be the default output when nothing was recognised.

### P59 readability

**v18:** The corpus authors' own error analysis indicates that the mechanism operates on this data. Alongside the corpus, Mohd Shamsuddin et al. (2024) present two small tables comparing the ensemble's label with the correct one. All three of the misclassified examples they give are neutral labels that should have been positive, and in all three the sentiment is carried by Malay: memang cantik sangat, selamat deepavali and raih gelar juara. In the correctly classified negative example, the sentiment is carried by an English word, worthless. Six author-selected examples are illustrative rather than statistical, and no error rate can be computed from them. Their uniformity is nonetheless difficult to dismiss: where the ensemble succeeded, the affect was in a language its tools covered, and in every case where it failed, the affect was not.

**v19:** The corpus authors' own error analysis indicates that this mechanism operates on their data. Alongside the corpus, Mohd Shamsuddin et al. (2024) present two small tables comparing the ensemble's label with the correct label. All three of the misclassified examples they give are neutral labels that should have been positive. In all three, the sentiment is carried by Malay: memang cantik sangat, selamat deepavali and raih gelar juara. In the correctly classified negative example, the sentiment is carried by an English word, worthless. Six author-selected examples are illustrative rather than statistical, and no error rate can be computed from them. Their uniformity is nonetheless difficult to dismiss. Where the ensemble succeeded, the affect was in a language its tools covered. In every case where it failed, the affect was not.

### P60 readability

**v18:** The second source has nothing to do with tooling. Some posts are genuinely hard to judge, and the annotators of these resources say so. Kasmuri and Basiron (2019) note that low agreement in sentiment annotation arises because sentiment texts are subjective, so evaluations differ from one annotator to another and are shaped by each annotator's background. Kong et al. (2023) make the same point about their own task, observing that tagging text with sentiment labels is highly subjective and influenced by personal beliefs, and that a clear guideline is needed for this reason. As Section 2.2 established, disagreement of this kind is not removed by collecting more judgements (Pavlick and Kwiatkowski, 2019).

**v19:** The second source has nothing to do with the tools. Some posts are difficult to judge, and the annotators of these resources say so. Kasmuri and Basiron (2019) note that low agreement in sentiment annotation arises because sentiment texts are subjective, so evaluations differ from one annotator to another and are shaped by each annotator's background. Kong et al. (2023) make the same point about their own task. They observe that tagging text with sentiment labels is highly subjective and influenced by personal beliefs, and that a clear guideline is needed for this reason. As Section 2.2 established, disagreement that arises from subjectivity is not removed by collecting more judgements (Pavlick and Kwiatkowski, 2019).

### P61 readability

**v18:** Separating the two sources matters because the labels they produce are indistinguishable and the responses they require are opposite. A genuinely neutral post is correctly labelled and belongs in the corpus. A falsely neutral post is an error that a better-resourced annotator would not have made. A single-model pipeline is structurally unable to tell them apart, because the evidence that would distinguish them, namely the affect the annotator could not read, is exactly the evidence that annotator does not have.

**v19:** Separating the two sources matters because the labels they produce are indistinguishable and the responses they require are opposite. A genuinely neutral post is correctly labelled and belongs in the corpus. A falsely neutral post is an error that a better-resourced annotator would not have made. A single-model pipeline is structurally unable to tell them apart. The evidence that would distinguish them is the affect the annotator could not read, and that is the evidence the annotator lacks.

### P62 C26 + readability

**v18:** The consequence is more damaging than the aggregate percentage suggests, because a false neutral does not only inflate one class. It also depletes another. Every strongly polarised post absorbed into the neutral class is a training example removed from a minority class that a downstream classifier needs most. At a 5.44% negative share, the smallest class in the corpus is also the one most exposed to that erosion.

**v19:** A false neutral does not only inflate one class. It also depletes another. Every strongly polarised post assigned to the neutral class is a training example removed from a minority class, which is where a classifier trained on the corpus has the fewest examples to learn from. At a 5.44% negative share, the smallest class in the corpus is also the class that this depletion reduces further.

### P64 readability

**v18:** Pooling several annotators is the response most often proposed when a single annotator is unreliable (Artstein and Poesio, 2008; Uma et al., 2021). MESocSentiment is evidence against that response, because it already was a consensus pipeline. Three sentiment analysers labelled every post and the majority label was assigned. The corpus skewed anyway.

**v19:** Pooling several annotators is a commonly proposed response when a single annotator is unreliable (Artstein and Poesio, 2008; Uma et al., 2021). MESocSentiment is evidence against that response, because it was already built as a consensus pipeline. Three sentiment analysers labelled every post and the majority label was assigned. The corpus skewed towards the neutral label anyway.

### P65 readability

**v18:** The reason is visible in the corpus authors' own reporting, and it is not the one that might be expected. Voting cancels error only to the extent that voters fail independently, and the usual guarantee of independence is architectural difference. Table 2 shows that architectural difference was present and did not help.

**v19:** The reason is visible in the corpus authors' own reporting, and it is not the reason that might be expected. Voting cancels error only to the extent that the voters fail independently. Independence would be expected where the voters differ in architecture, meaning that they are built in different ways. Table 2 shows that architectural difference was present and did not help.

### P67 readability

**v18:** Two things follow. The first is that every analyser skewed neutral before any vote was taken, so the skew was not produced by the voting rule. The second is that the analyser skewing hardest, at 85.8%, is pysentimiento, which is the transformer-based tool of the three, built on the neural architecture that underlies most current language models. The shared weakness is therefore not shallow processing, since the deepest model performed worst. None of the three is described by the corpus authors as covering Malay, and one is explicitly described as trained on four other languages. The property the three voters share is the language they cannot read, and a Malay affective token invisible to one is invisible to all. The ensemble does not cancel that error. It ratifies it, and unanimity produced this way is indistinguishable from confidence.

**v19:** Two observations follow from Table 2. The first is that every analyser skewed neutral before any vote was taken, so the skew was not produced by the voting rule. The second concerns the analyser that skewed hardest, pysentimiento, at 85.8%. It is the transformer-based tool of the three, built on the transformer architecture that underlies BERT (Devlin et al., 2019). The shared weakness is therefore not a lack of model capacity, since the transformer-based model performed worst. None of the three analysers is described by the corpus authors as covering Malay, and one is explicitly described as trained on four other languages. The property the three voters share is the language they do not cover. A Malay affect-bearing word that one analyser does not recognise is therefore unlikely to be recognised by the others. The ensemble does not cancel that error. It confirms it, and unanimity produced this way is indistinguishable from confidence. This shared language gap is the first weakness of the consensus pipeline.

### P68 readability

**v18:** The second weakness concerns the posts the ensemble cannot agree on. Where all three analysers returned different labels there was no majority, and the authors state their response directly: ambiguous cases "were removed to ensure the corpus only contains tweets from absolute categories". This affected 512 posts, or 2.53% of the 20,226 labelled. The difficulty is not the proportion but the composition. A post on which three analysers disagree is one where the signal is contested, or is carried by material none of them reads confidently. That description fits the heavily code-switched and particle-laden cases Section 2 identified as the hardest to annotate. The rule therefore removes the examples a robust classifier would most need, and removes them systematically rather than at random.

**v19:** The second weakness concerns the posts on which the ensemble could not agree. Where all three analysers returned different labels there was no majority. The authors state their response directly: ambiguous cases "were removed to ensure the corpus only contains tweets from absolute categories". This affected 512 posts, or 2.53% of the 20,226 labelled. The difficulty is not the proportion but the composition. A post on which three analysers disagree is one where the sentiment signal is contested, or is carried by words that none of them recognises confidently. That description fits the heavily code-switched and particle-laden posts that Section 2 identified as the hardest to annotate. The rule therefore removes the examples that a robust classifier particularly needs, and it removes them systematically rather than at random.

### P69 readability

**v18:** The effect on the corpus can be computed from the paper's own tables, and it runs in the wrong direction. Removing the contested posts left the neutral count unchanged at 15,422 while reducing the total from 20,226 to 19,714, so the neutral share rose by roughly two percentage points. Taken with the first weakness, static voting has a double effect: it keeps the labels it is confident about and wrong about, and deletes the ones it is uncertain about and would have learned from.

**v19:** The effect on the corpus can be computed from the paper's own tables, and it runs in the wrong direction. Removing the contested posts left the neutral count unchanged at 15,422 while reducing the total from 20,226 to 19,714. The neutral share therefore rose by roughly two percentage points. Taken with the first weakness, majority voting has a double effect. It keeps the labels it is confident about and wrong about, and it deletes the labels it is uncertain about and would have learned from.

### P70 readability

**v18:** The methodological literature on annotation supports treating that deletion as a loss rather than a cleanup. Uma et al. (2021) question the assumption that a single correct interpretation exists for every item. On that view, the 512 discarded posts were not noise removed from the corpus but signal removed from it.

**v19:** The methodological literature on annotation supports treating that deletion as a loss rather than as a cleaning step, since Uma et al. (2021) question the assumption that a single correct interpretation exists for every item. Under this view, the 512 discarded posts were not noise removed from the corpus but signal removed from it.

### P71 C27

**v18:** What the reviewed literature does not contain is any evaluation of a better procedure on this data. No study examined here adjudicates annotator disagreement on Malaysian code-mixed sentiment text, and the premise that annotators of different types fail independently, which is what licenses aggregation in the first place, is asserted rather than measured on this material. The evidence assembled above suggests that independence fails when the annotators share a language gap, but a suggestion is not a measurement and this review does not treat it as one. Both points are recorded here and returned to in Section 6 as questions for future research.

**v19:** No study examined here adjudicates annotator disagreement on Malaysian code-mixed sentiment text, and none measures whether annotators of different types fail independently, which is the premise on which aggregation rests. The evidence above suggests that they do not fail independently when they share a language gap. That remains a suggestion rather than a measurement, and it is returned to in Section 5 as a direction for future research.

### NEW 3.4 heading

**v18:** —

**v19:** 3.4 Where each family of model is limited as an annotator

### NEW 3.4 body (replaces Section 4)

**v18:** 4. Models as Annotation Instruments Section 3 established that the choice of annotator determines which errors a corpus will contain. This section asks where each family of model is limited when used as an annotator. Two families are examined: fine-tuned multilingual encoders, and generative models used directly as annotators. The question is not which architecture classifies best, which belongs to the comparative benchmarking placed outside the scope in Section 1. It is what each family cannot read, because that limitation is inherited by every corpus it labels. Fine-tuned multilingual encoders acquire their competence from exposure. An encoder here is a model that reads text and produces representations of it, rather than generating new text. Manukonda and Kodali (2025) illustrate the mechanism. They fine-tuned XLM-RoBERTa, a multilingual encoder model, over original, fully transliterated and partially transliterated versions of the same text, and report a macro F1 of 0.90 on the shared-task test set. The training method was masked language modelling, in which the model predicts words hidden from the input. Macro F1 is the mean of the per-class F1 scores, and F1 is the harmonic mean of precision and recall. The model handled the variant spellings because it had been shown them in training. A corollary follows from the method rather than from any claim the authors make. An encoder resolves the variation it has been trained on, so the coverage of a fine-tuned annotator is bounded by the coverage of its fine-tuning data. Extending that coverage requires more annotated or transliterated regional data, which is the resource whose scarcity motivated automated annotation in the first place. Two limits should be noted: the study is a shared-task system description rather than a full investigation, and the task is fake news detection in Malayalam rather than sentiment analysis in Malay. What transfers is the mechanism, not the result. Generative models locate their competence differently. Section 3.1 described the capability that follows from not being restricted to a fixed vocabulary. It is the capability the encoder lacks, and it is why generative annotation is attractive for a variety that changes faster than its resources. The competence is distributed unevenly across languages, and not in the way resource volume alone would predict. Jadhav et al. (2025) found frontier models trailing a fine-tuned BERT baseline by 10.2% and 14.1% accuracy when annotating Marathi. Adilazuarda et al. (2022) tested Indonesian code-mixed with four embedded languages, namely English, Sundanese, Javanese and Malay, and found robustness to English mixing lower than robustness to Javanese and Malay mixing across all models tested. They attribute the difference to the composition of the pre-training corpus. The direction of that result should be stated explicitly. The embedded language best represented in pre-training was the one the models handled least robustly. Robustness to code-mixing therefore does not follow directly from how much of a language a model has seen. The operative point is not the relative standing of the two families but the shape of their respective limitations. The encoder is reliable on what it has been shown and blind to what it has not. The generative model reasons about the unfamiliar, but its robustness on a given language pair cannot be predicted from the volume of data behind either language. Selecting an annotator is therefore not selecting a level of quality. It is selecting a failure mode, and the labels a corpus contains carry the signature of whichever mode was selected.

**v19:** The two families of model used as annotators in the reviewed studies are limited in different ways. The first is the fine-tuned multilingual encoder. An encoder is a model that reads text and produces representations of it rather than generating new text (Devlin et al., 2019). Manukonda and Kodali (2025) fine-tuned one such model on original and transliterated versions of the same text, and report that it handled the variant spellings it had been shown in training. It follows from the method, rather than from any claim the authors make, that a fine-tuned annotator resolves only the variation present in its fine-tuning data. Extending that coverage requires more annotated Malay-English data, which is the resource whose scarcity motivated automated annotation in the first place. The second family is the generative model, which is not restricted to a fixed vocabulary. Its robustness on a given language pair does not, however, follow from how much of either language it has seen. Adilazuarda et al. (2022) found that their models handled English mixing, the embedded language best represented in pre-training, less robustly than Javanese or Malay mixing. Jadhav et al. (2025) found generative annotators scoring below a fine-tuned encoder on a low-resource language. Selecting an annotator is therefore not selecting a level of quality. It is selecting a failure mode, and the labels a corpus contains reflect whichever mode was selected.

### P79 renumber

**v18:** 5. Evaluating Annotation Reliability

**v19:** 4. Evaluating Annotation Reliability

### P80 C29 edit + R4 46/47

**v18:** Sections 3 and 4 concerned how labels are produced. This section concerns how the labels that result are shown to be sound. Reliability is normally demonstrated with a chance-corrected agreement coefficient, of which Cohen's κ is the most widely used (Cohen, 1960; Artstein and Poesio, 2008). The coefficient measures how far the agreement two annotators actually reach exceeds the agreement expected by chance. Magnitudes are then read against conventions. In computational linguistics, values above 0.8 are generally treated as good reliability, and values between 0.67 and 0.8 as allowing tentative conclusions (Artstein and Poesio, 2008).

**v19:** Section 3 concerned how labels are produced. This section concerns how the reliability of the labels that result is evaluated. Reliability is normally assessed with a chance-corrected agreement coefficient, such as Cohen's κ (Cohen, 1960; Artstein and Poesio, 2008). The coefficient measures how far the agreement two annotators reach exceeds the agreement expected by chance. The resulting values are then read against conventions. In computational linguistics, values above 0.8 are generally treated as good reliability, and values between 0.67 and 0.8 as allowing tentative conclusions (Artstein and Poesio, 2008).

### P81 readability

**v18:** Those conventions assume that expected chance agreement is stable across datasets, and it is not. Feinstein and Cicchetti (1990) show that an imbalance in the marginal totals of an agreement table can convert a high observed agreement into a low coefficient. Their worked example illustrates the effect. Holding observed agreement at 0.85, an expected chance agreement of 0.50 yields κ = 0.70, while an expected chance agreement of 0.78 yields κ = 0.32. The annotators agreed on the same 85% of items in both cases. Byrt et al. (1993) formalise the effect, showing that κ reflects the distribution of data across categories as well as agreement, and propose a prevalence-adjusted coefficient in response. Di Eugenio and Glass (2004) name the effect the prevalence problem, and report a case in which two coders agreeing on 90 of 100 items yield κ values ranging from −0.048 to 0.80, depending only on how the two categories are distributed. Artstein and Poesio (2008) state the consequence for annotation directly: when one category is very common, high agreement can result from indiscriminate coding rather than from an ability to distinguish between categories.

**v19:** Those conventions assume that expected chance agreement is stable across datasets, and it is not. Feinstein and Cicchetti (1990) show that an imbalance in the marginal totals of an agreement table can convert a high observed agreement into a low coefficient. The marginal totals are the counts of items that each annotator assigned to each category. Their worked example illustrates the effect. Holding observed agreement at 0.85, an expected chance agreement of 0.50 yields κ = 0.70, while an expected chance agreement of 0.78 yields κ = 0.32. The annotators agreed on the same 85% of items in both cases. Byrt et al. (1993) formalise the effect, showing that κ reflects the distribution of data across categories as well as agreement, and propose a prevalence-adjusted coefficient in response. Di Eugenio and Glass (2004) name the effect the prevalence problem. They report a case in which two coders agreeing on 90 of 100 items yield κ values ranging from −0.048 to 0.80, depending only on how the two categories are distributed. Artstein and Poesio (2008) state the consequence for annotation directly: when one category is very common, high agreement can result from indiscriminate coding rather than from an ability to distinguish between categories.

### P82 C31 + readability

**v18:** That is the condition Malaysian code-mixed sentiment data is in. Section 3 established that the labelling methods available for this text produce heavily skewed class distributions, the largest corpus standing at 78.23% neutral. A skew of that size raises expected chance agreement, which is the quantity the correction depends on. The property that makes the labels unrepresentative is therefore the property that makes the statistic used to check them difficult to read. The difficulty runs in both directions. A low coefficient may indicate unreliable annotation, or a dominant class. A high one may indicate reliable annotation, or indiscriminate coding. Neither reading can be ruled out from the coefficient alone. This is the sense in which the annotation problem and the evaluation problem are one problem rather than two, and the reason correcting either alone leaves the other in place.

**v19:** That is the condition Malaysian code-mixed sentiment data is in. Section 3 established that the labelling methods available for this text produce heavily skewed class distributions, with the largest corpus at 78.23% neutral. A skew of that size raises expected chance agreement, which is the quantity the chance correction depends on. The property that makes the labels unrepresentative is therefore the property that makes the statistic used to check them difficult to interpret. The difficulty runs in both directions. A low coefficient may indicate unreliable annotation, or it may indicate a dominant class. A high coefficient may indicate reliable annotation, or it may indicate indiscriminate coding. Neither interpretation can be ruled out from the coefficient alone.

### P85 readability

**v18:** Three observations follow. The studies introducing two of the four resources report no agreement coefficient at all, including one whose corpus was annotated by three people working from a written guideline. The two coefficients that are reported were obtained for binary judgements, and neither is the three-class polarity task for which the resources are used. Romadhona et al. (2022) report a kappa value without stating which coefficient it is. Their annotation used five experts with the final label set by majority vote, and Cohen's κ is defined for two annotators.

**v19:** Three observations follow. First, the studies introducing two of the four resources report no agreement coefficient at all, including one whose corpus was annotated by three people working from a written guideline. Second, the two coefficients that are reported were obtained for binary judgements, and neither concerns the three-class polarity task for which the resources are used. Third, Romadhona et al. (2022) report a kappa value without stating which coefficient it is. Their annotation used five experts with the final label set by majority vote, whereas Cohen's κ is defined for two annotators.

### P86 R4 59 + readability

**v18:** None of the four corpora examined here therefore supplies what a reliability claim requires: a coefficient of a stated type, computed for the task the labels are used for, over annotators whose number and qualification are recorded. A corpus that did supply them would still face the interpretation problem above, because the class distributions these methods produce are the distributions under which the coefficient becomes hard to read. Establishing reliability for this data is not only unreported. With the instruments currently in use, it is not clearly achievable.

**v19:** None of the studies introducing the four corpora therefore supplies what a reliability claim requires. That requirement is a coefficient of a stated type, computed for the task the labels are used for, over annotators whose number and qualification are recorded. A corpus that did supply them would still face the interpretation problem described above, because the class distributions these labelling methods produce are the distributions under which the coefficient becomes difficult to interpret. Establishing reliability for this data is therefore not only unreported. With the instruments currently in use, it is not clearly achievable.

### P88 renumber

**v18:** 6. Synthesis: How the Challenges Compound

**v19:** 5. Synthesis: How the Challenges Compound

### P89 C32

**v18:** Sections 2 to 5 examined linguistic structure, annotation practice, model capability and reliability measurement in turn, which is how the studies reviewed here are organised. Read separately they describe four difficulties. Read together they describe one sequence, in which each difficulty creates the conditions for the next and the sequence returns to its own starting point. Figure 1 sets it out. Establishing that this structure exists is the contribution this review claims, and the directions in the second half of this section are traced to points within it.

**v19:** Sections 2 to 4 examined linguistic structure, annotation practice, the models used as annotators and reliability evaluation. Read separately, they describe four difficulties. Read together, they describe one sequence in which each difficulty creates the conditions for the next and the sequence returns to its own starting point, as Figure 1 sets out. Establishing that this structure exists is the contribution this review claims, and each direction in the second half of this section is traced to a point within it.

### P92 readability

**v18:** The first link runs from linguistic structure to systematic disagreement. Section 2 established three properties of this text. The consequence is not only that agreement is harder to reach. It is that disagreement takes a particular form. Where one annotator reads lah as a softener and another reads it as a marker of sarcasm, and each reading is stable, the disagreement recurs on the same construction in the same direction. Random disagreement is reduced by recruiting more annotators, because independent errors average out. Systematic disagreement is not, because additional annotators bring their own stable readings rather than noise around a shared one (Pavlick and Kwiatkowski, 2019). The usual response to unreliable annotation is therefore unsuited to the type of unreliability this text produces.

**v19:** The first link runs from linguistic structure to systematic disagreement. Section 2 established three properties of this text. The consequence is not only that agreement is harder to reach. It is that disagreement takes a particular form. Where one annotator reads lah as a softener and another reads it as a marker of sarcasm, and each reading is stable, the disagreement recurs on the same construction in the same direction. Random disagreement is reduced by recruiting more annotators, because independent errors average out. Systematic disagreement is not reduced in this way, because additional annotators bring their own stable readings rather than noise around a shared reading (Pavlick and Kwiatkowski, 2019). Pooling annotators, the response examined in Section 3.3, is therefore unsuited to the type of unreliability this text produces.

### P93 readability

**v18:** The second link runs from systematic disagreement to automation. Competent annotation of this material requires a fluent bilingual reader, and that requirement follows from the linguistic properties of the text rather than from any general fact about annotation. The corpus papers give cost and annotator availability as their reason for automating, and Mohd Shamsuddin et al. (2024) state that their tools "eliminated the need to find speakers fluent in Malay and English to label the dataset". Automation on this material is therefore downstream of the linguistic difficulty rather than an independent methodological preference.

**v19:** The second link runs from systematic disagreement to automation. Competent annotation of Malaysian code-mixed text requires a fluent bilingual reader, and that requirement follows from the linguistic properties of the text rather than from any general fact about annotation. Mohd Shamsuddin et al. (2024) give cost and annotator availability as their reason for automating, stating that their tools "eliminated the need to find speakers fluent in Malay and English to label the dataset". Automation of annotation for this text is therefore a consequence of the linguistic difficulty rather than an independent methodological preference.

### P94 readability

**v18:** The third link runs from automation to a shared limitation. The tools available for automation are those built for well-resourced languages. Section 3.3 documented the one regional case: none of the three analysers covers Malay, each skewed neutral before any vote was taken, and voting cancels error only to the extent that voters fail independently. Where the property they share is the language none of them reads, the ensemble ratifies the error instead of cancelling it.

**v19:** The third link runs from automation to a shared limitation. The tools used for automation in the reviewed studies are ones built for other, well-resourced languages. Section 3.3 documented the one Malaysian case. None of the three analysers is described as covering Malay, each skewed neutral before any vote was taken, and voting cancels error only to the extent that the voters fail independently. Where the property the voters share is the language none of them covers, the ensemble confirms the error instead of cancelling it.

### P95 readability + measured-agreement fix

**v18:** The fourth link runs from the shared limitation to extreme class skew. False neutrals accumulate rather than being corrected, and the corpus acquires a class distribution that no participant intended. MESocSentiment reaches 78.23% neutral. Posts on which the three analysers could not agree were removed, 512 of them, on the stated ground of retaining only "absolute categories". Those posts are not a random sample. They are the contested, heavily code-switched cases that the first link identifies as the source of the difficulty, and removing them raised both the neutral share and the measured agreement.

**v19:** The fourth link runs from the shared limitation to extreme class skew. False neutrals accumulate rather than being corrected, and the corpus acquires a class distribution that no participant intended. MESocSentiment reaches 78.23% neutral. Posts on which the three analysers could not agree were removed, 512 of them, on the stated ground of retaining only "absolute categories". Those posts are not a random sample. They are the contested, heavily code-switched cases that the first link identifies as the source of the difficulty. Removing them raised the neutral share and, by construction, the agreement among the three analysers.

### P96 R4 48 + readability

**v18:** The fifth link runs from extreme class skew to the difficulty of establishing reliability, and it is where the two halves of this review meet. The distribution produced at the fourth link is the specific condition under which a chance- corrected coefficient stops returning interpretable values (Feinstein and Cicchetti, 1990; Byrt et al., 1993). A researcher who suspects the labels are unsound and computes a coefficient obtains a low value, which is consistent with poor annotation and equally consistent with competent annotation of a skewed corpus. Raw agreement carries the same ambiguity in the opposite direction (Artstein and Poesio, 2008). The defect and the inability to detect the defect have one cause. That is what separates an unresolved problem from a merely difficult one: here the quality check is least informative exactly where quality is lowest.

**v19:** The fifth link runs from extreme class skew to the difficulty of establishing reliability, and it is where the two halves of this review meet. The distribution produced at the fourth link is the specific condition that makes a chance-corrected coefficient more difficult to interpret (Feinstein and Cicchetti, 1990; Byrt et al., 1993). A researcher who suspects the labels are unsound and computes a coefficient obtains a low value. That value is consistent with poor annotation, and it is also consistent with competent annotation of a skewed corpus. Raw agreement carries the same ambiguity in the opposite direction (Artstein and Poesio, 2008). The defect and the inability to detect the defect have one cause. That is what separates an unresolved problem from a merely difficult one: here the quality check is least informative where quality is lowest.

### P97 cross-ref + readability

**v18:** The sixth link closes the cycle. Corpora whose reliability was never established are released, trained on and evaluated against, so every downstream comparison inherits an error term that nobody has quantified. The more consequential edge is the one that returns. The annotators used to build the next corpus are fine-tuned on the last, and Section 4 showed that a fine-tuned encoder resolves only the variation it has been shown. The limitations of one generation of labels are transmitted to the instruments that produce the next, so the chain does not merely persist. It reproduces itself.

**v19:** The sixth link closes the cycle. Corpora whose reliability was never established are released, trained on and evaluated against, so every later comparison of models inherits an error term that nobody has quantified. The more consequential arrow in Figure 1 is the one that returns to the start. The annotators used to build the next corpus are fine-tuned on the last, and Section 3.4 showed that a fine-tuned encoder resolves only the variation it has been shown. The limitations of one generation of labels are therefore transmitted to the instruments that produce the next. The chain does not merely persist. It reproduces itself.

### P98 readability

**v18:** Read as a whole, the chain explains a pattern that the individual studies cannot. Each reviewed work intervenes at one link and does so competently. None addresses the chain as a chain, and an intervention at one link is assessed with an instrument compromised at another, so the assessment cannot establish whether the intervention worked. That is why effort in this area has been absorbed without accumulating.

**v19:** Read as a whole, the chain explains a pattern that the individual studies cannot. Each reviewed work intervenes at one link and does so competently. None addresses the chain as a chain. An intervention at one link is assessed with an agreement statistic compromised at another link, so the assessment cannot establish whether the intervention worked. That is why effort in this area has been absorbed without accumulating.

### P99 C33 lead-in

**v18:** The chain identifies where intervention would matter, not which intervention would succeed. Each of the five directions below is traced to a link, since a direction that cannot be traced to a finding is a preference rather than a conclusion.

**v19:** The chain identifies where intervention would matter, not which intervention would succeed. Each of the four directions below is traced to a link, since a direction that cannot be traced to a finding is a preference rather than a conclusion.

### P100 A5 + readability

**v18:** The first direction is agreement measurement under class skew, and it follows from the fifth link. Prevalence-adjusted coefficients exist (Byrt et al., 1993) but have not been evaluated on code-mixed sentiment data, so it is not known which behaves best under the distributions these corpora actually exhibit. The study requires no new data collection, only an existing annotated corpus, a set of candidate coefficients, and a comparison of how they behave as skew increases. It is a precondition for the others, because until reliability can be measured under prevailing conditions, no corpus built hereafter can be shown to improve on the ones described here.

**v19:** The first direction is agreement measurement under class skew, and it follows from the fifth link. Prevalence-adjusted coefficients exist (Byrt et al., 1993), but no study examined here evaluates them on code-mixed sentiment data, so it is not known which behaves best under the distributions these corpora exhibit. The study requires no new data collection. It requires only an existing annotated corpus, a set of candidate coefficients, and a comparison of how they behave as skew increases. It is a precondition for the other directions.

### P101 C33 D2+D4

**v18:** The second direction is a minimum reporting standard, and it follows from Table 3. A minimum set for any newly released corpus would comprise five elements: (1) the number of annotators and their stated qualification; (2) the availability of the annotation guideline; (3) the variant of the coefficient and the task it was computed for; (4) per-class rather than aggregate agreement; and (5) the full class distribution. Per-class agreement deserves particular emphasis, since an aggregate figure on a skewed corpus is dominated by the majority class and can conceal near-total disagreement on the minority polarities that matter most.

**v19:** The second direction is a minimum reporting standard, and it follows from Table 3. A minimum set for any newly released corpus would comprise six elements: (1) the number of annotators and their stated qualification; (2) the availability of the annotation guideline; (3) the variant of the coefficient and the task it was computed for; (4) per-class rather than aggregate agreement; (5) the full class distribution; and (6) the distribution of annotator judgements for each item, together with any items discarded, rather than only the resolved label. Per-class agreement deserves particular emphasis. An aggregate figure on a skewed corpus is dominated by the majority class, and it can conceal near-total disagreement on the minority polarities that matter most. The sixth element follows from the fourth link. Uma et al. (2021) report that models trained on the full distribution of annotator judgements can outperform models trained on aggregated labels. A corpus that reports what it discarded also allows a reader to judge whether its reported reliability was earned or obtained by removing the contested items.

### P102 D3 trims + readability

**v18:** The third direction is a shared annotation convention for affect-bearing particles, and it follows from the first link. Because the disagreement these particles generate is systematic rather than random, the appropriate remedy is a shared convention rather than additional annotators, and no such convention exists for lah, kan and their equivalents. A model is available. Mohammad (2016) proposes a questionnaire that separates the speaker's emotional state, the target of the opinion and the attitude taken toward it. It also treats sarcasm, ridicule and mockery as a distinct response rather than folding them into polarity, which is precisely the ambiguity Section 2.2 identified. Kong et al. (2023) adapt this scheme into a four-question guideline for Malaysian tweets. What is absent is not the design but its adaptation to Malaysian particles and its adoption across projects.

**v19:** The third direction is a shared annotation convention for affect-bearing particles, and it follows from the first link. Because the disagreement these particles generate is systematic rather than random, the appropriate remedy is a shared convention rather than additional annotators. No such convention was found among the studies reviewed here for lah, kan and their equivalents. Mohammad (2016) proposes a questionnaire that separates the speaker's emotional state, the target of the opinion and the attitude taken toward it. It also treats sarcasm, ridicule and mockery as a distinct response rather than folding them into polarity, which is the ambiguity Section 2.2 identified. Kong et al. (2023) adapt this scheme into a four-question guideline for Malaysian tweets. What is absent is not the design but its adaptation to Malaysian particles and its adoption across projects.

### P103 C33 D4 (folded into D2)

**v18:** The fourth direction is to publish label distributions rather than only resolved labels, and it follows from the fourth link. Current practice resolves disagreement by majority rule or removes it, discarding the information that the case was contested. Uma et al. (2021) report that models trained on the full distribution of annotator judgements can outperform models trained on aggregated labels. Publishing that distribution would preserve the cases that current pipelines delete.  It would also make the fourth link visible, since a corpus that reports what it discarded allows a reader to judge whether its reported reliability was earned or obtained by attrition.

**v19:** (deleted)

### P104 D5 -> fourth + readability

**v18:** The fifth direction is to test the independence premise, and it follows from the third link. Every consensus mechanism in this literature depends on the premise that annotators of different architecture fail independently, and on this material the premise is asserted throughout and measured nowhere. The study is a direct one: label a common sample with annotators of deliberately different competence, and measure the correlation of their errors rather than their individual accuracies. Low correlation would justify the aggregation strategies already in use. High correlation would indicate that consensus on this material adds confidence without adding evidence.

**v19:** The fourth direction is to test the independence premise, and it follows from the third link. Every consensus mechanism in the reviewed studies depends on the premise that annotators of different architecture fail independently, and on Malaysian code-mixed text the premise is asserted and not measured. The study is a direct one: label a common sample with annotators of deliberately different competence, and measure the correlation of their errors rather than their individual accuracies. Low correlation would justify the aggregation strategies already in use. High correlation would indicate that consensus on this text adds confidence without adding evidence.

### P107 renumber

**v18:** 7. Conclusion

**v19:** 6. Conclusion

### P108 C34

**v18:** This review examined one question: why reliable annotation and evaluation of Malaysian Malay-English code- mixed sentiment data remain unresolved. The answer usually given is architectural, and the evidence assembled here indicates that it is incomplete. Model choice accounts for part of the difficulty. The rest originates earlier, in the sentiment labels themselves and in the evidence offered that those labels are sound.

**v19:** This review examined one question: why reliable annotation and evaluation of Malaysian Malay-English code-mixed sentiment data have not yet been established. One common explanation concerns the model architecture, and the evidence assembled here indicates that it is incomplete. Model choice accounts for part of the difficulty, and the rest arises earlier, in the sentiment labels themselves and in the evidence offered that those labels are sound. What this review claims is not any single finding but the relation between the findings, set out in Figure 1 as a chain in which each difficulty creates the conditions for the next. An intervention at any one point in that chain is assessed by an agreement statistic compromised at another. Until reliability can be measured under the class distributions these corpora produce, no corpus built hereafter can be shown to improve on the ones examined here.

### P109 C34

**v18:** The contribution this review claims is not any of those findings taken alone but the relation between them. The linguistic properties of the text produce disagreement that is systematic rather than random, which makes fluent bilingual annotation necessary and expensive, which is why labelling is automated. The tools available for that automation cover neither Malay nor Manglish, so pooling them ratifies a shared error instead of cancelling it. The class skew that results is the precise condition under which the standard agreement coefficient stops returning interpretable values, so the defect and the inability to detect it have one cause rather than two. Each corpus built this way then trains the annotators that build the next. An intervention at any single point is assessed by an instrument compromised at another, which is why competent work at each link has not accumulated into progress.

**v19:** (deleted)

### P110 C34

**v18:** The directions set out in Section 6 follow from that structure rather than from preference. The first of them, an agreement measure that behaves interpretably under the class distributions these corpora actually exhibit, is a precondition for evaluating the rest. Until reliability can be measured under the conditions this data presents, no corpus built hereafter can be shown to improve on the ones examined here.

**v19:** (deleted)
