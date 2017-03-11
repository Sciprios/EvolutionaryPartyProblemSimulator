from Visualizer.Graphing.Graph import Graph
from Visualizer.Graphing.Vertex import Vertex
from Visualizer.Graphing.Edge import Edge
from itertools import combinations

class ConnectedGraph(Graph):
    """ Represents a fully connected graph. """

    def __init__(self, n_vertices):
        """ Generates a connected graph with n_vertices. """
        super().__init__()
        self._generate_vertices(n_vertices)
        self._generate_edges()

    def _generate_vertices(self, n_vertices):
        """ Generates n vertices. """
        count = 0
        while count < n_vertices:
            new_vertex = Vertex(count)
            self.add_vertex(new_vertex)
            count = count + 1
    
    def _generate_edges(self):
        """ Generates edges between all vertices. """
        combs = combinations(self.get_vertices(), 2)    # Create all possible combinations
        for combination in combs:
            new_edge = Edge(0, combination[0], combination[1])
            self.add_edge(new_edge)