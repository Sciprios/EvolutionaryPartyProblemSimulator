""" This module contains the unittests for the conversions methods module. """
from unittest.mock import MagicMock, Mock
from unittest import TestCase
import ConversionMethods

class TestValidationBrackets(TestCase):
    """ Tests the validation methods for brackets. """

    def test_equal_brackets(self):
        """ Ensures validation requires equal brackets. """
        valid_string = 'A' # A valid string containing a single variable.

        # Equal
        tst_strng = '{}'.format(valid_string)
        self.assertTrue(ConversionMethods.validate_string(tst_strng))

        tst_strng = '({})'.format(valid_string)
        self.assertTrue(ConversionMethods.validate_string(tst_strng))
        
        tst_strng = '((((({})))))'.format(valid_string)
        self.assertTrue(ConversionMethods.validate_string(tst_strng))

        # Unequal
        tst_strng = '({}'.format(valid_string)
        self.assertFalse(ConversionMethods.validate_string(tst_strng))

        tst_strng = '{})'.format(valid_string)
        self.assertFalse(ConversionMethods.validate_string(tst_strng))

        tst_strng = '(({})'.format(valid_string)
        self.assertFalse(ConversionMethods.validate_string(tst_strng))

        tst_strng = '({}))'.format(valid_string)
        self.assertFalse(ConversionMethods.validate_string(tst_strng))
    
    def test_valid_open_bracket_neighbours(self):
        """ Ensures brackets have valid neighbours. """
        # Valid
        # Before bracket
        valid_string = '(A)'
        self.assertTrue(ConversionMethods.validate_string(valid_string))    # Nothing is valid

        for i in ConversionMethods.OPERATORS:   # Operators are valid
            tst_strng = "{}{}{}".format(valid_string, i, valid_string)
            self.assertTrue(ConversionMethods.validate_string(tst_strng))
        tst_strng = "{}{}".format(ConversionMethods.INVERSE, valid_string)

        self.assertTrue(ConversionMethods.validate_string(valid_string))    # Inverse op. is valid

        # After bracket
        valid_string = "({})"
        for i in ConversionMethods.VARIABLES:   # variables are valid
            tst_strng = "({})".format(i)
            self.assertTrue(ConversionMethods.validate_string(tst_strng))

    def test_invalid_open_bracket_neighbours(self):
        """ Ensures brackets have valid neighbours. """
        # Valid
        # Before bracket
        valid_string = '(A)'
        for i in ConversionMethods.VARIABLES:   # Variables are invalid
            tst_strng = "{}{}".format(i, valid_string)
            self.assertFalse(ConversionMethods.validate_string(tst_strng))
        
        tst_strng = "{}{}".format(')', valid_string)
        self.assertTrue(ConversionMethods.validate_string(valid_string))    # Closing bracket is invalid

        # After bracket
        valid_string = "({})"
        self.assertFalse(ConversionMethods.validate_string('('))    # Nothing is invalid

        self.assertFalse(ConversionMethods.validate_string('()'))   # Closing bracket is invalid

        for i in ConversionMethods.OPERATORS:   # Operators are invalid
            tst_strng = "({})".format(i)
            self.assertFalse(ConversionMethods.validate_string(tst_strng))

class TestValidationCases(TestCase):
    """ Ensures the validation methods correctly validate strings completely. """

    def test_clauses(self):
        """ Validates single clauses. """
        clauses = self.get_clauses()
        for i in clauses:
            self.assertTrue(ConversionMethods.validate_string(i['strng']) is i['truth'])

    def get_clauses(self):
        """ Method to return some tru clauses. """
        clauses = [
            {
                'strng': 'A.B',
                'truth': True
            },
            {
                'strng': 'A+B',
                'truth': True
            },
            {
                'strng': 'A+B.C',
                'truth': True
            },
            {
                'strng': '¬A.¬B',
                'truth': True
            },
            {
                'strng': '¬A.B',
                'truth': True
            },
            {
                'strng': 'A.¬B',
                'truth': True
            },
            {
                'strng': 'AB',
                'truth': False
            },
            {
                'strng': 'A(B',
                'truth': False
            },
            {
                'strng': '((A)',
                'truth': False
            },
            {
                'strng': '.',
                'truth': False
            },
            {
                'strng': '¬',
                'truth': False
            },
            {
                'strng': 'A.BB',
                'truth': False
            }
        ]
        return clauses
