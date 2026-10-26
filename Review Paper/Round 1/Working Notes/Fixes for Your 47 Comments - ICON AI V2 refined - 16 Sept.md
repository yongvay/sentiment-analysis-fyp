# Fixes for Your 47 Comments — ICON AI NYV V2 (refined) – Copy

**File checked:** `ICON AI NYV V2 refined - Copy.pdf` (your comments L1–L47)
**Sources checked:** your PDFs in `References/`, plus Joshi 2020, Conneau 2020, Bowman and Dahl 2021, Maskat 2024, Vilares 2017 and Selvaraju 2024 online.

How to use this file:
- **Find** = the text in your paper now.
- **Replace with** = new text. You can copy and paste it.
- **Source** = what the paper really says, so you can answer Dr Ho if he asks.

---

## Part A — Five things to know first

1. **Two sources do not support your sentences. Please change them.**
   - **Selvaraju et al. (2024)** (L15). Its abstract never talks about a shortage of resources. It talks about gaps in *models*. Replace it with Maskat et al. (2024), then delete Selvaraju from the reference list.
   - **Winata et al. (2023)** (L2). I could not find "lower performance on code-switched text" in it. Doğruöz et al. (2021) says this clearly. Remove Winata 2023 from that sentence and from the reference list.
2. **Treffers-Daller et al. did not "find" the *lah* point** (L26). They repeat a claim from Tay et al. (2016), and they use the verb "suggest". Use the secondary citation below.
3. **Pavlick and Kwiatkowski** (L34). Dr Ho suggested "did not eliminate". The paper says something stronger: more context made disagreement **increase**. "Did not eliminate" would understate the finding.
4. **Vilares et al. (2017) is in your reference list but is no longer cited in the text.** Either cite it again or delete the entry.
5. **Citation style (Dr Ho #8) is still open.** The template says: *"References should be numbered and cited within the square brackets in order of appearance in the text."* Your paper still uses (Author, year). This touches every citation, so do it last, after all text changes. I can do this for you.

---

## Part B — Your comments, one by one

### Page 1–2 (Introduction)

#### L1 — "Only if this is cited by Joshi"
**Result: partly supported.** Joshi et al. say resources sit with a few high-resource languages: *"only a very small number of the over 7000 languages of the world are represented in the rapidly evolving language technologies."* They never talk about single-language vs mixed text. They never use the words "code-switching" or "code-mixing". So split the claim across two sources.

**Find:**
> However, many language resources and NLP models are developed primarily for individual languages (Joshi et al., 2020).

**Replace with:**
> However, language resources and NLP systems are concentrated on a small number of high-resource languages (Joshi et al., 2020), and many language models are trained mainly on monolingual data (Doğruöz et al., 2021).

Doğruöz (Section 7): *"these LMs are either trained primarily on monolingual datasets such as Wikipedia in the case of mBERT, or Common Crawl in the case of XLM-R."*

#### L2 — "Only if this is cited by references"
**Result:**
- The "Consequently…" sentence has **no source**. Its old citation (Vilares) does not explain the reason words are missed, so delete that sentence.
- "Can be lower" **is supported** by Doğruöz (Section 7): *"the performance on C-S is much worse than the performance on the same tasks in a monolingual setting."*
- Winata 2023: not found (see Part A).

**Find:**
> …not represented or adequately learned. Consequently, the sentiment polarity conveyed by those words may be underrepresented in the prediction, increasing the likelihood of an incorrect sentiment label. As a result, the performance on code-switched text can be lower than the performance on the same tasks in a monolingual setting (Doğruöz et al., 2021; Winata et al., 2023).

**Replace with:**
> …not represented or adequately learned. As a result, performance on code-switched text can be lower than performance on the same tasks in a monolingual setting (Doğruöz et al., 2021).

Then remove Winata et al. (2023) from the reference list. Also decide about Vilares (Part A, item 4).

#### L3 — "Both types" / transition is not smooth
**Why it is not smooth:** the paragraph talks about the problem, then suddenly defines terms. Fix: put the definitions in their **own short paragraph**, with a bridge sentence. Also rename "This problem" in the next paragraph, because it is now further away.

**Find:**
> …(Doğruöz et al., 2021). Both sentiment tools and language models are considered in this review. In this review, the term sentiment tool refers to systems that directly assign sentiment labels, such as lexicon-based analysers, and the term language model refers to models pretrained on large amounts of text, which can subsequently be fine-tuned for a downstream task such as sentiment classification.
>
> This problem is particularly relevant in the Malaysian context.

**Replace with (new paragraph after "…(Doğruöz et al., 2021)."):**
> Two terms from this discussion are used throughout the review. In this review, the term *sentiment tool* refers to systems that directly assign sentiment labels, such as lexicon-based analysers. The term *language model* is used specifically for pretrained language models, which are trained on large amounts of text and can then be fine-tuned for a downstream task such as sentiment classification (Devlin et al., 2019).
>
> The difficulty of analysing code-switched text is particularly relevant in the Malaysian context.

#### L4 — Definition of "language model" is too narrow
The new wording above fixes this too. It no longer says *what a language model is*. It says *which kind of language model this review means*. That is a scope choice (what the review covers), so it is not wrong. Devlin et al. (2019) describe the pre-train then fine-tune approach.

#### L5 — "such posts" is vague / L6 — "Hopefully can cite this"
**Result:**
- **"Common in Malaysian social media"** is supported by Kong et al. (2023): *"We note that in the collected tweets, mixing of English and Malay words within a single text was a common phenomenon."*
- **Maskat et al. (2024)** built **one** corpus, not several: 709,012 X posts from 50 Malaysian public figures. Also, not every post is code-switched. Each account needed *"at least 60 percent of the posts be composed in Malay-English codeswitching."*

**Find:**
> Malay-English code-switching is common in Malaysian social media, and corpora of several hundred thousand such posts have been compiled (Maskat et al., 2024).

**Replace with:**
> Malay-English code-switching is common in Malaysian social media (Kong et al., 2023), and a corpus of 709,012 X posts from 50 Malaysian public figures whose posts are mostly Malay-English code-switched has been compiled (Maskat et al., 2024).

Small slip in the same paragraph: "pretrained language model," → "pretrained language models,".

#### L7 — "little or no exposure"
**Result: supported. No change needed.** Doğruöz (Section 7): *"So, they are either not exposed to C-S data at all during training, or they miss out on several language pairs, types and functions of C-S."*

#### L8 — model capacity = number of parameters
**Result:** Conneau et al. do write *"Model capacity (i.e. the number of parameters in the model)"*, so your sentence was faithful to the source. Section 5.1 also says *"degrades performance across all languages"*, but the Introduction says *"overall performance"*. Dr Ho's version is still safer and reads better, so use it.

**Find:**
> Covering more languages also places demand on model capacity, that is the number of parameters in the model (Conneau et al., 2020). At a fixed parameter count, adding more languages initially benefits low-resource languages through positive transfer, but beyond a certain point performance degrades for all languages, an effect Conneau et al. (2020) term the curse of multilinguality.

**Replace with:**
> Covering more languages also places demand on model capacity, particularly when the total number of model parameters is fixed (Conneau et al., 2020). Under this condition, adding more languages initially benefits low-resource languages through positive transfer, but beyond a certain point overall performance begins to degrade, an effect Conneau et al. (2020) term the curse of multilinguality.

#### L9 — "discourage socially biased systems"
**Result: close, but not their words.** Bowman and Dahl, Section 1: *"they should disincentivize the use of systems with potentially harmful biases."* Figure 1: *"Benchmarks should reveal plausibly harmful social biases in systems."* They also write "should", not "must".

**Find:**
> Label quality is therefore only one requirement for reliable evaluation; Bowman and Dahl (2021) argue that a benchmark must also be valid for the task, offer adequate statistical power, and discourage socially biased systems.

**Replace with:**
> Label quality is therefore only one requirement for reliable evaluation. Bowman and Dahl (2021) argue that a benchmark should also be a valid test of the task, offer adequate statistical power, and discourage the use of systems with potentially harmful social biases.

### Page 3 (Introduction, continued)

#### L10 — "standard orthographic conventions"
**Result:** Abu Bakar et al. never say "orthographic". They say: *"Malaysians tend not to fully follow any abbreviations rules when writing on social media."* Use their idea. This also fixes the grammar slip "additional challenge".

**Find:**
> Labelling Manglish presents additional challenge, because annotators must interpret non-standard spellings and abbreviations that do not follow standard orthographic conventions (Abu Bakar et al., 2020), as well as English words respelled according to Malay pronunciation, such as kompem for "confirmed" and hensem for "handsome", which Kasmuri and Basiron (2019) describe as Malayanization words.

**Replace with:**
> Labelling Manglish presents additional challenges. Malaysian social media users tend not to follow standard abbreviation rules, so annotators must interpret non-standard spellings and abbreviations (Abu Bakar et al., 2020). Annotators must also interpret English words respelled according to Malay pronunciation, such as *kompem* for "confirmed" and *hensem* for "handsome", which Kasmuri and Basiron (2019) describe as Malayanization words.

#### L11 — "Malayanization words" exact term?
**Result: yes, exact. No change needed.** Kasmuri and Basiron: *"kompem (confirmed), rumate (roommate), hensem (handsome) and saikosis (psychotic). This paper categorized these words as Malayanization words."*

#### L12, L42, L43 — Table 3 (position and purpose)
Dr Ho made three points:
- Table 3 is far from where Section 1 first mentions it.
- A table must come after its first mention.
- No text discusses Table 3.

Fix all three in three steps.

**Step 1 — Section 1. Remove the mention of Table 3.** The old wording was also not true: SentiBahasaRojak fully meets **none** of the four criteria.

**Find:**
> When evaluated against these criteria, each resource meets some of them but none meets all four, as Table 3 shows.

**Replace with:**
> When evaluated against these criteria, none of the four resources meets all of them.

**Step 2 — Section 5.** After the paragraph that ends "…for the three-class sentiment distinction.", add this new paragraph. Put it **above** Table 3.
> Table 3 checks the four resources against the four criteria adopted in Section 1. A class distribution is treated as dominated when one label covers more than half of the labelled messages. MyCovid-Senti meets three criteria, but its study reports no inter-annotator agreement coefficient. MESocSentiment is the largest resource, but its labels are dominated by the neutral class and were assigned by sentiment tools, so no inter-annotator agreement coefficient is available. MY-EN-CS and SentiBahasaRojak each contain fewer than 2,400 labelled messages, and their agreement evidence covers only a two-category task or a single subset. None of the four resources therefore meets all the criteria adopted by this review for broad-topic sentiment analysis.

(The numbers come from your Table 3: 11,568 / 19,714 / 2,316 / 2,285, and 78.23% neutral.)

**Step 3 — Delete** the old paragraph **below** Table 3:
> Table 3 compares the four resources against the four criteria set out in Section 1. A class distribution is treated as dominated when one label covers more than half of the labelled messages.

#### L13 — "labelled messages" vs "posts"
**Result:** The MESocSentiment paper calls them **tweets**. MY-EN-CS uses **sentences** from blogs. The easiest fix is to say once what "message" means. After that, "posts" for MESocSentiment is simply one kind of message.

**Find (Section 1):**
> …at least 10,000 labelled messages, a class distribution that is not dominated by one label, everyday social-media language, and direct evidence that the labels are reliable.

**Add right after that sentence:**
> A message here means a single labelled social-media text, such as a tweet, a post or a blog sentence.

#### L14 — Artstein and Poesio: multi-π, multi-κ, Krippendorff's α
**Result: supported. No change needed.** Section 2.5: *"A generalization of Scott's π is proposed in Fleiss (1971), and a generalization of Cohen's κ is given in Davies and Fleiss (1982). We will call these coefficients multi-π and multi-κ."* Section 2.6 covers Krippendorff's α.

#### L15 — Selvaraju: "shortage of annotated code-mixed Malay resources"
**Result: NOT supported.** The abstract only says that *"existing sentiment analysis models conventionally cater to monolingual only"*. It says nothing about a lack of data. Maskat et al. (2024) say it directly: *"Datasets on Manglish social media text that are publicly accessible are scarce."*

**Find:**
> Resource availability is another limitation, as Selvaraju et al. (2024) reported a shortage of annotated code-mixed Malay resources.

**Replace with:**
> Resource availability is another limitation, as publicly accessible datasets of Manglish social-media text are scarce (Maskat et al., 2024).

Then **delete Selvaraju et al. (2024)** from the reference list. It is not cited anywhere else.

### Page 4 (Introduction end, Section 2)

#### L16 — "the methods used to assign labels"
Your review covers human annotation **and** automatic tools **and** generative models. So "procedures" (human only) is too narrow. "Approaches" covers all three, and it matches your Section 4 heading.

**Find (Section 1):** "the methods used to assign labels" → **Replace with:** "the approaches used to assign labels"
**Also in Section 7:** "(2) the methods used to assign labels may fail…" → "(2) the approaches used to assign labels may fail…"

#### L17 + L18 — "Reviews … are available elsewhere" / "No new system is proposed."
Use Dr Ho's two suggestions together.

**Find:**
> Reviews of sentiment classifiers and sentiment analysis more broadly are available elsewhere (Poria et al., 2023; Nazir et al., 2022). No new system is proposed.

**Replace with:**
> Existing reviews have examined sentiment classifiers and sentiment analysis more broadly (Poria et al., 2023; Nazir et al., 2022), whereas this review focuses on the annotation and evaluation of Manglish sentiment data rather than proposing a new system.

#### L19 + L20 — first contribution bullet ("as approaches to sentiment labelling" / "evidence")
Section 4.1 does discuss all three as ways to label data, so Dr Ho's addition is true.

About L20: the comment "Use evidence" is unclear, because the sentence already says "evidence". The new wording below keeps "evidence", so nothing else is needed.

**Find:**
> • It compares manual annotation, existing sentiment tools and generative models, focusing on the effort required for labelling and the evidence of label reliability.

**Replace with:**
> • It compares manual annotation, existing sentiment tools and generative models as approaches to sentiment labelling, focusing on the effort they require and the evidence they provide for label reliability.

#### L21 — "affect one another"
Section 6.1 explains the links by reasoning. It does not prove effects in both directions, so use the softer verb.

**Find:**
> • It shows how language difficulties, labelling methods and class imbalance affect one another, and identifies priorities for future research.

**Replace with:**
> • It examines the relationships among linguistic challenges, labelling methods and class imbalance, and identifies priorities for future research.

#### L22 — "methods that could be applied to its annotation" is too broad
Name exactly what counts. Your non-Malaysian sources do three things: they assign labels (Hovy, Mohammad), measure agreement (Cohen, Artstein and Poesio, Byrt, Di Eugenio), or find annotation errors (Weber and Plank, Weber-Genzel).

**Find:**
> (1) examine Malaysian Malay-English text or methods that could be applied to its annotation;

**Replace with:**
> (1) examine Malaysian Malay-English text, or propose or evaluate methods for assigning labels, measuring inter-annotator agreement, or identifying annotation errors;

### Page 5 (Sections 2–3)

#### L23 — "the evidence that the labels themselves are reliable"
**Find:**
> This review focuses on the evidence that the labels themselves are reliable.

**Replace with:**
> This review focuses on the evidence supporting the reliability of the labels themselves.

#### L24 + L25 — citation for "within a single sentence" / add "in Malay-English code-switched text"
Treffers-Daller et al. (abstract) define code-switching as *"the use of lexical items and grammatical features from two languages in one sentence"*. They say Malay-English code-switching *"is widely practiced across formal and informal situations."*

**Find:**
> Malay and English can appear within a single sentence. Treffers-Daller et al. (2022) found frequent switching within clauses in Malaysian classroom speech.

**Replace with:**
> In Malay-English code-switched text, both languages can appear within a single sentence (Treffers-Daller et al., 2022). In their study of Malaysian classroom speech, Treffers-Daller et al. (2022) found frequent switching within clauses.

#### L26 — Does Treffers-Daller really show the *lah* contrast?
**Result: second-hand.** Treffers-Daller et al. write: *"Tay et al. (2016) suggest lah modifies the utterance from one that has a highly assertive tone to a polite request or a friendly encouragement."* So the claim belongs to Tay et al., and the verb is "suggest", not "found".

**Find:**
> Treffers-Daller et al. (2022) found that lah can change an utterance from an assertive tone into a polite request or a friendly encouragement.

**Replace with:**
> Tay et al. (2016, as cited in Treffers-Daller et al., 2022) suggest that *lah* can change an utterance from a highly assertive tone into a polite request or a friendly encouragement.

You do **not** add Tay et al. to the reference list. With a secondary citation, only the source you read (Treffers-Daller) goes in the list.

### Page 6 (Section 4.1)

#### L27 — "subjectivity corpus"
**Result:** this is the authors' own term. Their title is *"Building a Malay-English code-switching subjectivity corpus for sentiment analysis"*. The corpus *"consists of opinionated and factual sentences"* taken from blogs. Keep the term, but say why the study is here: it is an example of manual annotation.

**Find:**
> Kasmuri and Basiron (2019) developed a subjectivity corpus from blogs.

**Replace with:**
> For example, Kasmuri and Basiron (2019) used human annotators to label blog sentences as opinionated or factual when building MY-EN-CS, a subjectivity corpus.

#### L28 — "other languages": name them
**Result:** Romadhona et al., Algorithm 1: the target languages for Malay sentences are English (en) and Chinese (zh). This also fixes a comma splice (two full sentences joined only by a comma).

**Find:**
> …by automatically translating parts of existing Malay sentences into other languages, the resulting code-mixed text was automatically generated…

**Replace with:**
> …by automatically translating parts of existing Malay sentences into English or Chinese, so the resulting code-mixed text was automatically generated…

#### L29 — "Citation needed" (stock-market posts, five experts)
**Result: supported.** Romadhona, Section 3.4.3: *"we crawl posts from Malaysia's financial and stock market websites, such as I3investor, and hired five native Malaysian experts who can read and write in Bahasa Rojak to manually annotate these posts."*

**Find:**
> The stock-market posts were collected and annotated by five experts as positive or negative. The reported inter-annotator agreement was calculated only the stock-market subset.

**Replace with:**
> The stock-market posts were collected from Malaysian financial and stock-market websites and annotated by five experts as positive or negative (Romadhona et al., 2022). The reported inter-annotator agreement was calculated only for the stock-market subset.

(This also adds the missing word "for".)

#### L30 — "If citation can be provided" (tools are quicker)
**Result: supported.** Mohd Shamsuddin et al.: *"the sentiment analysers were leveraged to make sentiment identification faster than manual labelling."*

**Find:**
> Automatic tools can assign labels more quickly.

**Replace with:**
> Sentiment tools can assign labels more quickly than manual annotation (Mohd Shamsuddin et al., 2024).

Two grammar slips in the same subsection:
- "However, manual work time-consuming" → "However, manual work **is** time-consuming"
- "on Malay-English code-switched therefore requires" → "on Malay-English code-switched **text** therefore requires"

### Page 7 (Section 4.2)

#### L31 — weak transition from 4.1 to 4.2
Add one opening sentence that links automatic labelling to a large neutral class.

**Find (start of 4.2):**
> MESocSentiment contains 19,714 posts, of which 78.23% are labelled neutral…

**Replace with:**
> Automatic labelling may produce a large neutral class, because a sentiment tool that does not recognise a sentiment-bearing expression may assign a neutral label. MESocSentiment, which was labelled automatically, contains 19,714 posts, of which 78.23% are labelled neutral…

#### L32 — "other Malaysian data" is vague; citation needed
**Result:** Kong et al. (2023) report 2,728 neutral out of 11,568 tweets, which is 23.6%.

**Find:**
> A neutral share of 78% is high compared with other Malaysian data. In Kong et al. (2023), three annotators labelled a COVID-19 Twitter dataset of which 23.6% of the posts were labelled neutral. The two datasets cover different content, so their class distributions are not directly comparable. It does suggest, however, that the neutral share in MESocSentiment warrants further investigation.

**Replace with:**
> The 78.23% neutral proportion in MESocSentiment is higher than that of the Malaysian COVID-19 Twitter dataset of Kong et al. (2023), in which three annotators labelled 2,728 of 11,568 tweets, or 23.6%, as neutral. The two datasets cover different content, so their class distributions are not directly comparable. The difference nevertheless suggests that the neutral proportion in MESocSentiment warrants further investigation.

#### L33 — include the examples
**Result:** these are Table 7 in Mohd Shamsuddin et al. (*"Samples of false tweets"*). All three were labelled Neutral, and the authors marked them Positive when they checked them by hand. Present them as the original authors' finding, not yours.

**Find:**
> …three contain Malay expressions that appear to convey positive sentiment but were labelled neutral. One of the expressions is memang cantik sangat, meaning really very beautiful.

**Replace with:**
> …three contain Malay expressions that appear to convey positive sentiment but were labelled neutral. The original authors identified these three tweets as incorrectly labelled when they checked them manually. The first describes a village in Penang as *memang cantik sangat*, meaning really very beautiful. The second, *Selamat deepavali buat followers bikers ranger*, wishes followers a happy Deepavali. The third, *Syabda raih gelar juara international series*, reports that an athlete won a championship title.

#### L34 — Pavlick: "did not eliminate" vs "did not reduce"
**Result:** Dr Ho's word would understate the finding. Section 5: *"Both measures of disagreement actually increase when raters see more context."* The authors conclude: *"we do not see evidence that increasing context helps, and it may in fact hurt."*

**Find:**
> …disagreement between raters persisted even when 50 judgements were collected for each item, and additional context did not eliminate the disagreement (Pavlick and Kwiatkowski, 2019).

**Replace with:**
> …disagreement between raters persisted even when 50 judgements were collected for each item (Pavlick and Kwiatkowski, 2019). Providing more context did not reduce this disagreement, and in their experiment disagreement increased as raters were shown more context.

If Dr Ho asks why you did not use "eliminate", show him the quote above.

### Page 8 (Section 4.3, Table 1)

#### L35, L38 — tables must use single spacing (Tables 1, 2, 3)
In Word, for **each** table:
1. Click inside the table. Click the small square with four arrows at the table's top-left corner. This selects the whole table.
2. Go to **Home → Paragraph**. Click the small arrow in the corner of the Paragraph group.
3. Set **Spacing Before = 0 pt**, **After = 0 pt**, **Line spacing = Single**.
4. Click **OK**.

#### L36, L41 — put the source into the caption
The template says captions are **bold, centred, 12 pt, and capitalised like the paper title** (Title Case: main words start with a capital).

**Table 1** — replace the caption and delete the "Source: …" line below the table:
> **Table 1. Neutral Labels in the 19,714 Retained MESocSentiment Posts, Calculated from Mohd Shamsuddin et al. (2024)**

Also change the column heading "Share" → "Proportion". Dr Ho asked you not to use "share".

**Table 3** — replace the caption and delete the "Source: …" line below the table:
> **Table 3. The Four Reviewed Resources Against the Four Criteria, Compiled from Kasmuri and Basiron (2019), Romadhona et al. (2022), Kong et al. (2023) and Mohd Shamsuddin et al. (2024)**

Note: the template itself says *"Sources and notes appear below the table, aligned left."* So Dr Ho's request goes against the template. Follow Dr Ho, because he is your reviewer. If he asks, you can show him this template line.

#### L37 — "Totals" is vague
**Find:**
> The totals also do not reveal whether the tools make mistakes on the same posts.

**Replace with:**
> The label counts in Table 1 also do not reveal whether the tools make errors on the same posts.

Also in this section: **76.24%** should be **76.25%** (15,422 ÷ 20,226 = 0.76248).

### Page 10 (Section 5, after Table 2)

#### L39 + L40 — citation for "defined for two coders" / five annotators
**Result: supported.**
- Cohen (1960) is about *"agreement between two judges"*.
- Artstein and Poesio (Section 2.5): *"Sometimes researchers run reliability studies with more than two coders, measure agreement separately for each pair of coders, and report the average. However, a better practice is to use generalized versions of the coefficients."*
- Romadhona et al. only say *"The kappa value of the Bahasa Rojak stock review dataset is 0.77"*. They never say how it was calculated.

**Find:**
> SentiBahasaRojak also used five annotators; Cohen's kappa in its original form is defined for two coders, studies involving more than two annotators should report how agreement was calculated and specify the coefficient or variant used.

**Replace with:**
> SentiBahasaRojak also used five annotators, but the study does not state how its kappa value was calculated (Romadhona et al., 2022). Cohen's kappa in its original form measures agreement between two annotators (Cohen, 1960). When more than two annotators are involved, agreement can be averaged over pairs of annotators or measured with a generalised coefficient (Artstein and Poesio, 2008). Studies involving more than two annotators should therefore report how agreement was calculated and specify the coefficient or variant used.

### Page 13 (Section 6.3)

#### L44 + L45 + L46 + L47 — Byrt wording, citation needed, "Working this out", "would show"
**Result:**
- **Byrt et al. (abstract):** *"When comparisons are made between agreement studies it can be misleading to report kappa values alone, and it is recommended that researchers also include quantitative indicators of bias and prevalence."* Byrt et al. do not say "hard to compare".
- **Byrt et al.** work with *"a 2 x 2 table of agreement"* and *"the simplest case, of two raters"*.
- **Di Eugenio and Glass:** Byrt et al. *"suggest that intercoder reliability be reported as three numbers: κCo and two adjustments of κCo, one with bias removed, the other with prevalence removed."*
- **Citation for L45:** none of the four resource studies reports bias or prevalence indices, so cite those four studies as the evidence.

**Find (from "Byrt et al. (1993) show…" to the end of 6.3):**
> Byrt et al. (1993) show that a single kappa value is hard to compare across studies, and recommend reporting separate indices for bias and prevalence alongside it. Di Eugenio and Glass (2004) apply this consideration to annotation studies, and suggest report kappa value together with a prevalence-adjusted figure. These approaches were developed for two raters and two categories, so their extension to three-class sentiment has not been examined in the studies reviewed here. Working this out on Manglish data would show whether a low kappa signals weak annotation or only the dominance of the neutral class.

**Replace with:**
> Byrt et al. (1993) note that reporting kappa values alone can be misleading when agreement studies are compared, and recommend that researchers also report indicators of bias and prevalence. Di Eugenio and Glass (2004) discuss this recommendation for discourse and dialogue annotation and suggest reporting kappa together with a bias-adjusted value and a prevalence-adjusted value. These indices were defined for two raters and two categories (Byrt et al., 1993). None of the four Malaysian resource studies reviewed here reports them, so their use with three-class sentiment labels has not been examined in these studies (Kasmuri and Basiron, 2019; Romadhona et al., 2022; Kong et al., 2023; Mohd Shamsuddin et al., 2024). Applying these analyses to three-class Manglish sentiment data could help determine how class distribution affects the interpretation of observed agreement and kappa.

---

## Part C — Small errors I noticed while reading (not in your comments)

| Where | Now | Change to |
|---|---|---|
| 4.2 | "One possible cause of incorrect neutral label" | "…incorrect neutral labels" |
| 4.2 | "A neutral share…", "the neutral share" | "proportion" (Dr Ho: no "share") |
| 5 | Two paragraphs in a row both start "The same issue can arise / arises in sentiment…" | Keep only one of these two sentences |
| 6.1 | "such as lah and meh which signal speaker's attitude and highly context-dependent" | "such as *lah* and *meh*, which signal the speaker's attitude and are highly context-dependent" |
| 6.1 | "The second effect concerns modelling." | "The second implication concerns modelling." |
| 6.1 | "as illustrated by the use of existing sentiment analysers used to label MESocSentiment" | "as illustrated by the sentiment analysers used to label MESocSentiment" |
| 6.2 | "allows researchers assess" | "allows researchers to assess" |
| 6.2 | "reported together alongisde" | "reported alongside" |
| 6.4 | "addressing the linguistic challenges identified in Section 6.1" | "…identified in Section 3" (the challenges are described in Section 3) |
| 6.4 | "Requiring annotators to assign between positive, negative and neutral can conceal an item with multiple plausible interpretations into a single label" | "Requiring annotators to choose between positive, negative and neutral can reduce an item with multiple plausible interpretations to a single label" |
| 6.2–6.5 headings | Mixed capital letters | Use the same style for all (template: Title Case) |
| 7 | "Examples reported in MESocSentiment study" | "Examples reported in the MESocSentiment study" |
| 7 | "it indicates further validation is needed" | "it indicates that further validation is needed" |
| 7 | "examine whether annotators and tools potential annotation errors" | "examine whether annotators and tools share potential annotation errors" |
| Header | "Open International Journal of Informatics (OIJI) Vol. 7 No. 2 (2019)" and "JOURNAL xxxx" | Template leftovers. Check whether ICON AI wants these. |

**Still open from Dr Ho's round 6:**
- **#8** Numbered citations in square brackets. See Part A.
- **#9** The abstract is still about 160 words. He asked for 200–250 words.

---

## Sources checked online

- [Joshi et al. 2020](https://aclanthology.org/2020.acl-main.560.pdf)
- [Conneau et al. 2020](https://aclanthology.org/2020.acl-main.747.pdf)
- [Bowman and Dahl 2021](https://aclanthology.org/2021.naacl-main.385.pdf)
- [Maskat et al. 2024](https://www.sciencedirect.com/science/article/pii/S2352340924000088)
- [Vilares et al. 2017 (author copy)](http://www.grupolys.org/biblioteca/VilAloGom2017a.pdf)
- [Selvaraju et al. 2024 (abstract only)](https://colab.ws/articles/10.1109/aidas63860.2024.10730298)

All other quotes come from the PDFs in your `References/Review Paper` and `References/General` folders.
