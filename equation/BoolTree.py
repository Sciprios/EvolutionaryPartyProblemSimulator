""" This module contains the classes required to make a boolean equation. """
from abc import ABC, abstractmethod

VARIABLES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class BooleanNode(ABC):
    """ An abstract node which contains everything required to create a tree. """

    @abstractmethod
    def evaluate(self, input_vector):   #pragma: no cover
        """ To be implemented to evaluate according to node type. """
        raise NotImplementedError

class Equation(BooleanNode):
    """ Used to analyse an equation. """
    _unparsed_equation = None
    _clauses = []

    def __init__(self, input_string):
        """ Initialises an eqaution by interpreting the input string. """
        self._set_unparsed_equation(input_string)
        self.generate_clauses()

    
    def _validate_string(self, eq_str):
        """ Validates the input string for this equation. """
        valid = True
        brack_count = 0
        i = 0
        # Only brackets and operators allowed not in a clause
        for symbol in eq_str:
            if symbol in VARIABLES: # Vars must be part of a clause
                if brack_count is 0:
                    valid = False
                    break
                if i < (len(eq_str) - 1):
                    if eq_str[i+1] not in ['.', '+', ')']: # Check the next symbol is good to be next to.
                        valid = False
                        break
                if i > 0:
                    if eq_str[i-1] not in ['.', '+', '(', '¬']: # Check the previous symbol is good to be next to.
                        valid = False
                        break
            elif symbol is ')':     # Brackets must be balanced
                if brack_count is 0:
                    valid = False
                    break
                else:
                    brack_count = brack_count - 1
            elif symbol is '(':
                brack_count = brack_count + 1
            elif symbol in ['+', '.']:  # Must have either a clause or variable next to it.
                if i is (len(eq_str) - 1):   # Is it the last character
                    valid = False
                    break
                elif i is 0:    # An operator cannot be the first item
                    valid = False
                    break
                if (eq_str[i+1] not in VARIABLES) and (eq_str[i+1] not in ['(', '¬']):
                    valid = False
                    break
                elif (eq_str[i-1] not in VARIABLES) and (eq_str[i-1] not in [')']):
                    valid = False
                    break
                if brack_count is 0:    # Cannot combine clauses using OR
                    if symbol is '+':
                        valid = False
                        break
            elif symbol is '¬':
                if i is (len(eq_str) - 1):  # Cannot be the last item
                    valid = False
                    break
                if eq_str[i+1] not in VARIABLES:
                    valid = False
                    break
            i = i + 1
        
        if brack_count is not 0:
            valid = False

        return valid
    
    def generate_clauses(self):
        """ Creates a clause array from the _unparsed_equation attribute. """
        bracket_index = 0
        bracket_count = 0
        i = 0
        for symbol in self._unparsed_equation:
            if symbol is '(':
                if bracket_count is 0:
                    bracket_index = i   # We have found a new clause.
                bracket_count = bracket_count + 1
            elif symbol is ')':
                bracket_count = bracket_count - 1
                if bracket_count is 0:  # Have we found the end to a clause?
                    new_clause = self._generate_clause(self._unparsed_equation[bracket_index+1:i])  # Only want to parse string not including brackets.
                    self._clauses.append(new_clause)
            i = i + 1
    
    def _generate_clause(self, clause):
        """ Generates an initial node for a clause. This method assumes "clause" is validated. """
        node = None
        if clause[0] in VARIABLES:  # First items a variable
            if len(clause) == 1:
                nde = VariableNode(clause[0])
                return nde
            elif clause[1] in ['.', '+']:
                lhs = VariableNode(clause[0])  # Generate a combining node with rest of clause.
                rhs = self._generate_clause(clause[2:])
                if clause[1] is '.':
                    return AndNode(lhs, rhs)    # It's an AND combination
                else:
                    return OrNode(lhs, rhs)     # It's an OR combination
        elif clause[0] is '(':  # First item's a opening bracket:
            # Find the end of this sub-clause
            brack_count = 0
            i = 0
            for j in clause:
                if j is '(':    # Found a new bracket opening
                    brack_count = brack_count + 1
                elif j is ')':  # Found a matching end bracket
                    brack_count = brack_count - 1
                    if i < len(clause) - 1: # Not the last symbol
                        if brack_count is 0:    # Got to the end of the brackets
                            lhs = self._generate_clause(clause[1:i])    # LHS in this clause
                            rhs = self._generate_clause(clause[i+2:])   # RHS after operator
                            if clause[i+1] is '.':
                                return AndNode(lhs, rhs)
                            else:
                                return OrNode(lhs, rhs)
                    else:
                        break
                i = i + 1
        elif clause[0] is '¬':  # Found an inversion
            i = 0
            while i < len(clause) - 1:
                if clause[i+1] in ['.', '+']:
                    lhs = InversionNode(self._generate_clause(clause[1:i+1]))   # Inverted part
                    rhs = self._generate_clause(clause[i+2:])   # Bit after inversion
                    if clause[i+1] is '.':
                        return AndNode(lhs, rhs)
                    else:
                        return OrNode(lhs, rhs)
                i = i + 1
            # Haven't found an operator so we will assume its a single clause
            return InversionNode(self._generate_clause(clause[1:]))
                
    def evaluate(self, input_vector):
        """ Evaluates the CNF equation through AND'ing the clauses. """
        if False in self.get_clause_evaluation(input_vector):
            return False
        else:
            return True
    
    def get_clause_evaluation(self, input_vector):
        """ Returns an array with the clause evaluations. """
        result = []
        for i in self._clauses:
            result.append(i.evaluate(input_vector))
        return result


    def _set_unparsed_equation(self, eq_str):
        """ Verifies and sets the unparsed equation attribute. """
        if self._validate_string(eq_str):
            self._unparsed_equation = eq_str
        else:
            raise AttributeError("The input string does not satisfy the validation requirements.")

