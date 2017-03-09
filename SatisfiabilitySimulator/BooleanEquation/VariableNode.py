from SatisfiabilitySimulator.BooleanEquation.BooleanNode import BooleanNode

class VariableNode(BooleanNode):
    """ A node which evaluates as a variable. """

    def __init__(self, var_char):
        """ Instantiates a variable node which uses the variable character provided. """
        self._variable = None
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

print("YAY")