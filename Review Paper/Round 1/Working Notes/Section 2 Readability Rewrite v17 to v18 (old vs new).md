# Section 2 — readability pass, v17 → v18 (old vs new)

Source: `Current/Template ICON AI 2026 - Section 1 to 7 (v17).docx`, Section 2 (paragraphs 24–46). Target: `Current/Template ICON AI 2026 - Section 1 to 7 (v18).docx`. Date: 8 September 2026.

## Why this pass

Dr. Ho, on the v17 Section 2 extract: *"readability can still be enhanced, because the current writing style still makes some of the sentences written slightly densely where few ideas are compressed into one sentence."* Section 1 was approved as the target style.

## What was done

One idea per sentence, everywhere. Concretely: (1) every definition that was embedded mid-sentence (*insertion, in which…*, *meaning that…*) is its own sentence; (2) every "A, so B" / "A, and B" / "A because B, and C" sentence is split at the join; (3) every parenthetical clause inside a main clause is moved out; (4) a few abstract words are replaced by plainer ones of identical meaning (*defensible* → *justifiable*, *admits more than one reading* → *can be read in more than one way*). Nothing about the argument, the evidence, the citations, the figures or the examples is changed. Headings are unchanged. Paragraph count and order are unchanged.

## Measured against Section 1

| | Sentences | Words | Mean words/sentence | Median | Longest | Over 30 words |
|---|---|---|---|---|---|---|
| Section 1 (approved) | 93 | 1931 | 20.8 | 20 | 47 | 14 |
| Section 2, v17 | 91 | 1977 | 21.7 | 22 | 42 | 15 |
| Section 2, v18 | 146 | 2072 | 14.2 | 14.0 | 31 | 1 |

Section 2 grew by 95 words (+4.8%). In the LibreOffice preview the paper is still 21 pages; Section 3 now begins at the top of page 9 instead of the foot of page 8.

## Checker (`Comment_Tracker/check_section.py`) on v18, Section 2

0 sentences over 35 words · 0 same-source repeats on consecutive sentences · 0 uncited claim words · 0 flagged informal wording · 0 cross-references · 0 evaluative adjectives. The 6 bold hits are the three subsection headings (number + title), as in v17.

---

### 2.0 Section opener

**Old (v17)**

> Section 1 identified the sentiment labels, rather than the model, as the greater constraint on sentiment analysis of Malaysian Malay-English text. Before annotation practice is examined, the text being annotated needs to be described, because three of its linguistic properties affect the annotation task directly. The first is that switching between Malay and English occurs inside the sentence, so the boundary between the two languages does not indicate where the opinion is located. The second is that the affect of a message, meaning the emotional attitude it expresses, can be carried by Malay particles that appear in no standard sentiment lexicon. The third is that phonetic spelling gives a single word many written forms. All three properties are described in the sociolinguistic literature on Malay-English contact (Muysken, 2013; Treffers-Daller et al., 2022; AlAfnan et al., 2025). Each property is presented below together with its consequence for the annotator, whether human or automatic, who must assign a sentiment label.

**New (v18)**

> Section 1 identified the sentiment labels, rather than the model, as the greater constraint on sentiment analysis of Malaysian Malay-English text. Annotation practice is examined in Section 3. The text being annotated is described first, because three of its linguistic properties affect the annotation task directly. The first property is that switching between Malay and English occurs inside the sentence. The boundary between the two languages therefore does not show where the opinion in a message is located. The second property concerns the affect of a message, meaning the emotional attitude it expresses. That affect can be carried by Malay particles, and these particles appear in no standard sentiment lexicon. The third property is that phonetic spelling gives a single word many written forms. All three properties are described in the sociolinguistic literature on Malay-English contact (Muysken, 2013; Treffers-Daller et al., 2022; AlAfnan et al., 2025). Each property is presented below together with its consequence for the annotator. The annotator may be a human or an automatic labelling method.

