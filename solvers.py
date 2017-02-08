""" This module contains classes which are capable of solving SAT problems. """
from abc import ABC, abstractmethod
import random

class GeneticAlgorithm(ABC):
    """ An abstract genetic algorithm for implementation. """

    _MAX_GENERATIONS = 1000     # Allocate a maximum number of generations for the program to run for
    _POP_SIZE = 10              # Size of the initial population
    _NUM_PARENTS = 2            # The number of parents to be selected
    _EQUATION = None            # The equation being assessed
    _variables = []             # List of variables allowed
    population = []             # List of organisms
    fitness_values = []         # Fitness values in the same order as the population

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
    
    def evaluation(self):
        """ Evaluates a population and returns the fitness values. """
        raise NotImplementedError("The evaluation method has not been inherited by the base class {}".format(type(self)))
    
    def parent_selection(self, fitness_values):
        """ Selects the number of parents required given the organisms fitness values. """
        raise NotImplementedError("The parent_selection method has not been inherited by the base class {}".format(type(self)))
    
    def reproduction(self, parents):
        """ Generates children from the provided parents. """
        raise NotImplementedError("The reproduction method has not been inherited by the base class {}".format(type(self)))
    
    def mutation(self, cur_pop):
        """ Mutates the provided population. """
         raise NotImplementedError("The mutation method has not been inherited by the base class {}".format(type(self)))
    
    def repopulate(self, new_pop):
        """ Places the new population into the instance population. """
        raise NotImplementedError("The mutation method has not been inherited by the base class {}".format(type(self)))