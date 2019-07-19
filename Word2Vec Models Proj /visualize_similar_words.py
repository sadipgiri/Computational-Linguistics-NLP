#!/usr/bin/env python3

'''
    Python3 program to visualize subset of similar words
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Date: 21st May, 2019
'''

from matplotlib import pyplot
from sklearn.decomposition import PCA
from gensim.models import KeyedVectors
import sys

vector_model = sys.argv[1]
x_axis_size = float(sys.argv[2])
y_axis_size = float(sys.argv[3])
num_words_to_display = int(sys.argv[4])

# resize the figure before plotting words
pyplot.figure(figsize=(x_axis_size, y_axis_size))

# loading the model -> in binary
model = KeyedVectors.load_word2vec_format(fname=vector_model, binary=False)

# vectors_list for decomposition using PCA
vectors = model[model.wv.vocab][:num_words_to_display]

# initialize PCA components: here its 2
# then transform the vectors using PCA .fit_transform() method
pca = PCA(n_components=2)
transformed_vectors = pca.fit_transform(vectors)

# Firstly, creating a scatter plot and plotting transformed vector points 
pyplot.scatter(transformed_vectors[:, 0], transformed_vectors[:, 1])

# number of words to display 
words = list(model.wv.vocab)[:num_words_to_display]

# Finally, plotting the words (name) in resepctive points
for i, word in enumerate(words):
    pyplot.annotate(word, xy=(transformed_vectors[i, 0], transformed_vectors[i, 1]))

pyplot.savefig('{0}_{1}words_{2}x{3}.png'.format(vector_model[:-4], str(num_words_to_display), str(x_axis_size), str(y_axis_size))) # [:-4] to not have .txt in image name from vector model name

# pyplot.show()

'''
    Techniques/Roadblocks:
    - Learned this interesting way to plot similar words together.
    - Although it took long time for me to understand PCA (Principal Component Analysis) and going through Sklearn documentation, I am glad I was to able to pull this off.
    - Also, learned to use matplotlib--very important data science programmable tool.
'''

'''
Note: 
    The concept of using decomposition algorithm taken from following medium article
        -> however, I use PCA instead of TSNE—-described used in the article.
    -https://medium.com/@aneesha/using-tsne-to-plot-a-subset-of-similar-words-from-word2vec-bb8eeaea6229
'''