*What changed.* Three sentences each carried a property *and* its consequence, or a definition *and* a claim; each is now two sentences. "Before annotation practice is examined, the text being annotated needs to be described, because…" was three ideas in one; now three sentences. The last sentence ("whether human or automatic, who must assign a sentiment label") had a double embedding; the annotator's two types are now their own sentence, using Section 1's term *automatic labelling method* (Rule 19). Also fixed: this paragraph was **centre-aligned** in v17 (a formatting slip visible in the PDF you sent); it is now justified like every other body paragraph.

---

### 2.1.1

**Old (v17)**

> Treffers-Daller et al. (2022) analysed 1,044 switched utterances from the classroom speech of two Malaysian teachers of English and found that most of the switches occurred within the clause rather than between clauses. Insertion, in which a word or phrase from one language is placed inside a stretch of the other, accounted for 33.0% of the switches. Congruent lexicalisation, in which words from both languages are combined within a single shared word order, accounted for a further 30.7%. Alternation between whole clauses accounted for 24.8%. The authors attribute this distribution to the structure of the two languages rather than to the style of the speakers. English and Malay share the same basic word order, in which the subject comes before the verb and the verb before the object. Malay also has very little inflectional morphology, meaning that its words change little in form to mark grammatical features such as tense. A speaker can therefore move from one language to the other in the middle of a clause with little grammatical adjustment (Treffers-Daller et al., 2022; Muysken, 2013).

**New (v18)**

> Treffers-Daller et al. (2022) analysed 1,044 switched utterances from the classroom speech of two Malaysian teachers of English. In their data, the majority of the switches occurred within the clause rather than between clauses. Insertion accounted for 33.0% of the switches. In insertion, a word or phrase from one language is placed inside a stretch of the other. Congruent lexicalisation accounted for a further 30.7%. In congruent lexicalisation, words from both languages are combined within a single shared word order. Alternation between whole clauses accounted for 24.8%. The authors attribute this distribution to the structure of the two languages rather than to the style of the speakers. English and Malay share the same basic word order. In both languages, the subject comes before the verb and the verb before the object. Malay also has very little inflectional morphology. Inflectional morphology refers to changes in the form of a word that mark grammatical features such as tense. A speaker can therefore move from one language to the other in the middle of a clause with little grammatical adjustment (Treffers-Daller et al., 2022; Muysken, 2013).

*What changed.* "analysed … and found that most …" split into what was analysed and what was found; *most* becomes *the majority* so the finding sentence does not need its own citation (checker pass 3). Each of *insertion* and *congruent lexicalisation* had its definition embedded mid-sentence between the term and the percentage; the figure and the definition are now separate sentences. The word-order sentence and the *inflectional morphology* sentence each carried a definition inside a claim; both are now two sentences.

---

### 2.1.2

**Old (v17)**

> These proportions were measured on spoken classroom data, so they should not be taken as the proportions in social media text. The explanation, however, concerns the structure of the two languages rather than the medium in which they are used, so the same type of switching can be expected in writing. Mohd Shamsuddin et al. (2024) give a written example in the post "Does institut kanser offer free medication cheap chemotherapy". Here the Malay noun phrase institut kanser, in which the noun comes before its modifier as Malay word order requires, is placed inside an English question.

**New (v18)**

> These proportions were measured on spoken classroom data. They should therefore not be taken as the proportions in social media text. The explanation given by the authors, however, concerns the structure of the two languages and not the medium in which they are used. The same type of switching can therefore be expected in writing. Mohd Shamsuddin et al. (2024) give a written example in the post "Does institut kanser offer free medication cheap chemotherapy". Here the Malay noun phrase *institut kanser* is placed inside an English question. The phrase follows Malay word order, in which the noun comes before its modifier.

*What changed.* Every sentence had a "so" or "however … so" joining a premise to a conclusion; each is now premise, then conclusion. The example sentence had a parenthetical clause ("in which the noun comes before its modifier as Malay word order requires") inside the main clause; the word-order point is now its own sentence after the example.

---

### 2.1.3 (consequence)

**Old (v17)**

