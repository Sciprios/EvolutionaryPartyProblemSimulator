""" Modules containing tests for the flipga class. """
from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
from solvers.experimental.EvoSAP import EvoSAP_AES

class TestEvoSAP(TestCase):
    """ Test class for the EvoSAP experimental classes. """

    @patch('solvers.EvoSAP.random')
    def test_AES_implementation(self, rand_mock):
        """ Ensures the AES implementation increments the eval_count. """
        eq = Mock()
        vars = Mock()

        ## Test cases
        ga = EvoSAP_AES(eq, ['A'])
        prev = ga.eval_count
        rand_mock.shuffle = Mock(return_value=[0])
        children = [{'A':    False}]    # A child who is wrong, to be flipped
        ga._calc_clausal_score = Mock()
        ga._calc_clausal_score.return_value = 1
        ga._heuristic_method(children)
        assert children[0]['A'] # Should now be true
        assert ga.eval_count > prev

    def test_evaluation(self):
        """ Tests the evaluation method. """
        eq = Mock()
        eq.get_clause_evaluation = Mock(return_value=[True, True, True, True, True])  # Standard value to check for
        vars = Mock()
        ga = EvoSAP_AES(eq, vars)
        prev = ga.eval_count
        ga.population = [1]   # Population of 1
        ga._evaluation()
        assert ga.fitness_values == [5]
        assert prev < ga.eval_count