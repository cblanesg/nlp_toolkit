"""
Useful functions to pre process text
"""

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk import word_tokenize
import unicodedata



def remove_accents(text):

    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    return str(text)


def remove_numbers(text):
    '''REmoves integers'''
    text = ''.join([i for i in text if not i.isdigit()])
    return(text)


def remove_punctuation(text):
    punctuation = {'!', '"','#', '$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~'}    
    text = ''.join(i for i in text if i not in punctuation)
    return(text)

def text_lowercase(text):
    text = text.lower()
    return(text)

def strip_whitespace(text):
    text = " ".join(text.split())
    return(text)

def remove_sp(text):
    sp = set(stopwords.words('spanish'))
    text = [i for i in text if i not in sp]

def remove_sp(text, lan):
    if lan == 'spanish':
        sp = set(stopwords.words('spanish'))
        words_tokens = word_tokenize(text)
        text = [i for i in words_tokens if i not in sp]
        text = ' '.join(text)

    elif lan == 'english':
        sp_en = set(stopwords.words('english'))
        words_tokens = word_tokenize(text)
        text = [i for i in words_tokens if i not in sp_en]
        text = ' '.join(text)

    else:
        text = 'stopwords only available in english or spanish'
    return(text)


def apply_stemming(text, lan):
    if lan == 'spanish':
        stemmer = SnowballStemmer('spanish')
        words_tokens = word_tokenize(text)
        text = [stemmer.stem(i) for i in words_tokens]
        text = ' '.join(text)

    elif lan == 'english':
        stemmer_en = SnowballStemmer('english')
        words_tokens = word_tokenize(text)
        text = [stemmer_en.stem(i) for i in words_tokens]
        text = ' '.join(text)

    else:
        text = 'Stemmer only available in english or spanish'
    return(text)



def clean_text(text,  
          accents = True, 
          punctuation=True, 
          numbers=True, 
          lowercase=True, 
          whitespace=True, 
          lan = 'spanish',
          stopwords = False, 
          stemming = False):

    if accents:
        text = remove_accents(text)

    if punctuation:
        text = remove_punctuation(text)

    if numbers:
        text = remove_numbers(text)

    if lowercase:
        text = text_lowercase(text)

    if whitespace:
        text = strip_whitespace(text)

    if stopwords:
        text = remove_sp(text, lan = lan)

    if stemming:
        text = apply_stemming(text, lan = lan)

    return(text)













