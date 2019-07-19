#!/usr/bin/env python3

'''
    japanese_tokenizer - Python3 program to segment words of languages which don't have word spacing or segmentation e.g. Japanese, Thai or Chinese.
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Date: 12th March, 2019
'''

import sys

def japanese_tokenizer(input_file, output_file, word_dict_file = 'japanese_wordlist.txt'):
    '''
        first, read japanese_wordlist.txt file to make a word dictionary
        secondly, each line of in.txt file
            -> replace \n from the line to get the in sentence format we want
            -> get new segmented line using maxmatch() algorithm
            -> write to each segmented line to output file [adding \n too!]
    '''
    with open(word_dict_file, 'r') as word_dict_file:
        with open(input_file, 'r') as input_file:
            with open(output_file, 'w') as output_file:
                word_dict = word_dict_file.read().splitlines()
                lines = input_file.read().splitlines()
                for line in lines:
                    string_to_write_format = '{0}\n'.format(' '.join(maxmatch(line, word_dict))) # ' '.join() will add space and make string out of list of strings
                    output_file.write(string_to_write_format)
    return


def maxmatch(sentence, word_dict):
    '''
        MAXMATCH ALGORITHM
            ➤ Using a dictionary, find the longest string of characters that
            appear in the dictionary.
            ➤ Save that string, and repeat on the remainder of the sentence.
            ➤ If a word is not encountered in the dictionary, save a single
            character and repeat on the remainder of the sentence.
            ➤ (This algorithm doesn’t handle unknown words well)
        
        Approach:
        - if sentence is empty -> return empty string
        - loop through the sentence and find word from right to left direction
            - if found -> add spaces around the word
                       -> our new sentence will be remaining word
                       -> recursively loop through our new sentence until we get the word matched
            - if not found -> pop first letter from the sentence and recursively call the algorithm with remaining sentence
    '''
    # if len(sentence) == 0:
    #     return ''
    # for i in range(len(sentence)):
    #     word = sentence[ :len(sentence) - i]
    #     #print(word)
    #     if word in word_dict:
    #         segmented_sentence = word + ' '
    #         sentence = sentence[len(word): ]
    #         #print(sentence)
    #         return segmented_sentence + maxmatch(sentence, word_dict)
    # return sentence[0] + ' ' + maxmatch(sentence[1:], word_dict)

    # NOTE: if there's spacing issue we could use list() instead and helper ' '.join() function to return string
        # above string function will add extra spaces at the end so -> better to use list
        # I think JUSTIN is also doing string manipulation so there's space in each line of his sample_out.txt file
    if len(sentence) == 0:
        return []
    for i in range(len(sentence)):
        word = sentence[:len(sentence) - i]
        if word in word_dict:
            words_list = [word]
            sentence = sentence[len(word):]
            return words_list + maxmatch(sentence, word_dict)
    return list(sentence[0]) + maxmatch(sentence[1:], word_dict)

if __name__ == '__main__':
    lst = sys.argv
    japanese_tokenizer(lst[1], lst[2])

    # print('-----TEST MAXMATCH ALGO-----')
    # word_dict = ['sadip', 'giri']
    # sentence = 'ijklmnopsadipgirifgiri,kelw9sdfjsjofi'
    # print(maxmatch(sentence, word_dict))
    # print(lst)
    # print('-----------')
    