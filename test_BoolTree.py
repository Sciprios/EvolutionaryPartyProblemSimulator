from unittest import TestCase
from BoolTree import SimpleNode

class TestSimpleNode(TestCase):
    """ Tests the simple node class. """

    def test_init(self):
        """ Ensures the node is initialised  """
        nde = SimpleNode('B')
        assert nde.id is 'B'
    
    def test_evaluate(self):
        """ Ensures the simple node evaluates itself properly. """
        nde = SimpleNode('A')
        assert nde.evaluate({'A': True})
        assert not nde.evaluate({'A': False})
        assert nde.evaluate({'B': True, 'A': True})
        assert not nde.evaluate({'A': False, 'B': True})