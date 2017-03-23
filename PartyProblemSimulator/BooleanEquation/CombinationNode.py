from abc import ABC, abstractmethod
from PartyProblemSimulator.BooleanEquation.BooleanNode import BooleanNode

class CombinationNode(BooleanNode, ABC):
    """ An abstract node which carries out an operation on its children. """

    def __init__(self, lhs_child, rhs_child):
        """ Instantiates an Combination node with two children. """
        self._lhs_child = None
        self._rhs_child = None
        self._set_lhs_child(lhs_child)
        self._set_rhs_child(rhs_child)
    
    def _set_lhs_child(self, child):
        """ Sets the reference of the left hand side child. """
        if issubclass(type(child), BooleanNode) or issubclass(type(child), CombinationNode):
            self._lhs_child = child
        else:
            raise AttributeError("The child of an CombinationNode must be a descendent of a BooleanNode.")
    
    def _set_rhs_child(self, child):
        """ Sets the reference of the right hand side child. """
        if issubclass(type(child), BooleanNode) or issubclass(type(child), CombinationNode):
            self._rhs_child = child
        else:
            raise AttributeError("The child of an CombinationNode must be a descendent of a BooleanNode.")