""" Tests the abstract classes. """
from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
from ..PartyProblem import PartyProblem

class TestPartyProblem(TestCase):
    """ Tests the PartyProblem class. """

    @patch('PartyProblemVisualizer.PartyProblem.PartyProblem._generate_vertices')
    @patch('PartyProblemVisualizer.PartyProblem.PartyProblem._generate_edges')
    @patch('PartyProblemVisualizer.PartyProblem.PartyProblem._generate_equation')
    @patch('PartyProblemVisualizer.PartyProblem.PartyProblem._set_algorithm')
    def test_initialisation(self, gen_v, gen_e, gen_eq, set_a):
        """ Ensures problem is generated correctly. """
        pp = PartyProblem(51, 15, "tst")
        assert gen_v.call_count == 1
        assert gen_e.call_count == 1
        assert gen_eq.call_count == 1
        assert set_a.call_count == 1