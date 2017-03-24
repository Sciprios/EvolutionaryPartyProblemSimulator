from PartyProblemSimulator.Solvers.GeneticAlgorithm import GeneticAlgorithm

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

    def _heuristic_method(self, population, equation):
        """ Performs a determined heuristic on the population. """
        raise NotImplementedError("The _heuristic_method method has been inherited and not implemented by class {}".format(type(self)))