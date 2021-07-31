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

# (H.B.) Genetic_Algorithm_Contin: The class of GA algorithm
class Genetic_Algorithm_Contin:
    # (H.B.) Class Constructor
    def __init__(self, file, MaxIt, nPop, pc, pm, Func, Crossover_Func, Beta,
                 Selection_Prob_Func, Selection_Algorithm, Tournament_Size, 
                 meautation_Rate, Number_Of_Continuous_Variables, Mutation_Func, gamma, Keep_Rate):
        # (H.B.) file: Includes variables' boundaries (Lower & Upper)
        self.Boundries = pd.read_excel(file)        
        # (H.B.) GA Parameters
        # (H.B.) nVar is Number of Decision Variables
        self.nVar = len(self.Boundries)

        # (H.B.) MaxIt is Maximum Number of Iterations
        self.MaxIt = MaxIt
        
        # (H.B.) nPop is Population Size
        self.nPop = nPop
        
        # (H.B.) pc is Crossover percentage
        self.pc = pc
        
        ''' (H.B.) nc is number of Offsprings (parents)
        nc can be calculated by two methods. The first one is in below
        which you can activate it from the comment mode by deleting the # sign.
        The second one is introduced based on Keep_Rate which you can find it
        in next lines.
        '''
        #self.nc = 2*round(self.pc*self.nPop/2)
        
        # (H.B) pm is Mutation percentage
        self.pm = pm
        
        # (H.B.) nm is Number of Mutants
        self.nm = round(self.pm*self.nPop)
        
        # (H.B.) Initialization

        
        # (H.B.) Empty_Individual is a set of chromosome structure and
        self.Empty_Individual = pop_initialization(
            self.nVar, self.nPop, self.Boundries, Func)['Empty_Individual']
        


        
        # (H.B.) Crossover_Func is crossover function
        self.Crossover_Func = Crossover_Func
        # (H.B.) Beta is seltion pressure
        self.Beta = Beta
        
        # (H.B.) calculation of parents selection probabilistics
        self.Selection_Prob_Func = Selection_Prob_Func
        
        ''' (H.B.) Selection_Algorithm refers to the algorithm that can
        select parents. If you use Roulette Wheel selection method,
        Selection_Prob_Func is utilized.
        '''
        self.Selection_Algorithm = Selection_Algorithm
        
        ''' (H.B.) Tournament_Size is utilized when you select the
        Tournament_Selection rather than Roulette Wheel. Tournament_Size refers
        to the number of initial chromosomes are participating in the
        tournament for the selection of the best parent from them.
        '''        
        self.Tournament_Size = Tournament_Size
        
        # (H.B.) meautation_Rate: meautation rate
        self.meautation_Rate = meautation_Rate
        
        '''
        (H.B.) Number_Of_Continuous_Variables is the number of variables that
        can obtain continuous values. According to the Genetic_Algorithm_Contin
        class, continuous variables must have lied at the end of the file.
        '''
        self.Number_Of_Continuous_Variables = Number_Of_Continuous_Variables
        
        # (H.B.) Mutation_Func: mutation function
        self.Mutation_Func = Mutation_Func
        
        ''' (H.B.) gamma is used for extending the alpha region. gamma is 
        utilized in the era of continuous variables.
        '''
        self.gamma = gamma
        
        # (H.B.) Keep_Rate is the percentage of the population that must be 
        # remained and cannot be inputted for crossover.
        self.Keep_Rate = Keep_Rate
        # (H.B.) The another way of calculating the nc
        self.nc = 2*round((math.ceil(self.nPop*self.Keep_Rate))/2)
        
        # (H.B.) Number of Function Evaluation
        self.NFE = []
        # (H.B.) Filling the chromosomes with random integers
        
        # (H.B.) pop is all of chromosomes' structures and costs
        self.pop = pop_initialization(self.nVar, self.nPop, self.Boundries, Func)['pop']
        # (H.B.) Sort population
        self.pop = self.pop.sort_values(by = ['Cost'])
        #self.nPop = len(self.pop)
        
        # (H.B.) Store the best solution
        self.Best_Solution = self.pop.iloc[0]

        # (H.B.) Each two parents are combined and creat a crossover. 
        # Accordingly, Number_Of_Crossovers equals to half of parents. 

        

        # (H.B.) Main Loop
        ######################################################################       
        # (H.B.) Crossover
        ######################################################################
        self.Iterations = []
        self.BestCost = []
        self.BestSol = []
        self.WorstCost = []
        NFE_In_Each_Iteration = 0
        
        for it in range(1, self.MaxIt):
            ###################################################################
            # (H.B.) Selection Probabilistics Calculation
            print(it)
            self.Worst_Cost = self.pop.iloc[-1]['Cost']
            self.WorstCost.append(self.Worst_Cost)
            self.Sum_Cost = sum(self.pop['Cost'])
            self.Number_Of_Keep = self.nPop-self.nc
            self.Pop_Keep = self.pop.iloc[0:self.Number_Of_Keep]
            self.Pop_Keep.index = range(0,self.Number_Of_Keep)
            #print(self.pop)
            self.Selection_Probabilistics = Selection_Prob_Func(self.Pop_Keep,
                                                                self.pop)
            ###################################################################
            self.Number_Of_Crossovers = int(self.nc)
        
            self.popc = np.matlib.repmat(
                self.Empty_Individual,self.nPop, 1)
            
            self.popc = pd.DataFrame(self.popc)
            self.popc.columns = ['Position', 'Cost']
            Crossed_Parents = []
            
            #for cross in range(0, self.Number_Of_Crossovers):
                
            while len(list(set(Crossed_Parents)))<self.Number_Of_Crossovers:
                # (H.B.) Select First Parent
                i1 = Selection_Algorithm(
                    self.Selection_Probabilistics, self.Pop_Keep,
                    self.Tournament_Size)
                
                p1 = self.pop.iloc[i1]
                # (H.B.) Select Second parent
                i2 = Selection_Algorithm(
                    self.Selection_Probabilistics, self.Pop_Keep,
                    self.Tournament_Size)
                p2 = self.pop.iloc[i2]
                #print(i1,i2)
                # (H.B.) Apply Crossover                
                (pop_k_child_1, pop_k_child_2) = self.Crossover_Func(
                    p1['Position'], p2['Position'], self.nVar - Number_Of_Continuous_Variables,
                    self.Number_Of_Continuous_Variables, self.gamma)
                self.popc['Position'].iloc[i1] = pop_k_child_1
                self.popc['Position'].iloc[i2] = pop_k_child_2
                
                #print((pop_k_child_1, pop_k_child_2))
                #print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                # (H.B.) Evaluate Offsprings
                pop_k_child_1_cost = Func(pop_k_child_1)
                NFE_In_Each_Iteration = NFE_In_Each_Iteration + 1
                pop_k_child_2_cost = Func(pop_k_child_2)
                NFE_In_Each_Iteration = NFE_In_Each_Iteration + 1
                self.popc['Cost'].iloc[i1] = pop_k_child_1_cost
                self.popc['Cost'].iloc[i2] = pop_k_child_2_cost 
                Crossed_Parents.append(i1)
                Crossed_Parents.append(i2)
            
            #self.popc.index = self.pop.index
            
            #print(len(Crossed_Parents))
            self.popc2 = self.popc.drop(Crossed_Parents)
            #print(self.popc2.shape)
            Empty_Indexes = list(self.popc2.index)    
            self.popc = self.popc.drop(Empty_Indexes)
            #print(self.popc.shape)
            #print(self.popc)   
            ###################################################################
            # (H.B.) Mutation
            ###################################################################
            self.popm = np.matlib.repmat(
                self.Empty_Individual, self.nm, 1)
            self.popm = pd.DataFrame(self.popm)
            self.popm.columns = ['Position', 'Cost']
            #print(self.popm)
            
            for k in range(0, self.nm):

                self.N_Keep = self.nPop-self.nc
                # (H.B.) Select Parent
                i = random.randint(1,  self.N_Keep-1)
                
                p = self.pop.iloc[i]
                #print(p['Position'])
                
                #print(Mutation(p['Position']))
                

                Mutant = Mutation_Func(p['Position'], self.Boundries,
                                  self.nVar, self.meautation_Rate,self.nVar - Number_Of_Continuous_Variables)

                self.popm['Position'].iloc[k] = Mutant
                self.popm['Cost'].iloc[k] = Func(Mutant) 

                NFE_In_Each_Iteration = NFE_In_Each_Iteration +1
            ###################################################################
            # (H.B.) Creat merged population
            
            # (H.B.) Sort
            self.pop = self.pop.sort_values(by = ['Cost'])
            self.pop = self.pop.iloc[0:self.N_Keep]

             
            self.pop = pd.concat([self.pop, self.popc, self.popm])
            
            # (H.B.) Truncation
            self.pop = self.pop.sort_values(by = ['Cost'])
            self.pop = self.pop.iloc[0:self.nPop]
            self.pop_Keep = self.pop.iloc[0:self.N_Keep]
            ###################################################################
            # (H.B.) Store the best solution ever found
            self.Best_Sol = self.pop.iloc[0]['Position']
            # (H.B.) Store the best cost ever found
            self.Best_Cost = self.pop.iloc[0]['Cost']
            ###################################################################
            # (H.B.) Store the worst solution ever found
            self.Worst_Cost = self.pop.iloc[-1]['Cost']
            self.WorstCost.append(self.Worst_Cost)
            ###################################################################
            # (H.B.) Show iteration information
            self.Iterations.append(it)
            self.BestCost.append(self.Best_Cost)
            self.BestSol.append(self.Best_Sol)
            self.NFE.append(NFE_In_Each_Iteration)
            #print(self.pop.shape)
        #plt.plot(self.Iterations, self.BestCost, color='green')
        plt.plot(self.NFE, self.BestCost, color='red')
        print(self.BestCost)
        
        
        
Address =   'C:\\HAMED\\Instadooni\\Products\\Genetic Algorithm\\Code\Python\\Data Sample\\Boundries.xlsx'    
p1 = Genetic_Algorithm_Contin(file = Address, MaxIt = 50, nPop = 50, pc = 0.8,
                              pm = 0.1, Func = MinOne,
                                Crossover_Func = Uniform_Crossover,
                                Beta = 8,
                                Selection_Prob_Func = Weighting_By_Cost,
                                Selection_Algorithm = Roulette_Wheel_Selection,
                                Tournament_Size = 4, meautation_Rate = 0.5,
                                Number_Of_Continuous_Variables = 3, 
                                Mutation_Func = Hybrid_Mutation, gamma = 0.1,
                                Keep_Rate = 0.4)   

