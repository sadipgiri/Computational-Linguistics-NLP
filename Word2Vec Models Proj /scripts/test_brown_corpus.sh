#!/bin/bash

# Bash script to execute all commands at once as specified
# Author: Sadip Giri (sadipgiri@bennington.edu)
# Date: 26th May, 2019

# At first, make all required directory
mkdir output_brown_100d output_brown_300d
# NOTE: here-> d means dimentsion but could train a model depending on different algorithm, window_size and other hyper-parameters 

./test_brown_corpus.py brown_100d_algo0_5window_size_min_count5_model.bin /Users/sadipgiri/Desktop/Final_Project_Computational_Linguistics/GoogleTestSet output_brown_100d output_brown_100d/eval.txt
./test_brown_corpus.py brown_300d_algo1_10window_size_min_count2_model.bin /Users/sadipgiri/Desktop/Final_Project_Computational_Linguistics/GoogleTestSet output_brown_300d/ output_brown_300d/eval.txt
