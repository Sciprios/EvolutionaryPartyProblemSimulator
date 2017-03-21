from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
from PartyProblemSimulator.Solvers.Organisms.Genes.Gene import Gene

class TestGene(TestCase):
    """ Tests the gene class. """

    @patch('PartyProblemSimulator.Solvers.Organisms.Genes.Gene.Gene.set_data')
    def test_init(self, set_data):
        """ Ensures it attempts to set the data of the gene. """
        some_data = Mock()
        gn = Gene(some_data)
        set_data.assert_called_with(some_data)
    
    def test_set_data(self):
        """ Ensure the data is set. """
        some_data = Mock()
        gn = Gene(some_data)    # We know set data is called here.
        assert gn._data is some_data
    
    def test_get_data(self):
        """ Ensures the retrieval of data works correctly. """
        some_data = Mock()
        gn = Gene(some_data)    # We know set data is called here.
        assert gn._data is some_data
        assert gn.get_data() is some_data
    
    def test_get_info(self):
        """ Ensure the retrieval of information throws an error. """
        gn = Gene(None)
        self.assertRaises(NotImplementedError, gn.get_information)