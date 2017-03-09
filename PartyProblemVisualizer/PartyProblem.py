from Graphing.Observer.GraphSubject import GraphSubject
from Graphing.Graph import Graph
from SatisfiabilitySimulator.solvers.GeneticAlgorithm
from threading import Thread

class PartyProblem(GraphSubject):
    """ Represents a party problem to be solved. """

    def __init__(self, graph_size, clique_size):
        """ Initializes instance variables and graph. """
        super().__init__()
        self._set_graph(Graph(graph_size))
    
    def run(self, method):
        """ Runs a simulation of this problem with the given method. """
        if isinstance(method, GeneticAlgorithm):

        else:
            raise TypeError("The method parameter of the run function must be a GeneticAlgorithm. ")
    
    def _update(self, method):
        """ Updates observers with progress of method. """
        while not method.finished:
            # Update Graph
            # Update observers with Graph
            self._notify_observers()

    def _set_graph(self, graph):
        """ Sets the graph instance. """
        if isinstance(graph, Graph):
            graph.connect_edges()   # Party problems use connected graphs
            self._graph = graph
    
    def _set_clique_size(self, size):
        """ Sets the clique size to be used. """
        if isinstance(size, int):
            if size > 0:
                self._clique_size = size
            else:
                self._clique_size = 0
        else:
            self._clique_size = 0