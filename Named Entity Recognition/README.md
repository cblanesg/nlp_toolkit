# Named Entity Recognition
These repo contains examples and best practices for building Named Entity Recognition (NER) models. The models can be used in a variety of applications, such as information extraction and filtering. It also plays an important role in other NLP tasks like question answering and text summarization. 

# What is NER?

Named Entity Recognition is the task of detecting and classifying real-world objects mentioned in text. Common named entities include person names, locations, organizations, etc. The goal of NER system is to identify all textual mentions of the named entities. 


# Models

## Dictionary Methods
The most simple task is from a dictionaryb method. For example, a Geographical Dictionay which includes all locations. A major source of difficulty is caused by the fact that many named entities terms can be incorrectly matched. 

`For example: "KEEP UP ON YOU READING WITH AUDIO BOOKS". 
	The Geographical Dictionary contains a city named On in Vietnam and a city named Reading in UK. So, the dictionary method would incorrectly find locations like On and Readin`

This major source of difficulty is caused by the fact that many named entity terms are ambiguous and one entity can have many meanings depending on the text context. 

NER usually involves assigning an entity label to each word in a sentence as shown un the figure below:

![image](https://github.com/maragones/ghost_recon/blob/master/Named%20Entity%20Recognition/ner.png)

## BERT
BERT (Bidirectional Encoder Representations from Transformers) is a method of pre-training languahe representations which obtains state-of-the-art results on a wide array of NLP taks (like NER). 

The input data for BERT model is a list of tokens representing a sentence. In the training data, each token has a entity label. After the fine tuning, the model predicts an entity label for each token in a given testing sentence. 


## Elmo for NER

ELMO understands both the meaning of the words and the context in which they are found, as opposed to GLOVE embeddings, which only capture the meaning of the words, and are unaware of the context. ELMO assigns embeddings to words based on the contexts in which they are used — to both capture the word meaning in that context as well as to fetch other contextual information. Instead of using a fixed embedding for each word like in GLOVE, ELMo looks at the entire sentence before assigning each word an embedding. It uses a bi-directional LSTM trained on specific tasks to create those word embeddings.

![image](https://github.com/maragones/ghost_recon/blob/master/Named%20Entity%20Recognition/elmo.png)

# Summary

| Document  | Cateory | Description | Model | Language | Data |
|-----------|---------|-------------|--------|---------|------|
