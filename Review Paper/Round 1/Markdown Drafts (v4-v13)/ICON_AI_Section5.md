# 5. Models as Annotation Instruments

Section 4 established that the choice of annotator determines which errors a corpus will contain. This section
asks where each family of model breaks down when used as an annotator. The question is not which architecture
classifies best, which belongs to the comparative benchmarking placed outside the scope in Section 1. It is
what each family cannot read, because that limitation is inherited by every corpus it labels.

Fine-tuned multilingual encoders acquire their competence from exposure. Manukonda and Kodali (2025)
illustrate the mechanism. They fine-tuned XLM-RoBERTa using masked language modelling over original, fully
transliterated and partially transliterated versions of the same text, and report a macro F1 of 0.90 on the
shared-task test set. The model handled the variant spellings because it had been shown them in training. A
corollary follows from the method rather than from any claim the authors make. An encoder resolves the
variation it has been trained on, so the coverage of a fine-tuned annotator is bounded by the coverage of its
fine-tuning data. Extending that coverage requires more annotated or transliterated regional data, which is
the resource whose scarcity motivated automated annotation in the first place. Two limits should be noted: the
study is a shared-task system description rather than a full investigation, and the task is fake news
detection in Malayalam rather than sentiment analysis in Malay. What transfers is the mechanism, not the
result.

Generative models locate their competence differently. Because they are not restricted to a task-specific
vocabulary, they can in principle interpret an unfamiliar spelling or an unseen slang term from context. This
is the capability the encoder lacks, and it is why generative annotation is attractive for a variety that
changes faster than its resources. The competence is distributed unevenly across languages, and not in the way
resource volume alone would predict. Jadhav et al. (2025) found frontier models trailing a fine-tuned BERT
baseline by 10.2% and 14.1% accuracy when annotating Marathi. Adilazuarda et al. (2022) tested Indonesian
code-mixed with four embedded languages, namely English, Sundanese, Javanese and Malay, and found robustness
to English mixing lower than robustness to Javanese and Malay mixing across all models tested. They attribute
the difference to the composition of the pre-training corpus. The direction is worth stating plainly. The
embedded language best represented in pre-training was the one the models handled least robustly. Robustness
to code-mixing therefore does not follow directly from how much of a language a model has seen.

The operative point is not the relative standing of the two families but the shape of their respective
limitations. The encoder is reliable on what it has been shown and blind to what it has not. The generative
model reasons about the unfamiliar, but its robustness on a given language pair cannot be predicted from the
volume of data behind either language. Selecting an annotator is therefore not selecting a level of quality.
It is selecting a failure mode, and the labels a corpus contains carry the signature of whichever mode was
selected.

---
---

# Part A — One error in the v3 material, and it was pointing the wrong way

## Adilazuarda et al. (2022) says the opposite of what the draft claimed

The v3 draft:

> "Examining Indonesian code-mixed with four embedded languages, Adilazuarda et al. found mixing with
> **English handled markedly better** than mixing with the local languages, Malay among them, and attributed
> the gap to pre-training corpus bias."

What the paper actually says, verbatim:

> "We also observe that **the robustness on English language are generally lower than Javanese and Malay in
> all models.** We conjecture that this is due to the bias from the pre-training corpus, since pre-training
> corpus is gathered from online platforms, and Indonesian-English code-mixing is particularly common in
> such platforms."

Robustness is measured as delta accuracy: important words are translated into the embedded language to
create synthetic code-mixed text, and the drop from the monolingual baseline is recorded. Lower robustness
on English means models degraded **more** when English was mixed in, not less. The draft had the direction
reversed.

**The correction improves the argument.** The draft's punchline was "generative reasoning is strongest where
it is least needed" — neat, but built on a reading the source contradicts. What the paper actually shows is
more useful to this review: the embedded language with by far the most pre-training data was the one the
models handled *least* robustly. So robustness to code-mixing does not follow directly from how much of a
language a model has seen, which weakens the architectural fix more sharply than the original claim did.

