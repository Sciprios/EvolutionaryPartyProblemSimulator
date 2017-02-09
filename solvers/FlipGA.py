from GeneticAlgorithm import GeneticAlgorithm
import random

class FlipGA(GeneticAlgorithm):
    """ An implementation of the FlipGA Algorithm. """

    def __init__(self, eq, vars):
        """ Initialise the constant variables. """
        self._NUM_PARENTS = 2
        self._EQUATION = eq
        self._MUTATION_RATE = 0.5
        self._POP_SIZE = 10
        self._variables = vars
    
    def _flip_children(self, children):
        """ Perform the flip heuristic on the children provided. """
        for org in children:
            rand_perm = random.shuffle(range(0, len(org)))  # Random permutations for flipping
            improve = 1
            while improve > 0:  # Keep flipping until we stop improving the solution
                improve = 0
                i = 0
                while i < len(org): # For all variables
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
    
    def _evaluation(self):
        """ Populates the fitness_value instance variable with the pop's values. """
        self.fitness_values.clear() # Empty fitness values
        for o in self.population:   # Add each organisms fitness value
            self.fitness_values.append(self._EQUATION.evaluate(o))

    def _parent_selection(self, fitness_values):
        """ Selects the number of parents required given the organisms fitness values. """
        parents = []
        cnt = 0
        used = []
        while cnt < self._NUM_PARENTS:
            i = 0
            max_i = 0
            while i < len(fitness_values):
                if (self.fitness_values[i] > self.fitness_values[max_i]) and (i not in used):
                    max_i = i
                i = i + 1
            parents.append(self.population[i])
            used.append(max_i)

    def _reproduction(self, parents):
        """ Generates children from the provided parents using a randomly chosen split value. """
        r = random.randint(0, len(self._variables) - 1) # Generate a random point for swapping

        # First child takes first part of first parent
        child_a = {}
        child_b = {}
        i = 0
        for v in self._variables:   # Determine the child's value for each variable
            if i <= r:
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
                r = random.randint(0, len(self._variables) - 1)
                i[self._variables[r]] = not i[self._variables[r]]   # Invert the variable

    def run(self):
        """ Executes the genetic algorithm. """
        self.finished = False
        self.generation = 0
        self.initialisation()   # Setup of initial population
        self._local_search(self.population)
        self._evaluation()
        # Carry on until we run out of generations or we found a solution
        while (len(self._variables) not in self.fitness_values) and (self.generation =< self._MAX_GENERATIONS):
            self.next_generation = []
            self.generation = self.generation + 1
            while len(next_generation) < self._POP_SIZE:    # Generate a new population
                parents = self._parent_selection(self.fitness_values)
                children = self._reproduction(parents)
                self._mutation(children)
                self._flip_children(children)
                self.next_generation.extend(children)
        self.finished = True