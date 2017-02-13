from solvers.HeuristicAlgorithm import HeuristicAlgorithm
from pprint import PrettyPrinter
from collections import Counter
import random

printer = PrettyPrinter(indent=4)

class EvoSAP(HeuristicAlgorithm):
    """ The EvoSAP algorithm. """

    def __init__(self, eq, vars):
        """ Instantiates the instance variables. """
        self._NUM_PARENTS = 1
        self._EQUATION = eq
        self._MUTATION_RATE = 0.5
        self._POP_SIZE = 1
        self._MAX_GENERATIONS = 500
        self._TABLE_SIZE = 10   # Var
        self._variables = vars
    
    def run(self):
        """ Runs the evolutionary algorithm. """
        self.initialisation()
    
    def initialisation(self):
        """ Instantiates the organism. """
        org = {}
        for v in self._variables:   # Randomly determine the value for each variable.
            val = None
            if random.random() < 0.5:
                val = False
            else:
                val = True
            org[v] = val
        self.population = [org]
    
    def _mutation(self, cur_pop):
        """ Mutates the provided population. """
        for i in cur_pop:
            r = random.random()
            if r < self._MUTATION_RATE: # Do we mutate the organism?
                r = random.randint(0, len(self._variables) - 1) # Which random variable to mutate
                i[self._variables[r]] = not i[self._variables[r]]   # Invert it
    
    def _heuristic_method(self, population):
        """ Performs a determined heuristic on the population. """
        for org in population:
            rand_perm = random.shuffle(list(range(0, len(self._variables))))  # Random permutations for flipping
            improve = 1
            while improve > 0:  # Keep flipping until we stop improving the solution
                improve = 0
                i = 0
                while i < len(self._variables): # For all variables
                    prev_res = self._calc_clausal_score(org)    # Get clausal score currently
                    prev_val = org[self._variables[i]]
                    if prev_val: # Flip the gene
                        org[self._variables[i]] = False
                    else:
                        org[self._variables[i]] = True
                    new_res = self._calc_clausal_score(org)
                    if new_res >= prev_res:
                        improve = improve + (new_res - prev_res)
                    else:
                        org[self._variables[i]] = prev_val  # The flip didn't help so reset
                    i = i + 1

    def _adaptive_heuristic(self, population):
        """ An adaptive heuristic used in ASAP. """
        pass