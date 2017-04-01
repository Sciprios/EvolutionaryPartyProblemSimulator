from PartyProblemSimulator.Solvers.Organisms.KitanoGenome import KitanoGenome
from PartyProblemSimulator.Solvers.Organisms.Genes.SubMatrixGene import SubMatrixGene
from PartyProblemSimulator.Solvers.BlindGA import BlindGA
from random import shuffle, randint

class BlindKitanoGA(BlindGA):
    """ The BlindGA genetic algorithm using morphogenetic encoding. """

    def __init__(self):
        """ Initializes the BlindGA with morphogenetic encodings. """
        BlindGA.__init__(self)
        self._set_mutation_rate(0.9)
    
    def _initialise(self, no_vars):
        """ Initialises the population of directly encoded genomes. """
        self._repopulate([])    # Empty pop
        while len(self.get_population()) < 10:
            new_organism = KitanoGenome(no_vars)
            self._add_organism(new_organism)
    
    def _reproduction(self, parents):
        """ Reproduces the organism from the parent. """
        genome_size = parents[0].get_expected_genome_size()
        population = [] # New population
        parent_a_genes = parents[0].get_genes() # Get the parents genes for crossover
        parent_b_genes = parents[1].get_genes()
        all_genes = []
        all_genes.extend(parent_a_genes)    # Generate a list of all genes
        all_genes.extend(parent_b_genes)
        while len(population) < 10:
            # Make child by randomly selecting genes then pruning
            child = KitanoGenome(genome_size)
            child.clear_genes()
            # Create a random permutation of the genes to be added
            shuffle(all_genes)
            # Add all genes to child then prune
            for gene in all_genes:
                child.add_gene(SubMatrixGene(gene.get_data()))
            child.prune_genome()
            population.append(child)
        return population
