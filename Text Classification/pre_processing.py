"""
This module contins function for the pre-processing step for NLP. 
1. Remove Punctutation
2. Remove stopwords 
3. Remove blank spaces 
4. Apply steeming
"""

## 1. Punctutations
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def lst_punct(list_words):
	no_punct = []
	for chr in list_words:
		if chr not in punctuations:
			no_punct = no_punct + chr
	return(no_punct)


def clean_lst(ls):
    new_ls = []
    for x in ls:
        x = x.replace('\xa0', '')
        x = x.replace('\n', '')
        out = x.replace('\t', '')
        new_ls.append(out)
    return(new_ls)