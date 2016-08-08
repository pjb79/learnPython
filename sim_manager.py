def getSimNames(strPath):
    import numpy as np
    import h5py
    
    f = h5py.File(strPath,"r")
    
    s = f['simNames'];
    s=s[0].tolist()
    simNames = [];
    
    for simNameRef in s:
    
        simName = f[simNameRef]    
        simName = np.array(simName)
        simName = simName.tolist();
        
        simName = [simNameElement[0] for simNameElement in simName]
    
        simName = ''.join(chr(i) for i in simName)
         
        simNames.append(simName)
    

    return simNames

def getSimData(simName, vlm):
    import numpy as np
    import h5py
    
    simNames = getSimNames(vlm[simName])
    varLoc = simNames.index(simName)
    
    f = h5py.File(vlm[simName],"r")
    
    simMatrix = np.array(f['simMatrix'][:,:,varLoc])
    simMatrix = simMatrix.reshape(5000,600,1)    
    simMatrix = np.transpose(simMatrix,(2,1,0))    
    
    return simMatrix, varLoc
    
def createSimMgrObj(cntlPath, sheet, account):
    
    return   

    

    