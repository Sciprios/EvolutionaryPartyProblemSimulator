from BooleanNode import BooleanNode

class InversionNode(BooleanNode):
    """ A node which inverts its child. """

    def __init__(self, child):
        """ Instantiates a variable node which uses the variable character provided. """
        self._child = None
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