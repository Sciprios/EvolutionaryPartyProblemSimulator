from unittest.mock import MagicMock, Mock
from unittest import TestCase
from BoolTree import SimpleNode, InverseNode, AndNode, OrNode

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

class TestInverseNode(TestCase):
    """ Tests the simple node class. """
    
    def test_evaluate(self):
        """ Ensures the simple node evaluates itself properly. """
        nde = InverseNode(SimpleNode('A'))
        assert not nde.evaluate({'A': True})
        assert nde.evaluate({'A': False})
        assert not nde.evaluate({'B': True, 'A': True})
        assert nde.evaluate({'A': False, 'B': True})

class TestAndNode(TestCase):
    """ Tests the AND node class. """

    def test_init(self):
        """ Ensures the node is initialised  """
        nde = AndNode(1, 1)
        assert nde.a == 1
        assert nde.b == 1
    
    def test_evaluate(self):
        """ Ensures the simple node evaluates itself properly. """
        fake_a = Mock()
        fake_b = Mock()

        nde = AndNode(fake_a, fake_b)

        # Both false
        fake_a.evaluate = MagicMock(return_value=False)
        fake_b.evaluate = MagicMock(return_value=False)
        assert not nde.evaluate({})

        # Both true
        fake_a.evaluate = MagicMock(return_value=True)
        fake_b.evaluate = MagicMock(return_value=True)
        assert nde.evaluate({})

        # OR case 1
        fake_a.evaluate = MagicMock(return_value=True)
        fake_b.evaluate = MagicMock(return_value=False)
        assert not nde.evaluate({})

        # OR case 2
        fake_a.evaluate = MagicMock(return_value=False)
        fake_b.evaluate = MagicMock(return_value=True)
        assert not nde.evaluate({})

class TestOrNode(TestCase):
    """ Tests the OR node class. """

    def test_init(self):
        """ Ensures the node is initialised  """
        nde = OrNode(1, 1)
        assert nde.a == 1
        assert nde.b == 1
    
    def test_evaluate(self):
        """ Ensures the simple node evaluates itself properly. """
        fake_a = Mock()
        fake_b = Mock()

        nde = OrNode(fake_a, fake_b)

        # Both false
        fake_a.evaluate = MagicMock(return_value=False)
        fake_b.evaluate = MagicMock(return_value=False)
        assert not nde.evaluate({})

        # Both true
        fake_a.evaluate = MagicMock(return_value=True)
        fake_b.evaluate = MagicMock(return_value=True)
        assert nde.evaluate({})

        # OR case 1
        fake_a.evaluate = MagicMock(return_value=True)
        fake_b.evaluate = MagicMock(return_value=False)
        assert nde.evaluate({})

        # OR case 2
        fake_a.evaluate = MagicMock(return_value=False)
        fake_b.evaluate = MagicMock(return_value=True)
        assert nde.evaluate({})