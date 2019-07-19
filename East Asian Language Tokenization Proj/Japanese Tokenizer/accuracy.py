#!/usr/bin/env python3

'''
    accuracy.py - Python3 program to return accuracy of Word Segmentation comparing two files:
        i.e. (1)gold standard file with (2)word segmented files
        NOTE: it matches each line of those two files and returns the accuracy percentage of our Word Segmentation (e.g. MaxMatch algorithm)
    Auhtor: Sadip Giri (sadipgiri@bennington.edu)
    Date: 12th March, 2019
'''

def accuracy(user_file='sadip_out.txt', gold_standard_file='gold_standard.txt'):
    '''
        - read user file
        - read gold standard file
        - count all lines that matches 
        - return percentage
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

if __name__ == '__main__':
    print('-----ACCURACY WITH GOLD STANDARD-----')
    print(accuracy())
    print('-----ACCURACY WITH JUSTIN OUTPUT-----')
    print(accuracy(gold_standard_file='sample_out.txt'))
    
    