**This also required a fix in the Introduction**, which said Adilazuarda et al. "show that robustness depends
on how well each language is represented during pre-training". That phrasing implies more representation
gives better robustness, which is what the paper found not to hold. It now reads: "robustness to code-mixing
varies with the embedded language and with the composition of the pre-training corpus." Accurate, and it
still supports the architectural framing it sits in.

---

# Part B — What was verified

| Claim | Source | Verified |
|---|---|---|
| Fine-tuned XLM-RoBERTa with MLM over original, fully transliterated and partially transliterated text | Manukonda and Kodali (2025) | ✅ abstract, verbatim |
| Macro F1 0.90 on the test set | Manukonda and Kodali (2025), Table 2 | ✅ |
| Shared-task system paper, not a full study | DravidianLangTech@NAACL 2025 Task 1; published in the Fifth Workshop on Speech, Vision, and Language Technologies for Dravidian Languages, pp. 176–181 | ✅ peer-reviewed ACL workshop |
| Language is Malayalam | Their released model is `MalayalamXLM_Roberta` | ✅ |
| Four embedded languages: English, Sundanese, Javanese, Malay | Adilazuarda et al. (2022) | ✅ |
| Robustness on English lower than on Javanese and Malay, in all models | Adilazuarda et al. (2022) | ✅ verbatim — see Part A |
| Attributed to pre-training corpus composition | Adilazuarda et al. (2022) | ✅ verbatim |
| GPT-4o −10.2%, Llama 3.1 405B −14.1% vs fine-tuned BERT on Marathi | Jadhav et al. (2025) | ✅ verified for Section 4 |

**Note on Manukonda and Kodali.** It is a shared-task system description, which is a weaker evidence class
than a full study, and the task is fake news detection rather than sentiment analysis. Section 5 states both
limits in the body and uses the paper only for the mechanism, not for the result. If Dr. Ho pushes on why a
Malayalam fake-news system appears in a Malay sentiment review, that sentence is the answer.

---

# Part C — New reference

One added. Sections 1 to 5 now cite **36 sources**, all peer-reviewed.

Manukonda, D. P., and Kodali, R. G. (2025). byteSizedLLM@DravidianLangTech 2025: Fake news detection in Dravidian languages using transliteration-aware XLM-RoBERTa and transformer encoder-decoder. *Proceedings of the Fifth Workshop on Speech, Vision, and Language Technologies for Dravidian Languages*, 176–181.

---

# Part D — Page budget

Section 5 came in at **500 words, 0.93 pages**, against the 0.90 suggested. On target.

| Component | Pages |
|---|---|
| Title, abstract | 1.00 |
| 1 Introduction | 3.01 |
| 2 Review Methodology | 0.60 |
| 3 and subsections | 3.44 |
| 4 and subsections, incl. 2 tables | 4.11 |
| 5 Models as Annotation Instruments | 0.93 |
| **Committed** | **13.09** |
| References, 45 entries at 8pt | 1.73 |
| **Left for Sections 6, 7 and 8** | **5.18** |

My earlier suggested split for the remainder was 1.20 + 3.30 + 0.70 = 5.20. That lands within 0.02 pages of
what is actually left, so the plan holds without further compression.

**Section 7 now has four open questions handed to it**, one more than when Section 4 was written:

1. The independence premise behind consensus voting is asserted, not measured on this material (4.3).
2. No peer-reviewed study adjudicates annotator disagreement on Malaysian code-mixed data (4.3).
3. No frequency measurement exists for particle use or phonetic spelling in Malaysian social media (3.2, 3.3).
4. Robustness to code-mixing is not predicted by pre-training volume, and nothing in the reviewed literature
   establishes what does predict it (5).

The fourth is new, and it comes directly from the Adilazuarda correction.
