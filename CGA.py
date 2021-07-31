import numpy as np
import pandas as pd
import numpy.matlib
import random
import matplotlib.pyplot as plt
import math
plt.style.use('seaborn-whitegrid')
# (H.B.) Importing the goal functions from Func.py
from Func import MinOne, Sphere, Sphere_np
# (H.B.) Importing the initialization methods from Initialization.py
from Initialization import pop_initialization
# (H.B.) Importing the Crossover function from Crossovers.py
# (H.B.) Single Crossiver: Single_Point_Crossover
# (H.B.) Double Point Crossover : Double_Point_Crossover
from Crossovers import Single_Point_Crossover, Double_Point_Crossover
# (H.B.) Uniform Crossover : Uniform_Crossover
# (H.B.) Uniform Crossover for continuous variables or mixed problems:
# Continuous_Uniform_Crossover
from Crossovers import Uniform_Crossover, Continuous_Uniform_Crossover
# (H.B.) Selection_Pros: calculation of the parents selection
# probabilities: Selection_Pros is utilized in the context of Roulette Wheel
from Selection_Prob_Cal import Weighting_By_Rank, Weighting_By_Cost
# (H.B.) Importing the parent selection methods from Selection_Methods
from Selection_Methods import Roulette_Wheel_Selection, Tournament_Selection
# (H.B.) Importing the mutation methods
from Mutations import Mutation, Hybrid_Mutation




# (H.B.) The Address refers to the location of the file, including lower bounds
# and upper bounds.
Address = 'C:\\HAMED\\Instadooni\\Products\\Genetic Algorithm\\Code\Python\\Data Sample\\Boundries.xlsx'        

