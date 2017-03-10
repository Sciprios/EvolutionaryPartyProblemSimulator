from unittest.mock import Mock, call, patch
from unittest import TestCase
from Graphing.Edge import Edge
from Graphing.Vertex import Vertex
from Graphing.Graph import Graph

class TestGraph(TestCase):
    """ Tests the graph class. """

    def test_init(self):
        """ Ensures the initialisation produces correct instance variables. """
        g = Graph()
        assert g._vertices == []
        assert g._edges == []
    
    def test_add_vertex(self):
        """ Ensures the safety of the adding of vertices. """
        g = Graph()
        a_vertex = Vertex(0)
        g._add_vertex(a_vertex) # Try adding a vertex
        assert g._vertices[0] is a_vertex
        not_vertex = Edge(a_vertex, a_vertex)
        try:
            g._add_vertex(not_vertex)   # Expect an error if its not a Vertex
            assert False
        except TypeError:
            assert True
    
    def test_add_edge(self):
        """ Ensures safety of adding edges to the graph. """
        vertex_one = Vertex(0)
        vertex_two = Vertex(1)
        g = Graph()

        g._vertices = [vertex_one, vertex_two]  # Try with everything correct
        e = Edge(vertex_one, vertex_two)
        g._add_edge(e)
        assert g._edges[0] == e

        g._edges.clear()    # Try the case where the vertices are not present
        g._vertices.clear()
        try:
            g._add_edge(e)
            assert False
        except ValueError:
            assert True
        
        try:    # Try case of not passing an edge through.
            g._add_edge(vertex_one)
            assert False
        except TypeError:
            assert True
        
    def test_get_vertices(self):
        """ Ensures vertices are returned correctly. """
        vertex_one = Vertex(0)
        vertex_two = Vertex(1)
        g = Graph()
        g._vertices = [vertex_one, vertex_two]
        assert g.get_vertices() == [vertex_one, vertex_two]
    
    def test_get_edges(self):
        """ Ensures edges are returned correctly. """
        vertex_one = Vertex(0)
        vertex_two = Vertex(1)
        edge = Edge(vertex_one, vertex_two)
        g = Graph()
        g._edges = [edge]
        assert g.get_edges() == [edge]