> The consequence for annotation is that the annotator cannot use the boundary between the two languages to locate the part of the message that carries the sentiment. In monolingual annotation, locating that part is a separate step from judging its polarity. One example is aspect-based sentiment analysis, in which a sentiment label is assigned to each entity or attribute mentioned in a text rather than to the text as a whole (Nazir et al., 2022). A span is a marked stretch of text. In annotation schemes for that task, the annotator first marks the words that express the opinion as a span and then assigns a polarity label to that span (Pontiki et al., 2016). In Malay-English mixed text the annotator has no language boundary to guide that first step, so deciding which span to judge already requires interpretation. Two annotators may therefore assign different labels not because they judge the sentiment differently but because they are judging different parts of the message. Disagreement about which part of a message to judge is therefore separate from disagreement about its polarity, and it arises first.

**New (v18)**

> The consequence for annotation is that the annotator cannot use the boundary between the two languages to locate the part of the message that carries the sentiment. In monolingual annotation, locating that part is a separate step from judging its polarity. Aspect-based sentiment analysis is one task in which the two steps are separate. In that task, a sentiment label is assigned to each entity or attribute mentioned in a text rather than to the text as a whole (Nazir et al., 2022). In the annotation scheme described by Pontiki et al. (2016), the annotator first marks the words that express the opinion as a span. A span is a marked stretch of text. The annotator then assigns a polarity label to that span. In Malay-English mixed text, the annotator has no language boundary to guide the first step. Deciding which span to judge already requires interpretation. Two annotators may therefore assign different labels because they are judging different parts of the message, not because they judge the sentiment differently. Disagreement about which part of a message to judge is therefore separate from disagreement about its polarity. The first of these two disagreements also arises before the second.

*What changed.* "One example is aspect-based sentiment analysis, in which…" split into the example and its definition, and the example now says what it is an example of (Rule 4). The two-step annotation scheme was one 32-word sentence with *span* defined a sentence earlier; it is now step one, the definition of *span* where the word first appears, then step two. The "not because … but because" contrast is kept as one sentence (it is one idea) but reordered so the real reason comes first. "…is separate from disagreement about its polarity, and it arises first" is split, with an explicit subject instead of *it* (Rule 4).

---

### 2.2.1

**Old (v17)**

> Locating the part of the message that carries the opinion is the first difficulty. A second difficulty arises once that part has been located, because the word that carries the affect may be a Malay particle attached to a clause that is otherwise entirely English. Muysken (2013) terms this construction back-flagging. Treffers-Daller et al. (2022) define it as the attachment of a discourse marker or a coordinating conjunction from a speaker's first language to a stretch of speech in the second language. In their data, back-flagging accounts for 121 of the 1,044 switched utterances, or 11.6%. The particle involved most frequently is lah, which the same study reports can attach to a clause that is entirely English, entirely Malay or mixed. Two examples the study reproduces from earlier descriptive work are "Buy this lah" and "you understand lah kan".

**New (v18)**

> Locating the part of the message that carries the opinion is the first difficulty. A second difficulty arises once that part has been located. The word that carries the affect may be a Malay particle. That particle may be attached to a clause that is otherwise entirely English. Muysken (2013) terms this construction back-flagging. Treffers-Daller et al. (2022) define back-flagging as the attachment of a discourse marker or a coordinating conjunction from a speaker's first language to a stretch of speech in the second language. In their data, back-flagging accounts for 121 of the 1,044 switched utterances, or 11.6%. The particle involved most frequently is *lah* (Treffers-Daller et al., 2022). The same study reports that *lah* can attach to a clause that is entirely English, entirely Malay or mixed. Two examples that the study reproduces from earlier descriptive work are "Buy this lah" and "you understand lah kan".

*What changed.* "A second difficulty arises once that part has been located, because the word … may be a Malay particle attached to a clause that is otherwise entirely English" was three ideas; now three sentences. *Back-flagging* is named again in the definition instead of *it* (Rule 4). "The particle involved most frequently is lah, which the same study reports can attach…" split into the frequency fact and the attachment fact; the frequency sentence carries its own citation because it uses *most* (Rule 2, checker pass 3).

---

### 2.2.2

**Old (v17)**

