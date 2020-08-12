# Word Embedding

This folder contains a general code for each of the models (which are trained with general corpus like Wikipedia data), examples of how to apply each of the three methods to train your own word embeddings. 

There are three ways for training word embedding: Word2Vec, GloVe and fastText (all methods provide pretrained models). 

# What is Word Embedding?
Word embedding is a technique to map words of phrases from a vocabulary to vectors or real numbers. The learned vector representtions of words capture syntactic and semantic word relationships. 

The objective is to have words with similar context occupy close spatial positions.  

# Models

| Model  | Description | Method | Comments|
|--------|-------------|--------|---------|
|Word2Vec|Model provided by Google and is trained on Google News data. This model has 300 dimensions and is trained on 3 million words from google news data (Released in 2013).| Neural Networks: They use a skip-gram and Common Bag Of Words (CBOW: takes the context of each word as the input and tries to predict the word corresponding to the context).| Skip Gram works well with small amount of data and rerpresent rare words well. CBOW works faster and has better representations for more frequent words. |
|GloVe| Global Vectors for word representation is provided by Stanford, they provide models with different dimensions (25, 50, 100, 200 to 300) based on 2, 6, 42, 840 billions tokens| The GloVe model is trained on the non-zero entries of a global word-word co-occurrence matrix, which tabulates how frequently words co-occur with one another in a given corpus.| |
|fastText| Model developed by Facebook. They provide 3 models with 300 dimensions each. | Each word is represented as bag of characters n-grams in addition to the word itself.|For example, for the word partial, with n=3, the fastText representation for the character n-grams is <pa, art, rti, tia, ial, al>. <and> are added as boundary symbols to separate the n-grams from the word itself.|

> These pretrained models are trained with general corpus and may note serve well with situations where you have a domain-specific langugage learning. In that case, you should take a random sample of your own data for the training and evaluate in all the data. 

# Summary

| Document  | Description | Model | Language | Data |
|--------|-------------|--------|---------|-------|
| word_embeddings.ipynb |Training process using all models. |Word2Vec<br>GloVe<br>fastText | en | Data obtained from NLTK |
| skipgram_embeddings.ipynb | Example of how to train your own data for a skip gram model (word2vec) | Skip gram | en | |
| visualization_embeddings.ipynb | Embeddings Visualization with T-SNE and PCA | Word2vec | en | Word2vec embeddings obtained from Google page: https://code.google.com/archive/p/word2vec/ |

