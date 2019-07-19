# Final Project Computational Linguistics
1. Program that solves analogies such as "dog is to cat as puppy is to ___".

2. Train different words to vectors models such as:

    - Brown Corpus Word2Vec with:
        - Dimenstions e.g. 50, 100, 200, 300
            - length of the vector (for each word); that is, the number of dimensions of the embedding.
        - Algorithm types:
            - CBOW (Continuos Bag of Words) or
                - The model predicts the current word from a window of surrounding context words. The order of context words does not influence prediction (bag-of-words assumption).
            - Skip Gram
                - The model uses the current word to predict the surrounding window of context words. The skip-gram architecture weighs nearby context words more heavily than more distant context words.
        - Window Size
            - the maximum distance between a target word and words around the target word; default is 5
        - Minimum Count:
            - minimum count of words to consider; that is, words with an occurence less than min_count are disgarded. Default is 5.

    - Glove Model -> used Stanford's Pre-trained Model
        4 types of pre-trained glove 

            - glove.6B.50d.txt
            - glove.6b.100d.txt
            - glove.6B.200d.txt
            - glove.6B.300d.txt

    - Google Model -> used Google's Pre-trained Model

3. Also, visualise different word to vector models using trasformation algorithm—PCA (Principal Component Analysis).
  
## Code Requirements

The code is in Python3 (version 3.0 or higher will work). The only other requirement is: <a href="https://www.numpy.org/">numpy</a>, <a href='https://radimrehurek.com/gensim/'>gensim</a>, <a href='https://www.nltk.org/'>nltk</a>, <a href='https://scikit-learn.org/stable/'>sklearn</a> and <a href='https://matplotlib.org/'>matplotlib</a>.

Download pre-trained models:
1. <a href='http://nlp.stanford.edu/data/glove.6B.zip'>Glove Models</a>
    - GloVe is an unsupervised learning algorithm for obtaining vector representations for words. Training is performed on aggregated global word-word co-occurrence statistics from a corpus, and the resulting representations showcase interesting linear substructures of the word vector space.
2. <a href='https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing'>Google Model</a>
    - The pre-trained Google word2vec model was trained on Google News data (about 100 billion words) and contains 3 million words and phrases and fit using 300-dimensional word vectors.

## Execution

### To train brown corpus, simply run:

```
./train_word_vector_model.py <algorithm_type> <window_size> <vector_dimension> <min_count>
```

> Algorithm_type => 0 (CBOW) or 1 (Skip Gram)

### To test different Brown Corpus Model, simply run:
```
./test_brown_corpus.sh 
```
[NOTE: provide different paths and different parameters or hyper-parameters in the bash script]

OR individually:

```
./test_brown_corpus.py <vector_model> <TestSet e.g. GoogleTestSet> <Output Dir> <Evaluation File>
```

### To test different Glove Model, simply run:
```
./test_glove_model.sh 
```
[NOTE: provide different paths and different parameters or hyper-parameters in the bash script]

OR individually: 

```
./test_glove_model.py <vector_model> <TestSet e.g. GoogleTestSet> <Output Dir> <Evaluation File>
```

### To test different Google Model, simply run:
```
./test_google_model.sh 
```
[NOTE: provide different paths and different parameters or hyper-parameters in the bash script]

OR individually:

```
./test_google_model.py <vector_model> <TestSet e.g. GoogleTestSet> <Output Dir> <Evaluation File>
```

### To visualise different word to vector model (word vector similarity), simply run:
```
./visualize_similar_word.py <vector_model> <x-axis_size> <y-axis_size> <num_of_words_to_display>
```

### Author

* **<a href="https://sadipgiri.github.io">Sadip Giri</a>** - (sadipgiri@bennington.edu)

### Contact

Feel free to contact me or open a ticket (PRs are always welcome!) with any questions, comments, suggestions, bug reports, etc.

### License

This project is licensed under the terms of the MIT license.

### Findings

I found out that traning our own word vectors might be the best approach for tasks like Word Analogy problem. However, for instance, word_to_vector_model_5_10 developed by Justin gave high accuracy around 85%. In addition to that, trained model on Brown Corpus including Glove model from Stanford and Google News (very large) model gave very low accuracy. Besides, this word embedding task might be very slow; especialy for large text files. Therefore, at that time, pre-trained model would be the way to go. Thus, the take-away of this project is that developing word to vector models depends on the application of the trained model since there will always be tradeoffs between time complexity, memory & accuracy.

##### Notes:
- Accuracy of different models could be found in there respective folders.
- Different hyper-parameters could be tuned for better performance.
- Roadblocks and findings of each task is mentioned as comments in respective python file.
- This project follows some ideas from Project 5; therefore, feel free to check out Project 5 (especially its readme that contains insights).

