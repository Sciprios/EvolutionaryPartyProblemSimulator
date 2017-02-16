from solvers.GeneticAlgorithm import GeneticAlgorithm
from pprint import PrettyPrinter
from collections import Counter
import random

printer = PrettyPrinter(indent=4)

class BlindGA(GeneticAlgorithm):
    """ An implementation of the FlipGA Algorithm. """

    def __init__(self, eq, vars):
        """ Initialise the constant variables. """
        self._NUM_PARENTS = 2
        self._EQUATION = eq
        self._MUTATION_RATE = 0.5
        self._POP_SIZE = 10
        self._MAX_GENERATIONS = 500
        self._variables = vars
    
    def _heuristic_method(self, population):
        """ Perform the flip heuristic on the children provided. """
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
    
    def _evaluation(self):
        """ Populates the fitness_value instance variable with the pop's values. """
        self.fitness_values.clear() # Empty fitness values
        for o in self.population:   # Add each organisms fitness value
            cnt = Counter(self._EQUATION.get_clause_evaluation(o))
            self.fitness_values.append(cnt[True])

    def _parent_selection(self, fitness_values):
        """ Selects the number of parents required given the organisms fitness values. """
        parents = []
        used = []
        while len(used) < self._NUM_PARENTS:
            i = -1
            max_i = 0
            while i < len(fitness_values):
                if ((fitness_values[i] > fitness_values[max_i]) or (i == -1)) and (i not in used):
                    max_i = i
                i = i + 1
            parents.append(self.population[max_i])
            used.append(max_i)
        return parents

    def _reproduction(self, parents):
        """ Generates children from the provided parents using a randomly chosen split value. """
        r = random.randint(0, len(self._variables)) # Generate a random point for swapping

        # First child takes first part of first parent
        child_a = {}
        child_b = {}
        i = 0
        for v in self._variables:   # Determine the child's value for each variable
            if i < r:
                child_a[v] = parents[0][v]
                child_b[v] = parents[1][v]
            else:
                child_a[v] = parents[1][v]
                child_b[v] = parents[0][v]
            i = i + 1
        return [child_a, child_b]

    def _mutation(self, cur_pop):
        """ Mutates the provided population. """
        for i in cur_pop:
            r = random.random()
            if r < self._MUTATION_RATE: # Do we mutate the organism?
                r = random.randint(0, len(self._variables) - 1) # Which random variable to mutate
                i[self._variables[r]] = not i[self._variables[r]]   # Invert it

    def run(self):  # pragma: no cover
        """ Executes the genetic algorithm. """
        self.finished = False
        self.generation = 0
        self.initialisation()   # Setup of initial population
        self._evaluation()
        # Carry on until we run out of generations or we found a solution
        while (len(self._EQUATION._clauses) not in self.fitness_values) and (self.generation < self._MAX_GENERATIONS):
            self.next_generation = []
            self.generation = self.generation + 1
            while len(self.next_generation) < self._POP_SIZE:    # Generate a new population
                parents = self._parent_selection(self.fitness_values)
                children = self._reproduction(parents)
                self._mutation(children)
                self.next_generation.extend(children)
                
            self._repopulate(self.next_generation)
            self._evaluation()
            print("Generation: {} - Best Fitness: {}".format(self.generation, self.get_best_org()['fitness']))
        self.finished = True
        printer.pprint("Best organism:")
        printer.pprint(self.get_best_org())