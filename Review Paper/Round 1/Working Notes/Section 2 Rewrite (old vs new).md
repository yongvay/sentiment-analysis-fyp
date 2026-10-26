# Section 2 — old vs new

Source: `Current/Template ICON AI 2026 - Section 1 to 7 (v16).docx`, Section 2 (paragraphs 24–46).
Target style: Section 1 of v16, which Dr. Ho accepted on 3 September.

What "the Section 1 style" means in practice, taken from the master tracker:

1. Every word that points at something names it in place (Rule 4). No *this material*, *that asymmetry*, *the effect*.
2. Formal but plain. No metaphors (*run in opposite directions*, *adds a regional layer*, *visible inside the study*), no phrasal verbs (*undone*, *stripped out*). Rule 3 and Rule 8.
3. Every claim about what people do or what the literature contains is hedged and carries its citation on the same sentence (Rules 2 and 6). Dr. Ho's own rewordings always add *may*, *can*, *suggests*.
4. Technical terms are defined the first time they appear (Rule 5): *affect*, *span*, *aspect-based sentiment analysis*, *inflectional morphology*, *normalise*, *precision*.
5. No sentence tells the reader what the paper is doing (Rule 17). Section 2's opener had one.
6. No sentence over 35 words. His replacements are longer than the originals, so length is spent on splitting, not on compression.
7. Nothing about the argument, the evidence, or the figures is changed.

Every paragraph is given as **Old** then **New**, with a one-line note. Italics in the new text mark non-English words on first use, as in Section 1.

---

## 2. Why Malaysian Code-Mixed Text Is Difficult to Annotate

### Paragraph 2.0 (section opener)

**Old**

> The studies selected under these criteria describe a body of text whose linguistic properties shape every later stage of the review, and those properties are therefore examined first. Three of them affect the annotation task directly. The first is that switching occurs inside the sentence and offers little reliable cue to where the opinion is located. The second is that affective meaning is often carried by function words that appear in no standard sentiment lexicon. The third is that phonetic spelling multiplies the surface forms of a single word. All three are already described in the sociolinguistic literature on Malay-English contact (Treffers-Daller et al., 2022; AlAfnan et al., 2025; Muysken, 2013). What this section adds is not the description but the consequence that each property carries for the annotator, whether human or automatic, who must assign a sentiment label. Each property is therefore presented together with a short statement of that consequence, and the linguistic description itself is not extended beyond what the consequence requires.

**New**

> Section 1 identified the sentiment labels, rather than the model, as the greater constraint on sentiment analysis of Malaysian Malay-English text. Before annotation practice is examined, the text being annotated needs to be described, because three of its linguistic properties affect the annotation task directly. The first is that switching between Malay and English occurs inside the sentence, so the boundary between the two languages does not indicate where the opinion is located. The second is that the affect of a message, meaning the emotional attitude it expresses, can be carried by Malay particles that appear in no standard sentiment lexicon. The third is that phonetic spelling gives a single word many written forms. All three properties are described in the sociolinguistic literature on Malay-English contact (Muysken, 2013; Treffers-Daller et al., 2022; AlAfnan et al., 2025). Each property is presented below together with its consequence for the annotator, whether human or automatic, who must assign a sentiment label.

*Note.* "These criteria" pointed at nothing, since Section 1 now compresses the search into one sentence; replaced by a bridge from Section 1's conclusion (R2 55, Rule 7). "Often carried" was an uncited frequency claim; now "can be carried" (Rule 2). *Affect* is defined at first use (Rule 5). The last two sentences narrated what the section does and are removed (Rule 17). "Function words" becomes "particles" so one term is used for the concept throughout (Rule 19).

---

### 2.1 Switching occurs within the sentence and offers little reliable structural cue

*Heading note (optional).* "Structural cue" is the kind of compressed noun phrase he queries. A plainer heading would be: **2.1 Switching occurs within the sentence and gives no reliable cue to where the opinion is located**. Your call; the body works with either.

### Paragraph 2.1.1

**Old**

