from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
from PartyProblemSimulator.Solvers.BlindKitanoGA import BlindKitanoGA

class TestBlindKitanoGA(TestCase):
    """ Tests the blind Kitano genetic algorithm. """
    
    @patch('PartyProblemSimulator.Solvers.BlindKitanoGA.BlindKitanoGA._set_mutation_rate')
    def test_init(self, mut_mck):
        """ Ensures the correct calls are made to prepare this algorithm. """
        ga = BlindKitanoGA()
        mut_mck.assert_called_with(0.5)

    @patch('PartyProblemSimulator.Solvers.BlindKitanoGA.KitanoGenome')
    def test_initialise(self, kit_genome):
        """ Ensures the method initialises itself correctly. """
        ga = BlindKitanoGA()
        ga._initialise(5)
        kit_genome.assert_called_with(5)
        assert kit_genome.call_count == 10  # BlindGA (Kitano) needs a population of size 10
    
    @patch('PartyProblemSimulator.Solvers.BlindKitanoGA.KitanoGenome')
    def test_reproduction(self, kit_genome):
        """ Tests the reproduction of parents into children. """
        ga = BlindKitanoGA()
        fake_parent = Mock()
        fake_parent.get_genes = Mock(return_value=[])
        result = ga._reproduction([fake_parent, fake_parent])
        assert len(result) == 10
