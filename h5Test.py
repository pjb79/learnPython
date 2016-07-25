def importSimObj(strPath):
    import numpy as np
    import h5py
    
    f = h5py.File(strPath,"r")
    
    simMatrix = np.array(f['simMatrix'])
    simMatrix = np.transpose(simMatrix,(2,1,0))    
    
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
    
    yield simNames
    yield simMatrix
    output = [];
    output.append(simNames)
    output.append(simMatrix)
    return
    

    