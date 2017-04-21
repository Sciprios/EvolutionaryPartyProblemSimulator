from PartyProblemSimulator.Solvers.HeuristicAlgorithm import HeuristicAlgorithm
from PartyProblemSimulator.Solvers.Organisms.BinaryGenome import BinaryGenome
from random import randint, shuffle

class FlipGA(HeuristicAlgorithm):
    """ The FlipGA genetic algorithm. """

    def __init__(self):
        """ Initializes the FlipGA method with predefined attributes. """
        HeuristicAlgorithm.__init__(self, 1000)
        self._set_mutation_rate(0.9)
    
    def _initialise(self, no_vars):
        """ Initialises the population of directly encoded genomes. """
        self._repopulate([])    # Empty pop
        while len(self.get_population()) < 10:
            new_organism = BinaryGenome(no_vars)
            self._add_organism(new_organism)
    
    def _selection(self, equation):
        """ Returns only organism. """
        parents = []
        parent_index = 0
        while parent_index < 2:
            current_best = None # Best organism so far
            best_fitness = -1 # Best fitness so far
            search_index = 0
            while search_index < len(self.get_population()):
                organism = self.get_population()[search_index] # Get this organism and its fitness
                fitness = organism.evaluate(equation)
                self._increment_eval_count()
                if (fitness > best_fitness) and not (organism in parents):  # As long as its not already a parent and better
                    current_best = organism
                    best_fitness = fitness
                search_index = search_index + 1
            parents.append(current_best)    # Add the parent to the parent's list
            parent_index = parent_index + 1
        self._set_best_genome(parents[0])   # First parent is the best
        return parents
    
    def _reproduction(self, parents):
        """ Reproduces the organism from the parent. """
        genome_size = len(parents[0].get_genes())
        population = [] # New population
        population.extend(parents)  # The parents carry on
        parent_a_genes = parents[0].get_genes() # Get the parents genes for crossover
        parent_b_genes = parents[1].get_genes()
        split_point = randint(0, genome_size)   # Choose a point to reproduce over
        while len(population) <= 10:
            new_gene_list = []
            new_gene_list.extend(parent_a_genes[0:split_point])
            new_gene_list.extend(parent_b_genes[split_point:genome_size])
            # Generate new child
            child = BinaryGenome(genome_size)
            child.clear_genes()
            for gene in new_gene_list:
                child.add_gene(gene)
            population.append(child)
        return population
    
    def _mutation(self, new_population):
        """ Mutates the population. """
        for organism in new_population:
            if randint(0, 100) > (self.get_mutation_rate() * 10):
                for gene in organism.get_genes():
                    if randint(0,100) > 50:
                        gene.mutate()

class FlipGA_1(FlipGA):
    """ FlipGA with the Mutation 1 method. """

    def _mutation(self, new_population):    # pragma: no cover
        """ Mutates the population. """
        for organism in new_population:
            if randint(0, 100) > (self.get_mutation_rate() * 10):
                for gene in organism.get_genes():
                    if randint(0,100) > 50:
                        gene.mutate()

class FlipGA_2(FlipGA):
    """ FlipGA with the mutation 2 method. """

    def _mutation(self, new_population):    # pragma: no cover
        """ Mutates the population. """
        for organism in new_population:
            if randint(0, 100) > (self.get_mutation_rate() * 10):
                crosspoint = randint(0, len(organism.get_genes()) - 1)
                for gene in organism.get_genes()[crosspoint:]:
                    gene.mutate()