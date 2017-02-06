""" This module contains a blind genetic algorithm. """

class BlindGA(object):
    """ Blind Genetic Algorithm for a SAT problem. """

    def __init__(self, equation, vars, population_size=10):
        """ Initializes instance variables and a population. """
        self._possible_vars = vars
        self._equation = equation
        self._max_pop_size = population_size
        self.pop = self._init_pop()
    
    def _init_pop(self):
        """ Returns a randomly generated population. """
        pass
    
    def _test_fitness(self, organism):
        """ Determines fitness of a given organism. """
        pass