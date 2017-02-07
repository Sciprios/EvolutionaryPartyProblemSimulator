""" This module contains the classes required to make a boolean equation. """
from abc import ABC, abstractmethod
from enum import Enum

class Symbols(Enum):
    LHS_BRACKET = '('
    RHS_BRACKET = ')'
    OR = '+'
    AND = '.'
    INVERSE = '¬'
    VARIABLES = ['A', 'B', 'C', 'D', 'E']

class BooleanNode(ABC):
    """ An abstract node which contains everything required to create a tree. """

    @abstractmethod
    def evaluate(self, input_vector):
        """ To be implemented to evaluate according to node type. """
        raise NotImplementedError

class Equation(BooleanNode):
    """ Used to analyse an equation. """
    _unparsed_equation = None
    _clauses = []

    def __init__(self, input_string):
        """ Initialises an eqaution by interpreting the input string. """
        self._set_unparsed_equation(input_string)

    
    def _validate_string(self, eq_str):
        """ Validates the input string for this equation. """
        pass
    
    def _generate_tree(self):
        """ Creates a tree from the _unparsed_equation attribute. """
        bracket_index = 0
        bracket_count = 0
        i = 0
        for symbol in self._unparsed_equation:
            if symbol is Symbols.LHS_BRACKET:
                if bracket_count is 0:
                    bracket_index = i   # We have found a new clause.
                bracket_count = bracket_count + 1
            elif symbol is Symbols.RHS_BRACKET:
                bracket_count = bracket_count - 1
                if bracket_count is 0:  # Have we found the end to a clause?
                    new_clause = self._generate_clause(self._unparsed_equation[bracket_index-1:i])  # Only want to parse string not including brackets.
                    self._clauses.append(new_clause)
            i = i + 1
    
    def _generate_clause(self, clause):
        """ Generates an initial node for a clause. This method assumes "clause" is validated. """
        node = None
        if clause[0] in Symbols.VARIABLES:  # First items a variable
            if clause[1] in [Symbols.AND, Symbols.OR]:
                lhs = VariableNode(symbol)  # Generate a combining node with rest of clause.
                rhs = self._generate_clause(clause[2:])
                if clause[1] is Symbols.AND:
                    return AndNode(lhs, rhs)    # It's an AND combination
                else:
                    return OrNode(lhs, rhs)     # It's an OR combination
            elif len(clause) == 1:
                return VariableNode(symbol)
        elif clause[0] is Symbols.LHS_BRACKET:  # First item's a opening bracket:
            # Find the end of this sub-clause
            brack_count = 0
            i = 0
            for j in clause:
                if j is Symbols.LHS_BRACKET:    # Found a new bracket opening
                    brack_count = brack_count + 1
                elif j is Symbols.RHS_BRACKET:  # Found a matching end bracket
                    brack_count = brack_count - 1
                    if brack_count is 0:    # Got to the end of the brackets
                        lhs = self._generate_clause(clause[1:i])    # LHS in this clause
                        rhs = self._generate_clause(clause[i+2:])   # RHS after operator
                        if clause[i+1] is Symbols.AND:
                            return AndNode(lhs, rhs)
                        else:
                            return OrNode(lhs, rhs)
                i = i + 1
        elif clause[0] is Symbols.INVERSE:  # Found an inversion
            i = 0
            while i < len(clause):
                if clause[i] in [Symbols.AND, Symbols.Or]:
                    lhs = InversionNode(self._generate_clause(clause[1:i+1]))   # Inverted part
                    rhs = self._generate_clause(clause[i+1:])   # Bit after inversion
                    if clause[i+1] is Symbols.AND:
                        return AndNode(lhs, rhs)
                    else:
                        return OrNode(lhs, rhs)
                i = i + 1
            # Haven't found an operator so we will assume its a single clause
            return InversionNode(self._generate_clause(clause[1:]))
                



    def evaluate(self, input_vector):
        """ Evaluates the CNF equation through AND'ing the clauses. """
        if False in self.get_clause_evaluation():
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

class Clause(object):
    """ A clause in the CNF boolean expression. """
    _first_node = None

    def __init__(self, node):
        """ Initialises a clause with an initial node. """
        self._set_first_node(node)

    def _set_first_node(self, node):
        """ Sets the first node value of this object. """
        if type(node) is BooleanNode:
            self._first_node = node
        else:
            raise AttributeError("The child of an OperatorNode must be a descendent of a BooleanNode.")

class StaticValueNode(BooleanNode):
    """ A class which allows a true or false statement to appear in the tree. """
    _value = None

    def __init__(self, value):
        """ Initialises the value for this node. """
        self._set_value(value)
    
    def evaluate(self, input_vector):
        """ This evaluates to the value given in _value. """
        return _value
    
    def _set_value(self, new_val):
        """ Sets the value of the node. """
        if new_val in [True, False]:
            self._value = new_val
        else:
            raise AttributeError("The value of a StaticValueNode myst be set to True or False.")
    
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
        if type(child) is BooleanNode:
            self._lhs_child = child
        else:
            raise AttributeError("The child of an OperatorNode must be a descendent of a BooleanNode.")
    
    def _set_rhs_child(self, child):
        """ Sets the reference of the right hand side child. """
        if type(child) is BooleanNode:
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
