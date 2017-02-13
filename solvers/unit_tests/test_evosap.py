""" Modules containing tests for the flipga class. """
from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
from solvers.EvoSAP import EvoSAP

class TestFlipGA(TestCase):
    """ Test class for the FlipGA class. """
    
    @patch('solvers.FlipGA.random')
    def test_mutation(self, rand_mock):
        """ Tests the mutation method. """
        ga = EvoSAP(None, ['A', 'B'])   # Instantiate Algorithm
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