def main():
    import numpy as np
    import scipy
    import matplotlib.pyplot as plt
    
    x=[]
    x.append(948)
    x.append(["ghf"])
    
    y=["cfgg"]
    
    z=x+y
    
    
    
    
    print(z[1])
    
    for e in z:
        print(e)
    
    g={"fshhf":"fhfu"}
    
    print(g["fshhf"])
        
    z1=scipy.randn(5000,10)
    z1mean = np.mean(z1,0)
    z1vol = np.std(z1,0)
    z1Adj = (z1-z1mean)/z1vol
    
    z1mean = np.mean(z1Adj,0)
    z1vol = np.std(z1Adj,0)
    
    plt.hist(z1Adj[:,1]**2,100)
    plt.figure()
    plt.scatter(z1Adj[:,1],z1Adj[:,2]**2)
    
    testFunc("test string")

    return

def testFunc(param):
    print(param)
    return