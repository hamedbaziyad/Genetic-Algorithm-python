import numpy as np 

def MinOne(x):
    z = sum(x)
    return z



def Sphere(x):
    New_List = []
    for t in range(0, len(x)):
        a = x[t]**2
        New_List.append(a)
        
    z = sum(New_List)
    return z


def Sphere_np(x):
    New_List = np.power(x, 2)
     
    z = np.sum(New_List)
    return z



