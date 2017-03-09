""" Tests the abstract classes. """
from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
from SatisfiabilitySimulator.Solvers.GeneticAlgorithm import GeneticAlgorithm
from SatisfiabilitySimulator.Solvers.HeuristicAlgorithm import HeuristicAlgorithm

class TestHeuristicAlgo(TestCase):
    """ Ensures no methods are implemented and throw errors. """

    def test_heuristic(self):
        """ Ensures the heuristic method throws a un-implemented exception. """
        ga = HeuristicAlgorithm()
        self.assertRaises(NotImplementedError, ga._heuristic_method, None)

class TestGeneticAlgorithm(TestCase):
    """ Tests the methods in the GeneticAlgorithm class.0 """

    def test_init(self):
        """ Instantiates instance variables. """
        ga = GeneticAlgorithm()
        assert ga._MAX_GENERATIONS == 1000
        assert ga._POP_SIZE == 10
        assert ga._NUM_PARENTS == 2
        assert ga._EQUATION == None
        assert ga._MUTATION_RATE == 0
        assert ga._variables == []
        assert ga.population == []
        assert ga.fitness_values == []
        assert ga.generation == 0
        assert ga.next_generation == []
        assert ga.finished == False
        assert ga.best_org == {}
        assert ga.eval_count == 0
    
    def test_initialisation(self):
        """ Tests the initialisation of the population. """
        ga = GeneticAlgorithm()
        ga._variables = ['1', '2', '3', '4']
        ga._POP_SIZE = 500  # Population size of 500
        
        ga.initialisation()
        assert len(ga.population) == 500

        ga._POP_SIZE = 1  # Population size of 1
        ga.initialisation()
        assert len(ga.population) == 1

        ga._POP_SIZE = 0  # Population size of 0
        ga.initialisation()
        assert len(ga.population) == 0

    def test_clausal_score(self):
        """ Tests the calculation of a clausal score. """
        ga = GeneticAlgorithm()
        ga._EQUATION = Mock()   # Setup fake equation
        ga._EQUATION.get_clause_evaluation = Mock(return_value=[True, True, False])
        res = ga._calc_clausal_score(None)    # Call method
        assert res == 2
        assert ga._EQUATION.get_clause_evaluation.called
    
    def test_get_best(self):
        """ Ensures the best organism is returned. """
        ga = GeneticAlgorithm()
        ga.population = [1, 2, 3, 4, 5] # Fake population and fitness values
        ga.fitness_values = [0, 5, 3, 10, 2]
        best = ga.get_best_org()    # Run method
        assert best['org'] == 4
        assert best['fitness'] == 10

    def test_run(self):
        """ Tests the execution. """
        ga = GeneticAlgorithm()
        self.assertRaises(NotImplementedError, ga.run)

    def test_evaluation(self):
        """ Evaluates a population and returns the fitness values. """
        ga = GeneticAlgorithm()
        self.assertRaises(NotImplementedError, ga._evaluation)
    
    def test_parent_selection(self):
        """ Selects the number of parents required given the organisms fitness values. """
        ga = GeneticAlgorithm()
        self.assertRaises(NotImplementedError, ga._parent_selection, None)
    
    def test_reproduction(self):
        """ Generates children from the provided parents. """
        ga = GeneticAlgorithm()
        self.assertRaises(NotImplementedError, ga._reproduction, None)
    
    def test_mutation(self):
        """ Mutates the provided population. """
        ga = GeneticAlgorithm()
        self.assertRaises(NotImplementedError, ga._mutation, None)
    