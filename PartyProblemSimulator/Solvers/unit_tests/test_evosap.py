from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
from PartyProblemSimulator.Solvers.EvoSAP import EvoSAP

class TestEvoSAP(TestCase):
    """ Tests the evosap algorithm class. """

    @patch('PartyProblemSimulator.Solvers.EvoSAP.EvoSAP._set_mutation_rate')
    def test_init(self, mut_mck):
        """ Ensures the correct calls are made to prepare this algorithm. """
        ga = EvoSAP()
        mut_mck.assert_called_with(0.9)
    
    @patch('PartyProblemSimulator.Solvers.EvoSAP.BinaryGenome')
    def test_init_pop(self, bin_genome):
        """ Ensures a new population is generate correctly. """
        ga = EvoSAP() # Try with empty population
        ga._initialise(5)
        bin_genome.assert_called_with(5)
    
    def test_selection(self):
        """ Sets the best genome as the induvidual. """
        ga = EvoSAP()
        set_best = Mock()   # Setup some fake methods
        get_pop = Mock(return_value=[1])
        ga._set_best_genome = set_best
        ga.get_population = get_pop
        res = ga._selection(None) # Run the method
        set_best.assert_called_with(1)  # First member of population
        assert res == [1]
    
    def test_reproduction(self):
        """ Ensures this method returns just the induvidual parent. """
        ga = EvoSAP()
        res = ga._reproduction([1])
        assert res == [1]
    
    @patch('PartyProblemSimulator.Solvers.EvoSAP.randint')
    def test_mutation(self, rand):
        """ Ensure each gene has a chance of mutating. """
        ga = EvoSAP()
        rand.return_value = 0   # Set a random value of 0 to ensure no genes should be mutated
        gene_1 = Mock() # Setup fake genome
        gene_2 = Mock()
        gene_3 = Mock()
        genome = Mock()
        genome.get_genes = Mock(return_value=[gene_1, gene_2, gene_3])
        ga._mutation([genome])
        assert rand.call_count == 3 # One for each gene
        rand.assert_called_with(0, 100) # Should choose a number between 0 and 100
        assert gene_1.mutate.call_count == 0
        assert gene_2.mutate.call_count == 0
        assert gene_3.mutate.call_count == 0
    
    