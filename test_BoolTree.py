from unittest.mock import MagicMock, Mock
from unittest import TestCase
from BoolTree import VariableNode, BooleanNode, InversionNode

class NotABooleanNode(object):
    """ This class is not a boolean node. """
    def say(self):
        type(self)

class aBooleanNode(BooleanNode):
    """ This class is a boolean node. """
    def say(self):
        return type(self)
    def evaluate(self, input_vector):
        return True

class TestVariableNode(TestCase):
    """ Tests the VariableNode class. """

    def test_setter(self):
        """ Ensures the relevant validation occurs when setting the inner variable. """
        tst_char = 'A'
        nde = VariableNode(tst_char)
        self.assertTrue(nde._variable == tst_char)

        tst_char = None
        with self.assertRaises(AttributeError):
            VariableNode(tst_char)

    def test_evaluation(self):
        """ Ensures the node returns the value of the relevant variable. """
        tst_char = 'A'
        tst_input_vector = {'A': True}
        nde = VariableNode(tst_char)
        assert nde.evaluate(tst_input_vector) is tst_input_vector[tst_char]

        tst_char = 'B'
        tst_input_vector = {'B': False}
        nde = VariableNode(tst_char)
        assert nde.evaluate(tst_input_vector) is tst_input_vector[tst_char]
        
        tst_char = 'C'
        tst_input_vector = {'A': True, 'B': False, 'C': True}
        nde = VariableNode(tst_char)
        assert nde.evaluate(tst_input_vector) is tst_input_vector[tst_char]

        tst_char = 'D'
        tst_input_vector = {'A': True, 'B': False, 'C': True}
        nde = VariableNode(tst_char)
        with self.assertRaises(Exception):
            nde.evaluate(tst_input_vector)

        tst_char = 'A'
        tst_input_vector = {}
        nde = VariableNode(tst_char)
        with self.assertRaises(Exception):
            nde.evaluate(tst_input_vector)

class TestInversionNode(TestCase):
    """ Tests the inversion node. """

    def test_setter_child(self):
        """ Ensures validation protects the child instance variable. """
        try:
            inv_nde = InversionNode(aBooleanNode())     # Hopefully no error when has BooleanNode.
        except AttributeError:
            assert False    # Must fail
        finally:
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


