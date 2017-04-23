from PartyProblemSimulator.Observation.Observer import Observer
from PartyProblemSimulator.Observation.Subject import Subject
from pygubu import Builder
from math import sin, cos
from tkinter import VERTICAL
from threading import Thread

class Visualizer(Subject, Observer):
    """ A visualizer gui which waits for updates and provides updates on user actions. """

    def __init__(self, master):
        """ Initialises this gui with an interface. """
        Subject.__init__(self)  # Call parent constructors
        Observer.__init__(self)
        self._update_thread = None  # Thread to update the graphs
        self._builder = Builder()   # Setup form from build file
        self._builder.add_from_file("PartyProblemSimulator/Visualizer/gui.ui")
        self.mainwindow = self._builder.get_object("frm_main")
        self._builder.get_object("cnv_display").config(width=250, height=250)
        self._builder.get_object("cnv_graph_fitness").config(width=500, height=250)
        self._builder.get_object("cnv_graph_evaluations").config(width=500, height=250)
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
            if (clique_size <= 1) or (clique_size > graph_size):
                raise Exception()
        except Exception:
            valid = False
            self._builder.get_object("lbl_error").config(text="Clique size must be an integer > 1.")
        
        if (method not in ["BlindGA", "EvoSAP", "EvoSAP1", "EvoSAP2", "FlipGA", "FlipGA1", "FlipGA2"]) and valid:
            self._builder.get_object("lbl_error").config(text="Please select a method from the list provided.")
            valid = False
        
        if valid:   # Reset error label if entry is valid.
            self._builder.get_object("lbl_error").config(text="")

        return valid
    
    def _update_gui(self, generation, eval_count, fitness, history, finished, graph):# pragma: no cover
        """ Updates the relevant gui components. """
        self._builder.get_object("lbl_generations").config(text="Generation: {}".format(generation))
        self._builder.get_object("lbl_eval_count").config(text="Eval Count: {}".format(eval_count))
        self._builder.get_object("lbl_best_fitness").config(text="Best Fitness: {0:.2f}/1".format(fitness))
        if finished:
            self._builder.get_object("lbl_error").config(text="Finished!")
            self._builder.get_object("btn_solve").config(state="normal")
        else:
            self._builder.get_object("lbl_error").config(text="Computing...")
        # Update plots on seperate threads for efficiency
        plots_thread = Thread(target=self._draw_plots, args=(history,))
        graph_thread = Thread(target=self._draw_graph, args=(graph,))
        plots_thread.start()
        graph_thread.start()
        plots_thread.join()
        graph_thread.join()

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
    
    def _draw_plots(self, history): # pragma: no cover
        """ Draws the plots. """
        cnv_graph_fitness = self._builder.get_object("cnv_graph_fitness")
        cnv_graph_evaluations = self._builder.get_object("cnv_graph_evaluations")
        cnv_graph_fitness.delete("all")
        cnv_graph_evaluations.delete("all")
        # Determine axis locations
        origin = (50, 220)
        end_x = (origin[0] + 430, origin[1])
        end_y = (origin[0], origin[1] - 210)
        # Draw graph axis
        cnv_graph_fitness.create_line(origin[0], origin[1], end_x[0], end_x[1], fill="black")
        cnv_graph_fitness.create_line(origin[0], origin[1], end_y[0], end_y[1], fill="black")
        cnv_graph_evaluations.create_line(origin[0], origin[1], end_x[0], end_x[1], fill="black")
        cnv_graph_evaluations.create_line(origin[0], origin[1], end_y[0], end_y[1], fill="black")
        # Label axis
        horizontal_label_location = ((origin[0] + end_x[0])/2, origin[1] + 20)
        cnv_graph_fitness.create_text(horizontal_label_location[0], horizontal_label_location[1], font="arial 10", text="Generation")
        cnv_graph_evaluations.create_text(horizontal_label_location[0], horizontal_label_location[1], font="arial 10", text="Generation")
        # Draw Horizontal labels
        label_x = 0
        label_y = origin[1] + 10
        if len(history['fitness']) >= 10:
            horizontal_increment = (end_x[0] - origin[0]) / 10  # Calculate increments to do horizontally
            count = 0
            while count < 11:
                label_x = origin[0] + (count * horizontal_increment)    # Determine axis details
                generation = len(history['fitness']) / 10
                cnv_graph_fitness.create_text(label_x, label_y, font="arial 8", text="{}".format(int(generation * count)))  # Label axis
                cnv_graph_evaluations.create_text(label_x, label_y, font="arial 8", text="{}".format(int(generation * count)))
                cnv_graph_fitness.create_line(label_x, label_y - 12, label_x, label_y - 8)  # Show a small line on the axis
                cnv_graph_evaluations.create_line(label_x, label_y - 12, label_x, label_y - 8)
                count = count + 1
        else:   # Special case if there are < 10 cases
            no_increments = len(history['fitness'])
            horizontal_increment = (end_x[0] - origin[0]) / (no_increments + 1)
            count = 1
            while count <= no_increments:
                label_x = origin[0] + (count * horizontal_increment)    # Determine axis details
                generation = len(history['fitness']) / 10
                cnv_graph_fitness.create_text(label_x, label_y, font="arial 8", text="{}".format(int(generation * count)))  # Label axis
                cnv_graph_evaluations.create_text(label_x, label_y, font="arial 8", text="{}".format(int(generation * count)))
                cnv_graph_fitness.create_line(label_x, label_y - 12, label_x, label_y - 8)  # Show a small line on the axis
                cnv_graph_evaluations.create_line(label_x, label_y - 12, label_x, label_y - 8)
                count = count + 1
            
        # Draw points and labels
        fitness_thread = Thread(target=self._draw_fitness_points, args=(cnv_graph_fitness, origin, end_y, end_x, history['fitness'],))
        evals_thread = Thread(target=self._draw_evaluation_points, args=(cnv_graph_evaluations, origin, end_y, end_x, history['evaluation'],))
        fitness_thread.start()
        evals_thread.start()
        fitness_thread.join()
        evals_thread.join()

        
    def _draw_fitness_points(self, cnv_graph_fitness, graph_origin, vertical_end, horizontal_end, fitness_history): # pragma: no cover
        """ Draws the fitness graph. """
        # Draw vertical axis values (Increments of 0.1 from 0)
        increment = (graph_origin[1] - vertical_end[1]) / 10
        count = 0
        while count < 1:
            text_location = (graph_origin[0], graph_origin[1] - ((count * 10) * increment))    # Add the label slightly to the left of axis
            cnv_graph_fitness.create_text(text_location[0] - 15, text_location[1], font="arial 8", text="{0:.1f}".format(count))   # Create label
            cnv_graph_fitness.create_line(text_location[0] - 2, text_location[1], text_location[0] + 2, text_location[1])
            count = count + 0.1
        # Draw points
        horizontal_increment = (horizontal_end[0] - graph_origin[0]) / len(fitness_history)    # Calculate an even spacing between fitness values
        count = 0
        previous_point = None
        if len(fitness_history) == 1:   # Special case of a single point
            location_y = graph_origin[1] - (fitness_history[0] * (graph_origin[1] - vertical_end[1]))
            location_x = graph_origin[0] + ((horizontal_end[0] - graph_origin[0]) / 2)
            cnv_graph_fitness.create_text(location_x, location_y, fill="blue", text="x")
        else:
            while count < len(fitness_history): # Do a line graph
                location_y = graph_origin[1] - (fitness_history[count] * (graph_origin[1] - vertical_end[1]))
                location_x = graph_origin[0] + (1 * (horizontal_increment * count)) + 5
                current_point = (location_x, location_y)
                if previous_point is not None:
                    cnv_graph_fitness.create_line(previous_point[0], previous_point[1], current_point[0], current_point[1], fill="blue")
                previous_point = current_point
                count = count + 1

    def _draw_evaluation_points(self, cnv_graph_evaluations, graph_origin, vertical_end, horizontal_end, evaluation_history): # pragma: no cover
        """ Draws the evaluation graph. """
        # Draw vertical axis values (Increments of 0.1 from 0)
        increment = (graph_origin[1] - vertical_end[1]) / 10
        count = 0
        while count <= 1:
            text_location = (graph_origin[0], graph_origin[1] - ((count * 10) * increment))    # Add the label slightly to the left of axis
            cnv_graph_evaluations.create_text(text_location[0] - 25, text_location[1], font="arial 8", text="{}".format(int(evaluation_history[-1] * count) + 1))   # Create label
            cnv_graph_evaluations.create_line(text_location[0] - 2, text_location[1], text_location[0] + 2, text_location[1])
            count = count + 0.1
        # Draw points
        horizontal_increment = (horizontal_end[0] - graph_origin[0]) / len(evaluation_history)    # Calculate an even spacing between evaluation values
        count = 0
        previous_point = None
        if len(evaluation_history) == 1:   # Special case of a single point
            location_y = vertical_end[1]    # Top most point
            location_x = graph_origin[0] + ((horizontal_end[0] - graph_origin[0]) / 2)
            cnv_graph_evaluations.create_text(location_x, location_y, fill="blue", text="x")
        else:
            while count < len(evaluation_history): # Do a line graph
                location_y = graph_origin[1] - ((evaluation_history[count] / evaluation_history[-1]) * (graph_origin[1] - vertical_end[1])) # position varies
                location_x = graph_origin[0] + (count * (horizontal_increment)) + 5
                current_point = (location_x, location_y)
                if previous_point is not None:
                    cnv_graph_evaluations.create_line(previous_point[0], previous_point[1], current_point[0], current_point[1], fill="blue")
                previous_point = current_point
                count = count + 1

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
        clique_size = int(self._builder.get_object("tb_clique_size").get()) # Get update parameters
        graph_size = int(self._builder.get_object("tb_graph_size").get())
        method = self._builder.get_object("cb_method").get()
        update_argument = {"clique_size": clique_size, "graph_size": graph_size, "method": method}    # Argument to update observers with
        for o in self._observers:
            o.update(update_argument)
        # Disable solve button
        self._builder.get_object("btn_solve").config(state="disabled")

    def update(self, args):
        """ Update details on form to show progress if required. """
        if ('graph' and 'generation' and 'evals' and 'best_fitness' and 'finished' and 'history') in args:
            if (self._update_thread is None) or (not self._update_thread.isAlive()):
                self._update_thread = Thread(target=self._update_gui, args=(args['generation'], args['evals'], float(args['best_fitness']), args['history'], args['finished'], args['graph'],))
                self._update_thread.start()