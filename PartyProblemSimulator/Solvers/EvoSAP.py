from PartyProblemSimulator.Solvers.HeuristicAlgorithm import HeuristicAlgorithm
from PartyProblemSimulator.Solvers.Organisms.BinaryGenome import BinaryGenome
from random import randint, shuffle

class EvoSAP(HeuristicAlgorithm):
    """ The EvoSAP genetic algorithm. """

    def __init__(self):
        """ Initializes the EvoSAP method with predefined attributes. """
        HeuristicAlgorithm.__init__(self, 1000)
        self._set_mutation_rate(0.9)
    
    def _initialise(self, no_vars):
        """ Initialises the population of directly encoded genomes. """
        while len(self.get_population()) < 1:
            new_organism = BinaryGenome(no_vars)
            self._add_organism(new_organism)
    
    def _selection(self, equation):
        """ Returns only organism. """
        self._set_best_genome(self.get_population()[0])
        return [self.get_population()[0]]
    
    def _reproduction(self, parents):
        """ Reproduces the organism from the parent. """
        return [parents[0]] # EvoSAP only has a single population member
    
    def _mutation(self, new_population):
        """ Mutates the population. """
        for organism in new_population:
            for gene in organism.get_genes():
                if randint(0,100) > (self.get_mutation_rate() * 10):
                    gene.mutate()

    def _heuristic_method(self, new_population, equation): # pragma: no cover
        """ Applies a local search heuristic on the population. """
        for organism in new_population:
            # Generate a random permutation of the genes
            random_permutation =  shuffle(list(range(0, len(organism.get_genes()))))
            improve = 1
            counter = 0
            while improve > 0:  # Flip until we stop improving the organism
                improve = 0
                self._increment_eval_count()    # Evaluating before flip
                old_fitness = organism.evaluate(equation)
                current_value = organism.get_genes()[counter].get_data() # Flip the next gene in list
                organism.get_genes()[counter].set_data(not current_value)
                self._increment_eval_count()    # Did we make an improvement?
                new_fitness = organism.evaluate(equation)
                if new_fitness >= old_fitness:
                    improve = improve + (new_fitness - old_fitness) # We did! Increment improvement
                else:
                    current_value = organism.get_genes()[counter].get_data() # We didn't :( Revert the flip
                    organism.get_genes()[counter].set_data(not current_value)
                counter = counter + 1

class EvoSAP_1(EvoSAP):
    """ EvoSAP with the Mutation 1 method. """

    def _mutation(self, new_population):
        """ Mutates the population. """
        for organism in new_population:
            if randint(0, 100) > (self.get_mutation_rate() * 10):
                for gene in organism.get_genes():
                    if randint(0,100) > 50:
                        gene.mutate()

class EvoSAP_2(EvoSAP):
    """ EvoSAP with the mutation 2 method. """

    def _mutation(self, new_population):
        """ Mutates the population. """
        for organism in new_population:
            if randint(0, 100) > (self.get_mutation_rate() * 10):
                crosspoint = randint(0, len(organism.get_genes()) - 1)
                for gene in organism.get_genes()[crosspoint:]:
                    gene.mutate()