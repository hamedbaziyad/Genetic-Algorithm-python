import pandas as pd
import numpy as np
import random
import numpy.matlib

from Func import MinOne


def pop_initialization (nPop, Boundries, Func):
    
    '''
    This function creats the initial population for GA.
    
    Arguments
    ----------
    nVar-- Integer
        Number of Variables or length of chromosomes.
        
    nPop-- Integer
        Population size.
        
    Boundries-- TYPE
        upper bounds and lower bounds of variables.
        

    Returns
    -------
    cache-- dictionary
        values of chromosomes and their costs.

    '''
    cache = {}
    
    nVar = len(Boundries)
    # (H.B.) Position is chromosomes' structure
    Position = [[0 for i in range(0, nVar)]]
    
    # (H.B.) Cost is the chromosome value
    Cost = [0]
    
    # (H.B.) Empty_Individual is a set of chromosome structure and
    # chromosome costs
    Empty_Individual = pd.DataFrame([Position, Cost])
    
    # (H.B.) Transposing the self.Empty_Individual
    Empty_Individual = Empty_Individual.T
    cache["Empty_Individual"] = Empty_Individual
    
    # (H.B.) pop is all of chromosomes' structures and costs
    pop = np.matlib.repmat(Empty_Individual, nPop, 1)
    pop = pd.DataFrame(pop)
    pop.columns = ['Position', 'Cost']
    
    #Boundries = pd.read_excel(Boundries_File)
    # (H.B.) Filling the chromosomes with random integers
    for POP in range(0, nPop):
        RANDS = []
        
        for VAR in range(
                0, nVar):
            Low = Boundries['Lower'].iloc[VAR]
            Up = Boundries['Upper'].iloc[VAR] 
            Rand_Int = random.randint(Low, Up)
            RANDS.append(Rand_Int) 
        pop['Position'].iloc[POP] = RANDS
        pop['Cost'].iloc[POP] = Func(RANDS)
    
  
    cache["pop"] = pop
   
    return cache
#Boundries = pd.read_excel('C:\\HAMED\\Instadooni\\Products\\Genetic Algorithm\\Code\Python\\Data Sample\\Boundries.xlsx') 
#pop_initialization (nVar=5, nPop=10, Boundries=Boundries, Func=MinOne)["pop"]