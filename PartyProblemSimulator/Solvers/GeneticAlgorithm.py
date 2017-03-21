 from PartyProblemSimulator.Observation.Subject import Subject

class GeneticAlgorithm(Subject):
    """ A genetic algorithm evolves a solution to a problem. """
    
    def __init__(self):
        """ Initializes the instance level variables. """
        self._population = []
        self._generation = 0
        self._eval_count = 0
        Subject.__init__()
    
    def notify_observers(self):
        """ Notifies observers on completion of a generation with the best organism and current stats. """
        # Arguments to be passed to each observer
        args = {
            'Best Organism': self._get_best_genome(), 
            'Generation': self.get_generation(),
            'Evaluations': self.get_num_evaluations()
        }
        for obs in self._observers:
            obs.update(args)
    
    def _get_best_genome(self):
        """ Retrieves the best genome from the population. """
        pass
    
    def get_population(self):
        """ Retrieves the population. """
        return self._population

    def get_generation(self):
        """ Retrieves the current generation this algorithm is on. """
        return self._generation
    
    def get_num_evaluations(self):
        """ Retrieves the number of evaluations this method has used. """
        return self._eval_count