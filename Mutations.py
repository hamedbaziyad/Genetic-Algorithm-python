import random
import math
def Mutation(x, Bounds, TotalVar, Mutation_Rate):
    '''
    This function executes a mutation function on discrete variables in which
    the value of the considered variables is changed randomly.
    
    Arguments
    ----------
    x-- list
        x is the selected chromosome for implementing mutation.
    Bounds-- DataFrame
        Bounds is an excel file comprising upper and lower bounds of variables.
        
    TotalVar-- integer
        Number of variables.
 
    Mutation_Rate-- scaler
        Mutation_ Rate refers to the percentages of variables that are changed
        under the mutation process.
 
    Returns
    -------
    x-- list
        Mutant chromosome.
    '''
    Number_Of_Effected_Gense = math.ceil((TotalVar)*Mutation_Rate)
    for i in range(0, Number_Of_Effected_Gense):
        j = random.randint(0, TotalVar-1)
        Low_Boundry = Bounds['Lower'].iloc[j]
        Upp_Boundry = Bounds['Upper'].iloc[j]
    
        
        Range = list(range(Low_Boundry, Upp_Boundry+1))
        #Range.remove(x[j])
        
        rand_index = random.randint(0, len(Range)-1)
        x[j] = Range[rand_index] 
        
    return x




def Hybrid_Mutation(x, Bounds, TotalVar, Mutation_Rate, nVar_Discrete):
    '''
    This function executes a mutation function on both of discrete and 
    continuous variables in which the value of the considered variables is
    changed randomly.
    
    Arguments
    ----------
    x-- list
        x is the selected chromosome for implementing mutation.
    Bounds-- DataFrame
        Bounds is an excel file comprising upper and lower bounds of variables.
        
    TotalVar-- integer
        Number of variables.
 
    Mutation_Rate-- scaler
        Mutation_ Rate refers to the percentages of variables that are changed
        under the mutation process.
    
    nVar_Discrete-- scaler
        Number of discrete variables
 
    Returns
    -------
    x-- list
        Mutant chromosome.
    '''
    Number_Of_Effected_Gense = math.ceil((TotalVar)*Mutation_Rate)
    for i in range(0, Number_Of_Effected_Gense):
        j = random.randint(0, TotalVar-1)
        Low_Boundry = Bounds['Lower'].iloc[j]
        Upp_Boundry = Bounds['Upper'].iloc[j]
        if j<=nVar_Discrete:

            Range = list(range(Low_Boundry, Upp_Boundry+1))
            #Range.remove(x[j])
            
            rand_index = random.randint(0, len(Range)-1)
            x[j] = Range[rand_index] 
        else:

            sigma = 0.1*(Upp_Boundry - Low_Boundry)
            a = x[j] + sigma*random.gauss(0,1)
            if a < Low_Boundry:
                x[j] = max(a, Low_Boundry)
            elif a>Upp_Boundry:
                x[j] = min(a, Low_Boundry)
            else:
                x[j] = a
    return x


'''
from Func import MinOne
import pandas as pd        
Bounds = pd.read_excel('C:\\HAMED\\Instadooni\\Products\\Genetic Algorithm\\Code\Python\\Data Sample\\Boundries.xlsx')         
from Initialization import pop_initialization
Population = pop_initialization (nVar=6, nPop=10, Boundries=Bounds, Func= MinOne)['pop']   


x = Population['Position'].iloc[0]
'''