> Malay-English switching occurs predominantly within the clause rather than between clauses. Treffers-Daller et al. (2022) analysed 1,044 switched utterances and found that insertion, in which a content word or phrase from one language is embedded in a stretch of the other, accounted for 33.0% of switches. Congruent lexicalisation, in which the grammar and vocabulary of both languages operate within a shared word order, accounted for a further 30.7%. Clause-level alternation accounted for 24.8%. The authors explain this distribution typologically rather than stylistically. English and Malay share Subject-Verb-Object (SVO) word order, and Malay carries very little inflectional morphology, so a speaker can move between the two languages mid-clause with minimal grammatical adjustment (Treffers-Daller et al., 2022; Muysken, 2013).

**New**

> Treffers-Daller et al. (2022) analysed 1,044 switched utterances from the classroom speech of two Malaysian teachers of English and found that most of the switches occurred within the clause rather than between clauses. Insertion, in which a word or phrase from one language is placed inside a stretch of the other, accounted for 33.0% of the switches. Congruent lexicalisation, in which words from both languages are combined within a single shared word order, accounted for a further 30.7%. Alternation between whole clauses accounted for 24.8%. The authors attribute this distribution to the structure of the two languages rather than to the style of the speakers. English and Malay share the same basic word order, in which the subject comes before the verb and the verb before the object. Malay also has very little inflectional morphology, meaning that its words change little in form to mark grammatical features such as tense. A speaker can therefore move from one language to the other in the middle of a clause with little grammatical adjustment (Treffers-Daller et al., 2022; Muysken, 2013).

*Note.* The old first sentence was a flat general claim with no citation on it; the claim is now attached to the study that supports it and bounded to that study's data (Rules 2, 6, and R3 11). "Typologically rather than stylistically" is said in plain words. "Inflectional morphology" is kept as the term the source uses, and defined (Rule 5). The SVO abbreviation is dropped because it is never used again.

### Paragraph 2.1.2

**Old**

> The corpus analysed is spoken, so the exact proportions should not be transferred to social media text. The structural explanation, however, is a property of the language pair rather than of the medium, and it therefore applies wherever the two languages are used together. A written instance is the post "Does institut kanser offer free medication cheap chemotherapy", in which a Malay noun phrase, in Malay head-initial word order, is embedded within an English question (Mohd Shamsuddin et al., 2024).

**New**

> These proportions were measured on spoken classroom data, so they should not be taken as the proportions in social media text. The explanation, however, concerns the structure of the two languages rather than the medium in which they are used, so the same type of switching can be expected in writing. Mohd Shamsuddin et al. (2024) give a written example in the post "Does institut kanser offer free medication cheap chemotherapy". Here the Malay noun phrase *institut kanser*, in which the noun comes before its modifier as Malay word order requires, is placed inside an English question.

*Note.* "Applies wherever the two languages are used together" was absolute; now "can be expected" (Rule 6). The 36-word sentence is split. "Head-initial word order" is replaced by what it means.

### Paragraph 2.1.3

**Old**

> The consequence for annotation is that the annotator cannot use a language boundary to locate the part of the message that carries the sentiment. In monolingual annotation this location step is separate from the judgement itself and largely mechanical. Annotation schemes for aspect-based sentiment analysis, for example, require the opinion target expression to be marked as an explicit span in the text before a polarity label is assigned to it (Pontiki et al., 2016; Nazir et al., 2022). In Malay-English mixed text, identifying that span is already an act of interpretation. Two annotators may therefore assign different labels not because they read the sentiment differently, but because they are reading different parts of the message. Disagreement about which span to judge precedes, and is separate from, disagreement about polarity.

**New**

> The consequence for annotation is that the annotator cannot use the boundary between the two languages to locate the part of the message that carries the sentiment. In monolingual annotation, locating that part is a separate step from judging its polarity. One example is aspect-based sentiment analysis, in which a sentiment label is assigned to each entity or attribute mentioned in a text rather than to the text as a whole (Nazir et al., 2022). A span is a marked stretch of text. In annotation schemes for that task, the annotator first marks the words that express the opinion as a span and then assigns a polarity label to that span (Pontiki et al., 2016). In Malay-English mixed text the annotator has no language boundary to guide that first step, so deciding which span to judge already requires interpretation. Two annotators may therefore assign different labels not because they judge the sentiment differently but because they are judging different parts of the message. Disagreement about which part of a message to judge is therefore separate from disagreement about its polarity, and it arises first.

*Note.* "Largely mechanical" was an uncited claim and is dropped. *Aspect-based sentiment analysis* and *span* are defined at first use (Rule 5), and the 39-word sentence is split into two, each carrying its own citation. "An act of interpretation" is stated literally.

