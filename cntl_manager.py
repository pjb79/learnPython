def fileLocationMap(searchDirs):
    import os
    import itertools
    import numpy as np    
    
    flm = []
    fileInd = []
    
    for sDir in searchDirs:
        currentDirFiles = os.listdir(sDir)    
    
        for f in currentDirFiles:
            fileInd.append(os.path.isfile(sDir + f))
            flm.append(sDir + f)
    
    flm = list(itertools.compress(flm, fileInd))
    flm = np.array(flm)
    
    return flm

def varLocationMap(flm):
    import numpy as np
    import sim_manager as sm
      
    vlm = np.empty((0,2))
    
    for f in flm:
        simNames = np.array(sm.getSimNames(f))
        fileLocations = np.tile(f,len(simNames))
        fileVLM = np.vstack([fileLocations,simNames]).T
        vlm = np.vstack([vlm,fileVLM])
    
    vlm = dict(zip(vlm[:,1], vlm[:,0]))
    return vlm

    
def readCntlFile(cntlPath):
    import numpy as np
    import pandas as pd
    import os
    import itertools
    import h5Test as h5
    
    df=pd.read_excel(cntlPath)
    
    n = len(df.index)
    
    for r in range(0,n):
        if(pd.isnull(df.iloc[r,0])):
            df.iloc[r,0] = df.iloc[r-1,0]
            
    ind = df['account name'] == "Standard"
    df = df.loc[ind,:]
    
    searchDirs = df['directories to be searched']
    ind = pd.notnull(searchDirs)
    searchDirs = searchDirs[ind].tolist()
    
    searchDirs = [str.replace(d,'YYYY_MM','2016-06') for d in searchDirs]
    searchDirs = [str.replace(d,'Y:\\Forecasting & Simulation','c:\d\mirror') for d in searchDirs]    
    
    varNames = df['variable name (If blank, all variables are obtained)']
    ind = pd.notnull(varNames)
    varNames = varNames[ind].tolist()
    
    flm = fileLocationMap(searchDirs)
    vlm = varLocationMap(flm)
    
    yield varNames
    yield vlm
   





