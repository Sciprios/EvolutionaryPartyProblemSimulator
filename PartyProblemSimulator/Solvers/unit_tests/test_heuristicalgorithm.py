from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
from PartyProblemSimulator.Solvers.HeuristicAlgorithm import HeuristicAlgorithm

class TestHeuristicAlgo(TestCase):
    """ Ensures no methods are implemented and throw errors. """

    @patch('PartyProblemSimulator.Solvers.HeuristicAlgorithm.HeuristicAlgorithm._repopulate')
    @patch('PartyProblemSimulator.Solvers.HeuristicAlgorithm.HeuristicAlgorithm._heuristic_method')
    @patch('PartyProblemSimulator.Solvers.HeuristicAlgorithm.HeuristicAlgorithm._mutation')
    @patch('PartyProblemSimulator.Solvers.HeuristicAlgorithm.HeuristicAlgorithm._reproduction')
    @patch('PartyProblemSimulator.Solvers.HeuristicAlgorithm.HeuristicAlgorithm._selection')
    def test_evolve(self, select, repro, mut, local_search, repop):
        """ Ensures the evolve method is updated. """
        ga = HeuristicAlgorithm(0)
        ga._evolve(None)
        assert select.call_count
        assert repro.call_count
        assert mut.call_count
        assert local_search.call_count
        assert repop.call_count