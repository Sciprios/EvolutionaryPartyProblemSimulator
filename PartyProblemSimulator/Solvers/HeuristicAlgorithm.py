from PartyProblemSimulator.Solvers.GeneticAlgorithm import GeneticAlgorithm
from random import shuffle

class HeuristicAlgorithm(GeneticAlgorithm):
    """ Defines the method for heuristic algorithms. """

    def _evolve(self, equation):
        """ Evolves the population a single generation. """
        new_population = []
        parents = self._selection(equation)
        new_population.extend(self._reproduction(parents))
        self._mutation(new_population)
        self._heuristic_method(new_population, equation)
        self._repopulate(new_population)

    def _heuristic_method(self, new_population, equation): # pragma: no cover
        """ Applies a local search heuristic on the population. """
        for organism in new_population:
            # Generate a random permutation of the genes
            random_permutation =  shuffle(list(range(0, len(organism.get_genes()))))
            improve = 1
            counter = 0
            while improve > 0:  # Flip until we stop improving the organism
                improve = 0
                self._increment_eval_count()    # Evaluating before flip
                old_fitness = organism.evaluate(equation)
                current_value = organism.get_genes()[counter].get_data() # Flip the next gene in list
                organism.get_genes()[counter].set_data(not current_value)
                self._increment_eval_count()    # Did we make an improvement?
                new_fitness = organism.evaluate(equation)
                if new_fitness >= old_fitness:
                    improve = improve + (new_fitness - old_fitness) # We did! Increment improvement
                else:
                    current_value = organism.get_genes()[counter].get_data() # We didn't :( Revert the flip
                    organism.get_genes()[counter].set_data(not current_value)
                counter = counter + 1