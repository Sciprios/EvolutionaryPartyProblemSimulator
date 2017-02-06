""" This module contains the classes required to make a boolean equation. """
from abc import ABC, abstractmethod

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

class BooleanNode(ABC):
    """ An abstract node which contains everything required to create a tree. """

    @abstractmethod
    def evaluate(self, input_vector):
        """ To be implemented to evaluate according to node type. """
        raise NotImplementedError

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