class VariableNode(BooleanNode):
    """ A node which evaluates as a variable. """
    _variable = None

    def __init__(self, var_char):
        """ Instantiates a variable node which uses the variable character provided. """
        self._set_variable(var_char)
    
    def evaluate(self, input_vector):
        """ Evaluates according to the value of the variable in input vector. """
        if self._variable in input_vector:
            return input_vector[self._variable]
        else:
            raise Exception("The variable {} is not provided in input vector.".format(self._variable))
    
    def _set_variable(self, variable):
        """ Setter for the variable of this node. """
        if variable is None:
            raise AttributeError("A VariableNode cannot have its value set to None.")
        else:
            self._variable = variable

class InversionNode(BooleanNode):
    """ A node which inverts its child. """
    _child = None

    def __init__(self, child):
        """ Instantiates a variable node which uses the variable character provided. """
        self._set_child(child)
    
    def evaluate(self, input_vector):
        """ Evaluates according to the value of the variable in input vector. """
        if self._child is None:
            raise AttributeError("_child cannot be none in an InversionNode.")
        else:
            return not (self._child.evaluate(input_vector))
    
    def _set_child(self, child):
        """ Setter for the child of this node. """
        if issubclass(type(child), BooleanNode):
            self._child = child
        else:
            raise AttributeError("The child of an OperatorNode must be a descendent of a BooleanNode.")

class CombinationOperatorNode(BooleanNode, ABC):
    """ An abstract node which carries out an operation on its children. """
    _lhs_child = None
    _rhs_child = None

    def __init__(self, lhs_child, rhs_child):
        """ Instantiates an operator node with two children. """
        self._set_lhs_child(lhs_child)
        self._set_rhs_child(rhs_child)
    
    def _set_lhs_child(self, child):
        """ Sets the reference of the left hand side child. """
        if issubclass(type(child), BooleanNode) or issubclass(type(child), CombinationOperatorNode):
            self._lhs_child = child
        else:
            raise AttributeError("The child of an OperatorNode must be a descendent of a BooleanNode.")
    
    def _set_rhs_child(self, child):
        """ Sets the reference of the right hand side child. """
        if issubclass(type(child), BooleanNode) or issubclass(type(child), CombinationOperatorNode):
            self._rhs_child = child
        else:
            raise AttributeError("The child of an OperatorNode must be a descendent of a BooleanNode.")

class AndNode(CombinationOperatorNode):
    """ This class allows two child nodes to be AND'ed together. """

    def evaluate(self, input_vector):
        """ And's two child nodes to produce an output. """
        return (self._lhs_child.evaluate(input_vector) and self._rhs_child.evaluate(input_vector))

class OrNode(CombinationOperatorNode):
    """ This class allows two child nodes to be OR'ed together. """

    def evaluate(self, input_vector):
        """ Or's two child nodes to produce an output. """
        return (self._lhs_child.evaluate(input_vector) or self._rhs_child.evaluate(input_vector))
