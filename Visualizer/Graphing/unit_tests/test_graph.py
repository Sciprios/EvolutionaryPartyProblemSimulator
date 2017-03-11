from unittest.mock import Mock, call, patch
from unittest import TestCase
from Visualizer.Graphing.Edge import Edge
from Visualizer.Graphing.Vertex import Vertex
from Visualizer.Graphing.Graph import Graph

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
        g.add_vertex(a_vertex) # Try adding a vertex
        assert g._vertices[0] is a_vertex
        not_vertex = Edge(0, a_vertex, a_vertex)
        try:
            g.add_vertex(not_vertex)   # Expect an error if its not a Vertex
            assert False
        except TypeError:
            assert True
    
    def test_add_edge(self):
        """ Ensures safety of adding edges to the graph. """
        vertex_one = Vertex(0)
        vertex_two = Vertex(1)
        g = Graph()

        g._vertices = [vertex_one, vertex_two]  # Try with everything correct
        e = Edge(0, vertex_one, vertex_two)
        g.add_edge(e)
        assert g._edges[0] == e

        g._edges.clear()    # Try the case where the vertices are not present
        g._vertices.clear()
        try:
            g.add_edge(e)
            assert False
        except ValueError:
            assert True
        
        try:    # Try case of not passing an edge through.
            g.add_edge(vertex_one)
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
        edge = Edge(0, vertex_one, vertex_two)
        g = Graph()
        g._edges = [edge]
        assert g.get_edges() == [edge]

    def test_get_edge(self):
        """ Ensure the correct edge is returned with given id. """
        vertex_one = Vertex(0)
        vertex_two = Vertex(1)
        edge_one = Edge(0, vertex_one, vertex_two)
        edge_two = Edge(500, vertex_one, vertex_two)
        g = Graph()
        g._edges = [edge_one, edge_two]
        assert g.get_edge(500) is edge_two
    
    def test_get_vertex(self):
        """ Ensure the correct edge is returned with given id. """
        vertex_one = Vertex(0)
        vertex_two = Vertex(1)
        g = Graph()
        g._vertices = [vertex_one, vertex_two]
        assert g.get_vertex(1) is vertex_two

    def test_get_vertex_edges(self):
        """ Ensures the graph can return only edges connected to a distinct vertex. """
        vertex_one = Vertex(0)
        vertex_other = Vertex(1)
        edge_one = Edge(0, vertex_one, vertex_other)
        edge_two = Edge(0, vertex_other, vertex_other)
        edge_three = Edge(0, vertex_other, vertex_one)
        g = Graph() # Generate graph with relevant edges
        g.add_vertex(vertex_one)
        g.add_vertex(vertex_other)
        g.add_edge(edge_one)
        g.add_edge(edge_two)
        g.add_edge(edge_three)
        edges = g.get_vertex_edges(vertex_one)  # Try to get edges connecting to vertex_one
        assert (edge_one and edge_three) in edges
        assert edge_two not in edges
    
    @patch('Visualizer.Graphing.Graph.Graph.remove_edge')
    def test_remove_vertex(self, rm_edge):
        """ Ensures a vertex and its corresponding edges are removed. """
        vertex_one = Vertex(0)  # Create some components
        vertex_two = Vertex(1)
        edge_one = Edge(0, vertex_one, vertex_two)
        g = Graph() # Generate graph and add components
        g.add_vertex(vertex_one)
        g.add_vertex(vertex_two)
        g.add_edge(edge_one)
        g.remove_vertex(vertex_one) # Remove the vertex
        assert vertex_one not in g.get_vertices()
        assert vertex_two in g.get_vertices()
        assert rm_edge.called_with(edge_one)    # Ensure remove edge was called

    def test_remove_edge(self):
        """ Ensures edges can be removed correctly. """
        vertex_one = Vertex(0)  # Create some components
        vertex_two = Vertex(1)
        edge_one = Edge(0, vertex_one, vertex_two)
        edge_two = Edge(0, vertex_one, vertex_two)
        g = Graph()
        g.add_vertex(vertex_one)
        g.add_vertex(vertex_two)
        g.add_edge(edge_one)
        g.add_edge(edge_two)
        g.remove_edge(edge_one)
        assert edge_one not in g.get_edges()