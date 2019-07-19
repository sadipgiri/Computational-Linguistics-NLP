# Ngram Models

## 1. Build Ngram Model
    - take in an input file and output a file with the probabilities for each unigram, bigram, and trigram of the input text.

    Execution
        - To build the model, use the following command in the terminal:

        ./build_ngram_model.py <input_file> <output_file>

## 2. Sentence Generation

    - take an ngram language model (output from the previous part 1, written to a file as described above), and outputs to a file sentences generated from the unigram, bigram, and trigram models.

    Execution
        - To randomly generate sentences, use the following command in the terminal:
        
        ./generate_from_ngram.py <input_file> <output_file>

## 3. Evaluate Language Model
    - calculate the perplexity on a test set is one way of evaluating the effectiveness of the language model. 
        - take in an ngram language model as input (output of Part 1), lambda values, a test file and and output file and calculate the perplexity of the test file.

    Execution
        - To evaluate the ngram model using perplexity, use the following command in the terminal:
        
        - ./ngram_perplexity.py <input_file> <lambda1> <lambda2> <lambda3> <test_file> <output_file>

<br/>
  
## Code Requirements

The code is in Python3 (version 3.0 or higher will work). Optional: <a href="https://www.nltk.org">nltk</a> could be used. However, NLTK package is not required since tasks like tokenization, stemming, etc. are written from scratch.

### Author

* **<a href="https://sadipgiri.github.io">Sadip Giri</a>** - (sadipgiri@bennington.edu)

### Contact

Feel free to contact me or open a ticket (PRs are always welcome!) with any questions, comments, suggestions, bug reports, etc.

### License

This project is licensed under the terms of the MIT license.
