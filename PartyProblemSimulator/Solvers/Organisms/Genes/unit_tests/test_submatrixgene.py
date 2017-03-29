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
    
    @patch('PartyProblemSimulator.Solvers.Organisms.Genes.SubMatrixGene.randint')
    def test_mutate(self, rand):
        """ Ensures the gene is mutated randomly. """
        smg = SubMatrixGene("abcd")   # Create a gene to mutate
        rand.return_value = 0   # Last 4 symbols should turn into an 'a'
        smg.mutate()
        assert smg.get_data() == "aaaa"

        smg = SubMatrixGene("abcdabcdabcd")
        smg.mutate()
        assert smg.get_data() == "aaaaaaaaaaaa"