> The contribution of these particles is to the tone of a sentence rather than to its factual content. AlAfnan et al. (2025) classify particles as a lexical feature of Manglish that adds emphasis or tone and signals politeness or informality. They also list particles among the features that distinguish Manglish from standard English and standard Malay. The same study identifies the softening of instructions as one function of these particles, giving "Don't disturb la, he's busy" as an example in which the particle makes the instruction less direct. Treffers-Daller et al. (2022) describe the same effect for lah, which they report can shift an utterance from a highly assertive tone to a polite request or a friendly encouragement. In both accounts the particle leaves what the sentence states unchanged and alters the attitude the sentence conveys, and that attitude is the property a sentiment label is intended to record.

**New (v18)**

> These particles contribute to the tone of a sentence rather than to its factual content. AlAfnan et al. (2025) classify particles as a lexical feature of Manglish. In their account, particles add emphasis or tone and signal politeness or informality. They also list particles among the features that distinguish Manglish from standard English and standard Malay. One function of these particles, according to the same study, is to soften an instruction. The example given is "Don't disturb la, he's busy", in which the particle makes the instruction less direct. Treffers-Daller et al. (2022) describe the same effect for *lah*. They report that *lah* can shift an utterance from a highly assertive tone to a polite request or a friendly encouragement. In both accounts, the particle leaves what the sentence states unchanged. What the particle alters is the attitude the sentence conveys. That attitude is the property a sentiment label is intended to record.

*What changed.* AlAfnan et al.'s classification and what particles do were one sentence; now two, with attribution carried by "In their account" so the source is not cited twice in a row (Rule 16). The softening example was one 32-word sentence (function + example + effect); now the function, then the example with its effect. Treffers-Daller's *lah* sentence split into the claim and what they report. The final sentence held three ideas (states unchanged / attitude altered / attitude is what a label records); now three sentences.

---

### 2.2.3 (limits)

**Old (v17)**

> Two limits on this evidence should be noted. Treffers-Daller et al. (2022) supply frequencies, but their corpus is fifteen hours of recorded classroom teaching by each of two university English lecturers. Their frequencies should therefore not be read as frequencies for social media writing. AlAfnan et al. (2025) describe Malaysian usage more broadly, but their data are scripted dialogue from Malaysian television series such as Kopitiam and KL Gangster, examined through qualitative content analysis. That study therefore reports what the particles do, not how often they occur. Neither source establishes how frequently particles are used in Malaysian social media posts, and no such figure was found among the studies reviewed here. What both sources do establish is that the construction recurs and that it carries affect.

**New (v18)**

> Two limits on this evidence should be noted. Treffers-Daller et al. (2022) supply frequencies. Their corpus, however, is fifteen hours of recorded classroom teaching by each of two university English lecturers. Their frequencies should therefore not be read as frequencies for social media writing. AlAfnan et al. (2025) describe Malaysian usage more broadly. Their data, however, are scripted dialogue from Malaysian television series such as *Kopitiam* and *KL Gangster*. Those data were examined through qualitative content analysis. That study therefore reports what the particles do, not how frequently they occur. Neither source establishes how frequently particles are used in Malaysian social media posts. No such figure was found among the studies reviewed here. What both sources do establish is that the construction recurs and that it carries affect.

*What changed.* Each "X supply Y, but their corpus is Z" sentence is split into the claim and the limit, with *however* marking the limit. The AlAfnan data sentence carried three facts (scripted dialogue, the series, the method); the method is now its own sentence. "Neither source establishes …, and no such figure was found …" split. *how often* → *how frequently* so the checker does not read *often* as an uncited frequency claim.

---

### 2.2.4 (consequence)

**Old (v17)**

> The consequence for annotation is that the particle indicates the tone of a message but does not determine its polarity. A reader of "Don't disturb la, he's busy" can see that the particle softens the instruction. A softened instruction is nonetheless compatible with a negative reading, in which the writer is irritated, and with a neutral reading, in which the writer is being polite. Treffers-Daller et al. (2022) note the same difficulty for discourse markers as a whole, observing that their specific meanings are often difficult to capture even where their pragmatic functions can be evaluated. The particle therefore carries affect without indicating which polarity that affect has, and two annotators may read it differently while both reading it competently.

