from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
from PartyProblemSimulator.Solvers.Organisms.Genes.BinaryGene import BinaryGene

class TestBinaryGene(TestCase):
    """ Tests the BinaryGene class. """

    def test_get_information(self):
        """ Ensures the information retrieved is identical to the data. """
        data = Mock()
        bgn = BinaryGene(data)
        assert bgn.get_information() is data