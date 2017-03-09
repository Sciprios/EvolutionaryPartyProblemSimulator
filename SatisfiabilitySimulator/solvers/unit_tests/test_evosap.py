""" Modules containing tests for the flipga class. """
from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
from SatisfiabilitySimulator.Solvers.EvoSAP import EvoSAP

class TestEvoSAP(TestCase):
    """ Test class for the EvoSAP class. """
    def test_init(self):
        """ Ensure properties of the genetic algorithm are set properly. """
        eq = Mock()
        vars = Mock()
        ga = EvoSAP(eq, vars)
        assert ga._NUM_PARENTS == 1
        assert ga._MUTATION_RATE == 0.9
        assert ga._POP_SIZE == 1
        assert ga._EQUATION is eq
        assert ga._variables is vars

    def test_evaluation(self):
        """ Tests the evaluation method. """
        eq = Mock()
        eq.get_clause_evaluation = Mock(return_value=[True, True, True, True, True])  # Standard value to check for
        vars = Mock()
        ga = EvoSAP(eq, vars)
        ga.population = [1]   # Population of 1
        ga._evaluation()
        assert ga.fitness_values == [5]
    
    def test_initialisation(self):
        """ Ensures population is initialised correctly. """
        eq = Mock()
        vars = ['1', '2', '3']
        ga = EvoSAP(eq, vars)
        ga.initialisation() # Call the method

        assert len(ga.population) == 1
        assert vars[0] in ga.population[0]
        assert vars[1] in ga.population[0]
        assert vars[2] in ga.population[0]
    
    @patch('SatisfiabilitySimulator.Solvers.EvoSAP.random')
    def test_heuristic_method(self, rand_mock):
        """ Ensures the algorithm flips children correctly. """
        eq = Mock()
        vars = Mock()

        ## Test cases
        ga = EvoSAP(eq, ['A'])
        rand_mock.shuffle = Mock(return_value=[0])
        children = [{'A':    False}]    # A child who is wrong, to be flipped
        ga._calc_clausal_score = Mock()
        ga._calc_clausal_score.return_value = 1
        ga._heuristic_method(children)
        assert children[0]['A'] # Should now be true

        ga = EvoSAP(eq, ['A', 'B'])
        rand_mock.shuffle = Mock(return_value=[0, 1])
        children = [{'A':    False, 'B':    True}]    # A child who is wrong, to be flipped
        ga._calc_clausal_score = Mock()
        ga._calc_clausal_score.return_value = 2

        ga._heuristic_method(children)
        self.assertTrue(children[0]['A']) # Should now be true
        self.assertFalse(children[0]['B'])  # Should not have been flipped

    def test_reproduction(self):
        """ Tests the reproduction mechanism returns an identical child. """
        eq = Mock()
        vars = ['A', 'B']
        ga = EvoSAP(eq, vars)

        # Test parents
        parent_a = {'A': True, 'B': False}
        parent_b = {'A': False, 'B': True}

        # Only takes first parent as duplicate.
        children = ga._reproduction([parent_a, parent_b])
        assert len(children) == 1
        assert children[0]['A'] == parent_a['A']
        assert children[0]['B'] == parent_a['B']