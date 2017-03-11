from SatisfiabilitySimulator.Solvers.GeneticAlgorithm import GeneticAlgorithm
from pprint import PrettyPrinter
from collections import Counter
import random

printer = PrettyPrinter(indent=4)

class BlindGA(GeneticAlgorithm):
    """ An implementation of the BlindGA Algorithm. """

    def __init__(self, eq, vars):
        """ Initialise the constant variables. """
        super().__init__()
        self._NUM_PARENTS = 2
        self._EQUATION = eq
        self._MUTATION_RATE = 0.9
        self._POP_SIZE = 10
        self._MAX_GENERATIONS = 5000
        self._variables = vars
    
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
        best = {'gen': -1, 'fit': -1}
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
            # Determine if it's dwindling
            if best['fit'] < self.get_best_org()['fitness']:
                best['fit'] = self.get_best_org()['fitness']
                best['gen'] = self.generation
            else:
                if self.generation > best['gen'] + 5000:
                    break
            print("Generation: {} - Best Fitness: {}".format(self.generation, self.get_best_org()['fitness']))
        self.finished = True
        print("Completed in generation: {}".format(self.generation))