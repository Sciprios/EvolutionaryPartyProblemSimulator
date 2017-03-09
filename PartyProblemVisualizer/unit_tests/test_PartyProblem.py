""" Tests the abstract classes. """
from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
from ..PartyProblem import PartyProblem
from PartyProblemSimulator.PartyProblemVisualizer.PartyProblem import PartyProblem
class TestPartyProblem(TestCase):
    """ Tests the PartyProblem class. """

    @patch('PartyProblemSimulator.PartyProblemVisualizer.PartyProblem.PartyProblem._generate_vertices')
    @patch('PartyProblemSimulator.PartyProblemVisualizer.PartyProblem.PartyProblem._generate_edges')
    @patch('PartyProblemSimulator.PartyProblemVisualizer.PartyProblem.PartyProblem._generate_equation')
    @patch('PartyProblemSimulator.PartyProblemVisualizer.PartyProblem.PartyProblem._get_edge_labels')
    def test_initialisation(self, get_lbl, gen_eq, gen_e, gen_v):
        """ Ensures problem is generated correctly. """
        algo = Mock()   # Create fake algorithm
        pp = PartyProblem(51, 15, algo) # Create an instance

        assert gen_v.call_count == 1    # Check results
        assert gen_e.call_count == 1
        assert gen_eq.call_count == 1
        assert get_lbl.call_count == 1
        assert algo.call_count == 1