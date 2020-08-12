# Sentence Similarity

# What is Sentence Similarity

Sentence similarity or semantic textual similarity is a measure of how similar two pieces of text are, or to what degree they express the same meaning. Related tasks include paraphrase or duplicate identification, search, and matching applications. The common methods used for text similarity range from simple word-vector dot products to pairwise classification, and more recently, **deep neural networks**.

Sentence Similarity is calculated by the following steps.
1. Obtain embeddings of the sentences
2. Taking the cosine similarity between them (as the following figure)

![sentence_sim](https://github.com/maragones/ghost_recon/blob/master/Sentence%20Similarity/sentence_sim.png)


# Methods

There are different baselines to obtain the semantic similarity between a pair of sentences:
1. `Cosine Similarity`: The most common method and easiest way of estimating the semantic similarity between a pair of sentences is by taking the average of the word embeddings of all words in the two sentences, and calculating the cosine between the resulting embedding. 
2. `Word Mover's Distance`: uses the word embeddings of the words in two texts to measure the minimum distance that the words in one text need to “travel” in semantic space to reach the words in the other text.
3. `Smooth Inverse Frequence`: Taking the average of the word embedding in a senetence tends to give too much weight to word that are quite relevant, semantically speaking. This method tries to solve this problem by weighting the average of the word embeddings in the sentence by a parameter that estimates the frequency of the word in a reference corpus. The second step is to compute a principal component of the resulting embeddings for a set of sentences. It then subtracts from these sentence embeddings their projections on their first principal component. This should remove variation related to frequency and syntax that is less relevant semantically.  
4. `Pre-trained encoder`: Unlike the other methods, Pre- trained encoder does not consider a bag-of-word method (do not consider the word order into account) and is not trained in a unsupervised manner. In some cases word order often goes with differences in meaning like:
    `the dog btes the man` VS `the man bites the dog`
    In this method, the sentence embedding is sensitive to variation. Additionally, supervised training can help sentence embeddings learn the maning of a sentence more directly. 
    The best pre- trained encoders are: **InferSent** (developed by Facebook) and **Google Sentence Encoder**.  
5. BERT: Bidirectional Encoder Representations from Transformers. (You can check a more detailed explanaition [here](https://github.com/maragones/ghost_recon/tree/master/BERT)). 


# Content

|Document     | Category|      Description      | Data   | Language|
|-------------|---------|-----------------------|--------|---------|
|sentence_sim.ipynb | Example | In this notebook we compare the results of Cosine Similarity and a Pre trained encoder Methods in a Sentence Similarity task | Handcrafted sample data, and GloVe pre- trained data set (obtained from: https://www.kaggle.com/watts2/glove6b50dtxt#glove.6B.50d.txt) | en |
