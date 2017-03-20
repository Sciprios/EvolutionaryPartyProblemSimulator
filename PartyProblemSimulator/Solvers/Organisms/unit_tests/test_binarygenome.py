from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
from PartyProblemSimulator.Solvers.Organisms.BinaryGenome import BinaryGenome

class TestBinaryGenome(TestCase):
    """ Tests the binary genome class. """

    @patch('PartyProblemSimulator.Solvers.Organisms.BinaryGenome.BinaryGenome._set_gene_count')
    @patch('PartyProblemSimulator.Solvers.Organisms.BinaryGenome.BinaryGenome._instantiate')
    def test_init(self, inst_mock, set_cnt_mock):
        """ Ensures the init initialises the number of genes to be expected.  """
        bgnm = BinaryGenome(gene_count=500)
        set_cnt_mock.assert_called_with(500)
        assert inst_mock.called
    
    @patch('PartyProblemSimulator.Solvers.Organisms.BinaryGenome.BinaryGenome._get_gene_count')
    def test_instantiate(self, get_cnt_mock):
        """ Ensures the gene count is returned appropriately. """
        get_cnt_mock.return_value = 5
        bgnm = BinaryGenome(gene_count=5) # Should call the function automatically.
        assert len(bgnm._genes) == 5
        get_cnt_mock.return_value = 7   # Try with another set of values.
        bgnm = BinaryGenome(gene_count=7) 
        assert len(bgnm._genes) == 7

    @patch('PartyProblemSimulator.Solvers.Organisms.BinaryGenome.BinaryGenome._instantiate')
    def test_evaluate(self, inst_mock):
        """ Ensures the evaluation method works correctly. """
        fake_equation = Mock()
        fake_equation.get_clause_evaluation = Mock(return_value=[False, False, False])  # 0%
        bgnm = BinaryGenome(gene_count=2)
        bgnm._genes = [True, True, True]
        assert bgnm.evaluate(fake_equation) == 0

    def test_set_gene_cnt(self):
        """ Ensures the gene count can be set correctly. """
        bgnm = BinaryGenome(5)
        bgnm._gene_count = 6
        bgnm._set_gene_count(500)
        assert bgnm._gene_count == 500