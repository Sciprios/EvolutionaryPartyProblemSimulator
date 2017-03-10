from Graphing.Vertex import Vertex
from Graphing.Edge import Edge

class Graph(object):
    """ This represents a graph consisting of edges and vertices. """

    def __init__(self):
        """ Initialises a graph with vertices and edges. """
        self._vertices = []
        self._edges = []
    
    def _add_vertex(self, vertex):
        """ Adds the vertex in a secure way. """
        if isinstance(vertex, Vertex):
            self._vertices.append(vertex)
        else:
            raise TypeError("A vertex must be of type Vertex to be added to a graph.")
    
    def _add_edge(self, edge):
        """ Adds an edge iff this graph contians its vertices. """
        if isinstance(edge, Edge):
            if (edge.get_origin() in self._vertices) and (edge.get_target() in self._vertices):
                self._edges.append(edge)
            else:
                raise ValueError("An Edge can only be added to a graph if its vertices are already there.")
        else:
            raise TypeError("An edge must be of type Edge to be added to a graph.")
    
    def get_vertices(self):
        """ Retrieves the vertices. """
        return self._vertices
    
    def get_edges(self):
        """ Retrieves the edges. """
        return self._edges