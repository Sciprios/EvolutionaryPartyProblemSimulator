from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
from PartyProblemSimulator.Solvers.Organisms.Genes.SubMatrixGene import SubMatrixGene

class TestSubMatrixGene(TestCase):
    """ Tests the SubMatrixGene class. """

    def test_get_info(self):
        """ Ensure we get the correct bit string for different encodings. """
        smgn = SubMatrixGene("abcd")    # One of each
        assert smgn.get_information() == [0, 1, 1, 0, 0, 0, 1, 1]
    
        smgn.set_data("aa")   # All of one encoding
        assert smgn.get_information() == [0, 1, 0, 1]