from Visualizer.Observation.Observer import Observer
from Visualizer.Observation.Subject import Subject
from pygubu import Builder
from math import sin, cos

class Visualizer(Subject, Observer):
    """ A visualizer gui which waits for updates and provides updates on user actions. """

    def __init__(self, master):
        """ Initialises this gui with an interface. """
        Subject.__init__(self)  # Call parent constructors
        Observer.__init__(self)
        self._builder = Builder()   # Setup form from build file
        self._builder.add_from_file("Visualizer/gui.ui")
        self.mainwindow = self._builder.get_object("frm_main")
        self._builder.get_object("cnv_display").config(width=500, height=500)
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
        method = self._builder.get_object("cb_method").get()

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
            if (clique_size <= 1) and (clique_size > graph_size):
                raise Exception()
        except Exception:
            valid = False
            self._builder.get_object("lbl_error").config(text="Clique size must be an integer > 1.")
        
        if method not in ["BlindGA", "EvoSAP", "FlipGA"]:
            self._builder.get_object("lbl_error").config(text="Please select a method from the list provided.")
        
        if valid:   # Reset error label if entry is valid.
            self._builder.get_object("lbl_error").config(text="")

        return valid

    def _draw_graph(self, graph):
        """ Draws the graph provided. """
        cnv_display = self._builder.get_object("cnv_display")
        cnv_display.delete("all")   # Clear canvas

        vertex_size = 10
        edge_thickness = 1
        # Draw vertices
        vertex_offset = vertex_size / 2
        center_canvas = (cnv_display.winfo_width() / 2, cnv_display.winfo_height() / 2)
        distance = center_canvas[0] / 1.5 #Quater of the screen
        degrees = 360 / len(graph.get_vertices())
        for vertex in graph.get_vertices():
            # Calculate a new location for the vertex on canvas
            center_x = center_canvas[0] + ((distance) * sin(degrees * vertex.get_id()))
            center_y = center_canvas[1] + ((distance) * cos(degrees * vertex.get_id()))
            vertex.set_location(x=center_x, y=center_y)
            cnv_display.create_oval(center_x - vertex_offset, center_y - vertex_offset, center_x + vertex_offset, center_y + vertex_offset, fill='cyan')

        # Draw edges
        for edge in graph.get_edges():
            start_x = edge.get_origin().get_location()[0]   # Get locations
            start_y = edge.get_origin().get_location()[1]
            end_x = edge.get_target().get_location()[0]
            end_y = edge.get_target().get_location()[1]
            colour = self._determine_colour(edge.get_colour())  # Determine colour
            cnv_display.create_line(start_x, start_y, end_x, end_y, width=edge_thickness, fill=colour)

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
        method = self._builder.get_object("cb_method").get()

        update_argument = {"clique_size": clique_size, "graph_size": graph_size, "method": method}    # Argument to update observers with

        for o in self._observers:
            o.update(update_argument)
        
        self._builder.get_object("btn_solve").config(state="disabled")

    def update(self, args):
        """ Update details on form to show progress if required. """
        if ('graph' and 'generation' and 'evals' and 'best_fitness' and 'ideal_fitness' and 'finished') in args:
            new_graph = args['graph']
            self._builder.get_object("lbl_generations").config(text="Generation: {}".format(args['generation']))
            self._builder.get_object("lbl_eval_count").config(text="Eval Count: {}".format(args['evals']))
            self._builder.get_object("lbl_best_fitness").config(text="Best Fitness: {}/{}".format(args['best_fitness'], args['ideal_fitness']))
            if args["finished"]:
                self._builder.get_object("lbl_error").config(text="Finished!")
                self._builder.get_object("btn_solve").config(state="normal")
            self._draw_graph(new_graph)