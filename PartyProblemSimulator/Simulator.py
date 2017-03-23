from PartyProblemSimulator.BooleanEquation.Equation import Equation
from PartyProblemSimulator.Observation.Observer import Observer
from PartyProblemSimulator.Observation.Subject import Subject
from PartyProblemSimulator.Graphing.ConnectedGraph import ConnectedGraph
from PartyProblemSimulator.Graphing.Vertex import Vertex
from PartyProblemSimulator.Graphing.Edge import Edge
from PartyProblemSimulator.Visualizer.Visualizer import Visualizer
from itertools import combinations
from threading import Thread
from tkinter import Tk
from time import sleep

from PartyProblemSimulator.Solvers.EvoSAP import EvoSAP
from PartyProblemSimulator.Solvers.FlipGA import FlipGA


class Simulator(Subject, Observer):
    """ A simulator to process party problems. """

    def __init__(self):
        """ Initializes a user interface and sets up callbacks. """
        Subject.__init__(self)
        Observer.__init__(self)
        self._graph = None
        self._method = None
        self._algo_thread = None
        self._poll_thread = None
        self._gui = None
    
    def start(self):
        """ Begins gui. """
        root = Tk()
        self._gui = Visualizer(root)
        self._gui.subscribe(self) # Register to gui
        self.subscribe(self._gui) # Register gui to this
        root.mainloop()

    def _solve(self, clique_size, graph_size, method):
        """ Solves the given clique problem. """
        # Generate a Graph
        self._graph = ConnectedGraph(graph_size)
        # Generate an equation to solve and its variables
        result = self._generate_equation(clique_size)
        self._equation = result[0]
        var_set = result[1]
        self._goal_fitness = len(self._equation._clauses)
        # Generate a method to solve equation
        self._method = self._determine_method(method)()
        # Run algorithm on a seperate thread
        self._algo_thread = Thread(target=self._method.run, args=(self._equation, len(var_set),))
        # Run poller on seperate thread
        self._poll_thread = Thread(target=self._poll)
        self._algo_thread.start()
        self._poll_thread.start()
    
    def _determine_method(self, method):
        """ Returns the Genetic Algorithm class to be instantiated. """
        if method == "EvoSAP":
            print("EvoSAP - Original")
            return EvoSAP
        elif method == "FlipGA":
            print("FlipGA - Original")
            return FlipGA

    def _poll(self):
        """ Polls the algorithm, updating observers when required. """
        cur_fit = -1
        org = None
        while not self._method.is_finished():
            org = self._method.get_best_genome()
            if org is not None:
                self._method.get_best_genome().evaluate(self._equation)
                # Update graph
                self._generate_graph(org)
                # Update observers
                self._notify_observers(org)
                sleep(0.5)
        # Update when finished
        org = self._method.get_best_genome()
        self._generate_graph(org)
        self._notify_observers(org)

    def _generate_graph(self, org):
        """ Generates a graph based on current state of method's best orgnism. """
        genome = org.get_genes()
        count = 0
        for gene in genome: # For each gene (edge)
            if gene.get_information():
                self._graph.get_edge(count).set_colour(1)
            else:
                self._graph.get_edge(count).set_colour(0)
            count = count + 1

    def _generate_equation(self, clique_size):
        """ Generates a boolean equation and variable set based on the parameters. """
        # Generate string equivalent
        bln_eq_str = ""
        var_set = []
        vertex_combinations = combinations(self._graph.get_vertices(), clique_size)    # Get all combinations of vertices
        for combination in vertex_combinations:
            # Generate clause and inverse clause
            clause_one = ""
            clause_two = ""
            for edge in self._graph.get_edges():  # Get all edges in this combination
                if (edge.get_origin() in combination) and (edge.get_target() in combination):
                    edge_id = str(edge.get_id())    # Found an edge in this combination
                    var_id = "{" + edge_id + "}"
                    clause_one = clause_one + "+¬" + var_id + ""
                    clause_two = clause_two + "+" + var_id + ""
                    
            # Format clause
            clause_one = "(" + clause_one[1:] + ")" # The substring removes the first redundant "AND" symbol
            clause_two = "(" + clause_two[1:] + ")"
            # Add clause to equation
            bln_eq_str = bln_eq_str + "." + clause_one + "." + clause_two
        # Generate variables list
        for edge in self._graph.get_edges():
            var_id = "{" + str(edge.get_id()) + "}"
            var_set.append(var_id)
        # Format Equation
        bln_eq_str = bln_eq_str[1:] # Removes redundant AND symbol
        # Generate equation object
        return (Equation(bln_eq_str), var_set)

    def _notify_observers(self, org):
        """ Notifies observers of genetic parameters and graph. """
        best_genome = self._method.get_best_genome()
        if best_genome is not None:
            args = {
                "generation": self._method.get_generation(),
                "evals": self._method.get_num_evaluations(),
                "best_fitness": best_genome.evaluate(self._equation),
                "graph": self._graph,
                "finished": self._method.is_finished()
            }
            for o in self._observers:
                o.update(args)

    def update(self, args):
        """ Get clique and graph size and begin simulation. """
        clique_size = args['clique_size']
        graph_size = args['graph_size']
        method = args['method']
        self._solve(clique_size, graph_size, method)
