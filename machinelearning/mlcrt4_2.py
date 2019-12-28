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
from sklearn import datasets, mixture
from sklearn.model_selection import train_test_split
digits = datasets.load_digits()

# Split the `digits` data into training and test sets
X_train, X_test, y_train, y_test, images_train, images_test = train_test_split(digits.data, digits.target, digits.images, test_size=0.25, random_state=42)

# X_train : pixel training data
# X_test : pixel testing data
# y_train : label training data
# y_test : pixel testing data
# images_train : image training data
# images_test : image testing data

# Number of training features
n_samples, n_features = X_train.shape

# Print out `n_samples`
print('Number of samples:', n_samples)

# Print out `n_features`
print('Number of features:', n_features)

# Number of Training labels
n_digits = len(np.unique(y_train))
print ('Number of training labels:', n_digits)

# Inspect `y_train`
print('Number of labled data:', len(y_train))

# Create the KMeans model
# insert the code. Make sure you set init='k-means++', and random_state=42
kmeans = KMeans(n_clusters=n_digits, init='k-means++', random_state=42)

# Fit the training data to the model
# insert code
kmeans = kmeans.fit(X_train)

# Retrieve the cluster centres
# insert code
centres = kmeans.cluster_centers_

# Don't change the code in this cell
# Figure size in inches
fig = plt.figure(figsize=(8, 3))

# Add title
fig.suptitle('Cluster Center Images', fontsize=14, fontweight='bold')

# For all labels (0-9)
for i in range(10):
    # Initialize subplots in a grid of 2X5, at i+1th position
    ax = fig.add_subplot(2, 5, 1 + i)
    # Display images
    ax.imshow(centres[i].reshape((8, 8)), cmap=plt.cm.binary)
    # Don't show the axes
    plt.axis('off')

# Show the plot
plt.show()

# Predict the labels for `X_test`
# Insert code
kmeans_test = kmeans.predict(X_test)

centres = kmeans.cluster_centers_

# Print out the confusion matrix with `confusion_matrix()`
# insert code

m_confusion = confusion_matrix(y_test, kmeans_test)
print(m_confusion)

# 1. Next try to initialize the k-means algorithm by providing one random sample from each class
# as the initial mean estimate for each cluster. You are allowed to make use of the class labels
# in order to draw a random sample from each class.

# Your code here
sampleX = []
sampleY = []
break_idx = 0

for i in range(0, len(y_train)):
    # appendx data (x) and label (y) when label matches
    if y_train[i] == break_idx:
        sampleX.append(X_train[i])
        sampleY.append(y_train[i])

        break_idx = break_idx + 1

    if break_idx == 10:
        break

sampleX = np.array(sampleX)
sampleY = np.array(sampleY)

kmeans_sample = KMeans(n_clusters=n_digits, init=sampleX, random_state=42)
kmeans_sample = kmeans_sample.fit(X_train)

# insert code
centres_sample = kmeans_sample.cluster_centers_
fig_sample = plt.figure(figsize=(8, 3))
fig_sample.suptitle('Images', fontsize=14, fontweight='bold')

for i in range(10):
    ax = fig_sample.add_subplot(2, 5, 1 + i)
    ax.imshow(centres_sample[i].reshape((8, 8)), cmap=plt.cm.binary)
    plt.axis('off')

# Show the plot
plt.show()


data = X_train.data
np.random.seed(1)

# Your code here
gmm_model = mixture.GaussianMixture(n_components=10, covariance_type='full')
gmm_model.fit(data)

# Extract the means as well as the covariances
# Your code here
mns = gmm_model.means_
covs = gmm_model.covariances_

# Reshape the images
im = mns.reshape(10, 8, 8)

# Don't change this code
# Figure size in inches
fig = plt.figure(figsize=(8, 3))

# Add title
fig.suptitle('Cluster Center Images', fontsize=14, fontweight='bold')

# For all labels (0-9)
for i in range(10):
    # Initialize subplots in a grid of 2X5, at i+1th position
    ax = fig.add_subplot(2, 5, 1 + i)

    # Display images
    ax.imshow(im[i].reshape((8, 8)), cmap=cm.binary)
    plt.axis('off')

# Show the plot
plt.show()

print (mns.shape)
print (covs.shape)


from scipy.stats import multivariate_normal
x = np.linspace(0, 5, 10, endpoint=False)
print(x)
y = multivariate_normal.pdf(x, mean=2.5, cov=0.5)
plt.plot(x, y)

# Your code here
samples = np.zeros((10,64))

from scipy.stats import multivariate_normal

print(mns.shape)
print(covs.shape)

for i in range(10):
    samples[i] = multivariate_normal.rvs(mean=mns[i], cov=covs[i], size=1, random_state=None)

im = samples.reshape(10,8,8)

# Don't Change this code
# Figure size in inches
fig = plt.figure(figsize=(8, 3))

# Add title
fig.suptitle('Cluster Center Images', fontsize=14, fontweight='bold')

# For all labels (0-9)
for i in range(10):
    # Initialize subplots in a grid of 2X5, at i+1th position
    ax = fig.add_subplot(2, 5, 1 + i)
    # Display images
    ax.imshow(im[i].reshape((8, 8)), cmap=plt.cm.binary)
    # Don't show the axes
    plt.axis('off')

# Show the plot
plt.show()