import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
# matplotlib.style.use('ggplot')
#plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
#
df = pd.read_csv('C:\\D\\GitHub\\learnPython\\DAT210x-master\\Module3\\Datasets\\wheat.data', index_col = 'id')


#
# TODO: Create a slice of your dataframe (call it s1)
# that only includes the 'area' and 'perimeter' features
# 
s1 = df[['area','perimeter']]


#
# TODO: Create another slice of your dataframe (call it s2)
# that only includes the 'groove' and 'asymmetry' features
# 
s2 = df[['groove','asymmetry']]

#
# TODO: Create a histogram plot using the first slice,
# and another histogram plot using the second slice.
# Be sure to set alpha=0.75
# 

#s1.hist()

plt.figure()
plt.hist(s1['area'], alpha = 0.75)
plt.hist(s1['perimeter'], alpha = 0.75)

plt.figure()
groove = s2['groove'].dropna(axis = 0)
asymmetry = s2['asymmetry'].dropna(axis = 0)
plt.hist(groove, alpha = 0.75)
plt.hist(asymmetry, alpha = 0.75)



