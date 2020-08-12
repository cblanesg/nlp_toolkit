"""
This module usic a really basic method to infer sentiment in finincial texts.
It uses a dictionary https://sraf.nd.edu/textual-analysis/resources/ of words
that have been classified.
"""

import pickle
import os

PATH = '/home/n/text_sentiment_region/' 

def load_dicts(path):
    """
    Load three sets of words (positive,negative and uncertain)
    """
    positive = pickle.load(open(path+'positive_finance.p','rb'))
    negative = pickle.load(open(path+'negative_finance.p','rb'))
    uncertain = pickle.load(open(path+'uncertain_finance.p','rb'))
    return positive,negative,uncertain

positive,negative,uncertain = load_dicts(PATH)



def get_sentiment(text):
    """
    Counts positive and negative finanancial words in text.
    Returns the percentage of pos/neg words in the text found in 
    the dictionary.
    """
    splitted_text = text.split() 
    neg_l = len([word for word in splitted_text if word in negative])
    pos_l = len([word for word in splitted_text if word in positive])

    if neg_l == pos_l == 0:
        return 0
    else:
        return (pos_l - neg_l)/ (pos_l + neg_l)*100


def get_uncertainty(text):
    """
    Counts positive and negative finanancial words in text.
    Returns the percentage of uncertain words in the text found in 
    the dictionary.
    """
    splitted_text = text.split()
    unc_l = len([word for word in splitted_text if word in uncertain])

    return unc_l/len(splitted_text)*100

def uncertainty_in_string(score):
    if score >30:
        return "strongly positive"
    if score >0:
        return "positive"
    if score == 0:
        return "neutral"
    if score <30:
        return "negative"

    return "strongly positive"


def sentiment_in_string(score):
    if score >30:
        return "strongly positive"
    if score >0:
        return "positive"
    if score == 0:
        return "neutral"
    if score <30:
        return "negative"

    return "strongly positive"