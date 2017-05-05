import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
df = pd.read_csv('C:\\D\\GitHub\\learnPython\\DAT210x-master\\Module3\\Datasets\\wheat.data', index_col = 'id')


#
# TODO: Create a 2d scatter plot that graphs the
# area and perimeter features
# 
s1 = df[['area','perimeter']]
plt.figure()
plt.scatter(x = s1['area'], y = s1['perimeter'])
plt.xlabel('Area')
plt.ylabel('Perimeter')


#
# TODO: Create a 2d scatter plot that graphs the
# groove and asymmetry features
# 
s2 = df.loc[:,['groove','asymmetry']]
s2.dropna(inplace = True, axis = 0)
plt.figure()
plt.scatter(x = s2['groove'], y = s2['asymmetry'])
plt.xlabel('Groove')
plt.ylabel('Asymmetry')


#
# TODO: Create a 2d scatter plot that graphs the
# compactness and width features
# 
s3 = df.loc[:,['compactness','width']]
s3.dropna(inplace = True, axis = 0)
plt.figure()
plt.scatter(x = s3['compactness'], y = s3['width'])
plt.xlabel('Compactness')
plt.ylabel('Width')



# BONUS TODO:
# After completing the above, go ahead and run your program
# Check out the results, and see what happens when you add
# in the optional display parameter marker with values of
# either '^', '.', or 'o'.


plt.show()


