from Vertex import Vertex

class Edge(object):
    """ An edge connecting two vertices in a graph. """
    
    def __init__(self, identifier, initial_vertex, end_vertex):
        """ Sets the vertices this edge connects. """
        self._set_initial_vertex(initial_vertex)
        self._set_end_vertex(end_vertex)

    def get_initial_vertex(self):
        """ returns the initial vertex. """
        return self._initial_vertex
    
    def get_end_vertex(self):
        """ returns the end vertex. """
        return self._end_vertex
    
    def get_id(self):
        """ Retrieves the identifier of this edge. """
        return self._id
    
    def _set_initial_vertex(self, vertex):
        """ Sets the initial vertex. """
        if isinstance(vertex, Vertex):
            self._initial_vertex = vertex
    
    def _set_end_vertex(self, vertex):
        """ Sets the end vertex. """
        if isinstance(vertex, Vertex):
            self._end_vertex = vertex

    def _set_identifier(self, id):
        """ Sets the id of this edge. """
        if isinstance(id, int):
            self._id = id