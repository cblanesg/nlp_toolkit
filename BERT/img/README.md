# BERT
The purpose of this folder is to explain the general model of BERT and how to adapt the model for different language tasks.  

# What is BERT?
BERT `(Bidirectional Encoder Representations from Transformers)` is designed to pre- train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layer. As a result, the pre-trained BERT model can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks:
1. [Question Answering](https://github.com/maragones/ghost_recon/tree/master/Question%20Answering)
2. [Named Entity Recognition](https://github.com/maragones/ghost_recon/tree/master/Named%20Entity%20Recognition)
3. [Text Classification](https://github.com/maragones/ghost_recon/blob/master/Text%20Classification/bert_classification.ipynb)
4. [Entailment](https://github.com/maragones/ghost_recon/tree/master/Entailment)

In contrast to previous models which looked at a text sequence either from left to right or combined left-to-right and right-to-left training. BERT shows that a language model which is bidirectionally trained can have a deeper sense of langugage context and flow than single-direction language models. BERT uses a technique named **Masked LM (MLM)**, which allows bidirectional training models. 
> Masked LM (MLM): Randomly masks words in the sentence and then it tries to predict them. Masking means that the model looks in both directions and it uses the full context of the sentence, both left and right surroundings, in order to predict the masked word. Unlike the previous language models, it takes both the previous and next tokens into account at the same time.

Unidirectional means that each word is only contextualized using the words to its left (or right). For example, in the sentence `I made a bank deposit` the unidirectional representation of bank is only based on `I made a` but not `deposit`. Some previous work does combine the representations from separate left-context and right-context models, but only in a "shallow" manner. BERT represents "bank" using both its left and right context — `I made a ... deposit` — starting from the very bottom of a deep neural network, so it is deeply bidirectional.


## How does it work? 

BERT relies on a Transformer (the attention mechanism that learns contextual relationships between words in a text). The Transformer includes two mechanisms:
1. Encoder: reads the text input. 
2. Decoder: produces a prediction for the task. 

The input to the encoder for BERT is a sequence of tokens, which are first converted into vectors and then processed in the neural network. When training language models, the main challenge is defining a prediction goal (many models predicts the next word in a sequence). The main problem of this approach is the limitation of context learning. BERT uses to strategies to overcome this challenge: **Masked LM** and **Next Sentence Prediction (NSP)

### Masked LM

As mentioned before, 15% of the words in each sequence (a sequence can be each sentence) are replaced with a `MASK` token. The purpose of the model is to predicr the original value of the masked words, based in the context provided by the non-masked words. The steps of the prediction are the following:
1. Add a classification layer on topof the encoder output
2. Multiply the output vectors by the embedding matrix (transforming them into the vocab dimension)
3. Calculate the probability of each word in the vocabulary with softmax. 

![image](https://github.com/maragones/ghost_recon/blob/master/BERT/masked.png)


### Next Sentence Prediction (NSP)

In the BERT training process, the model receives pairs of sentences as input and learns to predict if the second sentence in the pair is the subsequent sentence in the original document. During training, 50% of the inputs are a pair in which the second sentence is the subsequent sentence in the original document, while in the other 50% a random sentence from the corpus is chosen as the second sentence. The assumption is that the random sentence will be disconnected from the first sentence.

To distinguish between two sentences in training, the input is processed is the following way:
1. A `[CLS]`token is inserted at the beggining of the firts sentence and `[SEP]`token is inserted at the end of each sentence.
2. A sentence embedding indicating Sentence A or Sentence B is added to each token. 
3. A positional embedding is added to each token to indicate its position in the sequence. 

![image](https://github.com/maragones/ghost_recon/blob/master/BERT/input_image.png)

To predict if the second sentence is indeed connected to the first, the following steps are performed:
1. The entire input sequence goes through the Transformer model.
2. The output of the [CLS] token is transformed into a 2×1 shaped vector, using a simple classification layer (learned matrices of weights and biases).
3. Calculating the probability of IsNextSequence with softmax.

When training the BERT model, Masked LM and Next Sentence Prediction are trained together, with the goal of minimizing the combined loss function of the two strategies.

## How to use BERT (Fine-tuning)?

BERT can be used to many language tasks (mentioned before), to adapt BERT to each task is relatively easy. You only have to add a small layer to the core model. 

1. **Classification task, Sentiment Analysis**: Add a classification layer on top of the Transformer output for the [CLS] token.
2. **Question Answering**: The software receives a question regarding a text sequence and is required to mark the answer in the sequence. A Question Answering model can be trained by learning two extra vectors that mark the beginning and the end of the answer.
3. **NER**: the software receives a text sequence and is requiered to mark the various type of entities that appear in the text. Using BERT, a NER model can be trained by feeding the output vector of each token into a classification layer that predicts the NER label.

## Extras
1. **Model size**: BERT_large, with 345 million parameters, is the largest model of its kind. It is demonstrably superior on small-scale tasks to BERT_base, which uses the same architecture with “only” 110 million parameters.
2. **more training steps == higher accuracy**: On the MNLI task, the BERT_base accuracy improves by 1.0% when trained on 1M steps (128,000 words batch size) compared to 500K steps with the same batch size.
3. BERT’s bidirectional approach (MLM) converges slower than left-to-right approaches (because only 15% of words are predicted in each batch) but bidirectional training still outperforms left-to-right training after a small number of pre-training steps.

![image](https://github.com/maragones/ghost_recon/blob/master/BERT/accuracy_bert.png)

4. Time for training compute
![image](https://github.com/maragones/ghost_recon/blob/master/BERT/time_bert.png)



