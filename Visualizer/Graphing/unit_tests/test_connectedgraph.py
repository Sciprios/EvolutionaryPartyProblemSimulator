from unittest.mock import Mock, call, patch
from unittest import TestCase
from PartyProblemSimulator.Visualizer.Graphing.Edge import Edge
from PartyProblemSimulator.Visualizer.Graphing.Vertex import Vertex
from PartyProblemSimulator.Visualizer.Graphing.Graph import Graph
from PartyProblemSimulator.Visualizer.Graphing.ConnectedGraph import ConnectedGraph

class TestConnectedGraph(TestCase):
    """ Tests the connected graph class. """

    @patch('PartyProblemSimulator.Visualizer.Graphing.ConnectedGraph.ConnectedGraph._generate_vertices')
    @patch('PartyProblemSimulator.Visualizer.Graphing.ConnectedGraph.ConnectedGraph._generate_edges')
    def test_init(self, gen_edg, gen_ver):
        """ Ensures the graph is instantiated through the right methods. """
        cg = ConnectedGraph(333)
        assert gen_edg.call_count == 1
        assert gen_ver.call_count == 1
        gen_ver.assert_called_with(333)
    
    @patch('PartyProblemSimulator.Visualizer.Graphing.ConnectedGraph.ConnectedGraph._generate_edges')
    def test_gen_vertices(self, gen_edg):
        """ Tests the generation of all vertices. """
        cg = ConnectedGraph(333)
        assert len(cg._vertices) == 333

    @patch('PartyProblemSimulator.Visualizer.Graphing.ConnectedGraph.Edge')
    @patch('PartyProblemSimulator.Visualizer.Graphing.ConnectedGraph.ConnectedGraph._generate_vertices')
    def test_gen_edges(self, gen_ver, edge):
        """ Test the generation of all possible edges. """
        cg = ConnectedGraph(3)
        v1 = Vertex(0)
        v2 = Vertex(1)
        v3 = Vertex(2)
        cg._vertices = [v1, v2, v3]
        edge.return_value = Edge(0, v1, v2)
        cg._generate_edges()
        assert len(cg._edges) == 3