# Natural Language Processing Toolkit

The purpose of this repo is to include a set of tools and examples of Natural Language Processing (NLP) models useful for developers. This repo provides various scenarios that the user might encounter and identifies various models that can be used to analyze each one. The optimal model for each scenario is determined based on the user's needs and criteria. 

## Content

The following table is a summary of the most commonly used NLP scenarios covered in the repository. Each scenario is provided with relevant functions and end-to-end examples of each mdoel (demonstrated in Jupyter notebook). 

| Scenario                              |  Models | Description|Languages|
|-------------------------|  ------------------- |-------|---|
|Embeddings | - Word2Vec <br>- fastText<br>- Glove<br>- Doc2Vec| Embedding is the process of converting a word or a piece of text to a continuous vector space of real number, usually, in low dimension. The objective is to **capture context of a word in a document** | English, Spanish|
|Sentiment Analysis | - Aspect Based Sentiment Analysis <br> - Dictionary Methods <br> - VADER| . Sentiment Analysis tries to identify and extract opinions within a given text. Most of the models use the relative frequency of key words to measure the presence of each category (positive, negative, neutral) in texts. | English, Spanish |
|Text Classification| - Naive Bayes Classification<br> - BERT | Text classification is a supervised learning method of learning and predicting the category or the class of a document given its text content.| English |
| Named Entity Recognition | - BERT | Named entity recognition (NER) is the task of classifying words or key phrases of a text into predefined entities of interest. | English |
| Sentence Similarity | - BERT<br>-  GenSen | Sentence similarity is the process of computing a similarity score given a pair of text documents. | English| 
| Textual Entailment (Natural Language Inference) | - BERT<br>- RoBERTa | Textual entailment is the task of classifying the binary relation between two natural-language texts, text and hypothesis, to determine if the text agrees with the hypothesis or not.| English|
| Question Answering |- BERT | Question answering (QA) is the task of retrieving or generating a valid answer for a given query in natural language, provided with a passage related to the query. | English |
| Sentence Similarity |-BERT | Sentence similarity is the process of computing a similarity score given a pair of text documents. | English | 
| Conversational Interfaces (chatbots)| |  | | 
| Syntactic Similarity | - Smith Waterman Algorithm | Capture the syntactic similarity between texts. | English | 

### Text Processing

Almost all scenarios need a pre-processing step, which consists in the following steps:
1. Remove punctuation and non-alphabetical character.
2. Remove words which appear in less than 1% of the vocabulary and more than 99% of the corpus (depending on the scenario).
2. Apply lowercase to the text. 
3. Tokenize
4. Steeming. 
5. Remove stopwords. 


|Section | Description | Method | Language | 
|-------------------| ------------------- |-------------|-------------|
| pre_process.py | Functions to pre process text: remove punctuation, lowercase, tokens, steeming and stopwords | | English and Spanish |



