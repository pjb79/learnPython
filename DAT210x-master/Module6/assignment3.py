#
# This code is intentionally missing!
# Read the directions on the course lab page!

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.manifold import Isomap
from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.svm import SVC

# import data and drop unneeded columns
X = pd.read_csv('C:\\Users\\pjbca\\Documents\\GitHub\\learnPython\\DAT210x-master\\Module6\\Datasets\\parkinsons.data')
X = X.drop('name',axis =1)

# split into x and y
y = X.loc[:,['status']]
X = X.drop('status', axis = 1)

# split into test and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7)

# preprocess
#T = preprocessing.Normalizer().fit(X_train)
#T = preprocessing.MaxAbsScaler().fit(X_train)
#T = preprocessing.MinMaxScaler().fit(X_train)
#T = preprocessing.KernelCenterer().fit(X_train)
T = preprocessing.StandardScaler().fit(X_train)

X_train = T.transform(X_train)
X_test = T.transform(X_test)

# dimensionality reduction
#pca = PCA(n_components = 6)
#pca.fit(X_train)
#X_train = pca.transform(X_train)
#X_test = pca.transform(X_test)

iso = Isomap(n_neighbors=5, n_components=4)
iso.fit(X_train)
X_train = iso.transform(X_train)
X_test = iso.transform(X_test)
  
# creat svc classifier
bestScore = 0
for g in np.arange(0.001,0.1,0.001):
    for C in np.arange(0.05,2,0.05):
        svc = SVC(kernel='rbf', C=C, gamma = g)
        svc.fit(X_train, y_train)
        yFit = svc.predict(X_test)
        score = accuracy_score(y_test, yFit)
        if score > bestScore:
            bestScore = score
            bestC = C
            bestg = g