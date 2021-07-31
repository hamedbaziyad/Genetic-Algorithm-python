import math

'''
This file calculates the selection probability of each chromosome in kept
population. Chromosomes with fewer costs have more chances to select
as parents,  deciding to create children. It is important that this file
only calculates the Chromosomes' probabilities. The probabilities are used
in a variable entitled selection_probabilistics for choosing the best
chromosomes. Finally, the selected parents from selection_probabilistics
are fed to some selection methods (prepared in Selection_Methods file) such as
Roulette Wheel (or Weighted Random Pairing).
'''
def Weighting_By_Rank (kept_Population, Population):
    
    '''
    This function calculates the chromosomes' selection probabilities by
    weighting based on their ranks. Indeed, the lower rank, the more chance
    to select.
    
    Arguments
    ----------
    kept_Population-- dataframe
        It is comprising a sorted set of chromosomes based on their costs.
        Thus, it is a subset of the best population.
        
    Population-- dataframe
        Population dataframe. In this function, the population is irrelevant
        and is added only for some integration processes.

    Returns
    -------
    Selection_Probabilistics_List-- list
        Selection Probabilities of Chromosomes.
    '''
    # (H.B.)  Number_of_Kept_Chromosomes refers to the number of remained
    # chromosomes for parent selection.
    Number_of_Kept_Chromosomes = len(kept_Population)
    
    # (H.B.) Probs_numerator: numerator of probabilities.
    Probs_numerator = []
    for i in range(0,len(kept_Population)):
        numerator = (Number_of_Kept_Chromosomes-(i+1)+1)
        Probs_numerator.append(numerator)
        
    # (H.B.) Sum_Probs_numerator: denominator of probabilities.
    Sum_Probs_numerator = sum(Probs_numerator)
    
    # (H.B.) Selection_Probabilistics_List refers the probabilistic of
    #  selection of each chromosome
    Selection_Probabilistics_List = []
    
    for i in range(0, len(kept_Population)):
        Normed = Probs_numerator[i]/Sum_Probs_numerator
        Selection_Probabilistics_List.append(Normed)
    
    return Selection_Probabilistics_List




def Weighting_By_Cost (kept_Population, Population):
    '''
    This function calculates the chromosomes' selection probabilities by
    weighting based on their costs. Indeed, the lower cost, the more chance
    to select.
    
    Arguments
    ----------
    kept_Population-- dataframe
        It is comprising a sorted set of chromosomes based on their costs.
        Thus, it is a subset of the best population.
        
    Population-- dataframe
        Population dataframe. In this function, the population is not
        irrelevant here.

    Returns
    -------
    Selection_Probabilistics_List-- list
        Selection Probabilities of Chromosomes.
    '''
    # (H.B.)  Number_of_Kept_Chromosomes refers to the number of remained
    # chromosomes for parent selection.
    Number_of_Kept_Chromosomes = len(kept_Population)
    
    # (H.B.) Probs_numerator: numerator of probabilities.
    Probs_numerator = []
    # (H.B.) Max_Cost refers to maximum cost in population.
    Max_Cost = Population['Cost'].iloc[Number_of_Kept_Chromosomes]
    #print(Population)
    for i in range(0,len(kept_Population)):

        numerator = abs((kept_Population['Cost'].iloc[i]+0.000001)-Max_Cost)
        Probs_numerator.append(numerator)
    
    # (H.B.) Sum_Probs_numerator: denominator of probabilities.
    Sum_Probs_numerator = sum(Probs_numerator)

    # (H.B.) Selection_Probabilistics_List refers the probabilistic of
    #  selection of each chromosome    
    Selection_Probabilistics_List = []
    for i in range(0, len(kept_Population)):
        Normed = Probs_numerator[i]/Sum_Probs_numerator
        Selection_Probabilistics_List.append(Normed)
        
    return Selection_Probabilistics_List


'''
TEST
from Func import MinOne
import pandas as pd        
Boundries = pd.read_excel('C:\\HAMED\\Instadooni\\Products\\Genetic Algorithm\\Code\Python\\Data Sample\\Boundries.xlsx')         
from Initialization import pop_initialization
Population = pop_initialization (nVar=6, nPop=10, Boundries=Boundries, Func= MinOne)['pop']        
Population = Population.sort_values(by = ['Cost'])
kept_Population = Population.iloc[0:5]

Weighting_By_Rank (kept_Population = kept_Population, Population = Population)
Weighting_By_Cost (kept_Population = kept_Population, Population = Population)
'''