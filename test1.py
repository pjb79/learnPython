from h5Test import importSimObj as iSO
import numpy as np
from matplotlib import pyplot as plt

simNames, simMatrix = iSO("C:\\D\Mirror\\dev - 2015-06\\ESG_output_5000sc_600mo\\AUD\\Aud_equity_1.mat")

#output = iSO("C:\\D\Mirror\\dev - 2015-06\\ESG_output_5000sc_600mo\\AUD\\Aud_equity_1.mat")
#simNames = output[0];
#simMatrix = output[1];

#del output

m=np.mean(simMatrix,2)
plt.plot(np.transpose(m))