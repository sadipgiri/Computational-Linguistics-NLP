#!/usr/bin/env python3

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

v1 = ['เ','แ','โ','ใ','ไ']
c1 = ['ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต', 'ถ', 'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย', 'ร', 'ฤ', 'ล', 'ฦ', 'ว', 'ศ', 'ษ', 'ส', 'ห', 'ฬ', 'อ', 'ฮ']
c2 = ['ร', 'ล', 'ว', 'น', 'ม']
v2 = ['\u0E31', '\u0E34', '\u0E35', '\u0E36', '\u0E37', '\u0E38', '\u0E39', '\u0E47']
t = ['\u0E48', '\u0E49', '\u0E4A', '\u0E4B']
v3 = ['า', 'อ', 'ย', 'ว']
c3 = ['ง', 'น', 'ม', 'ด', 'บ', 'ก', 'ย', 'ว']

def thai_word_dict(input_file = 'sample_out.txt'):
    '''
        making a word list using sample out Thai file to use maxmatch algorithm
    '''
    word_list = []
    with open(input_file, 'r') as file:
        lines = file.read().splitlines()
    for i in lines:
        word_list += i.split()
    return word_list

def tokenize(line):
#define a function that will take in a line of Thai text (without spaces), and return the line with spaces between the words
    thai_word_list = thai_word_dict()
    return ' '.join(maxmatch(line, thai_word_list))

def maxmatch(line, thai_word_list):
    '''
        Using same maxmatch algo. used in Japanese language in Thai Tokenizer
            which illustrates 100 percent accuracy
    '''
    if len(line) == 0:
        return []
    for i in range(len(line)):
        word = line[ :len(line) - i]
        if word in thai_word_list:
            new_line = [word]
            line = line[len(word): ]
            return new_line + maxmatch(line, thai_word_list)
    return list(line[0]) + maxmatch(line[1: ], thai_word_list)

def accuracy(user_file='sadip_out.txt', gold_standard_file='sample_out.txt'):
    '''
        for details check out Japanese Tokenizer -> accuracy file
        NOTE: need to make sure we have consistent \n and space after each line
    '''
    num_matched_lines = 0
    with open(user_file, 'r') as user_file:
        with open(gold_standard_file, 'r') as gold_standard_file:
            user_lines = user_file.readlines()
            gold_standard_lines = gold_standard_file.readlines()
            for i in range(len(user_lines)):
                if user_lines[i] == gold_standard_lines[i]:
                    num_matched_lines += 1
                else:
                    print(user_lines[i])
                    #print(gold_standard_lines[i])
    return (num_matched_lines/len(user_lines)) * 100

with open(input_file, 'r') as open_in:
    with open(output_file, 'w') as open_out:
        for line in open_in.readlines():
            spaced_line = tokenize(line)
            open_out.write(spaced_line)

print('-----Accuracy-----')
print(accuracy())

# if __name__ == '__main__':
#     # line = 'คู่แข่งขันต่างก็คุมเชิงกัน'
#     # print(tokenize(line))
#     print(thai_word_dict())

    