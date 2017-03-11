from Visualizer.Graphing.Vertex import Vertex
from Visualizer.Graphing.Edge import Edge

class Graph(object):
    """ This represents a graph consisting of edges and vertices. """

    def __init__(self):
        """ Initialises a graph with vertices and edges. """
        self._vertices = []
        self._edges = []
    
    def add_vertex(self, vertex):
        """ Adds the vertex in a secure way. """
        if isinstance(vertex, Vertex):
            self._vertices.append(vertex)
        else:
            raise TypeError("A vertex must be of type Vertex to be added to a graph.")
    
    def add_edge(self, edge):
        """ Adds an edge iff this graph contians its vertices. """
        if isinstance(edge, Edge):
            if (edge.get_origin() in self._vertices) and (edge.get_target() in self._vertices):
                self._edges.append(edge)
            else:
                raise ValueError("An Edge can only be added to a graph if its vertices are already there.")
        else:
            raise TypeError("An edge must be of type Edge to be added to a graph.")
    
    def remove_vertex(self, vertex):
        """ Removes the vertex from this graph, cascading all its edges. """
        if vertex in self.get_vertices():
            for e in self.get_edges():
                if (e.get_origin() is vertex) or (e.get_target() is vertex):
                    self.remove_edge(e)
            self._vertices.remove(vertex)
    
    def remove_edge(self, edge):
        """ Removes the given edge. """
        if edge in self.get_edges():
            self._edges.remove(edge)

    def get_vertices(self):
        """ Retrieves the vertices. """
        return self._vertices
    
    def get_edges(self):
        """ Retrieves the edges. """
        return self._edges
    
    def get_edge(self, id):
        """ Retrieves an edge based on the id provided. """
        edge = None
        for e in self.get_edges():
            if e.get_id() == id:
                edge = e
                break
        return edge
    
    def get_vertex_edges(self, vertex):
        """ Retrieves all edges connected to the given edge. """
        edges = []
        for e in self.get_edges():
            if (e.get_origin() is vertex) or (e.get_target() is vertex):
                edges.append(e)
        return edges