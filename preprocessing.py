import json
from nltk.tokenize import word_tokenize
import re
import operator
from collections import Counter
from nltk.corpus import stopwords
import string
import enchant      #module from pyenchant

from nltk import bigrams    #To convert words into tuples to get more context

d = enchant.Dict("en_US") #To check if words are english USA

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
'''
The regular expressions are compiled with the flags re.VERBOSE, to allow spaces in the regexp to be
ignored (see the multi-line emoticons regexp), and re.IGNORECASE to catch both upper and lowercases.
'''

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens] #converts all tokens to lowercase only if they are not emoticons
    return tokens

count_all = Counter()
punctuation = list(string.punctuation) #List of punctuations
stop = stopwords.words('english')+punctuation+['rt', 'via', 'RT'] #List of stopwords, punctuations, and rt, via words


with open('stream_apple.json', 'r') as f:
    for line in f:
        tweet = json.loads(line) #Loading tweets in json file
        terms = [term for term in preprocess(tweet['text']) if (term not in stop)]
        #terms_bigram = bigrams(terms) # will take a list of terms and convert them into tuples
        #count_all.update(terms_bigram)#Keeps a count of the terms
        print(terms)
    #print(count_all.most_common(200)) #200 most used terms