---

### 2.2 Affective meaning is carried by particles that belong to neither standard language

### Paragraph 2.2.1

**Old**

> Locating the opinion-bearing span is only the first difficulty. A second arises once the span has been found. In Malay-English mixed writing, the element that carries the affect is often a Malay particle attached to a clause that is otherwise entirely in English (Treffers-Daller et al., 2022). The construction is a distinct type of code-switching, which Muysken (2013) terms back-flagging. Treffers-Daller et al. (2022) define it as the attachment of a discourse marker or co-ordinate conjunction from a speaker's first language to a stretch of speech in the second. Back-flagging accounts for 121 of the 1,044 switched utterances in their data, or 11.6%. The particle involved most frequently is lah, which the same study reports can attach to a clause that is entirely English, entirely Malay or mixed. Two examples it reproduces from earlier descriptive work are "Buy this lah" and "you understand lah kan".

**New**

> Locating the part of the message that carries the opinion is the first difficulty. A second difficulty arises once that part has been located, because the word that carries the affect may be a Malay particle attached to a clause that is otherwise entirely English. Muysken (2013) terms this construction back-flagging. Treffers-Daller et al. (2022) define it as the attachment of a discourse marker or a coordinating conjunction from a speaker's first language to a stretch of speech in the second language. In their data, back-flagging accounts for 121 of the 1,044 switched utterances, or 11.6%. The particle involved most frequently is *lah*, which the same study reports can attach to a clause that is entirely English, entirely Malay or mixed. Two examples the study reproduces from earlier descriptive work are "Buy this lah" and "you understand lah kan".

*Note.* The old third sentence cited Treffers-Daller et al. (2022), a study of classroom speech, for a claim about "mixed writing" and said "often". He caught exactly this misuse at R2 62 and R3 11, and the R4 self-check found it again in Section 1. The claim is now "may be", and the source is cited only for what it contains (Rules 2, 6). "It reproduces" becomes "the study reproduces" (Rule 4).

### Paragraph 2.2.2

**Old**

> What these particles contribute is pragmatic rather than propositional, and the pragmatic work they do is affective. AlAfnan et al. (2025) classify particles as a lexical feature that adds emphasis or tone and signals politeness or informality. The same study identifies the softening of directives as one of their pragmatic functions, giving "Don't disturb la, he's busy" as an instance in which the particle makes an instruction less direct. Treffers-Daller et al. (2022) describe the effect more precisely: lah shifts an utterance from a highly assertive tone to a polite request or a friendly encouragement. These particles belong to Manglish rather than to either source language, and AlAfnan et al. (2025) list them among the features that distinguish Manglish from standard English and standard Malay. In both accounts the particle leaves unchanged what the sentence states. What it changes is how the sentence is to be taken, which is the property a sentiment label is meant to record.

**New**

> The contribution of these particles is to the tone of a sentence rather than to its factual content. AlAfnan et al. (2025) classify particles as a lexical feature of Manglish that adds emphasis or tone and signals politeness or informality. They also list particles among the features that distinguish Manglish from standard English and standard Malay. The same study identifies the softening of instructions as one function of these particles, giving "Don't disturb la, he's busy" as an example in which the particle makes the instruction less direct. Treffers-Daller et al. (2022) describe the same effect for *lah*, which they report can shift an utterance from a highly assertive tone to a polite request or a friendly encouragement. In both accounts the particle leaves what the sentence states unchanged and alters the attitude the sentence conveys, and that attitude is the property a sentiment label is intended to record.

*Note.* "Pragmatic rather than propositional" was the hardest sentence in the section (Rule 1); it is now said in ordinary words. The two AlAfnan et al. (2025) claims are merged into one sentence so the source is not cited twice in a row (Rule 16). "Describe the effect more precisely" ranked one source above the other for no reason; now "describe the same effect". "How the sentence is to be taken" was informal (Rule 3).

### Paragraph 2.2.3

**Old**

> Two limits on this evidence should be noted, and they run in opposite directions. Treffers-Daller et al. (2022) supply frequencies, but from classroom speech. Their corpus is fifteen hours of recorded teaching by each of two university English lecturers, so the rates should not be read as rates for social media writing. AlAfnan et al. (2025) describe Malaysian usage more broadly, but their data are scripted dialogue from Malaysian television series such as Kopitiam and KL Gangster, examined through qualitative content analysis. That study therefore reports what the particles do and not how often they occur. Neither source establishes a frequency for particle use in Malaysian social media posts, and no such figure is currently available. What both sources do establish is that the construction is regular and that it carries affect.

