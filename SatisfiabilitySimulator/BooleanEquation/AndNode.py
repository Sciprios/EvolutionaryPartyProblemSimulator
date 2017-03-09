from SatisfiabilitySimulator.BooleanEquation.CombinationNode import CombinationNode

class AndNode(CombinationNode):
    """ This class allows two child nodes to be AND'ed together. """

    def evaluate(self, input_vector):
        """ And's two child nodes to produce an output. """
        return (self._lhs_child.evaluate(input_vector) and self._rhs_child.evaluate(input_vector))