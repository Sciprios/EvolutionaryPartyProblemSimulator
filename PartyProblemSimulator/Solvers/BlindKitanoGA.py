from PartyProblemSimulator.Solvers.Organisms.KitanoGenome import KitanoGenome
from PartyProblemSimulator.Solvers.BlindGA import BlindGA

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
        while len(population) <= 10:
            # Make child
        return population
    
    def _mutation(self, new_population):
        """ Mutates the population. """
        for organism in new_population:
            if randint(0, 100) > (self.get_mutation_rate() * 10):
                for gene in organism.get_genes():
                    if randint(0,100) > 50:
                        gene.mutate()