**New**

> Two limits on this evidence should be noted. Treffers-Daller et al. (2022) supply frequencies, but their corpus is fifteen hours of recorded classroom teaching by each of two university English lecturers. Their frequencies should therefore not be read as frequencies for social media writing. AlAfnan et al. (2025) describe Malaysian usage more broadly, but their data are scripted dialogue from Malaysian television series such as *Kopitiam* and *KL Gangster*, examined through qualitative content analysis. That study therefore reports what the particles do, not how often they occur. Neither source establishes how frequently particles are used in Malaysian social media posts, and no such figure was found among the studies reviewed here. What both sources do establish is that the construction recurs and that it carries affect.

*Note.* "Run in opposite directions" was a metaphor (Rule 8). "No such figure is currently available" was a claim about the whole literature; now bounded to what this review examined (Rule 6). "Regular" is replaced by "recurs", which is what the evidence shows.

### Paragraph 2.2.4

**Old**

> The consequence for annotation is that the particle fixes the tone of a message without fixing its polarity. A reader of "Don't disturb la, he's busy" can see that the particle softens the instruction. Softening is nonetheless compatible with a negative reading, in which the writer is irritated, and with a neutral one, in which the writer is being polite. Treffers-Daller et al. (2022) concede the same point about the category as a whole, observing that the specific meanings of discourse markers are often difficult to capture even where their pragmatic functions can be evaluated. The affective signal is therefore carried by a token whose contribution is real but underdetermined, and two annotators may read it differently while both reading it competently.

**New**

> The consequence for annotation is that the particle indicates the tone of a message but does not determine its polarity. A reader of "Don't disturb la, he's busy" can see that the particle softens the instruction. A softened instruction is nonetheless compatible with a negative reading, in which the writer is irritated, and with a neutral reading, in which the writer is being polite. Treffers-Daller et al. (2022) note the same difficulty for discourse markers as a whole, observing that their specific meanings are often difficult to capture even where their pragmatic functions can be evaluated. The particle therefore carries affect without indicating which polarity that affect has, and two annotators may read it differently while both reading it competently.

*Note.* "Fixes the tone" and "a token whose contribution is real but underdetermined" are stated literally (Rules 1, 8). "Concede" implied reluctance the source does not show; now "note" (Rule 9).

### Paragraph 2.2.5

**Old**

> Disagreement of this type is not removed by adding annotators. Pavlick and Kwiatkowski (2019) show that where a task admits more than one defensible reading, disagreement between annotators is reproducible and persists as further ratings are collected, rather than resolving toward a single label. A corpus built by majority vote over such items therefore records the majority reading as though it were the only defensible one. The variation it conceals is systematic rather than random. An agreement coefficient computed over these items registers genuine interpretive difference and not annotator error.

**New**

> Disagreement of this kind is not necessarily reduced by adding annotators. Pavlick and Kwiatkowski (2019) find that where an item admits more than one defensible reading, disagreement between annotators is reproducible and persists as further judgements are collected, rather than converging on a single label. A corpus built by majority vote over such items therefore records the majority reading as though it were the only defensible one, and the variation it conceals is systematic rather than random. An agreement coefficient computed over such items reflects genuine differences in interpretation rather than annotator error alone.

*Note.* The first and last sentences were absolute ("is not removed", "and not annotator error"); both are now hedged the way he hedges (Rule 6). "Show" becomes "find" (R1 13).

### Paragraph 2.2.6

**Old**

> The first property examined in this section produces disagreement about which part of a message to judge. The second produces disagreement about how to judge a part whose reading is genuinely open.

**New**

> The first property examined in this section produces disagreement about which part of a message to judge. The second produces disagreement about how to judge that part once it has been found, because more than one reading of it is defensible.

*Note.* "Whose reading is genuinely open" is said plainly.

---

### 2.3 Phonetic spelling multiplies the surface forms of a single word

### Paragraph 2.3.1

**Old**

