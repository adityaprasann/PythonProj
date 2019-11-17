import numpy as np
from matplotlib import pylab as plt
from sklearn.decomposition import PCA
import load_iris as ld
from skimage import io
from skimage.transform import resize

# Create synthetic data
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])

# Instantiate and fit PCA model
pca = PCA(n_components=2)
pca.fit(X)

print("Percentage of variance explained by each of the selected components:")
print(pca.explained_variance_ratio_)


data, classes, labels = ld.load_iris2('./data/iris/iris_train.txt')

# Fit PCA
pca = PCA(n_components=3)
pca.fit(data)

# Plot
plt.plot(range(0, 3), pca.explained_variance_ratio_)
plt.ylabel('Explained Variance')
plt.xlabel('Principal Components')
plt.title('Explained Variance Ratio')
plt.show()

label_color_dict = {'0': 'navy', '1': 'turquoise', '2': 'darkorange'}
cvec = [label_color_dict[str(label)] for label in labels]

x_new = PCA(n_components=3).fit_transform(data)
plt.scatter(x_new[:, 0], x_new[:, 1], c=cvec, edgecolor='', alpha=0.5)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()

# Import all faces as a flattened array
ic = io.ImageCollection('./data/att_faces/*/*.png')
ic = np.array(ic)
ic_flat = ic.reshape((len(ic), -1))

# Shape of array
number, m, n = ic.shape

def view_image(n=0):
    plt.imshow(ic[n], cmap='gray', interpolation='nearest')
    plt.show()
view_image()

pca = PCA(n_components=200)
pca.fit(ic_flat)

print(pca)

plt.plot(range(0, 200), pca.explained_variance_ratio_)
plt.title('Explained Variance Ratio')
plt.show()

pr_ic_flat = pca.transform(ic_flat)
back_pr_ic_flat = pca.inverse_transform(pr_ic_flat)

ic_restore = back_pr_ic_flat.reshape((number, m, n))

def view_image_restore(n=0):
    plt.imshow(ic_restore[n],cmap='gray', interpolation='nearest')
    plt.show()
view_image_restore()

ben = io.ImageCollection('./Ben_bw.png')[0]
ben = np.array(ben)
ben_flat = ben.reshape((10304, -1))
pr_ben_flat = pca.transform(ben_flat)
back_pr_ben_flat = pca.inverse_transform(pr_ben_flat)
resized_ben = resize(back_pr_ben_flat, (112, 92), anti_aliasing=True)
ben_flat = ben.reshape(1, -1)

def view_image_ben(n=92):
    plt.imshow(resized_ben[n], cmap='gray', interpolation='nearest')
    plt.show()
view_image_ben()


# Import all faces as a flattened array
icall = io.ImageCollection('./data/att_faces/*/*.png:./Ben_bw.png')
icall = np.array(icall)
icall_flat = icall.reshape((len(icall), -1))

# Shape of array
number, m, n = icall.shape

def view_image(n=0):
    plt.imshow(icall[n], cmap='gray', interpolation='nearest')
    plt.show()

pca_all = PCA(n_components=200)
pca_all.fit(icall_flat)

print(pca_all)

pr_ic_flat_all = pca_all.transform(icall_flat)
back_pr_ic_flat_all = pca.inverse_transform(pr_ic_flat_all)

ic_restore_all = back_pr_ic_flat_all.reshape((number, m, n))

def view_image_restore_all(n=0):
    plt.imshow(ic_restore_all[n],cmap='gray', interpolation='nearest')
    plt.show()
view_image_restore_all()




