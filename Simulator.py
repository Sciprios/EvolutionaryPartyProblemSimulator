from SatisfiabilitySimulator.BooleanEquation.Equation import Equation
from SatisfiabilitySimulator.Solvers.BlindGA import BlindGA
from SatisfiabilitySimulator.Solvers.FlipGA import FlipGA
from Visualizer.Observation.Observer import Observer
from Visualizer.Observation.Subject import Subject
from Visualizer.Graphing.ConnectedGraph import ConnectedGraph
from Visualizer.Graphing.Vertex import Vertex
from Visualizer.Graphing.Edge import Edge
from Visualizer.Visualizer import Visualizer
from itertools import combinations
from threading import Thread
from tkinter import Tk
from time import sleep


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

    def _solve(self, clique_size, graph_size):
        """ Solves the given clique problem. """
        # Generate a Graph
        self._graph = ConnectedGraph(graph_size)
        # Generate an equation to solve and its variables
        result = self._generate_equation(clique_size)
        equation = result[0]
        var_set = result[1]
        self._goal_fitness = len(equation._clauses)
        # Generate a method to solve equation
        self._method = FlipGA(equation, var_set)
        # Run algorithm on a seperate thread
        self._algo_thread = Thread(target=self._method.run)
        # Run poller on seperate thread
        self._poll_thread = Thread(target=self._poll)
        self._algo_thread.start()
        self._poll_thread.start()

    def _poll(self):
        """ Polls the algorithm, updating observers when required. """
        while not self._method.finished:
            if self._method.get_best_org() is not None:
                # Update graph
                self._generate_graph()
                # Update observers
                self._notify_observers()
            sleep(1)
        # Update when finished
        if self._method.get_best_org() is not None:
            self._notify_observers()

    def _generate_graph(self):
        """ Generates a graph based on current state of method's best orgnism. """
        truth_assignments = self._method.get_best_org()['org']
        for variable in truth_assignments: # For each variable (edge)
            edge_id = int(variable[1:-1])
            if truth_assignments[variable]:
                self._graph.get_edge(edge_id).set_colour(0)
            else:
                self._graph.get_edge(edge_id).set_colour(1)

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
                    clause_one = clause_one + "." + var_id + ""
                    clause_two = clause_two + ".¬" + var_id + ""
                    var_set.append(var_id)
            # Format clause
            clause_one = "(" + clause_one[1:] + ")" # The substring removes the first redundant "AND" symbol
            clause_two = "(" + clause_two[1:] + ")"
            # Add clause to equation
            bln_eq_str = bln_eq_str + "." + clause_one + "." + clause_two
        # Format Equation
        bln_eq_str = bln_eq_str[1:] # Removes redundant AND symbol
        # Generate equation object
        return (Equation(bln_eq_str), var_set)

    def _notify_observers(self):
        """ Notifies observers of genetic parameters and graph. """
        if self._method.get_best_org() is not None:
            args = {
                "generation": self._method.generation,
                "evals": self._method.eval_count,
                "best_fitness": self._method.get_best_org()['fitness'],
                "ideal_fitness": self._goal_fitness,
                "graph": self._graph,
                "finished": self._method.finished
            }
            for o in self._observers:
                o.update(args)
    
    def update(self, args):
        """ Get clique and graph size and begin simulation. """
        clique_size = args['clique_size']
        graph_size = args['graph_size']
        self._solve(clique_size, graph_size)

if __name__ == '__main__':
    simulator = Simulator()
    simulator.start()