> The first two properties concern where the sentiment is and how it is to be read. The third concerns whether the words carrying it can be recognised at all. Malaysian users spell phonetically rather than to a dictionary standard, so a single word appears in many written forms. Maskat and Rahman (2020) provide a formal categorisation of this variation for Malay. Working from a corpus of 6,241 Twitter posts collected between 2014 and 2018, they sort what they call Social Media Malay Language into five categories. The five are spelling variants, Malay-English mixed sentences, loan words written with Malay phonology, slang-based spellings, and vowel-less words.

**New**

> The first two properties concern where the sentiment in a message is located and how it should be read. The third concerns whether the words that carry it can be recognised at all. Maskat and Rahman (2020) document Malay social media users spelling words as they are pronounced rather than as a dictionary lists them, so that a single word can appear in many written forms. Working from a corpus of 6,241 Twitter posts collected between 2014 and 2018, they sort what they call Social Media Malay Language into five categories: spelling variants, Malay-English mixed sentences, loan words spelled according to Malay pronunciation, slang-based spellings, and vowel-less words.

*Note.* "Malaysian users spell phonetically" was a claim about all Malaysian users with no citation on the sentence, the same defect as R4 24; it is now attributed to the study that documents it (Rules 2, 6). "Written with Malay phonology" is said plainly. The five categories are listed in the same sentence that announces them (Rule 10).

### Paragraph 2.3.2

**Old**

> The variation within each category is wide. Among the spelling variants Maskat and Rahman (2020) record, macam mana appears as mcmana, camne, camner, mcmner and cane. The vowel-less category reduces a word to consonants or to a single character, so jangan is written jgn and pada is written pd. The slang category adds a regional layer, with besar written besaq in the north and beso on the east coast. The categories also combine, and the same study gives x suko as a form drawing on the slang and vowel-less categories at once.

**New**

> Each category contains many forms. Among the spelling variants that Maskat and Rahman (2020) record, *macam mana* appears as *mcmana*, *camne*, *camner*, *mcmner* and *cane*. In the vowel-less category a word is reduced to its consonants or to a single character, so *jangan* is written *jgn* and *pada* is written *pd*. The slang category varies by region, with *besar* written *besaq* in the north and *beso* on the east coast. The categories can also combine, and the same study gives *x suko* as a form that belongs to the slang and vowel-less categories at once.

*Note.* "Wide" was an undefined evaluative adjective (Rule 18). "Adds a regional layer" was a metaphor (Rule 8).

### Paragraph 2.3.3

**Old**

> Whether this variation can be undone automatically is the question that matters for annotation, and Maskat and Rahman (2020) tested it directly. They attempted to normalise two of the five categories, spelling variants and vowel-less words, using n-gram similarity indices and Levenshtein distance. Their benchmark was a ground truth of 1,176 similar-word pairs covering 435 unique words, identified by hand by a native Malay speaker. Measured against that benchmark, the highest precision reported for any configuration is 0.43, and most configurations fall well below it. The authors conclude that similarity matching can detect the two categories but that a more sophisticated technique is needed, and they state that normalisation of the remaining three categories is open for future research.

**New**

> The question that matters for annotation is whether this variation can be reversed automatically, and Maskat and Rahman (2020) tested this directly. They attempted to normalise two of the five categories, spelling variants and vowel-less words, meaning that they tried to map each non-standard form automatically to its standard spelling. The methods used were two measures of string similarity, n-gram similarity and Levenshtein distance, each of which scores how closely two spellings resemble one another. The benchmark was a set of 1,176 pairs of similar words covering 435 distinct words, identified by hand by a native Malay speaker. Precision here is the proportion of the matches proposed by a method that were correct. On that benchmark, the highest precision reported for any configuration was 0.43, and most of the configurations reported were lower than that. The authors conclude that similarity matching can detect the two categories but that a more sophisticated technique is needed, and they state that normalisation of the remaining three categories is left for future research.

*Note.* "Undone" was informal (Rule 3). *Normalise*, the two similarity measures, and *precision* are each defined at first use (Rule 5). "Fall well below" is replaced by what the paper reports.

### Paragraph 2.3.4

**Old**

> Two limits on this evidence should be noted. Only Selangor slang was handled, so the slang category is represented more narrowly than the regional range the same paper describes. More consequentially for this review, English words were removed before the experiment and code-mixed posts were excluded from the evaluation subsets. The reported precision is therefore a measurement on Malay text with the English stripped out, not on Malay-English mixed text, and no equivalent measurement for the mixed case is available.

