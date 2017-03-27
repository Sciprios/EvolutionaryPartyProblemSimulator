from PartyProblemSimulator.Solvers.Organisms.KitanoGenome import KitanoGenome
from PartyProblemSimulator.Solvers.BlindGA import BlindGA
from random import shuffle, randint

class BlindGAm(BlindGA):
    """ The BlindGA genetic algorithm using morphogenetic encoding. """

    def __init__(self):
        """ Initializes the FlipGA method with predefined attributes. """
        BlindGA.__init__(self, 1000)
        self._set_mutation_rate(0.5)
    
    def _initialise(self, no_vars):
        """ Initialises the population of directly encoded genomes. """
        while len(self.get_population()) < 10:
            new_organism = KitanoGenome(no_vars)
            self._add_organism(new_organism)
    
    def _reproduction(self, parents):
        """ Reproduces the organism from the parent. """
        genome_size = len(parents[0].get_genes())
        population = [] # New population
        population.extend(parents)  # The parents carry on
        parent_a_genes = parents[0].get_genes() # Get the parents genes for crossover
        parent_b_genes = parents[1].get_genes()
        all_genes = []
        all_genes.extend(parent_a_genes)    # Generate a list of all genes
        all_genes.extend(parent_b_genes)
        while len(population) <= 10:
            # Make child by randomly selecting genes then pruning
            child = KitanoGenome(no_vars)
            child.clear_genes()
            # Create a random permutation of the genes to be added
            shuffle(all_genes)
            # For odd sized genomes we need a single extra symbol
            if randint(0, 100) > 50:
                all_genes = [parent_b_genes[0]] + all_genes
            else:
                all_genes = [parent_a_genes[0]] + all_genes
            # Add all genes to child then prune
            for gene in all_genes:
                child.add_gene(gene)
            child.prune_genome()
            population.append(child)
        return population
