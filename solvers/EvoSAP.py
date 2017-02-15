from solvers.HeuristicAlgorithm import HeuristicAlgorithm
from pprint import PrettyPrinter
from collections import Counter
import random

printer = PrettyPrinter(indent=4)

class EvoSAP(HeuristicAlgorithm):
    """ The EvoSAP algorithm. (Variation on FlipGA) """

    def __init__(self, eq, vars):
        """ Instantiates the instance variables. """
        self._NUM_PARENTS = 1
        self._EQUATION = eq
        self._MUTATION_RATE = 0.
        self._POP_SIZE = 1
        self._MAX_GENERATIONS = 50
        self._TABLE_SIZE = 10   # Var
        self._variables = vars
    
    def run(self):
        """ Executes the genetic algorithm. """
        self.finished = False
        self.generation = 0
        self.initialisation()   # Setup of initial population
        self._evaluation()
        self._heuristic_method(self.population)
        print("Generation: {} - Best Fitness: {}".format(self.generation, self.get_best_org()['fitness']))
        # Carry on until we run out of generations or we found a solution
        while (len(self._EQUATION._clauses) not in self.fitness_values) and (self.generation < self._MAX_GENERATIONS):
            self.next_generation = []
            self.generation = self.generation + 1
            
            # Generate a new population (1 organism)
            self.next_generation = self._reproduction(self.population)
            self._mutation(self.next_generation)
            self._heuristic_method(self.next_generation)
            
            # IF the new population is better swap with the old one.
            new_fitness = self._evaluation(org=self.next_generation[0])
            if self.fitness_values[0] <= new_fitness:
                self._repopulate(self.next_generation)
            self._evaluation()
            print("Generation: {} - Best Fitness: {}".format(self.generation, self.get_best_org()['fitness']))
        self.finished = True
        print("Completed in generation {} with organism:".format(self.generation))
        printer.pprint(self.get_best_org())
    
    def _evaluation(self, org=None):
        """ Populates the fitness_value instance variable with the pop's values. """
        if org:
            return Counter(self._EQUATION.get_clause_evaluation(org))[True]
        else:
            self.fitness_values.clear() # Empty fitness values
            for o in self.population:   # Add each organisms fitness value
                cnt = Counter(self._EQUATION.get_clause_evaluation(o))
                self.fitness_values.append(cnt[True])
    
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
        for i in cur_pop:   # For each organism (one)
            for j in self._variables:   # For each gene
                r = random.random()
                if r < self._MUTATION_RATE: # Do we mutate this gene?
                    i[j] = not i[j]   # Invert it
    
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
                
    def _reproduction(self, parents):
        """ Generates a child from the single parent chromeosone. """
        child_a = {}
        for v in self._variables:
            child_a[v] = parents[0][v]
        return [child_a]