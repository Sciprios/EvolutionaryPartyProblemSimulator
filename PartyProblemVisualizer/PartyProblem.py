from Graphing.Observer.GraphSubject import GraphSubject
from Graphing.Graph import Graph
from SatisfiabilitySimulator.solvers.GeneticAlgorithm
from SatisfiabilitySimulator.equation.BoolTree.Equation
from threading import Thread
from itertools import combinations

class PartyProblem(GraphSubject):
    """ Represents a party problem to be solved. """

    def __init__(self, graph_size, clique_size):
        """ Initializes instance variables and graph. """
        super().__init__()
        self._set_graph(Graph(graph_size))
    
    def run(self, method):
        """ Runs a simulation of this problem with the given method. """
        if isinstance(method, GeneticAlgorithm):
            eq = Equation()

        else:
            raise TypeError("The method parameter of the run function must be a GeneticAlgorithm. ")
    
    def _generate_equation(self):
        """ Generates an equation based on the clique size of this problem. """
        vertex_combinations = combinations(self._graph.get_vertices(), self._clique_size)
        equation = ""
        for comb in vertex_combinations:
            edges = self._graph.get_edges_between(comb)
            clause_all = ""
            clause_none = ""
            for e in edges:
                clause = clause + ".{" + str(e.get_id) + "}"
            clause = clause [1:] # Remove spare AND idenfitier.
            clause_none = clause.replace("{", "¬{") # Creates clause with the inverted clique
            equation = equation + "+(" + clause_all + ")+(" + clause_none + ")"
        equation = equation[1:] # Removes spare OR operator.
        return equation


    def _update(self, method):
        """ Updates observers with progress of method. """  # NOT FINISHED
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