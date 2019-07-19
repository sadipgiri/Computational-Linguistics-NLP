#!/bin/bash

# Bash script to execute all commands at once as specified
# Author: Sadip Giri (sadipgiri@bennington.edu)
# Date: 26th May, 2019

# At first, make all required directory
mkdir output_google_model

./test_google_word2vec_model.py /Users/sadipgiri/Desktop/Final_Project_Computational_Linguistics/GoogleNews-vectors-negative300.bin /Users/sadipgiri/Desktop/Final_Project_Computational_Linguistics/GoogleTestSet output_google_model output_google_model/eval.txt
