from Graphing.Vertex import Vertex

class Edge(object):
    """ An edge joining two vertices. """

    def __init__(self, origin, target):
        """ Initializes this edge with an origin and a target. """
        self._set_origin(origin)
        self._set_target(target)
    
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
    
    def get_origin(self):
        """ Retrieves the origin vertex of this edge. """
        return self._origin
    
    def get_target(self):
        """ Retrieves the target vertex of this edge. """
        return self._target