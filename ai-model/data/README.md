---
language:
- en
task_categories:
- text2text-generation
---

# WikiLarge

<!-- Provide a quick summary of the dataset. -->

HuggingFace implementation of the WikiLarge corpus for sentence simplification gathered by Zhang, Xingxing and Lapata, Mirella. 

/!\ I am not one of the creators of the dataset, I just needed a HF version of this dataset and uploaded it. I encourage you to read the paper introducing the dataset: [Sentence Simplification with Deep Reinforcement Learning](https://aclanthology.org/D17-1062) (Zhang & Lapata, EMNLP 2017)

<!-- ## Dataset Details

### Dataset Description -->

<!-- Provide a longer summary of what this dataset is. -->



<!-- - **Curated by:** [More Information Needed]
- **Funded by [optional]:** [More Information Needed]
- **Shared by [optional]:** [More Information Needed]
- **Language(s) (NLP):** [More Information Needed]
- **License:** [More Information Needed]

### Dataset Sources [optional] -->

<!-- Provide the basic links for the dataset. -->

<!-- - **Repository:** [More Information Needed]
- **Paper [optional]:** [More Information Needed]
- **Demo [optional]:** [More Information Needed] -->

## Uses

This dataset can be used to train sentence simplification models.

<!-- ### Direct Use -->

<!-- This section describes suitable use cases for the dataset. -->

<!-- [More Information Needed]

### Out-of-Scope Use -->

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. -->

<!-- [More Information Needed] -->

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->

- **Size of the generated dataset:** 69.3 MB

An example of 'train' looks as follows.
```
{
    'complex': 'Sensing of both the external and internal environments at the cellular level relies on signal transduction . Many disease processes , such as diabetes , heart disease , autoimmunity , and cancer arise from defects in signal transduction pathways , further highlighting the critical importance of signal transduction to biology , as well as medicine .',
    'simple': 'A signal transduction in biology , is a cellular mechanism .'
}
```

<!-- ## Dataset Creation

### Curation Rationale

<!-- Motivation for the creation of this dataset. -->

<!-- [More Information Needed]

### Source Data

<!-- This section describes the source data (e.g. news text and headlines, social media posts, translated sentences, ...). -->

<!-- #### Data Collection and Processing

<!-- This section describes the data collection and processing process such as data selection criteria, filtering and normalization methods, tools and libraries used, etc. -->

<!-- [More Information Needed]

#### Who are the source data producers?

<!-- This section describes the people or systems who originally created the data. It should also include self-reported demographic or identity information for the source data creators if this information is available. -->

<!-- [More Information Needed]

### Annotations [optional]

<!-- If the dataset contains annotations which are not part of the initial data collection, use this section to describe them. -->

<!-- #### Annotation process

<!-- This section describes the annotation process such as annotation tools used in the process, the amount of data annotated, annotation guidelines provided to the annotators, interannotator statistics, annotation validation, etc. -->

<!-- [More Information Needed]

#### Who are the annotators?

<!-- This section describes the people or systems who created the annotations. -->

<!-- [More Information Needed]

#### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->

<!-- [More Information Needed]

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

<!-- [More Information Needed]

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

<!-- Users should be made aware of the risks, biases and limitations of the dataset. More information needed for further recommendations. -->

## Citation

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

```
@InProceedings{D17-1063,
  author = 	"Zhang, Xingxing
		and Lapata, Mirella",
  title = 	"Sentence Simplification with Deep Reinforcement Learning",
  booktitle = 	"Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing",
  year = 	"2017",
  publisher = 	"Association for Computational Linguistics",
  pages = 	"595--605",
  location = 	"Copenhagen, Denmark",
  url = 	"http://aclweb.org/anthology/D17-1063"
}
```

**ACL:**

Xingxing Zhang and Mirella Lapata. 2017. Sentence Simplification with Deep Reinforcement Learning. In Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing, pages 584–594, Copenhagen, Denmark. Association for Computational Linguistics.

<!-- ## Glossary [optional]

<!-- If relevant, include terms and calculations in this section that can help readers understand the dataset or dataset card. -->

<!-- [More Information Needed]

## More Information [optional]

[More Information Needed]

## Dataset Card Authors [optional]

[More Information Needed]

## Dataset Card Contact

[More Information Needed] -->