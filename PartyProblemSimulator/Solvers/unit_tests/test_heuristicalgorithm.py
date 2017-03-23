from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
from PartyProblemSimulator.Solvers.HeuristicAlgorithm import HeuristicAlgorithm

class TestHeuristicAlgo(TestCase):
    """ Ensures no methods are implemented and throw errors. """

    def test_heuristic(self):
        """ Ensures the heuristic method throws a un-implemented exception. """
        ga = HeuristicAlgorithm(500)
        self.assertRaises(NotImplementedError, ga._heuristic_method, None, None)