def Genetic_Algorithm(Crossover_Rate = 0.3, nPop = 20, Func = MinOne, MaxIt = 30,
                  Mutation_Rate = 0.2, Crossover_Func = Double_Point_Crossover,
                  Selection_Prob_Func = Weighting_By_Rank,
                  Selection_Algorithm = Tournament_Selection,
                  Tournament_Size = 4, nCon = 2,
                  Mutation_Func = Mutation, gamma = 0.3,
                  Keep_Rate = 0.5, file = Address):
    
    '''
    This function creats the initial population for GA.
    
    Arguments
    ----------
    Crossover_Rate-- Scaler
        Percentage of chromosomes that need to be merged.
        
    nPop-- Integer
        Population size.
        
    Func-- function
        Cost function of our problem.

    MaxIt-- Integer
        Maximum number of iterations.
   
    Mutation_Rate-- scaler
        Percentage of chromosomes that need to be mutated.        

    Crossover_Func-- Function
        Crossover function. 

    Selection_Prob_Func-- Function
        Selection_Prob_Func comprised a list of functions, calculating the
        probability of being selected as a parent. In this package, Roulette
        Wheel Selection utilizes this probability.
        
    Selection_Algorithm-- Function
        This function tries to find the best parents for creating new children 
        (offsprings).
        
    Tournament_Size-- Integer
       When you want to use the Tournament Selection method for finding the
       best parents, you need to determine Tournament_Size. Tournament_Size
       refers to the initial number of chromosomes that participate in the
       tournament

    nCon-- Integer
        The number of continuous variables.

    Mutation_Func-- Function
        Mutation_Func comprised a list of functions, mutating the chromosomes. 
        
    gamma-- Scaler
        It is utilized in Continuous Uniform Crossover for extending the alpha.     
        
    Keep_Rate-- Scaler
        Percentage of the best chromosomes.        
        
    file-- String
        Full address and file name of upper and lower bounds.        

    Parents_Probabilities-- Function
        


    Returns
    -------
    Cache-- dictionary
        It comprises final population, the best chromosome, and the best cost.

    '''
    Cache = {}                        
    Boundries = pd.read_excel(file)   
    nVar = len(Boundries)           
    nDis = nVar - nCon
    Initialized_Pop = pop_initialization (nPop, Boundries, Func)['pop']
    Pop = Initialized_Pop.sort_values(by = ['Cost'])
    Number_Of_Kept_Pop = int(math.ceil(nPop*Keep_Rate))
    Number_of_Crossed_Parents= 2*round((math.ceil(nPop*Crossover_Rate))/2)
    Number_Of_Mutants = math.ceil((nVar)*Mutation_Rate)
    
    Iterations = []       # (H.B.) Sequence of iterations 
    BestCosts = []         # (H.B.) The minimum value of population in each iteration 
                          # is stored in the BestCost list
    BestSols = []          # (H.B.) The best chromosome's position is stored in the 
                          # BestSols list
    WorstCosts = []        # (H.B.) # (H.B.) The best chromosome's position is 
                          # stored in the WorstCosts list
    for it in range(1, MaxIt):
        
        Iterations.append(it)
        BestCosts.append(Pop['Cost'].iloc[0])
        BestSols.append(Pop['Position'].iloc[0])
        WorstCosts.append(Pop['Cost'].iloc[-1])
        Kept_Population = Pop.iloc[0:Number_Of_Kept_Pop]
        BestCost = Pop['Cost'].iloc[0]
        BestIndex = Pop.index[0]
        # (H.B.) Crossover
        Offsprings = []
        for i in range(1, Number_of_Crossed_Parents):
            # (H.B.) Selection algorithm is determined 
            if Selection_Algorithm == Roulette_Wheel_Selection:
                Selection_Probabilities = Selection_Prob_Func(Kept_Population, Pop)
                Parent1_Index = Roulette_Wheel_Selection(
                    Selection_Probabilities, Selection_Probabilities)
                Parent1 = Pop['Position'].iloc[Parent1_Index]
                
                Parent2_Index = Roulette_Wheel_Selection(
                    Selection_Probabilities, Selection_Probabilities)
                Parent2 = Pop['Position'].iloc[Parent2_Index]
            elif Selection_Algorithm == Tournament_Selection:
                Parent1_Index = Tournament_Selection(Kept_Population, Tournament_Size)
                Parent1 = Pop['Position'].iloc[Parent1_Index]
                
                Parent2_Index = Tournament_Selection(Kept_Population, Tournament_Size)
                Parent2 = Pop['Position'].iloc[Parent2_Index]
            else:
                print('Your selection methods is not considered in this code.')
            
            # (H.B.) Crossover function is determined
            if Crossover_Func == Single_Point_Crossover:
                Child1, Child2 = Single_Point_Crossover(Parent1, Parent2)
                
            elif Crossover_Func == Double_Point_Crossover:
                Child1, Child2 = Double_Point_Crossover(Parent1, Parent2)    
            
            elif Crossover_Func == Uniform_Crossover:
                Child1, Child2 = Uniform_Crossover(Parent1, Parent2)     
            
            elif Crossover_Func == Continuous_Uniform_Crossover:
                Child1, Child2 = Continuous_Uniform_Crossover(Parent1, Parent2,
                                                              nDis,
                                                             nCon, gamma) 
            else:
                print('This crossover is not considered in this code.')
                
            Child1 = [Child1]
            Child2 = [Child2]
            
            Child1_Cost = [Func(Child1[0])]
            Child2_Cost = [Func(Child2[0])]
            
            
              
                
            Individual_1 = pd.DataFrame([Child1, Child1_Cost])
            Individual_2 = pd.DataFrame([Child2, Child2_Cost])
            Individual_1 = Individual_1.T
            Individual_2 = Individual_2.T
            
            Offsprings.append(Individual_1)
            Offsprings.append(Individual_2)
            
        Offsprings = pd.concat(Offsprings)
        Offsprings.columns = ['Position', 'Cost']    
        Offsprings.index = range(0, len(Offsprings))
        
        Pop = Kept_Population.append(Offsprings, ignore_index=True)
        Pop.index = list(range(0, len(Pop)))
        Pop = Pop.sort_values(by = ['Cost'])
        # (H.B.) Mutation
        for i in range(0, Number_Of_Mutants):
            
            r = random.randint(0, len(Pop)-1)
            if Mutation_Func == Mutation:
                Pop['Position'].iloc[r] = Mutation(Pop['Position'].iloc[r],
                                                   Boundries, nVar, Mutation_Rate)
                Pop['Cost'].iloc[r] = Func(Pop['Position'].iloc[r])
                
            elif Mutation_Func == Hybrid_Mutation:
                Pop['Position'].iloc[r] = Hybrid_Mutation(Pop['Position'].iloc[r],
                                                   Boundries, nVar, Mutation_Rate, nDis)
                Pop['Cost'].iloc[r] = Func(Pop['Position'].iloc[r])

        Pop = Pop.sort_values(by = ['Cost'])
        print("Iteration {} from {}".format(it, MaxIt))
        

    Cache["Population"] = Pop
    Cache["BestSol"] = Pop["Position"].iloc[0]
    Cache["BestCost"] = Pop["Cost"].iloc[0]
    Cache["Iterations"] = Iterations
    Cache["BestCosts"] = BestCosts
    Cache["BestSols"] = BestSols
    Cache["WorstCosts"] = WorstCosts
    return Cache


GA = Genetic_Algorithm(Crossover_Rate = 0.3, nPop = 20, Func = MinOne, MaxIt = 100,
                  Mutation_Rate = 0.2, Crossover_Func = Uniform_Crossover,
                  Selection_Prob_Func = Weighting_By_Rank,
                  Selection_Algorithm = Tournament_Selection,
                  Tournament_Size = 4, nCon = 2,
                  Mutation_Func = Hybrid_Mutation, gamma = 0.01,
                  Keep_Rate = 0.5, file = Address)        

plt.plot(GA["Iterations"], GA["BestCosts"], color='blue')        
#plt.plot(GA["Iterations"], GA["WorstCosts"], color='yellow')        
print(GA["BestCosts"])
        
