#!/usr/bin/env python3
"""
    Python3 program to clean and count tokens from text file
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Date: 03/02/2019
"""

import regex as re
import sys

def tokenization(filename):
    '''
        first read the file
        clean text using helper_clean_text function
        return dictionary with counts of each word
            make a new helper_counter_function()
    '''
    with open(filename) as file:
        text = file.read()
    new_text = helper_clean_text(text)
    return helper_counter(new_text.split())

def helper_clean_text(text):
    '''
        substitute various characters with space to .split() according to space

        NOTE: regex expression looks messy -> could define each expression separatly specifying their need
              also, could manipulate the reg exp according to someone's needs  
    '''
    new_text = text
    subs_chars = [r'([<].*["][>])|([<][a-zA-Z]+[0-9]*[>])|([<][/][a-zA-Z]+[0-9]*[>])|([<].*[/][>])|(http.+[\s>])|([.][\s{"&),])|([.][0-9]+)|(\n)|([0-9]+[.][0-9]+)|([a-zA-Z]*[0-9]+[a-zA-Z]*)|([.]{3})|([&][gl][t][;])|([-_^–!;=:~,#}&(){*/+|])|([[])|([]])', r"([']{2,})", r"(\s[']+[a-zA-Z][']+\s)", r"(\s['])|([']\s)", r'(")', r'([.]\s)', r'(\\s)']
    for i in subs_chars:
        new_text = re.sub(i, ' ', new_text)
    return new_text

def write_sorted_word_count_file(input_file, output_file):
    '''
        tokenization returns dictionary with counts
        helper_sort_dictionary() to return sorted list of tuples for constructive output as assigned
    '''
    dct = tokenization(input_file)
    sorted_dct = helper_sort_dictionary(dct)
    with open(output_file, 'w') as file:
        for i in sorted_dct:
            file.write('{0}\t{1}\n'.format(i[0], i[1]))

def helper_counter(word_list):
    '''
        change word list to lowercase using list comprehension
        set() to return unique words for counting
        .count() to count each unique words from original list
    '''
    dct = {}
    word_list = [i.lower() for i in word_list]
    unique_word_list = set(word_list)
    for i in unique_word_list:
        dct[i] = word_list.count(i)
    return dct

def helper_sort_dictionary(dct):
    '''
        using list comprehension to loop through each item of dictionary and 
        return sorted list of tuples
    '''
    return [(i, dct[i]) for i in sorted(dct, key=dct.get, reverse=True)]

if __name__ == '__main__':
    print('-----LEVEL1-----')
    print('-----sample.xml-----testing-----')
    write_sorted_word_count_file('sample.xml', 'level1_sadip_sample_output.txt')
    print('-----wikipedia------assignment-----')
    argument_list = sys.argv # list all terminal system arguments
    write_sorted_word_count_file(argument_list[1], argument_list[2])
    
