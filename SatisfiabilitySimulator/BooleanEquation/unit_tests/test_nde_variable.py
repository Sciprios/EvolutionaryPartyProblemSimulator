from unittest.mock import MagicMock, Mock
from unittest import TestCase
from PartyProblemSimulator.SatisfiabilitySimulator.BooleanEquation.VariableNode import VariableNode

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