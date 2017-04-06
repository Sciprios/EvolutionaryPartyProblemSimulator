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
        self.clear_genes()
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
            gene = SubMatrixGene(symbols)
            self.add_gene(gene)
            cnt = cnt + 1
        self.prune_genome()
    
    def prune_genome(self):
        """ Prunes the genome to ensure its of the correct size. """
        max_length = self.get_expected_genome_size()
        removables = []
        gene_index = 0
        new_length = 0
        while gene_index < len(self.get_genes()):    # For each gene see if it fits or prune until it does
            current_gene = self.get_genes()[gene_index]
            if current_gene.get_data() == "" or current_gene.get_information() == "":   # Check if its an empty gene
                removables.append(current_gene) 
            if ((new_length + len(current_gene.get_information())) <= max_length):   # IF this gene does fit in
                new_length = new_length + len(current_gene.get_information())
            else:
                no_components = len(current_gene.get_data())
                current_component = 0
                while current_component < no_components:   # For each component
                    current_gene.set_data(current_gene.get_data()[:-1])
                    if (new_length + len(current_gene.get_information())) <= max_length:  # Does it now fit?
                        new_length = new_length + len(current_gene.get_information())
                        break
                    current_component = current_component + 1
                if current_gene.get_data() == "" or current_gene.get_information() == "":   # If this gene has nothing left, add it to removal list
                    removables.append(current_gene)
            gene_index = gene_index +  1
        for gene in removables: # Remove all empty genes
            self.remove_gene(gene)
    
    def _set_expected_genome_size(self, genome_size):
        """ Safely sets the expected gene count of this genome, ensuring its even. """
        if genome_size > 0:
            if genome_size % 2 == 0:
                self._expected_genome_size = genome_size
            else:
                self._expected_genome_size = genome_size + 1
        else:
            self._expected_genome_size = 2

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
        count = 1
        for bit in bit_string:  # Generate input vector
            id = "{" + str(count) + "}"
            input_vector[id] = bit
            count = count + 1
        clausal_result = equation.get_clause_evaluation(input_vector)
        score = sum(clausal_result) / len(clausal_result)   # Calculate the percentage of clauses met.
        return score