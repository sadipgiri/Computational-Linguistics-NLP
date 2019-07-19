#!/bin/bash

# Bash script to execute all commands at once as specified
# Author: Sadip Giri (sadipgiri@bennington.edu)
# Date: 26th May, 2019

# At first, make all required directory
mkdir output_glove_model_50d output_glove_model_100d output_glove_model_200d output_glove_model_300d
# NOTE: here-> d means dimentsion

./test_glove_model.py /Users/sadipgiri/Desktop/Final_Project_Computational_Linguistics/glove.6B/glove.6B.50d.txt /Users/sadipgiri/Desktop/Final_Project_Computational_Linguistics/GoogleTestSet output_glove_model_50d output_glove_model_50d/eval.txt
./test_glove_model.py /Users/sadipgiri/Desktop/Final_Project_Computational_Linguistics/glove.6B/glove.6B.100d.txt /Users/sadipgiri/Desktop/Final_Project_Computational_Linguistics/GoogleTestSet output_glove_model_100d output_glove_model_100d/eval.txt
./test_glove_model.py /Users/sadipgiri/Desktop/Final_Project_Computational_Linguistics/glove.6B/glove.6B.200d.txt /Users/sadipgiri/Desktop/Final_Project_Computational_Linguistics/GoogleTestSet output_glove_model_200d output_glove_model_200d/eval.txt
./test_glove_model.py /Users/sadipgiri/Desktop/Final_Project_Computational_Linguistics/glove.6B/glove.6B.300d.txt /Users/sadipgiri/Desktop/Final_Project_Computational_Linguistics/GoogleTestSet output_glove_model_300d output_glove_model_300d/eval.txt
