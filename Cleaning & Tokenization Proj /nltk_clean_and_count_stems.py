#!/usr/bin/env python3
"""
    Python3 program to clean, stemmize and count tokens from text file
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Date: 03/02/2019
"""

import sys
import regex as re
import nltk
from clean_and_count_tokens import helper_clean_text, helper_counter, helper_sort_dictionary

def count_cleaned_and_stemmized_tokens(input_filename, output_filename):
    '''
        get tokens first using our previous tokenization function [need keys since it returns frq. dict]
        initializing porter stemmer using nltk package and stemmized each word
        using helper counter to return freq. dict of each stemmized tokens
        sorting the dict and writing according to given format in the specified file
    '''
    with open(input_filename) as file:
        text = file.read()
    tokens = helper_clean_text(text).split()
    porter_stemmer = nltk.PorterStemmer()
    stemmized_tokens = [porter_stemmer.stem(i) for i in tokens]
    stemmized_dict = helper_counter(stemmized_tokens)
    sorted_stemmized_dct = helper_sort_dictionary(stemmized_dict)
    with open(output_filename, 'w') as file:
        for i in sorted_stemmized_dct:
            file.write('{0}\t{1}\n'.format(i[0], i[1]))

if __name__ == '__main__':
    print('-----LEVEL2-----')
    print('-----sample.xml-----testing-----')
    count_cleaned_and_stemmized_tokens('sample.xml', 'level2_sadip_stemmized_sample_output.txt')
    print('-----wikipedia------assignment-----')
    argument_lists = sys.argv # list all terminal system arguments
    count_cleaned_and_stemmized_tokens(argument_lists[1], argument_lists[2])

