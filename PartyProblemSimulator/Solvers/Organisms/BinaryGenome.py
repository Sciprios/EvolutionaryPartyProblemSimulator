from PartyProblemSimulator.Solvers.Organisms.Genome import Genome
from PartyProblemSimulator.Solvers.Organisms.Genes.BinaryGene import BinaryGene
from random import randint

class BinaryGenome(Genome):
    """ A binary encoding of a genome consisting of bits. """

    def __init__(self, genome_size):
        """ Initialises the number of genes required in this genome. """
        Genome.__init__(self, genome_size)

    def _instantiate(self):
        """ Initialises this genome with a random set of binary values. """
        count = 0
        while count < self.get_expected_genome_size():
            if randint(0, 100) < 50:        # Randomize the value to apply to the gene
                self.add_gene(BinaryGene(False))
            else:
                self.add_gene(BinaryGene(True))
            count = count + 1
        
    def get_genome_length(self):
        """ Retrieves the length of this genome. """
        return self.get_expected_genome_size()
    
    def evaluate(self, equation):
        """ Evaluates this genome against the given equation. """
        input_vector = {}
        count = 0   # Generate the input vector
        for gene in self.get_genes():
            gene_id = "{" + str(count) + "}" # Generate the identifier for this gene in the equation.
            input_vector[gene_id] = gene.get_information()
            count = count + 1
        clausal_result = equation.get_clause_evaluation(input_vector)
        score = sum(clausal_result) / len(clausal_result)   # Calculate the percentage of clauses met.
        return score

