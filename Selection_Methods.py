import numpy as np
import random
from random import sample
 
def Roulette_Wheel_Selection(probabilities, Population):
    '''
    This function returns the index of the best choromosome based on the
    calculated probabilities of Selection_Prob_Cal.py
    
    Arguments
    ----------
    probabilities-- dataframe
        probabilities refer to selection Probabilities of Chromosomes,
        coming from Selection_Probabilistics_List in Selection_Prob_Cal.py..
        
    Population-- dataframe
        Population dataframe. In this function, the population is irrelevant
        and is added only for some integration processes.
 
    m-- integer
        m is the sampling size for Tournament Selection. m is redundant for
        Roulette_Wheel_Selection.

    Returns
    -------
    i-- integer
        index of the best chromosome.

    '''
    # (H.B) Generating a random number
    r = random.uniform(0,1)
    # (H.B.) Changing the list of probabilities into an array.
    np_P = np.array(probabilities)
    # (H.B.) Calculating the cumulative probabilities
    np_P_cumsum = np.cumsum(np_P)
    P_cumsum = list(np_P_cumsum)
    
    # (H.B.) Find the parent index
    for i in range(0, len(P_cumsum)):
        if r<= P_cumsum[i]:
            return i
            break
    
    
def Tournament_Selection(Population, m):
    '''
    This function returns the index of the best choromosome in a
    comparative environment.
    
    Arguments
    ----------
    probabilities-- dataframe
        probabilities refer to selection Probabilities of Chromosomes,
        coming from Selection_Probabilistics_List in Selection_Prob_Cal.py.
        
    Population-- dataframe
        Population dataframe. In this function, the population is irrelevant
        and is added only for some integration processes.
 
    m-- integer
        m is the sampling size for Tournament Selection. 

    Returns
    -------
    i-- integer
        index of the best chromosome.
    '''

    Selected_Parents = Population.sample(n = m)
    Selected_Parents = Selected_Parents.sort_values(by = ['Cost'])
    Index = Selected_Parents.index[0]
    return Index

    
    
'''
from Func import MinOne
import pandas as pd        
Boundries = pd.read_excel('C:\\HAMED\\Instadooni\\Products\\Genetic Algorithm\\Code\Python\\Data Sample\\Boundries.xlsx')         
from Initialization import pop_initialization
Population = pop_initialization (nVar=6, nPop=10, Boundries=Boundries, Func= MinOne)['pop']        


from Selection_Prob_Cal import Weighting_By_Rank, Weighting_By_Cost
probabilities = Weighting_By_Rank (kept_Population = kept_Population, Population = Population)
probabilities = Weighting_By_Cost (kept_Population = kept_Population, Population = Population)
'''