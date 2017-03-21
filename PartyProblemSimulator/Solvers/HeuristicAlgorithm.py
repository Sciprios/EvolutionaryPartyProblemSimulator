from PartyProblemSimulator.Solvers.GeneticAlgorithm import GeneticAlgorithm

class HeuristicAlgorithm(GeneticAlgorithm):
    """ Defines the method for heuristic algorithms. """

    def _evolve(self):
        """ Evolves the population a single generation. """
        new_population = []
        parents = self._selection()
        new_population.extend(self._reproduction(parents))
        self._mutation(new_population)
        self._heuristic_method(new_population)
        self._repopulate(new_population)

    def _heuristic_method(self, population):
        """ Performs a determined heuristic on the population. """
        raise NotImplementedError("The _heuristic_method method has been inherited and not implemented by class {}".format(type(self)))