# Import different modules for using with the notebook
from code import interact

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.metrics import confusion_matrix
from sklearn.cluster import KMeans

from numpy.random import randint
from skimage import io
from sklearn import datasets

# Load in the `digits` data
digits = datasets.load_digits()
print(digits.keys())

# Find the number of unique labels
number_digits = len(np.unique(digits.target))
print(number_digits)
print(np.unique(digits.target))

def show_digits(k=0):
    """
    Show the digits in the training set
    """
    plt.imshow(digits.images[k], cmap=cm.binary)
    plt.show()
show_digits()

pca = PCA(2)
originaldig = np.array(digits.images)
flattendigits = originaldig.reshape((len(originaldig), -1))
pca.fit(flattendigits)

reduced_data_pca = pca.transform(flattendigits)

# Don't change the code in this block
colors = ['black', 'blue', 'purple', 'yellow', 'white',
          'red', 'lime', 'cyan', 'orange', 'gray']

for i in range(len(colors)):
    x = reduced_data_pca[:, 0][digits.target == i]
    y = reduced_data_pca[:, 1][digits.target == i]
    plt.scatter(x, y, marker='o', s=20, facecolors=colors[i], edgecolors='k')

# PCA Scatter Plot
plt.legend(digits.target_names, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title("Regular PCA Scatter Plot")
plt.show()

lda = LDA(n_components=2)
reduced_data_lda = lda.fit_transform(flattendigits, digits.target)

# Don't change the code in this block
colors = ['black', 'blue', 'purple', 'yellow', 'white',
          'red', 'lime', 'cyan', 'orange', 'gray']

for i in range(len(colors)):
    x = reduced_data_lda[:, 0][digits.target == i]
    y = reduced_data_lda[:, 1][digits.target == i]
    plt.scatter(x, y, marker='o', s=20, facecolors=colors[i], edgecolors='k')

# LDA Scatter Plot
plt.legend(digits.target_names, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel('First LDA Component')
plt.ylabel('Second LDA Component')
plt.title("LDA Scatter Plot")
plt.show()