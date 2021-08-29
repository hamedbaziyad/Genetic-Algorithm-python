# Genetic-Algorithm-python
This repository helps you to optimize an objective function by Genetic Algorithm (GA) in the Python environment.
This project comprises seven files, namely Func.py, Initialization.py, Selection_Prob_Cal.py, Selection_Methods.py, Crossovers.py, Mutations.py and CGA.py.
## 1. Func.py
In this section, desired functions that you want to optimize are defined. The functions are utilized for calculating the costs of chromosomes. For instance, the MinOne and Sphere functions were represented there. You can add every function in this file.
## 2. Initialization.py
This file includes a function called *pop_initialization*, creating the initial population for GA. Defined functions in *Func.py* are employed for calculating the chromosomes' costs here.
## 3. Selection_Prob_Cal.py
This file calculates the *selection probability* of each chromosome in kept population. Chromosomes with fewer costs have more chances to select as parents, deciding to create offsprings. It is important that this file only calculates the Chromosomes' probabilities. The probabilities are used in a variable entitled *selection_probabilistics* for choosing the best chromosomes. Finally, the selected parents from *selection_probabilistics* are fed to some selection methods (prepared in Selection_Methods file) such as Roulette Wheel (or Weighted Random Pairing).
## 4. Selection_Methods.py
A list of selection methods is prepared in this file, returning the index of the best chromosomes for creating new offspring.
## 5. Crossovers.py
A list of crossover functions is listed in this file, trying to merge selected parents for creating new children. Selected parents come from the output of *Selection_Methods.py*.
## 6. Mutations.py
Mutation functions are defined in Mutations.py, attempting to mutate the chromosomes.
## 7. CGA.py
CGA.py is the main file, employing six other files for the execution of the Genetic Algorithm.
