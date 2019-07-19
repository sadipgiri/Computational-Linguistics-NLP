#!/usr/bin/env python3
"""
    Python3 program to clean and count stems from text file creating Porter Stemmer from scratch
        Paper - https://tartarus.org/martin/PorterStemmer/def.txt
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Date: 03/02/2019
"""

import sys
import regex as re
from porter_stemmer_helpers import step1a, step1b, step1c, step2, step3, step4, step5a, step5b
from clean_and_count_tokens import helper_clean_text, helper_counter, helper_sort_dictionary

def porter_stemmer(word):
    word = step1a(word)
    word = step1b(word)
    word = step1c(word)
    word = step2(word)
    word = step3(word)
    word = step4(word)
    word = step5a(word)
    word = step5b(word)
    return word

def my_clean_count_stems(input_filename, output_filename):
    '''
        get tokens first using cleaning function
        using my Porter Stemmer for stemmization
        using helper counter to return freq. dict of each stemmized tokens
        sorting the dict and writing according to given format in the specified file
    '''
    with open(input_filename) as file:
        text = file.read()
    tokens = helper_clean_text(text).split()
    stemmized_tokens = [porter_stemmer(i) for i in tokens]
    stemmized_dict = helper_counter(stemmized_tokens)
    sorted_stemmized_dct = helper_sort_dictionary(stemmized_dict)
    with open(output_filename, 'w') as file:
        for i in sorted_stemmized_dct:
            file.write('{0}\t{1}\n'.format(i[0], i[1]))

if __name__ == "__main__":
    print('-----LEVEL3-----')
    print('-----USING MY OWN PORTER STEMMER-----')
    print('-----sample.xml-----testing-----')
    my_clean_count_stems('sample.xml', 'level3_sadip_stemmized_sample_output.txt')
    print('-----wikipedia------assignment-----')
    argument_lists = sys.argv # list all comandline arguments
    my_clean_count_stems(argument_lists[1], argument_lists[2])