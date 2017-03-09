from Vertex import Vertex
from Edge import Edge

class Graph(object):
    """ A graph which can be utilised in a Party problem. """

    def __init__(self, no_vertices, connected):
        """ Generates a graph with the given number of vertices and edges determined by whether it is connected or not. """
        self._vertices = []
        self._edges = []
    
    def _generate_vertices(self, no_vertices):
        """ Generates the given number of vertices without locations. """
        count = 0
        while count < no_vertices:
            vertex = Vertex(count)
            self.add_vertex(vertex)

    def connect_edges(self):
        """ Generates edges between all vertices. """
        start_index = 0
        while start_index < len(self._vertices):
            current_index = start_index + 1
            while current_index < len(self._vertices):
                edge = Edge(self._vertices[start_index], self._vertices[current_index]) # Create an edge
                self.add_edge(edge)

    def add_edge(self, edge):
        """ Adds an edge to this graph. """
        if isinstance(edge, Edge):
            if (edge.get_initial_vertex() in self._vertices) and (edge.get_end_vertex() in self._vertices): # Check both vertices are present in this graph.
                self._edges.append(edge)

    def add_vertex(self, vertex):
        """ Adds a vertex to this graph. """
        if isinstance(vertex, Vertex):
            if vertex not in self._vertices:
                self._vertices.append(vertex)
    
    def remove_edge(self, edge):
        """ Removes an edge from this graph. """
        if isinstance(edge, Edge):
            if edge in self._edges:
                self._edges.remove(edge)
    
    def remove_vertex(self, vertex):
        """ Removes a vertex and any relevant edges from this graph. """
        if isinstance(vertex, Vertex):
            if vertex in self._vertices:    # Ensure vertex exists.
                self._vertices.remove(vertex)
                for e in self._edges:   # Remove all edges with this vertex as part of it.
                    if (e.initial_vertex == vertex) or (e.end_vertex == vertex):
                        self._edges.remove(e)
    
    def get_vertex(self, id):
        """ Retrieves a vertex with the given id. """
        vertex = None
        if isinstance(id, int):
            for v in self._vertices:
                if v.get_id() == id:
                    vertex = v
                    break
        return vertex

    def get_edge(self, id):
        """ Retrieves an edge with the given id. """
        edge = None
        if isinstance(id, int):
            for e in self._edges:
                if e.get_id() == id:
                    edge = e
                    break
        return edge
    
    def get_edges(self):
        """ Retrieves all edges. """
        return self._edges
    
    def get_vertices(self):
        """ Retrieves all vertices. """
        return self._vertices