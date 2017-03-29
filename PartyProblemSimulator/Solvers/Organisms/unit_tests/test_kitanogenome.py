from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
from PartyProblemSimulator.Solvers.Organisms.KitanoGenome import KitanoGenome
from PartyProblemSimulator.Solvers.Organisms.Genes.SubMatrixGene import SubMatrixGene

class TestKitanoGenome(TestCase):
    """ Tests the kitano genome class. """

    @patch('PartyProblemSimulator.Solvers.Organisms.KitanoGenome.KitanoGenome._instantiate')
    def test_init(self, inst_mock):
        """ Ensures the init initialises the number of genes to be expected.  """
        bgnm = KitanoGenome(genome_size=500)
        assert inst_mock.called
    
    @patch('PartyProblemSimulator.Solvers.Organisms.KitanoGenome.KitanoGenome.prune_genome')
    @patch('PartyProblemSimulator.Solvers.Organisms.KitanoGenome.SubMatrixGene')
    def test_instantiate_1(self, sm_gene, prune_mock):
        """ Ensures a random number of sub matrices are generated. """
        kgnm = KitanoGenome(genome_size=10)
        assert sm_gene.call_count == 10     # Generated 10 Genes?
        assert len(kgnm._genes) == 10
        assert prune_mock.call_count == 1
    
    def test_instantiate_prune(self):
        """ Ensures a random number of sub matrices are generated. """
        kgnm = KitanoGenome(genome_size=10)
        length = kgnm.get_genome_length()
        grammar = ""
        assert length == 10
        grammar = ""
        kgnm = KitanoGenome(genome_size=15)        # Try an odd size
        length = kgnm.get_genome_length()
        assert length == 16
        kgnm = KitanoGenome(genome_size=15)        # Try a different size
        kgnm._expected_genome_size = 6
        kgnm.prune_genome()
        length = kgnm.get_genome_length()
        assert length == 6
        kgnm = KitanoGenome(genome_size=10)        # Try a different size
        kgnm._expected_genome_size = 6
        kgnm.prune_genome()
        length = kgnm.get_genome_length()
        assert length == 6
        kgnm = KitanoGenome(9)
        kgnm.clear_genes()
        x1 = SubMatrixGene("aadc")
        x2 = SubMatrixGene("aadc")
        x3 = SubMatrixGene("c")
        x4 = SubMatrixGene("cb")
        x5 = SubMatrixGene("b")
        x6 = SubMatrixGene("da")
        kgnm._genes = [x1,x2,x3,x4,x5,x6]
        kgnm.prune_genome()
        length = kgnm.get_genome_length()
        assert length == 10
    
    @patch('PartyProblemSimulator.Solvers.Organisms.KitanoGenome.KitanoGenome._instantiate')
    def test_evaluate(self, inst_mock):
        """ Ensures the evaluation method works correctly. """
        # Setup fake components
        gene_one = Mock()
        gene_one.get_information = [1,1,1]
        gene_two = Mock()
        gene_two.get_information = [0,0,0]
        fake_equation = Mock()      # Fake equation to evaluate it against
        fake_equation.get_clause_evaluation = Mock(return_value=[False, False, False])  # 0%
        kgnm = KitanoGenome(genome_size=2)
        kgnm._genes = []
        assert kgnm.evaluate(fake_equation) == 0