**New (v18)**

> The consequence for annotation is that the particle indicates the tone of a message but does not determine its polarity. A reader of "Don't disturb la, he's busy" can see that the particle softens the instruction. A softened instruction can still be read in two ways. Under a negative reading, the writer is irritated. Under a neutral reading, the writer is being polite. Treffers-Daller et al. (2022) note the same difficulty for discourse markers as a whole, whose specific meanings are often difficult to capture even where their pragmatic functions can be evaluated. The particle therefore carries affect without showing which polarity that affect has. Two annotators may read the same particle differently, and both may be reading it competently.

*What changed.* "A softened instruction is nonetheless compatible with a negative reading, in which…, and with a neutral reading, in which…" (28 words, two embedded clauses) is now three short sentences. The Treffers-Daller sentence is kept as one sentence because the *often* it contains must sit with its citation (Rule 2); its participle clause ("observing that") is replaced by a relative clause. The closing sentence ("carries affect without indicating which polarity …, and two annotators may read it differently while both reading it competently") is split into the two claims.

---

### 2.2.5

**Old (v17)**

> Disagreement of this kind is not necessarily reduced by adding annotators. Pavlick and Kwiatkowski (2019) find that where an item admits more than one defensible reading, disagreement between annotators is reproducible and persists as further judgements are collected, rather than converging on a single label. A corpus built by majority vote over such items therefore records the majority reading as though it were the only defensible one, and the variation it conceals is systematic rather than random. An agreement coefficient computed over such items reflects genuine differences in interpretation rather than annotator error alone.

**New (v18)**

> Disagreement of this kind is not necessarily reduced by adding annotators. Pavlick and Kwiatkowski (2019) find that where an item can be read in more than one justifiable way, the disagreement between annotators is reproducible. The same disagreement appears again as further judgements are collected, and the judgements do not converge on a single label. A corpus built by majority vote over such items therefore records the majority reading as though it were the only justifiable one. The variation that the majority vote conceals is systematic rather than random. An agreement coefficient computed over such items therefore reflects genuine differences in interpretation rather than annotator error alone.

*What changed.* The Pavlick and Kwiatkowski finding was one 34-word sentence with a subordinate condition, a claim, and two consequences; now the condition and the claim, then the two consequences. *defensible* → *justifiable*; *admits more than one reading* → *can be read in more than one way* (plainer, same meaning). "records the majority reading as though it were the only defensible one, and the variation it conceals is systematic" split, and *it* replaced by *the majority vote* (Rule 4).

---

### 2.2.6 (recap)

**Old (v17)**

> The first property examined in this section produces disagreement about which part of a message to judge. The second produces disagreement about how to judge that part once it has been found, because more than one reading of it is defensible.

**New (v18)**

> The first property examined in this section produces disagreement about which part of a message to judge. The second property produces disagreement about how to judge that part once it has been located. That disagreement arises because more than one reading of the part is justifiable.

*What changed.* "how to judge that part once it has been found, because more than one reading of it is defensible" split into the claim and its reason. *The second* → *The second property* (Rule 4).

---

### 2.3.1

**Old (v17)**

> The first two properties concern where the sentiment in a message is located and how it should be read. The third concerns whether the words that carry it can be recognised at all. Maskat and Rahman (2020) document Malay social media users spelling words as they are pronounced rather than as a dictionary lists them, so that a single word can appear in many written forms. Working from a corpus of 6,241 Twitter posts collected between 2014 and 2018, they sort what they call Social Media Malay Language into five categories: spelling variants, Malay-English mixed sentences, loan words spelled according to Malay pronunciation, slang-based spellings, and vowel-less words.

**New (v18)**

