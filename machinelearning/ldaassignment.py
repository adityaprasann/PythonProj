import numpy as np
from matplotlib import pylab as plt
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

# Create synthetic data
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
y = np.array([1, 1, 1, 2, 2, 2])

# Instantiate & fit the model: LDA
clf = LDA()
clf.fit(X, y)

print(clf.predict([[-0.8, -1]]))

# import training data
wine_train = np.loadtxt('./data/wine/wine_train.txt', delimiter=',')
wine_train_labels = wine_train[:, -1]
wine_train_classes = list(set(wine_train_labels))
wine_train_classes = np.array(wine_train_classes, dtype=int)
wine_train_labels = np.array(wine_train_labels, dtype = int)
wine_train = wine_train[:,:-1]

# import testing data
wine_test = np.loadtxt('./data/wine/wine_test.txt', delimiter=',')
wine_test_labels = wine_test[:, -1]
wine_test_classes = list(set(wine_test_labels))
wine_test_classes = np.array(wine_test_classes, dtype=int)
wine_test_labels = np.array(wine_test_labels, dtype = int)
wine_test = wine_test[:, :-1]

label_color_dict = {'1': 'navy', '2': 'turquoise', '3': 'darkorange'}
cvec = [label_color_dict[str(label)] for label in wine_test_labels]

x_new = PCA(n_components=2).fit_transform(wine_test)
plt.scatter(x_new[:, 0], x_new[:, 1], c=cvec, edgecolor='', alpha=0.5)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCA')
plt.show()

y_new = LDA(n_components=2).fit(wine_test, wine_test_labels).transform(wine_test)
plt.scatter(y_new[:, 0], x_new[:, 1], c=cvec, edgecolor='', alpha=0.5)
plt.xlabel('LD1')
plt.ylabel('LD2')
plt.title('LDA')
plt.show()

