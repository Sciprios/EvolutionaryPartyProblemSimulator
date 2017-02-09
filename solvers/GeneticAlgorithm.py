""" This module contains classes which are capable of solving SAT problems. """
import random

class GeneticAlgorithm(object):
    """ An abstract genetic algorithm for implementation. """

    _MAX_GENERATIONS = 1000     # Allocate a maximum number of generations for the program to run for
    _POP_SIZE = 10              # Size of the initial population
    _NUM_PARENTS = 2            # The number of parents to be selected
    _EQUATION = None            # The equation being assessed
    _MUTATION_RATE = 0          # The mutation rate
    _variables = []             # List of variables allowed
    population = []             # List of organisms
    fitness_values = []         # Fitness values in the same order as the population
    generation = 0              # Current generation
    next_generation = []        # Holds the next generation
    finished = False            # Flag determines whether algorithm has finished or not
    best_org = {}               # A dictionary containing the best organism and relevant fitness value

    def run(self):
        """ Executes the genetic algorithm. """
        raise NotImplementedError("The run method has not been inherited by the base class {}".format(type(self)))

    def initialisation(self):
        """ Initialises a population. """
        cnt = 0
        while cnt < self._POP_SIZE:
            org = {}
            for v in self._variables:
                val = None
                if random.random() < 0.5:
                    val = False
                else:
                    val = True
                org[v] = val
            self.population.append(org)
    
    def _evaluation(self):
        """ Evaluates a population and returns the fitness values. """
        raise NotImplementedError("The evaluation method has not been inherited by the base class {}".format(type(self)))
    
    def _parent_selection(self, fitness_values):
        """ Selects the number of parents required given the organisms fitness values. """
        raise NotImplementedError("The parent_selection method has not been inherited by the base class {}".format(type(self)))
    
    def _reproduction(self, parents):
        """ Generates children from the provided parents. """
        raise NotImplementedError("The reproduction method has not been inherited by the base class {}".format(type(self)))
    
    def _mutation(self, cur_pop):
        """ Mutates the provided population. """
         raise NotImplementedError("The mutation method has not been inherited by the base class {}".format(type(self)))
    
    def _repopulate(self, new_pop):
        """ Places the new population into the instance population. """
        raise NotImplementedError("The mutation method has not been inherited by the base class {}".format(type(self)))
    
    def _calc_clausal_score(self, org):
        """ Calculates the clausal score for this organism. """
        res = self._EQUATION.get_clause_evaluation(org)   # Get truth values for clauses.
        cnt = 0
        for r in res:   # Count number of true clauses
            if r:
                cnt = cnt + 1
        return cnt

    def get_best_org(self):
        """ Returns the best organism in the population. """
        if self.finished:
            i = self.fitness_values.index(max(self.fitness_values)) # Get the index of best organism
            return {'org': self.population[i], 'fitness': self.fitness_values[i]}
        else:
            return None