from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
from PartyProblemSimulator.Solvers.BlindGA import BlindGA

class TestBlindGA(TestCase):
    """ Tests the BlindGA algorithm class. """

    @patch('PartyProblemSimulator.Solvers.BlindGA.BlindGA._set_mutation_rate')
    def test_init(self, mut_mck):
        """ Ensures the correct calls are made to prepare this algorithm. """
        ga = BlindGA()
        mut_mck.assert_called_with(0.5)
    
    @patch('PartyProblemSimulator.Solvers.BlindGA.BinaryGenome')
    def test_initialise(self, bin_genome):
        """ Ensures the method initialises itself correctly. """
        ga = BlindGA()
        ga._initialise(5)
        bin_genome.assert_called_with(5)
        assert bin_genome.call_count == 10  # BlindGA needs a population of size 10
    
    def test_selection(self):
        """ Ensures the highest scorers are returned. """
        ga = BlindGA()
        eq = Mock() # Setup a fake equation
        parent_one = Mock() # Setup some potential parents and a stupid genome
        parent_one.evaluate = Mock(return_value=1000)
        parent_two = Mock()
        parent_two.evaluate = Mock(return_value=900)
        not_a_parent = Mock()
        not_a_parent.evaluate = Mock(return_value=-50)
        ga._set_best_genome = Mock()    # Fake some of the ga's methods
        ga.get_population = Mock(return_value=[not_a_parent, parent_one, parent_two])
        results = ga._selection(eq)
        assert parent_one in results    # Check the correct parents are returned
        assert parent_two in results
        assert not_a_parent not in results
        parent_one.evaluate.assert_called_with(eq)  # Ensure organisms are evaluated correctly.
        parent_two.evaluate.assert_called_with(eq)
        not_a_parent.evaluate.assert_called_with(eq)
        ga._set_best_genome.assert_called_with(parent_one)  # Ensure best genome is set

    @patch('PartyProblemSimulator.Solvers.BlindGA.randint')
    def test_reproduction(self, rand):
        """ Ensures parents are crossed over randomly. """
        ga = BlindGA()
        parent = Mock()
        parent.get_genes = Mock(return_value=[1,2,3])
        parents = [parent, parent, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        ga._reproduction(parents)
        assert rand.call_count == 1
    
    @patch('PartyProblemSimulator.Solvers.BlindGA.randint')
    def test_mutation(self, rand):
        """ Ensure each gene has a chance of mutating. """
        ga = BlindGA()
        rand.return_value = 100   # Set a random value of 100 to ensure all genes should be mutated
        gene_1 = Mock() # Setup fake genome
        gene_2 = Mock()
        gene_3 = Mock()
        genome = Mock()
        genome.get_genes = Mock(return_value=[gene_1, gene_2, gene_3])
        ga._mutation([genome])
        assert rand.call_count == 4 # One for each gene and one for organism
        rand.assert_called_with(0, 100) # Should choose a number between 0 and 100
        assert gene_1.mutate.call_count == 1
        assert gene_2.mutate.call_count == 1
        assert gene_3.mutate.call_count == 1
        
        rand.call_count = 0 # Reset call_counts
        gene_1.mutate.call_count = 0
        gene_2.mutate.call_count = 0
        gene_3.mutate.call_count = 0

        rand.return_value = 0   # Try forcing a non-mutate
        ga._mutation([genome])
        assert rand.call_count == 1 # One for each gene and one for organism
        rand.assert_called_with(0, 100) # Should choose a number between 0 and 100
        assert gene_1.mutate.call_count == 0
        assert gene_2.mutate.call_count == 0
        assert gene_3.mutate.call_count == 0