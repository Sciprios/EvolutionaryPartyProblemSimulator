from unittest.mock import MagicMock, Mock
from unittest import TestCase
from equation.BoolTree import VariableNode, BooleanNode, CombinationOperatorNode, InversionNode, AndNode, OrNode, Clause

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

class CombNode(CombinationOperatorNode):
    """ This is a CombinationOperator Class. """
    def __init__(self):
        pass
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
        except AttributeError:
            assert False    # Oh no it failed for the AND node!
        else:
            try:
                nde = OrNode(bool_nde, bool_nde)
            except AttributeError:
                assert False    # Oh no it failed for the AND node!
            else:
                assert True # No errors is a good thing!
        
        # Hopefully no errors with a combination node.
        try:
            nde = AndNode(comb_node, comb_node)
        except AttributeError:
            assert False    # Oh no it failed for the AND node!
        else:
            try:
                nde = OrNode(comb_node, comb_node)
            except AttributeError:
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
            else:
                assert False    # No error
        else:
            assert False    # No error

        # Try forcing errors (rhs node)
        try:
            nde = AndNode(bool_nde, not_bool_nde)
        except AttributeError:
            try:
                nde = OrNode(bool_nde, not_bool_nde)
            except AttributeError:
                assert True # Got an error!
            else:
                assert False    # No error
        else:
            assert False    # No error

class TestAndNode(TestCombinationNode):
    """ Tests the AndNode class. """

    def test_evaluation(self):
        """ Test the evaluation of the and function. """
        fake_true_child = Mock()    # A child to return true.
        fake_false_child = Mock()   # A child to return false.
        nde = AndNode(aBooleanNode(), aBooleanNode())   # Instantiate a node with replaceable children.
        fake_true_child.evaluate = MagicMock(return_value=True)
        fake_false_child.evaluate = MagicMock(return_value=False)

        # 1 AND 1
        nde._lhs_child = fake_true_child
        nde._rhs_child = fake_true_child
        self.assertTrue(nde.evaluate({}))

        # 0 AND 0
        nde._lhs_child = fake_false_child
        nde._rhs_child = fake_false_child
        self.assertFalse(nde.evaluate({}))

        # 1 AND 0
        nde._lhs_child = fake_true_child
        nde._rhs_child = fake_false_child
        self.assertFalse(nde.evaluate({}))

        # 0 AND 1
        nde._lhs_child = fake_false_child
        nde._rhs_child = fake_true_child
        self.assertFalse(nde.evaluate({}))

class TestOrNode(TestCombinationNode):
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

class TestClause(TestCase):
    """ Tests the Clause class. """

    def test_setting_of_node(self):
        """ Tests the validation of its node. """
        bool_nde = aBooleanNode()
        comb_node = CombNode()
        not_bool_nde = NotABooleanNode()

        # Try boolean node
        try:
            nde = Clause(bool_nde)
        except AttributeError:
            assert False
        else:
            assert True
        
        # Try comb node
        try:
            nde = Clause(comb_node)
        except AttributeError:
            assert False
        else:
            assert True
        
        # Try non-valid node
        try:
            nde = Clause(not_bool_nde)
        except AttributeError:
            assert True
        else:
            assert False