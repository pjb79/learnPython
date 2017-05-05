import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
df = pd.read_csv('C:\\D\\GitHub\\learnPython\\DAT210x-master\\Module3\\Datasets\\wheat.data', index_col = 'id')



fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the area,
# perimeter and asymmetry features. Be sure to use the
# optional display parameter c='red', and also label your
# axes
# 
ax.scatter(xs = df['area'], ys = df['perimeter'], zs = df['asymmetry'], c = 'red')


fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the width,
# groove and length features. Be sure to use the
# optional display parameter c='green', and also label your
# axes
# 
ax.scatter(xs = df['width'], ys = df['groove'], zs = df['length'], c = 'green')