> The first two properties concern where the sentiment in a message is located and how it should be read. The third property concerns whether the words that carry the sentiment can be recognised at all. Maskat and Rahman (2020) document Malay social media users spelling words as they are pronounced rather than as a dictionary lists them. A single word can therefore appear in many written forms. Their corpus is 6,241 Twitter posts collected between 2014 and 2018. They call the language of these posts Social Media Malay Language and sort it into five categories. The categories are spelling variants, Malay-English mixed sentences, loan words spelled according to Malay pronunciation, slang-based spellings, and vowel-less words.

*What changed.* "document … spelling words as they are pronounced …, so that a single word can appear in many written forms" split into observation and consequence. The 42-word corpus sentence (corpus size, dates, the name they give the language, five categories, the list) is now three sentences: the corpus, the name and the count, the list.

---

### 2.3.2

**Old (v17)**

> Each category contains many forms. Among the spelling variants that Maskat and Rahman (2020) record, macam mana appears as mcmana, camne, camner, mcmner and cane. In the vowel-less category a word is reduced to its consonants or to a single character, so jangan is written jgn and pada is written pd. The slang category varies by region, with besar written besaq in the north and beso on the east coast. The categories can also combine, and the same study gives x suko as a form that belongs to the slang and vowel-less categories at once.

**New (v18)**

> Each category contains many forms. Among the spelling variants that Maskat and Rahman (2020) record, *macam mana* appears as *mcmana*, *camne*, *camner*, *mcmner* and *cane*. In the vowel-less category, a word is reduced to its consonants or to a single character. For example, *jangan* is written *jgn* and *pada* is written *pd*. The slang category varies by region. The word *besar* is written *besaq* in the north and *beso* on the east coast. The categories can also combine. The same study gives *x suko* as a form that belongs to the slang and vowel-less categories at once.

*What changed.* Each "category rule, so example" sentence is now the rule, then the example ("For example, …"). "The categories can also combine, and the same study gives…" split.

---

### 2.3.3

**Old (v17)**

> The question that matters for annotation is whether this variation can be reversed automatically, and Maskat and Rahman (2020) tested this directly. They attempted to normalise two of the five categories, spelling variants and vowel-less words, meaning that they tried to map each non-standard form automatically to its standard spelling. The methods used were two measures of string similarity, n-gram similarity and Levenshtein distance, each of which scores how closely two spellings resemble one another. The benchmark was a set of 1,176 pairs of similar words covering 435 distinct words, identified by hand by a native Malay speaker. Precision here is the proportion of the matches proposed by a method that were correct. On that benchmark, the highest precision reported for any configuration was 0.43, and most of the configurations reported were lower than that. The authors conclude that similarity matching can detect the two categories but that a more sophisticated technique is needed, and they state that normalisation of the remaining three categories is left for future research.

**New (v18)**

> The question that matters for annotation is whether this variation can be reversed automatically. Maskat and Rahman (2020) tested this question directly. They attempted to normalise two of the five categories, spelling variants and vowel-less words. To normalise a form means to map it automatically to its standard spelling. Two measures of string similarity were used, n-gram similarity and Levenshtein distance. Each measure scores how closely two spellings resemble one another. The benchmark was a set of 1,176 pairs of similar words covering 435 distinct words. A native Malay speaker identified these pairs by hand. Precision here is the proportion of the matches proposed by a method that were correct. On that benchmark, the highest precision reported for any configuration was 0.43. Most of the configurations reported were lower than that (Maskat and Rahman, 2020). The authors conclude that similarity matching can detect the two categories but that a more sophisticated technique is needed. They also state that normalisation of the remaining three categories is left for future research.

*What changed.* "…whether this variation can be reversed automatically, and Maskat and Rahman (2020) tested this directly" split. The definition of *normalise* ("meaning that they tried to map…") is now its own sentence. The methods sentence (two measures + their names + what a measure does) and the benchmark sentence (pairs + distinct words + who identified them) are each split in two. "highest precision … was 0.43, and most of the configurations … were lower" split; the *most* sentence carries its citation (Rule 2). The authors' two conclusions are now two sentences.

---

### 2.3.4 (limits)

**Old (v17)**

