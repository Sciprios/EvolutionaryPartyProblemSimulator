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
        no_sub_matrices = self.get_expected_genome_size()
        # Give each sub matrix a random number of symbols
        cnt = 0
        while cnt < no_sub_matrices:
            symbols = ""
            no_symbols = randint(self.get_expected_genome_size() / no_sub_matrices, 4)  # Random number of symbols
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
                if (no_sub_matrices % 2) != 0:    # If genome is uneven in size add an extra element to the end.
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
        """ Prunes the genome to ensure its of the correct size. """
        max_length = self.get_expected_genome_size()
        gene_index = len(self.get_genes()) - 1    # Start from the end
        while self.get_genome_length() > max_length:
            current_gene = self.get_genes()[gene_index]    # Get gene to prune
            component_index = len(current_gene.get_data()) - 1
            while (self.get_genome_length() > max_length) and (component_index > 0):    # For each component
                current_gene.set_data(current_gene.get_data()[:-1]) # Prune it
                component_index = component_index - 1
                print("--Current: {}, Max: {}".format(self.get_genome_length(), max_length))
            if self.get_genome_length() < max_length:   # IF pruning went one to far
                current_gene.set_data(current_gene.get_data() + "e")    
            elif self.get_genome_length() > max_length:
                if component_index == 0:    # Try converting to single bit gene
                    current_gene.set_data("e")
                    if self.get_genome_length() > max_length:
                        self.remove_gene(current_gene)
            print("Current: {}, Max: {}".format(self.get_genome_length(), max_length))
            gene_index = gene_index - 1

    def get_genome_length(self):
        """ Retrieves the length of this genome. """
        length = 0
        for gene in self.get_genes():
            length = length + len(gene.get_information())
        return length

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
        print("Bit string length: {}, Expected size: {}".format(len(input_vector), self.get_expected_genome_size()))
        clausal_result = equation.get_clause_evaluation(input_vector)
        score = sum(clausal_result) / len(clausal_result)   # Calculate the percentage of clauses met.
        return score