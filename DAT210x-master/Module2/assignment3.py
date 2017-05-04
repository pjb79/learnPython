import pandas as pd

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
servoData = pd.read_csv('c:\\d\\DAT210x-master\\DAT210x-master\\Module2\\Datasets\\servo.data', header = None, names = ['motor', 'screw', 'pgain', 'vgain', 'class'])


# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
servo5 = servoData.loc[servoData['vgain']==5,:]
print(len(servo5))


# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
servoSlice = servoData.loc[(servoData['motor']=='E') & (servoData['screw']=='E'),:]
print(len(servoSlice))



# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
servoPGAIN = servoData.loc[servoData['pgain']==4,:]
print(servoPGAIN.describe())



# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!



