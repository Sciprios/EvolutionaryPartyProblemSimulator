from unittest.mock import MagicMock, Mock
from unittest import TestCase
from PartyProblemSimulator.SatisfiabilitySimulator.BooleanEquation.CombinationNode import CombinationNode
from PartyProblemSimulator.SatisfiabilitySimulator.BooleanEquation.BooleanNode import BooleanNode
from PartyProblemSimulator.SatisfiabilitySimulator.BooleanEquation.AndNode import AndNode
from PartyProblemSimulator.SatisfiabilitySimulator.BooleanEquation.OrNode import OrNode

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

class CombNode(CombinationNode):
    """ This is a Combination Class. """
    def __init__(self):
        pass
    def evaluate(self, input_vector):
        return True

class TestCombinationNode(TestCase):
    """ Runs tests on the validation of children setting. """

    def test_child_validation(self):
        """ Ensures the validation on setting child nodes is correct. """
        bool_nde = aBooleanNode()
        comb_node = CombNode()
        not_bool_nde = NotABooleanNode()
        # Hopefully no errors
        try:
            nde = AndNode(bool_nde, bool_nde)
        except AttributeError:  # pragma: no cover
            assert False    # Oh no it failed for the AND node!
        else:
            try:
                nde = OrNode(bool_nde, bool_nde)
            except AttributeError:  # pragma: no cover
                assert False    # Oh no it failed for the AND node!
            else:
                assert True # No errors is a good thing!
        
        # Hopefully no errors with a combination node.
        try:
            nde = AndNode(comb_node, comb_node)
        except AttributeError:  # pragma: no cover
            assert False    # Oh no it failed for the AND node!
        else:
            try:
                nde = OrNode(comb_node, comb_node)
            except AttributeError:  # pragma: no cover
                assert False    # Oh no it failed for the AND node!
            else:
                assert True # No errors is a good thing!
        
        # Try forcing errors (lhs node)
        try:
            nde = AndNode(not_bool_nde, bool_nde)
        except AttributeError:
            try:
                nde = OrNode(not_bool_nde, bool_nde)
            except AttributeError:
                assert True # Got an error
            else:  # pragma: no cover
                assert False    # No error
        else:  # pragma: no cover
            assert False    # No error

        # Try forcing errors (rhs node)
        try:
            nde = AndNode(bool_nde, not_bool_nde)
        except AttributeError:
            try:
                nde = OrNode(bool_nde, not_bool_nde)
            except AttributeError:
                assert True # Got an error!
            else:  # pragma: no cover
                assert False    # No error
        else:  # pragma: no cover
            assert False    # No error