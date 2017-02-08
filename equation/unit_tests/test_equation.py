from unittest.mock import MagicMock, Mock
from unittest import TestCase
from equation.BoolTree import Equation, VariableNode, BooleanNode, CombinationOperatorNode, InversionNode, AndNode, OrNode, Clause


class TestEquation(TestCase):
    """ Tests the Equation class. """

    def test_evaluate(self):
        """ Ensures the evaluate class tests response for a False. """
        nde = Equation('')

        rtn_val = [True, True, True]
        nde.get_clause_evaluation = MagicMock(return_value=rtn_val)
        self.assertTrue(nde.evaluate({}))

        rtn_val = [True, False, True]
        nde.get_clause_evaluation = MagicMock(return_value=rtn_val)
        self.assertFalse(nde.evaluate({}))
    
    def test_gen_tree(self):
        """ Ensures the method generates the set of clauses. """
        pass