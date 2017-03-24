from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
from PartyProblemSimulator.Solvers.Organisms.BinaryGenome import BinaryGenome

class TestBinaryGenome(TestCase):
    """ Tests the binary genome class. """

    @patch('PartyProblemSimulator.Solvers.Organisms.BinaryGenome.BinaryGenome._set_genome_size')
    @patch('PartyProblemSimulator.Solvers.Organisms.BinaryGenome.BinaryGenome._instantiate')
    def test_init(self, inst_mock, set_cnt_mock):
        """ Ensures the init initialises the number of genes to be expected.  """
        bgnm = BinaryGenome(genome_size=500)
        assert inst_mock.called
    
    @patch('PartyProblemSimulator.Solvers.Organisms.BinaryGenome.BinaryGenome._get_genome_size')
    def test_instantiate(self, get_cnt_mock):
        """ Ensures the gene count is returned appropriately. """
        get_cnt_mock.return_value = 5
        bgnm = BinaryGenome(genome_size=5) # Should call the function automatically.
        assert len(bgnm._genes) == 5
        get_cnt_mock.return_value = 7   # Try with another set of values.
        bgnm = BinaryGenome(genome_size=7) 
        assert len(bgnm._genes) == 7

    @patch('PartyProblemSimulator.Solvers.Organisms.BinaryGenome.BinaryGenome._instantiate')
    def test_evaluate(self, inst_mock):
        """ Ensures the evaluation method works correctly. """
        fake_equation = Mock()
        fake_equation.get_clause_evaluation = Mock(return_value=[False, False, False])  # 0%
        bgnm = BinaryGenome(genome_size=2)
        bgnm._genes = []
        assert bgnm.evaluate(fake_equation) == 0

