# Sentiment Analysis

This folder contains a general code for each model and end-to-end examples. 

# What is Sentiment Analysis?
Sentiment Analysis, also known as opinion mining is a sub-field of NLP that tries to identify and exract opinions from a given text. 

## Classification Algorithms
The classification step usally involes statistical models like the following:
1. Naive Bayes: predicts the category of a text
2. Linear Regression: Predicts some value given a set of features
3. Support Vector Machines: Uses a representation of text examples as points in a multidimensional space. These examples are mapped so that the examples of the different categories (sentiments) belong to distinct regions of that space. Then, new texts are mapped onto that same space and predicted to belong to a category based on which region they fall into.
4. Deep Learning: Uses artificial neural networks to process data.

## Aspect Based Sentiment Analysis

Most of the Sentiment Analysis methods detects the sentiment of an overall text. Unlike this methods, Aspect Based Sentiment Analysis (ABSA) is an advanced sentiment analysis technique that identifies and provides corresponding sentiment scores to the aspects of a given text. ABSA a powerful tool for getting actionable insight from your text data. 

For example consider the sentence following resturant review

`The ambiance is charming. Uncharacteristically, the service was DREADFUL.When we wanted to pay our bill at the end of the evening, our waitress was nowhere to be found...`

While most of the sentiment analysis model will correctly classify the sentiment of this model as negative (averaging throughout the text), ABSA will provide more granular insight by higlighting that while the **service** and the **waitress** provided a negative experience, the restaurant **ambiance** was positive. 


# Summary

| Document  | Description | Model | Language | Data |
|-----------|-------------|--------|---------|------|
|inv_sentiment.py| Example of Sentiment Analysis using Dictionary Methods applied in financial text. | Dictionary Method | en | Data obtained from: 'https://sraf.nd.edu/textual-analysis/resources/' (financial words already classified)| 
