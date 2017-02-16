from solvers.GeneticAlgorithm import GeneticAlgorithm

class HeuristicAlgorithm(GeneticAlgorithm):
    """ Defines the method for heuristic algorithms. """

    def _heuristic_method(self, population):
        """ Performs a determined heuristic on the population. """
        raise NotImplementedError("The _heuristic_method method has been inherited and not implemented by class {}".format(type(self)))