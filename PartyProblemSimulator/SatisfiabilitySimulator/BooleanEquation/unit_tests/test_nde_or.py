from unittest.mock import MagicMock, Mock
from unittest import TestCase
from PartyProblemSimulator.SatisfiabilitySimulator.BooleanEquation.OrNode import OrNode
from PartyProblemSimulator.SatisfiabilitySimulator.BooleanEquation.BooleanNode import BooleanNode

class aBooleanNode(BooleanNode):  # pragma: no cover
    """ This class is a boolean node. """
    def say(self):
        return type(self)
    def evaluate(self, input_vector):
        return True

class TestOrNode(TestCase):
    """ Tests the OrNode class. """

    def test_evaluation(self):
        """ Test the evaluation of the or function. """
        fake_true_child = Mock()    # A child to return true.
        fake_false_child = Mock()   # A child to return false.
        nde = OrNode(aBooleanNode(), aBooleanNode())   # Instantiate a node with replaceable children.
        fake_true_child.evaluate = MagicMock(return_value=True)
        fake_false_child.evaluate = MagicMock(return_value=False)

        # 1 OR 1
        nde._lhs_child = fake_true_child
        nde._rhs_child = fake_true_child
        self.assertTrue(nde.evaluate({}))

        # 0 OR 0
        nde._lhs_child = fake_false_child
        nde._rhs_child = fake_false_child
        self.assertFalse(nde.evaluate({}))

        # 1 OR 0
        nde._lhs_child = fake_true_child
        nde._rhs_child = fake_false_child
        self.assertTrue(nde.evaluate({}))

        # 0 OR 1
        nde._lhs_child = fake_false_child
        nde._rhs_child = fake_true_child
        self.assertTrue(nde.evaluate({}))