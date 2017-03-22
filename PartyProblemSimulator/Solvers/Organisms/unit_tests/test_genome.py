from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
from PartyProblemSimulator.Solvers.Organisms.Genome import Genome

class TestGenome(TestCase):
    """ Tests the genome class. """

    @patch('PartyProblemSimulator.Solvers.Organisms.Genome.Genome._instantiate')
    def test_init(self, inst_mock):
        """ Tests the instantiation of a genome. """
        gnm = Genome(0)
        assert gnm._genes == []
        assert inst_mock.called
    
    def test_instantiate(self):
        """ Tests the _instantiate method of the genome. """
        self.assertRaises(NotImplementedError, Genome, 0)    # We know a genome instantiates on init.
    
    @patch('PartyProblemSimulator.Solvers.Organisms.Genome.Genome._instantiate')
    def test_evaluate(self, inst_mock):
        """ Tests the evaluate method functions for a genome. """
        gnm = Genome(0)
        self.assertRaises(NotImplementedError, gnm.evaluate, None)
    
    @patch('PartyProblemSimulator.Solvers.Organisms.Genome.Genome._instantiate')
    def test_add_gene(self, inst_mock):
        """ Ensures the adding of genes functions. """
        gnm = Genome(0)
        gnm.add_gene(True)
        assert gnm._genes == [True] # Try adding multiple times
        gnm.add_gene(False)
        assert gnm._genes == [True, False]
        gnm.add_gene(True)
        assert gnm._genes == [True, False, True]
    
    @patch('PartyProblemSimulator.Solvers.Organisms.Genome.Genome._instantiate')
    def test_remove_gene(self, inst_mock):
        """ Ensures genes are removed correctly. """
        gnm = Genome(0)
        gene_one = "gene one"
        gene_two = "gene two"
        gene_three = "gene three"
        gnm._genes = [gene_one, gene_two, gene_three]
        gnm.remove_gene(gene_two)
        assert gnm._genes == [gene_one, gene_three] # Ensure both remain
    
    @patch('PartyProblemSimulator.Solvers.Organisms.Genome.Genome._instantiate')
    def test_get_genes(self, inst_mock):
        """ Ensures all genes are returned correctly. """
        gnm = Genome(0)
        gnm._genes = [True, False]
        assert gnm._genes is gnm.get_genes()    # is checks references not equivalency.

    @patch('PartyProblemSimulator.Solvers.Organisms.Genome.Genome._instantiate')
    def test_set_genome_size(self, inst_mock):
        """ Ensures the gene count can be set correctly. """
        gnm = Genome(5)
        gnm._genome_size = 6
        gnm._set_genome_size(500)
        assert gnm._genome_size == 500

    @patch('PartyProblemSimulator.Solvers.Organisms.Genome.Genome._instantiate')
    def test_clear_genome(self, inst_mock):
        """ Ensures the gene count can be set correctly. """
        gnm = Genome(5)
        gnm._genes = [1, 2, 3, 4, 5]
        gnm.clear_genes()
        assert len(gnm.get_genes()) == 0