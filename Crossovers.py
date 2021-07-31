import random
import math
from random import sample 
def Single_Point_Crossover(x1, x2):
    '''
    This function executes a single crossover in which the second parts of the
    chromosomes is changed with each other.
    
    Arguments
    ----------
    x1-- list
        x1 is the first parent position.
    x2-- list
        x2 is the econd parent position.
        
    nVar_Discrete-- integer
        Number of discrete variables.
 
    nVar_Continuous-- integer
        Number of continuous variables. 
        
    gamma-- scaler
        It is not used here.

    Returns
    -------
    (y1, y2)-- integer
        New childeren.
    '''
    nVar = len(x1)
    Cut_Point = random.randint(1, nVar-1)
    y1 = x1[0:Cut_Point] + x2[Cut_Point:]
    y2 = x2[0:Cut_Point] + x1[Cut_Point:]
    return (y1, y2)



def Double_Point_Crossover(x1, x2):
    '''
    This function executes a double point crossover in which the middle parts of the
    chromosomes is interchanged with each other.
    
    Arguments
    ----------
    x1-- list
        x1 is the first parent position.
    x2-- list
        x2 is the econd parent position.
        
    nVar_Discrete-- integer
        Number of discrete variables.
 
    nVar_Continuous-- integer
        Number of continuous variables. 
        
    gamma-- scaler
        It is not used here.

    Returns
    -------
    (y1, y2)-- integer
        New childeren.
    '''
    nVar = len(x1)
    list1 = [i for i in range(1,nVar-1)]
    Cut_Points = sample(list1,2)

        
    Left_Cut_Point = min(Cut_Points)
    Right_Cut_Point = max(Cut_Points)
    y1 = x1[0:Left_Cut_Point] + x2[Left_Cut_Point:Right_Cut_Point] + x1[Right_Cut_Point:]
    y2 = x2[0:Left_Cut_Point] + x1[Left_Cut_Point:Right_Cut_Point] + x2[Right_Cut_Point:]
    return (y1, y2)


def Uniform_Crossover(x1, x2):
    '''
    This function executes a uniform crossover in which every point of a
    chromosome can be interchanged with each other. 
    
    Arguments
    ----------
    x1-- list
        x1 is the first parent position.
    x2-- list
        x2 is the econd parent position.
        
    nVar_Discrete-- integer
        Number of discrete variables.
 
    nVar_Continuous-- integer
        Number of continuous variables. 
        
    gamma-- scaler
        It is not used here.

    Returns
    -------
    (y1, y2)-- integer
        New childeren.
    '''
    nVar = len(x1)
    Alpha = []
    for i in range(0, nVar):
        rand = random.randint(0,1)
        Alpha.append(rand)
    y1 = []   
    y2 = [] 
    for num in range(0, nVar):
        y1.append(Alpha[num]*x1[num] + (1-Alpha[num])*x2[num])
        y2.append((1-Alpha[num])*x1[num] + Alpha[num]*x2[num])
  
    return(y1, y2)



def Continuous_Uniform_Crossover(x1, x2, nVar_Discrete, nVar_Continuous, gamma):
    '''
    This function executes a continuous uniform crossover in which 
    percentage of every point of a chromosome can be interchanged with each
    other. 
    
    Arguments
    ----------
    x1-- list
        x1 is the first parent position.
    x2-- list
        x2 is the econd parent position.
        
    nVar_Discrete-- integer
        Number of discrete variables.
 
    nVar_Continuous-- integer
        Number of continuous variables. 
        
    gamma-- scaler
        It is utilized for extending the intervals.

    Returns
    -------
    (y1, y2)-- integer
        New childeren.
    '''
    Alpha = []
    for i in range(0, nVar_Discrete):
        rand = random.randint(0,1)
        Alpha.append(rand)
    w1 = []   
    w2 = [] 
    for num in range(0, nVar_Discrete):
        w1.append(Alpha[num]*x1[num] + (1-Alpha[num])*x2[num])
        w2.append((1-Alpha[num])*x1[num] + Alpha[num]*x2[num])
    for i in range(0, nVar_Continuous):
        rand = random.uniform(-gamma,1+gamma)
        Alpha.append(rand)
    z1 = []   
    z2 = [] 
    for num in range(nVar_Discrete, len(x1)):
        z1.append(Alpha[num]*x1[num] + (1-Alpha[num])*x2[num])
        z2.append((1-Alpha[num])*x1[num] + Alpha[num]*x2[num])        
    
    y1 = w1 + z1
    y2 = w2 + z2
    return(y1, y2)

'''
from Func import MinOne
import pandas as pd        
Boundries = pd.read_excel('C:\\HAMED\\Instadooni\\Products\\Genetic Algorithm\\Code\Python\\Data Sample\\Boundries.xlsx')         
from Initialization import pop_initialization
Population = pop_initialization (nVar=6, nPop=10, Boundries=Boundries, Func= MinOne)['pop']   


x1 = Population['Position'].iloc[0]
x2 = Population['Position'].iloc[2]
'''







