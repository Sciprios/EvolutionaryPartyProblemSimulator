from PartyProblemSimulator.SatisfiabilitySimulator.BooleanEquation.CombinationNode import CombinationNode

class OrNode(CombinationNode):
    """ This class allows two child nodes to be OR'ed together. """

    def evaluate(self, input_vector):
        """ Or's two child nodes to produce an output. """
        return (self._lhs_child.evaluate(input_vector) or self._rhs_child.evaluate(input_vector))