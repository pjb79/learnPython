import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
from sklearn import manifold


# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')
plt.close('all')

#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
dset = []
colours = []

#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.

filePath = 'C:\\D\\GitHub\\learnPython\\DAT210x-master\\Module4\\Datasets\\ALOI\\32\\'
allFiles = [f for f in listdir(filePath) if isfile(join(filePath, f))]



for f in allFiles:
    tempArray = misc.imread(filePath + f)
    dset.append(tempArray.reshape(-1))
    colours.append('b')
    
    
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#



#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
filePath = 'C:\\D\\GitHub\\learnPython\\DAT210x-master\\Module4\\Datasets\\ALOI\\32i\\'
allFiles = [f for f in listdir(filePath) if isfile(join(filePath, f))]

for f in allFiles:
    tempArray = misc.imread(filePath + f)
    dset.append(tempArray.reshape(-1))
    colours.append('r')

#
# TODO: Convert the list to a dataframe
#
dset = pd.DataFrame(dset)



#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
iso = manifold.Isomap(n_neighbors=6, n_components=3)
iso.fit(dset)
transformT = iso.transform(dset)



#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('2D Scatter')
ax.scatter(transformT[:,0],transformT[:,2], marker='.',alpha=0.7, c = colours)




#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('3D Scatter')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.scatter(transformT[:,0], transformT[:,1], transformT[:,2], c=colours, marker='.', alpha=0.75)



#plt.show()

