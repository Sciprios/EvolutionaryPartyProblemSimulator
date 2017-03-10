""" Modules containing tests for the flipga class. """
from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
from SatisfiabilitySimulator.Solvers.FlipGA import FlipGA

class TestFlipGA(TestCase):
    """ Test class for the FlipGA class. """
    
    def test_init(self):
        """ Ensure properties of the genetic algorithm are set properly. """
        eq = Mock()
        vars = Mock()
        ga = FlipGA(eq, vars)
        assert ga._NUM_PARENTS == 2
        assert ga._MUTATION_RATE == 0.9
        assert ga._POP_SIZE == 10
        assert ga._EQUATION is eq
        assert ga._variables is vars
    
    @patch('SatisfiabilitySimulator.Solvers.FlipGA.random')
    def test_heuristic_method(self, rand_mock):
        """ Ensures the algorithm flips children correctly. """
        eq = Mock()
        vars = Mock()

        ## Test cases
        ga = FlipGA(eq, ['A'])
        rand_mock.shuffle = Mock(return_value=[0])
        children = [{'A':    False}]    # A child who is wrong, to be flipped
        ga._calc_clausal_score = Mock()
        ga._calc_clausal_score.return_value = 1
        ga._heuristic_method(children)
        assert children[0]['A'] # Should now be true

        ga = FlipGA(eq, ['A', 'B'])
        rand_mock.shuffle = Mock(return_value=[0, 1])
        children = [{'A':    False, 'B':    True}]    # A child who is wrong, to be flipped
        ga._calc_clausal_score = Mock()
        ga._calc_clausal_score.return_value = 2

        ga._heuristic_method(children)
        self.assertTrue(children[0]['A']) # Should now be true
        self.assertFalse(children[0]['B'])  # Should not have been flipped

    def test_evaluation(self):
        """ Tests the evaluation method. """
        eq = Mock()
        eq.get_clause_evaluation = Mock(return_value=[True, True, True, True, True])  # Standard value to check for
        vars = Mock()
        ga = FlipGA(eq, vars)
        ga.population = [1,1,1,1,1,1,1,1,1,1]   # Population of 10
        ga._evaluation()
        assert ga.fitness_values == [5,5,5,5,5,5,5,5,5,5]

    def test_selection(self):
        """ Tests the parent selection method. """
        a = Mock()  # Setup fake population
        b = Mock()
        c = Mock()
        ga = FlipGA(None, None) # Instantiate our instance
        ga.population = [a, b, c]
        fitness_values = [100, 90, 0]
        parents = ga._parent_selection(fitness_values)
        assert a in parents
        assert b in parents

        ga.population = [a, b, c]
        fitness_values = [0, 90, 5]
        parents = ga._parent_selection(fitness_values)
        assert b in parents
        assert c in parents
    
    @patch('SatisfiabilitySimulator.Solvers.FlipGA.random')
    def test_reproduction(self, rand_mock):
        """ Tests the reproduction of the FlipGA. """
        ga = FlipGA(None, ['A', 'B']) # Instantiate algorithm
        # Fake parents
        parent_a = {
            'A': True,
            'B': False
        }
        parent_b = {
            'A': False,
            'B': True
        }
        parents = [parent_a, parent_b]
        rand_mock.randint = Mock(return_value=1)    # Split parents between A and B
        children = ga._reproduction(parents)
        assert children[0]['A'] == parent_a['A']
        assert children[0]['B'] == parent_b['B']
        assert children[1]['A'] == parent_b['A']
        assert children[1]['B'] == parent_a['B']

        parents = [parent_a, parent_b]
        rand_mock.randint = Mock(return_value=2)    # No split as beyond number of vars A and B
        children = ga._reproduction(parents)
        assert children[0]['A'] == parent_a['A']    # Child a should get all genes from parent a
        assert children[0]['B'] == parent_a['B']
        assert children[1]['A'] == parent_b['A']    # Child b should get all genes from parent b
        assert children[1]['B'] == parent_b['B']
    
    @patch('SatisfiabilitySimulator.Solvers.FlipGA.random')
    def test_mutation(self, rand_mock):
        """ Tests the mutation method. """
        ga = FlipGA(None, ['A', 'B'])   # Instantiate Algorithm
        pop = [ # Population
            {
                'A': True,
                'B': False
            },
            {
                'A': False,
                'B': False
            }
        ]
        rand_mock.random = Mock(return_value=0)     # Cause a mutation
        ga._mutation(pop)
        assert pop[0]['A'] is False
        assert pop[0]['B'] is True
        assert pop[1]['A'] is True
        assert pop[1]['B'] is True

        pop = [ # Repopulate
            {
                'A': True,
                'B': False
            },
            {
                'A': False,
                'B': False
            }
        ]
        rand_mock.random = Mock(return_value=1)     # Don't mutate
        ga._mutation(pop)
        assert pop[0]['A'] is True
        assert pop[0]['B'] is False
        assert pop[1]['A'] is False
        assert pop[1]['B'] is False