class GeneticAlgorithm(object):
    """ A genetic algorithm evolves a solution to a problem. """
    
    def __init__(self, max_generations):
        """ Initializes the instance level variables. """
        self._eval_count = 0
        self._repopulate([])    # Empty population
        self._set_generation(0)
        self._set_best_genome(None)
        self._set_max_generation(max_generations)
        self._set_mutation_rate(0.5)
        self._history_evaluations = []
        self._history_fitness = []
        self._set_finished_flag(False)
    
    def run(self, equation, no_vars):  # pragma: no cover
        """ Runs the genetic algorithm on the given equation. """
        self._history_evaluations = []
        self._history_fitness = []
        self._set_generation(0) # Reset algorithm attributes
        self._set_finished_flag(False)
        self._reset_eval_count()
        self._initialise(no_vars)  # Initialize a population
        while (self.get_generation() <= self.get_max_generation()) and ((self.get_best_genome() is None) or (self.get_best_genome().evaluate(equation) != 1)):
            self._set_generation(self.get_generation() + 1)
            self._evolve(equation)
            self._history_fitness.append(self.get_best_genome().evaluate(equation))
            self._history_evaluations.append(self.get_num_evaluations())
            print("Generation: {} - Best Fitness: {}".format(self.get_generation(), self.get_best_genome().evaluate(equation)))
        self._set_finished_flag(True)
        print("Algorithm finished with {} evaluations.".format(self.get_num_evaluations()))
    
    def _initialise(self): # pragma: no cover
        """ Initializes the population of organisms. """
        raise NotImplementedError("The initialise method has not been implemented by the base class {}".format(type(self)))
    
    def _evolve(self, equation): # pragma: no cover
        """ Evolves the instance's population through a single generation. """
        new_population = []
        parents = self._selection(equation)
        new_population.extend(self._reproduction(parents))
        self._mutation(new_population)
        self._repopulate(new_population)
    
    def _selection(self, equation): # pragma: no cover
        """ Selection of parents from the population and identifies the best genome. """
        raise NotImplementedError("The _selection method has not been inherited by the base class {}".format(type(self)))

    def _reproduction(self, parents): # pragma: no cover
        """ Reproduces children based on the selected parents. """
        raise NotImplementedError("The _reproduction method has not been inherited by the base class {}".format(type(self)))

    def _mutation(self, new_population): # pragma: no cover
        """ Mutates the new population. """
        raise NotImplementedError("The _mutation method has not been inherited by the base class {}".format(type(self)))

    def _repopulate(self, new_population): # pragma: no cover
        """ Repopulates the population of this genetic algorithm. """
        self._population = new_population

    def _set_generation(self, gen): # pragma: no cover
        """ Sets the generation. """
        if gen >= 0 :
            self._generation = gen
        else:
            self._generation = 0
    
    def _set_best_genome(self, best): # pragma: no cover
        """ Safely sets the best genome. """
        self._best_genome = best
    
    def _set_mutation_rate(self, mut_rate): # pragma: no cover
        """ Sets the mutation rate of this method. """
        if mut_rate < 0:
            self._mutation_rate = 0
        elif mut_rate > 1:
            self._mutation_rate = 1
        else:
            self._mutation_rate = mut_rate
    
    def _increment_eval_count(self): # pragma: no cover
        """ Increments the number of evaluations. """
        self._eval_count = self._eval_count + 1
    
    def _set_max_generation(self, max): # pragma: no cover
        """ Sets the max generation of the algorithm. """
        if max > 0:
            self._max_generation = max
        else:
            self._max_generation = 1
    
    def _set_finished_flag(self, flag):
        """ Sets the finished flag. """
        self._finished = flag

    def _reset_eval_count(self): # pragma: no cover
        """ Resets the evaluation count to 0. """
        self._eval_count = 0
    
    def _add_organism(self, new_org): # pragma: no cover
        """ Adds an organism to the population. """
        self._population.append(new_org)

    def get_best_genome(self): # pragma: no cover
        """ Retrieves the best genome from the population. """
        return self._best_genome

    def get_max_generation(self): # pragma: no cover
        """ Retrieves the maximum generation. """
        return self._max_generation
    
    def get_mutation_rate(self): # pragma: no cover
        """ Retrieves the mutation rate. """
        return self._mutation_rate

    def get_population(self): # pragma: no cover
        """ Retrieves the population. """
        return self._population

    def get_generation(self): # pragma: no cover
        """ Retrieves the current generation this algorithm is on. """
        return self._generation
    
    def get_num_evaluations(self): # pragma: no cover
        """ Retrieves the number of evaluations this method has used. """
        return self._eval_count
    
    def is_finished(self): # pragma: no cover
        """ Determines if this GA is finished. """
        return self._finished
    
    def get_evaluation_history(self): # pragma: no cover
        """ Retrieves the history of evaluation count. """
        return self._history_evaluations
    
    def get_fitness_history(self): # pragma: no cover
        """ Retrieves the history of best fitness. """
        return self._history_fitness