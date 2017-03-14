from abc import ABC, abstractmethod

class BooleanNode(ABC):
    """ An abstract node which contains everything required to create a tree. """

    @abstractmethod
    def evaluate(self, input_vector):   #pragma: no cover
        """ To be implemented to evaluate according to node type. """
        raise NotImplementedError