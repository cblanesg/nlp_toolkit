# Text Classification



# What is Text Classification?

Classfication is the task of choosing the correct class label for a given input. In multiple class classficiation each instance may be assigned multiple labels; in open class classification, the set of labels is not defined in advance; and in sequence classification, a list of inputs are jointly classified. 

A classifier is called supervised if it is built based on training corpora containing the correct label for each input. Text classification in a supervised learning method, learns and predicts the category or the class of a document given its text content. 

# Document Classification
Document or a pice of text can also be labeled with categories. From the corpora we can build classifiers that will automatically tag new documents with appropriate category labels. 

Steps:
1. Construct a list of documents, labeled with the appropiate category. 
2. Define a feature extractor for documents (those aspects of the data that gives you insights of what is relevant to the classification. Are aspects of the data that the model should pay attention to).
	> For document topic identification you can define a feature for each word (or keyword), indicating whether the document contains that word. The features in a bag-of-words model can be constructed from the most frequent words. 

# Models

## BERT: Bidirectional Encoder Representations from Transformers
Language representation model, open-sources by Google in 2018. BERT is designed to pre- train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. BERT model can be fine- tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task- specific architecture modifications. (Click [here](https://github.com/maragones/ghost_recon/tree/master/BERT) for a more detalied explanaition of BERT )

## Naive Bayes Classification
The goal of this model is to learn the relationships between words and categories. The taining set is used to learn the distributions of words for documents from category k. This distribution is then used to classify each of the documents in the test set. The aim is to infer the probability that document i belongs to category k given a word profile (features). 

The classifier begins by calculating the **prior probability** of each label, which is determined by checking the frequency of each label in the training set. The contribution of each feature is then combined with this prior probability, to arrive at a likelihood estimatefor each label. The label shose likelihood estimate is the highest is then assigned to the input value. Individual features make their contribution to the overall decision by "voting against" labels that don't occur with that feature very often. The likelihood score for each label is reduced by multiplying it by the probability that an input value with that label would have the feature. 

`For example: if the word "run" occurs in 12% of the sport documents, 10% in the murder mystery documents and 2% in the automotive documents, then the likelihood score for sports label will be multipled by 0.12, 0.1 for mystery and 0.02 for automotive label. The overall effect will be to reduce the score for the murder mystery document slighlty more than the score for sports label. `

Assumption: given a documents category, words are generated independently (the assumption is wrong because the use of word is highly correlated with any data set). Even that the features are not independent, it has proven to ba a useful classifier for a diverse set of tasks.


# Summary

| Document  | Cateory | Description                   | Model | Language | Data |
|-----------|---------|-------------------------------|--------|---------|------|
| gender_identification.ipynb | Example | Simple model for classifying names into gender categories (male, female). In this model we create a training set to train a `naive Bayes` classifier. | Naive Bayes Classifier with Known Categories. | en | Data from nltk|
|bert_classification.ipynb | Example | BERT model for Binary Text Classification | BERT model: `Bidirectional Encoder Representations from Transformers`. | en | Yelp Reviews | 
|convert_examples_to_features.py | Function for bert_classification.ipynb example | Function that converts text examples to features  (input for BERT model) | en | | 
|document_classification.ipynb | Example |Simple model of Documet Classification | Naive Bayes Classification | en | Movie Reviews provided by nltk |