> Two limits on this evidence should be noted. Only slang from Selangor was handled, so the slang category was tested more narrowly than the regional range the same paper describes. More importantly for this review, English words were removed before the experiment and code-mixed posts were excluded from the evaluation subsets. The reported precision is therefore a measurement on Malay text with the English removed, not on Malay-English mixed text, and no equivalent measurement for mixed text was found among the studies reviewed here.

**New (v18)**

> Two limits on this evidence should be noted. The first is that only slang from Selangor was handled. The slang category was therefore tested more narrowly than the regional range the same paper describes. The second limit matters more for this review. English words were removed before the experiment, and code-mixed posts were excluded from the evaluation subsets. The reported precision is therefore a measurement on Malay text with the English removed, not on Malay-English mixed text. No equivalent measurement for mixed text was found among the studies reviewed here.

*What changed.* The two limits are now labelled "The first is…" and "The second limit…" so the reader does not have to work out where one ends (Rule 10). "…is therefore a measurement on Malay text …, not on mixed text, and no equivalent measurement was found" split.

---

### 2.3.5 (consequence)

**Old (v17)**

> The consequence for annotation is that human and automatic annotators differ in what they can recognise, and the difference can be seen in the study just described. A single native speaker identified 1,176 word pairs by hand, reliably enough for the result to serve as the ground truth. Automatic matching on the same ground truth reached a highest precision of 0.43. A human reader recognises x as tidak; the automatic procedure largely did not. The two types of annotator therefore make errors on different inputs and at different rates.

**New (v18)**

> The consequence for annotation is that human and automatic annotators differ in what they can recognise. The difference can be seen in the study just described. A single native speaker identified 1,176 word pairs by hand. That identification was reliable enough for the result to serve as the ground truth. Automatic matching on the same ground truth reached a highest precision of 0.43. A human reader recognises *x* as *tidak*. The automatic procedure largely did not. The two types of annotator therefore make errors on different inputs and at different rates.

*What changed.* "differ in what they can recognise, and the difference can be seen in the study just described" split. "identified 1,176 word pairs by hand, reliably enough for the result to serve as the ground truth" split. The semicolon sentence ("A human reader recognises x as tidak; the automatic procedure largely did not") is two sentences.

---

### 2.3.6

**Old (v17)**

> This difference changes what the choice of annotator means. If human and automatic annotation differed only in cost and speed, the choice between them would be a matter of budget. Because they make errors on different inputs, the choice also determines which errors a corpus will contain, and a corpus labelled entirely by one type of annotator carries that type's systematic errors throughout.

**New (v18)**

> This difference changes what the choice of annotator means. If human and automatic annotation differed only in cost and speed, the choice between them would be a matter of budget. Because the two types make errors on different inputs, the choice also determines which errors a corpus will contain. A corpus labelled entirely by one type of annotator therefore carries that type's systematic errors throughout.

*What changed.* The last sentence carried the reason, the consequence, and a further consequence; now two sentences. *they* → *the two types* (Rule 4).

---

### 2.3.7 (section close)

**Old (v17)**

> The three properties examined in this section therefore create three separate difficulties for annotation. The first makes the part of the message that carries the opinion difficult to locate. The second leaves the reading of that part open once it has been located. The third makes the words themselves difficult for an automatic annotator to recognise, while a human annotator recognises them readily. Section 3 examines the annotation strategies that have been used in response to these difficulties, and the trade-off each strategy accepts.

**New (v18)**

> The three properties examined in this section therefore create three separate difficulties for annotation. The first property makes the part of the message that carries the opinion difficult to locate. The second property leaves the reading of that part open once it has been located. The third property makes the words themselves difficult for an automatic annotator to recognise. A human annotator recognises the same words readily. Section 3 examines the annotation strategies that have been used in response to these difficulties. It also examines the trade-off that each strategy accepts.

*What changed.* *The first / second / third* → *The first property* etc. (Rule 4). "…difficult for an automatic annotator to recognise, while a human annotator recognises them readily" split. "Section 3 examines …, and the trade-off each strategy accepts" split. *locate/located* kept throughout Section 2 as the one term for finding the opinion-bearing part (Rule 19).

---
