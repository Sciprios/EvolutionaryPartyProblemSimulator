from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
from PartyProblemSimulator.Solvers.GeneticAlgorithm import GeneticAlgorithm

class TestGeneticAlgorithm(TestCase):
    """ Tests the genetic algorithm class. """

    @patch('PartyProblemSimulator.Solvers.GeneticAlgorithm.GeneticAlgorithm._set_max_generation')
    @patch('PartyProblemSimulator.Solvers.GeneticAlgorithm.GeneticAlgorithm._set_best_genome')
    @patch('PartyProblemSimulator.Solvers.GeneticAlgorithm.GeneticAlgorithm._set_generation')
    @patch('PartyProblemSimulator.Solvers.GeneticAlgorithm.GeneticAlgorithm._repopulate')
    def test_init(self, repop, set_gen, set_genome, set_max):
        """ Ensures the init instantiates a genetic algorithm correctly. """
        max_generations = Mock()
        ga = GeneticAlgorithm(max_generations)
        set_gen.assert_called_with(0)   # Check everything has been called.
        set_genome.assert_called_with(None)
        set_max.assert_called_with(max_generations)
        repop.assert_called_with([])
