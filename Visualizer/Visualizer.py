from Visualizer.Observation.Observer import Observer
from Visualizer.Observation.Subject import Subject
from pygubu import Builder

class Visualizer(Subject, Observer):
    """ A visualizer gui which waits for updates and provides updates on user actions. """

    def __init__(self, master):
        """ Initialises this gui with an interface. """
        Subject.__init__(self)  # Call parent constructors
        Observer.__init__(self)
        self._builder = Builder()   # Setup form from build file
        self._builder.add_from_file("Visualizer/gui.ui")
        self.mainwindow = self._builder.get_object("frm_main")
        self._setup_eventhandlers()

    def _setup_eventhandlers(self): # pragma : no cover
        """ Sets the event handlers for form controls. """
        btn_solve = self._builder.get_object("btn_solve")
        btn_solve.config(command=self._btn_solve_press)

    def _btn_solve_press(self):
        """ Notify observers that a problem is ready to be solved. """
        if self._validate_input(): # Extract form information if valid
            self._notify_observers()

    def _validate_input(self):
        """ Extracts and validates the input. """
        valid = True
        clique_size = self._builder.get_object("tb_clique_size").get()
        graph_size = self._builder.get_object("tb_graph_size").get()

        # Validation
        try:
            graph_size = int(graph_size)
            if graph_size < 1:
                raise Exception()
        except Exception:
            valid = False
            self._builder.get_object("lbl_error").config(text="Graph size must be an integer > 1.")
        
        try:
            clique_size = int(clique_size)
            if clique_size < 1:
                raise Exception()
        except Exception:
            valid = False
            self._builder.get_object("lbl_error").config(text="Clique size must be an integer > 1.")
        
        if valid:   # Reset error label if entry is valid.
            self._builder.get_object("lbl_error").config(text="")

        return valid

    def _draw_graph(self, graph):
        """ Draws the graph provided. """
        cnv_display = self._builder.get_object("cnv_display")
        cnv_display.delete("all")   # Clear canvas

        vertex_size = 10
        edge_thickness = 2

        # Draw edges
        for edge in graph.get_edges():
            start_x = edge.get_origin().get_location()[0]   # Get locations
            start_y = edge.get_origin().get_location()[1]
            end_x = edge.get_target().get_location()[0]
            end_y = edge.get_target().get_location()[1]
            colour = self._determine_colour(edge.get_colour())  # Determine colour
            cnv_display.create_line(start_x, start_y, end_x, end_y, width=edge_thickness, fill=colour)

        # Draw vertices
        vertex_offset = vertex_size / 2
        for vertex in graph.get_vertices():
            center_x = vertex.get_location()[0]
            center_y = vertex.get_location()[1]
            cnv_display.create_oval(center_x - vertex_offset, center_y - vertex_offset, center_x + vertex_offset, center_y + vertex_offset, fill='cyan')

    def _determine_colour(self, colour_code):
        """ Determines the colour code of an edge. """
        if colour_code == 0:
            return 'red'
        elif colour_code == 1:
            return 'green'
        elif colour_code == 2:
            return 'cyan'
        else:
            return 'blue'

    def _notify_observers(self):
        """ Notifies observers. """
        clique_size = int(self._builder.get_object("tb_clique_size").get())
        graph_size = int(self._builder.get_object("tb_graph_size").get())

        update_argument = {"clique_size": clique_size, "graph_size": graph_size}    # Argument to update observers with

        for o in self._observers:
            o.update(update_argument)

    def update(self, args):
        """ Update details on form to show progress if required. """
        if ('graph' and 'generation' and 'evals' and 'best_fitness') in args:
            new_graph = args['graph']
            self._builder.get_object("lbl_generations").config(text="Generation: {}".format(args['generation']))
            self._builder.get_object("lbl_eval_count").config(text="Eval Count: {}".format(args['evals']))
            self._builder.get_object("lbl_best_fitness").config(text="Best Fitness: {}".format(args['best_fitness']))
            self._draw_graph(new_graph)
        
        # TEST IF IN DOUBT
        #from Visualizer.Graphing.Graph import Graph
        #from Visualizer.Graphing.Vertex import Vertex
        #from Visualizer.Graphing.Edge import Edge
        #new_graph = Graph()
        #vertex_one = Vertex(0, location_x=50, location_y=100)
        #vertex_two = Vertex(1, location_x=200, location_y=200)
        #edge_one = Edge(0, vertex_one, vertex_two)
        #new_graph.add_vertex(vertex_one)
        #new_graph.add_vertex(vertex_two)
        #new_graph.add_edge(edge_one)
        #self._draw_graph(new_graph)