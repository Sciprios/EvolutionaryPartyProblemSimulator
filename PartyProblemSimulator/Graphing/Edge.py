from PartyProblemSimulator.Graphing.Vertex import Vertex
from PartyProblemSimulator.Graphing.Component import Component

class Edge(Component):
    """ An edge joining two vertices. """

    def __init__(self, identifier, origin, target, colour=0):
        """ Initializes this edge with an origin and a target. """
        super().__init__(identifier)
        self._set_origin(origin)
        self._set_target(target)
        self.set_colour(colour)
    
    def _set_origin(self, origin):
        """ Safely sets the origin of this edge. """
        if isinstance(origin, Vertex):
            self._origin = origin
        else:
            raise TypeError("You can only set the origin of an edge to a Vertex.")
    
    def _set_target(self, target):
        """ Safely sets the origin of this edge. """
        if isinstance(target, Vertex):
            self._target = target
        else:
            raise TypeError("You can only set the target of an edge to a Vertex.")
    
    def set_colour(self, colour):
        """ Sets the colour value for an edge. """
        if isinstance(colour, int):
            self._colour = colour
        else:
            raise TypeError("The colour of an edge must be of type Integer.")

    def get_origin(self):
        """ Retrieves the origin vertex of this edge. """
        return self._origin
    
    def get_target(self):
        """ Retrieves the target vertex of this edge. """
        return self._target
    
    def get_colour(self):
        """ Retrieves the colour of this edge. """
        return self._colour