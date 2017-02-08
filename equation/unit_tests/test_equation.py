from unittest.mock import MagicMock, Mock, call
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
    
    def test_gen_clause_list(self):
        """ Ensures the method generates the set of clauses. """
        eq = Equation('')
        eq._generate_clause = MagicMock(return_value="FakeClause")  # Fake the generation of a clause node.
        
        eq._unparsed_equation = '(ABCD).(1234).(9876)'  # Setup some fake clauses
        expected_calls = [call('ABCD'), call('1234'), call('9876')]
        eq._generate_clauses()
        eq._generate_clause.assert_has_calls(expected_calls)

        eq._unparsed_equation = '(ABCD)'  # Setup a fake clause
        expected_calls = [call('ABCD')]
        eq._generate_clauses()
        eq._generate_clause.assert_has_calls(expected_calls)

        eq._unparsed_equation = ''  # Setup no fake clauses
        expected_calls = []
        eq._generate_clauses()
        eq._generate_clause.assert_has_calls(expected_calls)
    
    def test_gen_clause(self):
        """ Ensures the clause generation method creates the correct tree structure. """
        eq = Equation('')

        # Non-sub clause check
        rslt = eq._generate_clause('A.B.C')
        assert type(rslt) is AndNode    # Check the node types
        assert type(rslt._lhs_child) is VariableNode
        assert type(rslt._rhs_child) is AndNode

        vec = {'A': True, 'B': True, 'C': True}
        assert rslt.evaluate(vec)   # Check some evaluations.
        vec = {'A': False, 'B': True, 'C': True}
        self.assertFalse(rslt.evaluate(vec))
        vec = {'A': True, 'B': True, 'C': False}
        self.assertFalse(rslt.evaluate(vec))
        vec = {'A': False, 'B': False, 'C': True}
        self.assertFalse(rslt.evaluate(vec))

        # With inversion?
        rslt = eq._generate_clause('¬A.B')
        assert type(rslt) is AndNode    # Check the node types
        assert type(rslt._lhs_child) is InversionNode
        assert type(rslt._rhs_child) is VariableNode

        vec = {'A': True, 'B': True}
        self.assertFalse(rslt.evaluate(vec))   # Check some evaluations.
        vec = {'A': False, 'B': True}
        self.assertTrue(rslt.evaluate(vec))

        # Sub Clause check
        rslt = eq._generate_clause('A.(B+C).D')
        assert type(rslt) is AndNode    # Check the node types
        assert type(rslt._lhs_child) is VariableNode
        assert type(rslt._rhs_child) is AndNode

        vec = {'A': True, 'B': True, 'C': True, 'D': True}
        assert rslt.evaluate(vec)   # Check some evaluations.
        vec = {'A': True, 'B': False, 'C': True, 'D': True}
        assert rslt.evaluate(vec)
        vec = {'A': True, 'B': True, 'C': True, 'D': False}
        self.assertFalse(rslt.evaluate(vec))
        vec = {'A': True, 'B': True, 'C': False, 'D': False}
        self.assertFalse(rslt.evaluate(vec))
        vec = {'A': True, 'B': False, 'C': True, 'D': False}
        self.assertFalse(rslt.evaluate(vec))

        # Inversion check
        rslt = eq._generate_clause('A.(¬B.¬C).D')
        assert type(rslt) is AndNode    # Check the node types
        assert type(rslt._lhs_child) is VariableNode
        assert type(rslt._rhs_child) is AndNode

        vec = {'A': True, 'B': False, 'C': False, 'D': True}
        assert rslt.evaluate(vec)   # Check some evaluations.
        vec = {'A': True, 'B': False, 'C': True, 'D': True}
        self.assertFalse(rslt.evaluate(vec))
        vec = {'A': False, 'B': False, 'C': False, 'D': False}
        self.assertFalse(rslt.evaluate(vec))
        vec = {'A': False, 'B': False, 'C': False, 'D': True}
        self.assertFalse(rslt.evaluate(vec))