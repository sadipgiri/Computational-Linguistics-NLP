#!/usr/bin/env python3

'''
    Word analogy python3 program -> that solves analogies such as "dog is to cat as puppy is to ___".
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Date: 26th May, 2019
'''

import numpy as np
import os
import sys
from gensim.models import KeyedVectors

words_vector_file = sys.argv[1]
input_directory = sys.argv[2]
output_directory = sys.argv[3]
evaluation_file = sys.argv[4]

# load the model -> in binary for using gensim models builtin most siilar function
model = KeyedVectors.load_word2vec_format(fname=words_vector_file, binary=True)

def compare_and_return_fourth_vector(word1,word2,word3):
    '''

    '''
    word1 = word1.lower()
    word2 = word2.lower()
    word3 = word3.lower()
    list_of_words = list(model.wv.vocab)
    if (word1 not in list_of_words) or (word2 not in list_of_words) or (word3 not in list_of_words):
        return 'none'
    return model.most_similar(positive=[word1.lower(), word2.lower()], negative=[word3.lower()], topn=1)[0][0] # gives a list of tuple consisting of word and the predicted probability

def read_write_format(input_dir, output_dir, evaluation_file):
    '''
        Task:
            - Create new analogy test files out of input_test (GoogleTestFile)
                - including evaluation file within it (accuracy of each file; plus, total accuracy!)

        Approach:
            - List all test files (only .txt) e.g. .txt files in GoogleTestFile
            - Loop through all words (2 pairs/4 wrods) and compare 4 test word with fourth predicted word 
            - Finally write fourth predicted words in all new Output file for each test files
            - At the same time, write evaluation files in each output dir according to given format
                - including: accuracy of each file and total accuracy of that output dir type.
    '''
    # track total accuracy:
    total_correct_guesses = 0
    total_guesses = 0
    # to finally write evaluation file:
    eval_write_format = []
    # list all .txt files from given input test dir e.g. GoogleTestFile
    input_files = [file for file in os.listdir(input_dir) if file.endswith('.txt')]
    for file in input_files:
        print('Loading: {0}'.format(file))
        # to track accuracy of each file
        temp_correctly_guessed =  0
        temp_write_format = []
        # read each file's lines
        with open('{0}/{1}'.format(input_dir, file), 'r') as f:
            lines = f.read().splitlines()
        temp_total_words = len(lines)
        # for each line with 4 words: find predicted fourth word and compare with existing 4th word
            # -> using above compare function
        for line in lines:
            words = line.split()
            fourth_word = compare_and_return_fourth_vector(words[0], words[1], words[2])
            if fourth_word == words[3].lower():
                temp_correctly_guessed += 1
            temp_write_format.append(' '.join(words[:3] + [fourth_word + '\n'])) # could use .capitlize() to follow case consistency!!
        # finally, write 3 words + 4th predicted word in output dir epecified
        with open('{0}/{1}'.format(output_dir,file), 'w') as write_file:
            write_file.write(''.join(temp_write_format))
        print('Done: {0}'.format(file))
        eval_write_format.append(file + '\n')
        eval_write_format.append('ACCURACY: {0}% ({1}/{2})\n'.format(temp_correctly_guessed/temp_total_words * 100, temp_correctly_guessed, temp_total_words))
        total_correct_guesses += temp_correctly_guessed
        total_guesses += temp_total_words
    # finally include total accuracy in evaluation file:
    eval_write_format.append('Total accuracy: {0}% ({1}/{2})'.format(total_correct_guesses/total_guesses * 100, total_correct_guesses, total_guesses))
    with open(evaluation_file, 'w') as eval_file:
        eval_file.write(''.join(eval_write_format))
    return 'Hurray Done!'

# finally: execute everything at once:
read_write_format(input_directory, output_directory, evaluation_file)


'''
    Techniques/Roadblocks:
        - Learned how to use pre-trained Brown Corpus word to vector model.
        - Also, used gensim builtin word_similarity functionality which is super fast than our techniques.
        - Was able to play with binary as well as word to vector txt file formats for faster computations.
        - Adapted Project 5 GoogleTestSet read write functionality.
'''