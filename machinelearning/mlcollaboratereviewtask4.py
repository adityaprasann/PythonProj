# Import different modules for using with the notebook
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
im = io.imread('./data/cartoon.png')
plt.imshow(im/np.max(im))
plt.show()

# Format data
m, n = im.shape[:2]
data = im.reshape(m*n, 4)
data = np.array(data, dtype=float)


# Your code here
def getCluster(num_cluster):
    kmeans = KMeans(n_clusters=num_cluster, random_state=0).fit(data)
    RGB = kmeans.cluster_centers_.round(0)
    new_image = []
    for i in range(0, m * n):
        new_image.append(RGB[kmeans.labels_[i]])
    new_image = np.array(new_image)
    return new_image

num_cluster = 3
new_image = getCluster(num_cluster)
new_image = new_image.reshape(m, n, 4)
new_image = np.asarray(new_image, dtype="uint8")
plt.imshow(new_image)

new_cluster = 0
for i in range(num_cluster, 255 * 255 * 255):
    cluster_image = getCluster(i)
    if np.array_equal(cluster_image, data):
        new_cluster = i
        break

print('new_cluster: :', new_cluster)