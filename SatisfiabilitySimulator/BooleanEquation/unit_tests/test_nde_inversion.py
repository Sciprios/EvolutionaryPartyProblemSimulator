from unittest.mock import MagicMock, Mock
from unittest import TestCase
from BooleanEquation.BooleanNode import BooleanNode
from BooleanEquation.InversionNode import InversionNode

class NotABooleanNode(object):  # pragma: no cover
    """ This class is not a boolean node. """
    def say(self):
        type(self)

class aBooleanNode(BooleanNode):  # pragma: no cover
    """ This class is a boolean node. """
    def say(self):
        return type(self)
    def evaluate(self, input_vector):
        return True

class TestInversionNode(TestCase):
    """ Tests the inversion node. """

    def test_setter_child(self):
        """ Ensures validation protects the child instance variable. """
        try:
            inv_nde = InversionNode(aBooleanNode())     # Hopefully no error when has BooleanNode.
        except AttributeError:
            assert False    # Must fail
        else:
            assert True     # No error! Yay!
        
        with self.assertRaises(AttributeError):
            inv_nde = InversionNode(NotABooleanNode())  # Error raised when not a BooleanNode.
    
    def test_evaluate(self):
        """ Ensures the inversion node inverts its childs evaluation. """
        child = Mock()
        inv_nde = InversionNode(aBooleanNode())

        child.evaluate = MagicMock(return_value=True)   # When child returns true
        inv_nde._child = child
        self.assertFalse(inv_nde.evaluate({}))

        child.evaluate = MagicMock(return_value=False)  # When child returns false
        inv_nde._child = child
        self.assertTrue(inv_nde.evaluate({}))