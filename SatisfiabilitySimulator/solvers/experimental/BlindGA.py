from collections import Counter
from solvers.BlindGA import BlindGA
import random

class BlindGA_AES(BlindGA):
    """ BlindGA Class which counts fitness evaluations. """

    def _evaluation(self, org=None):
        """ Populates the fitness_value instance variable with the pop's values. """
        if org:
            self.eval_count = self.eval_count + 1
            return Counter(self._EQUATION.get_clause_evaluation(org))[True]
        else:
            self.fitness_values.clear() # Empty fitness values
            for o in self.population:   # Add each organisms fitness value
                self.eval_count = self.eval_count + 1
                cnt = Counter(self._EQUATION.get_clause_evaluation(o))
                self.fitness_values.append(cnt[True])
    

class BlindGA_1(BlindGA_AES):
    """ BlindGA mutation method one (Randomly). """

    def _mutation(self, cur_pop):
        """ Mutates the provided population. """
        for i in cur_pop:
            r = random.random()
            if r < self._MUTATION_RATE: # Do we mutate this organism?
                for var in self._variables:
                    r = random.random()
                    if r < self._MUTATION_RATE: # Do we mutate this variable?
                        i[var] = not i[var]

class BlindGA_2(BlindGA_AES):
    """ BlindGA mutation method two (Partial flip). """

    def _mutation(self, cur_pop):
        """ Mutates the provided population. """
        for i in cur_pop:
            r = random.random()
            if r < self._MUTATION_RATE: # Do we mutate this organism?
                r = random.randint(0, len(self._variables) - 1) # Get a random position to mutate before
                cnt = 0
                while cnt <= r: # Invert each variable up to r
                    i[self._variables[cnt]] = not i[self._variables[cnt]]   # Invert
                    cnt = cnt + 1

class BlindGA_3(BlindGA_AES):
    """ BlindGA mutation method three (Forced Positive). """

    def _mutation(self, cur_pop):
        """ Mutates the provided population. """
        cnt = 0
        for i in cur_pop:
            r = random.random()
            if r < self._MUTATION_RATE: # Do we mutate this organism?
                fitness = self.fitness_values[cnt]
                new_fitness = -1
                mut_cnt = 0
                while (new_fitness < fitness) and (mut_cnt < 100):    # Do until we've made a positive change.
                    mutations_made = [] # Remember the mutations made
                    for var in self._variables: # Method 1 mutation
                        r = random.random()
                        if r < self._MUTATION_RATE: # Do we mutate this variable?
                            mutations_made.append(var)
                            i[var] = not i[var]
                    mut_cnt = mut_cnt + 1
                    cnter = Counter(self._EQUATION.get_clause_evaluation(i))
                    new_fitness = cnter[True]
                    self.eval_count = self.eval_count + 1   # Need to increment counter
            cnt = cnt + 1