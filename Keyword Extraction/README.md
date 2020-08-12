# Key Word Extraction

# What is Key Word Extraction?
Keyword extraction (also known as keyword detection or keyword analysis) is a text analysis technique that consists of automatically extracting the most important words and expressions in a text. It helps summarize the content of a text and recognize the main topics which are being discussed. Keyword extraction simplifies the task of finding relevant words and phrases within unstructured text. This includes emails, social media posts, chat conversations, and any other types of data that are not organized in any predefined way.

## Simple Statistical Approaches
1. **Word Frequency**: Listing the words and phrases that most commonly appear within a text. Word frequency approaches consider documents as a mere ‘bag of words’, leaving aside crucial aspects related to the meaning, structure, grammar, and sequence of words.
2. **Word collocations and co-ocurrences**: Word collocations and co-occurrences can help you understand the semantic structure of a text and count separate words as one. Co-occurrences refer to words that tend to co-occur in the same corpus. (Embeddings are based in statistical co-ocurrence methods. )
3. **TF-IDF** (term frequency-inverse document frequency): measures how important a word is to a document in a collection of documents. This metric calculates the number of times a word appears in a text (term frequency) and compares it with the inverse document frequency (how rare or common that word is in the entire data set). Multiplying these two quantities provides the TF-IDF score of a word in a document. The higher the score is, the more relevant the word is to the document.
4. **RAKE** (Rapid Automatic Keyword Extraction): Keyword extraction method which uses a list of stopwords and phrase delimiters to detect the most relevant words or phrases in a piece of text.

### RAKE
Steps:
1. Split the text into a list of tokens and remove stopwords from that list (removal of stopwords are included in the pre-processing folder)
2. Matrix of word co-ocurrances. Each row shows the number of times that a given content word co-occurs with every other content word in the candidate phrases.
3. Scores: Words are given a score. That score can be calculated as the **degree of a word in the matrix** (i.e. the sum of the number of co-occurrences the word has with any other content word in the text), as the **word frequency** (i.e. the number of times the word appears in the text), or as the **degree of the word divided by its frequency.**
4. Select: A keyword or keyphrase is chosen if its score belongs to the top T scores where T is the number of keywords you want to extract. T defaults to one third of the content words in the document.


## Linguistic Approaches
Keyword extraction methods often make use of linguistic information about texts and the words they contain. 

1. PoS: nouns and noun pharses are given higher scores since they usually contain more 

## Grpah-based Approaches

# Content




