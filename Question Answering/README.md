# Question Answering


# What is Question Answering?

Question Answering is a classical NLP task which consists of determining the relevant "answer" (snippet of text out of a provided passage) that answers a user's "question". This task is a subset of Machine Comprehension, or measuring how well a machine comprehends a passage of text. The Stanford Question Answering Dataset (SQuAD) leader board displays the state-of-the-art models in this space. Traditional QA models are variants of Bidirectional Recurrent Neural Networks (BRNN).

The goal is to find the text for any new question and context provided. This is a closed dataset meaning that the answer to a question is always a part of the context and also a continuous span of context.

![image](https://github.com/maragones/ghost_recon/blob/master/Question%20Answering/qa.png)

The problem has two parts:
1. Getting the sentence having the right answer
2. Once the sentence is finalized, getting the corret answer from the sentenece. 

## Methods

**Sentence Embeddings** provides semantic sentence representations. It is trained on natural language inference data and generalizes well to many different tasks. The goal of this method is to create a vocabulary from the training data and use this vocabulary to train infersent model (sentence embedding). Once the model is trained, provide sentence as input to the encoder function which will return a 4096-dimensional vector irrespective of the number of words in the sentence.
