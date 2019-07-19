#!/usr/bin/env python3

'''
    python3 program to train word to vector model using Brown Corpus
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Date: 23rd May, 2019
'''

from nltk.corpus import brown, stopwords
from gensim.models import Word2Vec
from nltk.stem.porter import PorterStemmer
import sys

# get important parameters from sys
algorithm_type = int(sys.argv[1])
window_size = int(sys.argv[2])
vector_dimension = int(sys.argv[3])
min_count = int(sys.argv[4]) 

# gives me the list of sentences from Brown Corpus
sentences = brown.sents() # list of list of words

# used stemming before fitting word to vector model
porter = PorterStemmer()

stop_words = stopwords.words('english')

def preprocessing(sentences):
    '''
        Task: pre-process/clean sentences
        Approach:
            - lower case
            - remove stop words
            - remove punctuation
            - stemming using porter stemmer
        -> used very handy python list comprehensions tool.
    '''
    new_sentences = []
    for sentence in sentences:
        new_sentences.append([porter.stem(word).lower() for word in sentence if (word.lower() not in stop_words) and (word.lower().isalpha())])
    return new_sentences

# fit word to vector model using gensim functionality
model = Word2Vec(sentences=preprocessing(sentences), size=vector_dimension, window=window_size, min_count=min_count, sg=algorithm_type)

# about the model
print(model)

# saving it in binary as well as word to vector txt
model.wv.save_word2vec_format('brown_{0}d_algo{1}_{2}window_size_min_count{3}_model.bin'.format(vector_dimension, algorithm_type, window_size, min_count))

# saving model in word to vector txt
model.wv.save_word2vec_format('brown_{0}d_algo{1}_{2}window_size_min_count{3}_model.txt'.format(vector_dimension, algorithm_type, window_size, min_count), binary=False)

'''
    Techniques/Roadblocks:
    - Learned how to train word to vector model using Gensim library; especially being able to tune hyperparameters such as: window_size, min_count, dimenstions, etc as explained in Readme.
        - Although I didn't have to write lots of code, I had to read a lot of documentation to train word2vec model as well as load model in binary or word2vec txt format.
    - Used previous methods such as: Porter Stemmer(), nltk brown corpus, list comprehensions.
    Future Work: could deal with effective preprocessing of texts and training good word2vec model depending on the particular task.
'''








