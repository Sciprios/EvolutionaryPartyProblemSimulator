""" Modules containing tests for the BlindGA class. """
from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
from solvers.BlindGA import BlindGA

class TestBlindGA(TestCase):
    """ Test class for the BlindGA class. """
    
    def test_init(self):
        """ Ensure properties of the genetic algorithm are set properly. """
        eq = Mock()
        vars = Mock()
        ga = BlindGA(eq, vars)
        assert ga._NUM_PARENTS == 2
        assert ga._MUTATION_RATE == 0.9
        assert ga._POP_SIZE == 10
        assert ga._EQUATION is eq
        assert ga._variables is vars

    def test_evaluation(self):
        """ Tests the evaluation method. """
        eq = Mock()
        eq.get_clause_evaluation = Mock(return_value=[True, True, True, True, True])  # Standard value to check for
        vars = Mock()
        ga = BlindGA(eq, vars)
        ga.population = [1,1,1,1,1,1,1,1,1,1]   # Population of 10
        ga._evaluation()
        assert ga.fitness_values == [5,5,5,5,5,5,5,5,5,5]

    def test_selection(self):
        """ Tests the parent selection method. """
        a = Mock()  # Setup fake population
        b = Mock()
        c = Mock()
        ga = BlindGA(None, None) # Instantiate our instance
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
    
    @patch('solvers.BlindGA.random')
    def test_reproduction(self, rand_mock):
        """ Tests the reproduction of the BlindGA. """
        ga = BlindGA(None, ['A', 'B']) # Instantiate algorithm
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
    
    @patch('solvers.BlindGA.random')
    def test_mutation(self, rand_mock):
        """ Tests the mutation method. """
        ga = BlindGA(None, ['A', 'B'])   # Instantiate Algorithm
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
        rand_mock.randint = Mock(return_value=0)    # Mutate the A variable
        ga._mutation(pop)
        assert pop[0]['A'] is False
        assert pop[0]['B'] is False
        assert pop[1]['A'] is True
        assert pop[1]['B'] is False

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
        rand_mock.randint = Mock(return_value=0)    # Mutate the A variable
        ga._mutation(pop)
        assert pop[0]['A'] is True
        assert pop[0]['B'] is False
        assert pop[1]['A'] is False
        assert pop[1]['B'] is False