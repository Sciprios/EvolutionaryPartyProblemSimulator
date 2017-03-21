from PartyProblemSimulator.Solvers.Organisms.Genome import Genome
from PartyProblemSimulator.Solvers.Organisms.Genes.SubMatrixGene import SubMatrixGene
from random import randint

class KitanoGenome(Genome):
    """ A genome which represents a graph as a grammar. """

    def __init__(self, genome_size):
        """ Initialises the size of the genome. """
        Genome.__init__(self, genome_size)
    
    def _instantiate(self):
        """ Initialises this genome with a random grammatical representation. """
        # Generate number of sub-matrices to use
        no_sub_matrices = randint(1, self._get_genome_size())   # Each submatrix has a minimum of 2 components
        # Give each sub matrix a random number of symbols
        cnt = 0
        symbols = ""
        while cnt < no_sub_matrices:
            no_symbols = randint(self._get_genome_size() / no_sub_matrices, 4)  # Random number of symbols
            while len(symbols) < no_symbols:
                symbol = randint(1, 4)
                if symbol == 1:
                    symbols = symbols + ('a')
                elif symbol == 2:
                    symbols = symbols + ('b')
                elif symbol == 3:
                    symbols = symbols + ('c')
                elif symbol == 4:
                    symbols = symbols + ('d')
            gene = SubMatrixGene(symbols)
            self.add_gene(gene)
        self.prune_genome()
    
    def prune_genome(self):
        """ Prunes the genome to ensure it has the correct size. """
        max_size = self._get_genome_size()
        genome = self.get_genes()
        # Calculate length
        length = 0
        prev_gene = None
        for gene in genome:
            if length < max_size:
                length = length + (len(gene.get_data()) * 2)    # Two values in each component.
            elif length == max_size:
                self.remove_gene(gene)
            elif length > max_size:   # We know the last gene to be checked is too long.
                diff = length - max_size
                prev_gene.set_data(prev_gene.get_data()[0:-diff])   # Prune last gene
            prev_gene = gene
    
    def evaluate(self, equation):
        """ Evaluates this genome against the given equation. """
        bit_string = []
        for gene in self.get_genes():   # Generate a bit string
            bit_string.extend(gene.get_information())
        input_vector = {}
        count = 0
        for bit in bit_string:  # Generate input vector
            id = "{" + str(count) + "}"
            input_vector[id] = bit
            count = count + 1
        clausal_result = equation.get_clause_evaluation(input_vector)
        score = sum(clausal_result) / len(clausal_result)   # Calculate the percentage of clauses met.
        return score