**New**

> Two limits on this evidence should be noted. Only slang from Selangor was handled, so the slang category was tested more narrowly than the regional range the same paper describes. More importantly for this review, English words were removed before the experiment and code-mixed posts were excluded from the evaluation subsets. The reported precision is therefore a measurement on Malay text with the English removed, not on Malay-English mixed text, and no equivalent measurement for mixed text was found among the studies reviewed here.

*Note.* "Stripped out" was informal (Rule 3). "Is available" was a claim about the whole literature; now bounded to the studies reviewed (Rule 6).

### Paragraph 2.3.5

**Old**

> The consequence for annotation is an asymmetry between the two types of annotator, and it is visible inside the study just described. A single native speaker recovered 1,176 word pairs by hand, reliably enough for the result to serve as ground truth. Automated matching against that same ground truth reached a highest precision of 0.43. A human reader recovers x as tidak without effort. The automatic procedure largely does not. The two types of annotator therefore do not fail on the same inputs, and they do not fail at the same rate.

**New**

> The consequence for annotation is that human and automatic annotators differ in what they can recognise, and the difference can be seen in the study just described. A single native speaker identified 1,176 word pairs by hand, reliably enough for the result to serve as the ground truth. Automatic matching on the same ground truth reached a highest precision of 0.43. A human reader recognises *x* as *tidak*; the automatic procedure largely did not. The two types of annotator therefore make errors on different inputs and at different rates.

*Note.* "An asymmetry" is named as what it is (Rule 4). "Visible inside the study" was a metaphor (Rule 8). "Fail" is the word he called too strong at R1 40; now "make errors" (Rule 6). "Without effort" was an unsupported claim and is dropped.

### Paragraph 2.3.6

**Old**

> That asymmetry changes what the choice of annotator is. If human and automatic annotation differed only in cost and speed, the choice would be a matter of budget. Because they fail on different inputs, the choice determines which errors a corpus will contain, and a corpus labelled entirely by one type carries that type's systematic weakness throughout.

**New**

> This difference changes what the choice of annotator means. If human and automatic annotation differed only in cost and speed, the choice between them would be a matter of budget. Because they make errors on different inputs, the choice also determines which errors a corpus will contain, and a corpus labelled entirely by one type of annotator carries that type's systematic errors throughout.

*Note.* "That asymmetry" and "fail" as above. "One type" is completed to "one type of annotator" (Rule 4).

### Paragraph 2.3.7 (section close)

**Old**

> The three properties examined in this section therefore place three distinct demands on annotation. The first makes the opinion-bearing span difficult to locate. The second leaves its reading underdetermined once located. The third makes the tokens themselves unrecoverable to an automatic annotator while they remain transparent to a human one. Section 3 examines the annotation strategies used in response, and the trade-offs each one accepts.

**New**

> The three properties examined in this section therefore create three separate difficulties for annotation. The first makes the part of the message that carries the opinion difficult to locate. The second leaves the reading of that part open once it has been located. The third makes the words themselves difficult for an automatic annotator to recognise, while a human annotator recognises them readily. Section 3 examines the annotation strategies that have been used in response to these difficulties, and the trade-off each strategy accepts.

*Note.* "Underdetermined", "unrecoverable" and "transparent" are replaced by ordinary words (Rule 1). "Opinion-bearing span" and "tokens" give way to the terms used throughout the section (Rule 19).

---

## Terms now used consistently across Section 2

| Concept | One term |
|---|---|
| The words in a message that express the opinion | *the part of the message that carries the opinion* (or *the sentiment*) |
| The emotional attitude a message expresses | *affect* (defined in 2.0) |
| The two kinds of annotator | *human annotator* / *automatic annotator* |
| Errors made by an annotator | *errors* (never *fail*) |
| Spelling categories | the five names from Maskat and Rahman (2020) |

## What this rewrite does not do

- No figure, percentage, example or citation has been added or removed, with one exception: the uncited claim "largely mechanical" (2.1.3) and the uncited "without effort" (2.3.5) are dropped rather than propped up.
- Subsection headings are unchanged unless you take the optional suggestion under 2.1.
- Word count moves from about 1,816 to about 1,980. Directness costs words, as the tracker notes; nothing has been compressed.
