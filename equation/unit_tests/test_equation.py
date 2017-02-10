from unittest.mock import MagicMock, Mock, call, patch
from unittest import TestCase
from equation.BoolTree import Equation, VariableNode, BooleanNode, CombinationOperatorNode, InversionNode, AndNode, OrNode


class TestEquation(TestCase):
    """ Tests the Equation class. """
    @patch('equation.BoolTree.Equation._validate_string')
    def test_evaluate(self, val):
        """ Ensures the evaluate class tests response for a False. """
        nde = Equation('(A)')

        rtn_val = [True, True, True]
        nde.get_clause_evaluation = MagicMock(return_value=rtn_val)
        self.assertTrue(nde.evaluate({}))

        rtn_val = [True, False, True]
        nde.get_clause_evaluation = MagicMock(return_value=rtn_val)
        self.assertFalse(nde.evaluate({}))
    
    @patch('equation.BoolTree.Equation._generate_clause')
    def test_gen_clause_list(self, gen_clause):
        """ Ensures the method generates the set of clauses. """
        gen_clause.return_value = "FakeClause" # Fake the generation of a clause node.
        eq = Equation('(A)')
        
        eq._unparsed_equation = '(ABCD).(1234).(9876)'  # Setup some fake clauses
        expected_calls = [call('ABCD'), call('1234'), call('9876')]
        eq.generate_clauses()
        eq._generate_clause.assert_has_calls(expected_calls)

        eq._clauses = []    # Reset clauses
        eq._unparsed_equation = '(ABCD)'  # Setup a fake clause
        expected_calls = [call('ABCD')]
        eq.generate_clauses()
        eq._generate_clause.assert_has_calls(expected_calls)

        eq._clauses = []    # Reset clauses
        eq._unparsed_equation = ''  # Setup no fake clauses
        expected_calls = []
        eq.generate_clauses()
        eq._generate_clause.assert_has_calls(expected_calls)
    
    def test_gen_clause(self):
        """ Ensures the clause generation method creates the correct tree structure. """
        eq = Equation('(A)')

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
        rslt = eq._generate_clause('¬A+(B)+B')
        assert type(rslt) is OrNode    # Check the node types
        assert type(rslt._lhs_child) is InversionNode
        assert type(rslt._rhs_child) is OrNode

        vec = {'A': True, 'B': True}
        self.assertTrue(rslt.evaluate(vec))   # Check some evaluations.
        vec = {'A': True, 'B': False}
        self.assertFalse(rslt.evaluate(vec))

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

    def test_clausal_evaluation(self):
        """ Tests the evaluation of a selection of clauses. """
        eq = Equation('(A)')   # Equation object to test.
        fke_clause_true = Mock()    # Fake clause to return true
        fke_clause_true.evaluate = MagicMock(return_value=True)
        fke_clause_false = Mock()   # Fake clause to return false
        fke_clause_false.evaluate = MagicMock(return_value=False)

        eq._clauses = [fke_clause_true, fke_clause_false, fke_clause_true]
        res = eq.get_clause_evaluation({})
        assert (res[0] and (not res[1]) and res[2])

        eq._clauses = [fke_clause_true, fke_clause_true, fke_clause_true]
        res = eq.get_clause_evaluation({})
        assert (res[0] and res[1] and res[2])

        eq._clauses = [fke_clause_false, fke_clause_false, fke_clause_false]
        res = eq.get_clause_evaluation({})
        assert not (res[0] or res[1] or res[2])

    def test_str_validation(self):
        """ Ensures the string validation method validates strings correctly. """
        test_cases = self.gen_validation_cases()
        eq = Equation('(A)')
        for case in test_cases:
            self.assertTrue(eq._validate_string(case['str']) == case['exp'], case)

    def gen_validation_cases(self):
        """ Returns some string test cases for validation. """
        return [
            {
                'str': 'A.B',
                'exp': False
            },
            {
                'str': '(A).(B)',
                'exp': True
            },
            {
                'str': '(A)',
                'exp': True
            },
            {
                'str': '(A)+(B)',
                'exp': False
            },
            {
                'str': '(A+C+D).(B+D)',
                'exp': True
            },
            {
                'str': '(A+C+D).(B+D).(A)',
                'exp': True
            },
            {
                'str': '(AC)',
                'exp': False
            },
            {
                'str': '(+A).(D)',
                'exp': False
            }
            ,
            {
                'str': '(A¬)',
                'exp': False
            },
            {
                'str': '(¬A)',
                'exp': True
            }
        ]