#!/bin/bash

# Bash script to execute all commands at once as specified
# Author: Sadip Giri (sadipgiri@bennington.edu)
# Date: 11th May 2019

# At first, make all required directory
mkdir output00v output01v output02v output03v output10v output11v output12v output13v
# NOTE: here-> 1st 0 means should_normalize or not (1) and 
# 2nd 0 means Euclidean distance, 1 manhattan distance, 2 cosine distance & 3 average of all those distances (I created to see the underlying difference)

./word_analogy.py vectormodel.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output00v output00v/eval.txt 0 0
./word_analogy.py vectormodel.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output01v output01v/eval.txt 0 1
./word_analogy.py vectormodel.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output02v output02v/eval.txt 0 2
./word_analogy.py vectormodel.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output03v output03v/eval.txt 0 3
./word_analogy.py vectormodel.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output10v output10v/eval.txt 1 0
./word_analogy.py vectormodel.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output11v output11v/eval.txt 1 1
./word_analogy.py vectormodel.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output12v output12v/eval.txt 1 2
./word_analogy.py vectormodel.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output13v output13v/eval.txt 1 3
