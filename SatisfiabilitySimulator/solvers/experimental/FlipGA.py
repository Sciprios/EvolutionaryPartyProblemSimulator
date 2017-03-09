from collections import Counter
from SatisfiabilitySimulator.Solvers.FlipGA import FlipGA
import random

class FlipGA_AES(FlipGA):
    """ FlipGA Class which counts fitness evaluations. """

    def _heuristic_method(self, population):
        """ Perform the flip heuristic on the children provided. """
        for org in population:
            rand_perm = list(range(0, len(self._variables)))  # Random permutations for flipping
            random.shuffle(rand_perm)
            improve = 1
            while improve > 0:  # Keep flipping until we stop improving the solution
                improve = 0
                i = 0
                while i < len(self._variables): # For all variables
                    prev_res = self._calc_clausal_score(org)    # Get clausal score currently
                    prev_val = org[self._variables[rand_perm[i]]]
                    self._eval_count = self._eval_count + 1   # Increment Counter
                    if prev_val: # Flip the gene
                        org[self._variables[rand_perm[i]]] = False
                    else:
                        org[self._variables[rand_perm[i]]] = True
                    new_res = self._calc_clausal_score(org)
                    self._eval_count = self._eval_count + 1   # Increment Counter
                    if new_res >= prev_res:
                        improve = improve + (new_res - prev_res)
                    else:
                        org[self._variables[rand_perm[i]]] = prev_val  # The flip didn't help so reset
                    i = i + 1

    def _evaluation(self):
        """ Populates the fitness_value instance variable with the pop's values. """
        self.fitness_values.clear() # Empty fitness values
        for o in self.population:   # Add each organisms fitness value
            cnt = Counter(self._EQUATION.get_clause_evaluation(o))
            self._eval_count = self._eval_count + 1
            self.fitness_values.append(cnt[True])
    

class FlipGA_1(FlipGA_AES):
    """ FlipGA mutation method one (Randomly). """

    def _mutation(self, cur_pop):
        """ Mutates the provided population. """
        for i in cur_pop:
            r = random.random()
            if r < self._MUTATION_RATE: # Do we mutate this organism?
                for var in self._variables:
                    r = random.random()
                    if r < self._MUTATION_RATE: # Do we mutate this variable?
                        i[var] = not i[var]

class FlipGA_2(FlipGA_AES):
    """ FlipGA mutation method two (Partial flip). """

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

class FlipGA_3(FlipGA_AES):
    """ FlipGA mutation method three (Forced Positive). """

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
                    self._eval_count = self._eval_count + 1   # Need to increment counter
            cnt = cnt + 1