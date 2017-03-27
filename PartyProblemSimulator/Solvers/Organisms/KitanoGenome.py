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
        no_sub_matrices = self.get_genome_size()
        # Give each sub matrix a random number of symbols
        cnt = 0
        while cnt < no_sub_matrices:
            symbols = ""
            no_symbols = randint(self.get_genome_size() / no_sub_matrices, 4)  # Random number of symbols
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
            if cnt == 0:  # First element
                if self.get_genome_size() % 2 != 0:    # If genome is uneven in size add an extra element to the end.
                    rand = randint(0, 1)
                    if rand == 0:
                        symbols = symbols + 'f'
                    else:
                        symbols = symbols + 'e'
            gene = SubMatrixGene(symbols)
            self.add_gene(gene)
            cnt = cnt + 1
        self.prune_genome()

    def prune_genome(self):
        """ Prunes the genome to ensure it has the correct size. """
        max_size = self.get_genome_size()
        spare_genes = []
        # Calculate length
        # DEBUG
        print("Max size: {}".format(max_size))
        d_length = 0
        for gene in self.get_genes():
            d_length = d_length + len(gene.get_information())
        print("Before prune: {}".format(d_length))
        length = 0
        for gene in self.get_genes():
            length = length + len(gene.get_information())   # What would the length be with this gene
            if length > max_size:
                diff = length - max_size
                if diff < len(gene.get_information()):  # Is the difference prunable?
                    componenets_to_remove = int(diff / 2)    # Two bits per componenet
                    gene.set_data(gene.get_data()[componenets_to_remove:])  # Prune the grammar
                    length = length - diff
                else:
                    spare_genes.append(gene)  # This one isn't needed
                    length = length - len(gene.get_information())
        for gene in spare_genes:
            self.remove_gene(gene)
        # DEBUG
        d_length = 0
        for gene in self.get_genes():
            d_length = d_length + len(gene.get_information())
        print("After prune: {}".format(d_length))
    
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
        print("Bit string length: {}, Expected size: {}".format(len(input_vector), self.get_genome_size()))
        clausal_result = equation.get_clause_evaluation(input_vector)
        score = sum(clausal_result) / len(clausal_result)   # Calculate the percentage of clauses met.
        return score