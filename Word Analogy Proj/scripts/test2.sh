#!/bin/bash

# Bash script to execute all commands at once as specified
# Author: Sadip Giri (sadipgiri@bennington.edu)
# Date: 11th May 2019

# At first, make all required directory
mkdir output00vv output01vv output02vv output03vv output10vv output11vv output12vv output13vv
# NOTE: here-> 1st 0 means should_normalize or not (1) and 
# 2nd 0 means Euclidean distance, 1 manhattan distance, 2 cosine distance & 3 average of all those distances (I created to see the underlying difference)

./word_analogy.py samplemodel.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output00vv output00vv/eval.txt 0 0
./word_analogy.py samplemodel.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output01vv output01vv/eval.txt 0 1
./word_analogy.py samplemodel.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output02vv output02vv/eval.txt 0 2
./word_analogy.py samplemodel.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output03vv output03vv/eval.txt 0 3
./word_analogy.py samplemodel.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output10vv output10vv/eval.txt 1 0
./word_analogy.py samplemodel.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output11vv output11vv/eval.txt 1 1
./word_analogy.py samplemodel.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output12vv output12vv/eval.txt 1 2
./word_analogy.py samplemodel.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output13vv output13vv/eval.txt 1 3
