from PartyProblem import PartyProblem
from  math import sin, cos
import tkinter as tk
import pygubu

class MainForm:
    def __init__(self, master):
        # Create a builder
        self.builder = builder = pygubu.Builder()
        # Load an ui file
        builder.add_from_file('gui.ui')
        # Create the widget using a master as parent
        self.mainwindow = builder.get_object('frm_main', master)
        # Add event handlers
        self._add_eventhandlers()
        # Create instance variables
        self._party_problem = None
        self._vertices = []

    def _add_eventhandlers(self):
        """ Adds event handlers to buttons on the form. """
        # Solve button
        btn_solve = self.builder.get_object('btn_solve')
        btn_solve.configure(command=self._btn_solve_click)

    def _btn_solve_click(self):
        """ Attempts to solve the given problem. """
        # Get inputs from form
        clique_size = self.builder.get_object('tb_clique_size').get()
        graph_size = self.builder.get_object('tb_graph_size').get()
        try:
            clique_size = int(clique_size)
            graph_size = int(graph_size)

            # Generate Party Problem object
            self._party_problem = PartyProblem(clique_size, graph_size)
            self._display_graph()
        except ValueError:
            lbl_error = self.builder.get_object('lbl_error')
            lbl_error.config(text="Please ensure you only use numbers in the input fields.")
        else:
            lbl_error = self.builder.get_object('lbl_error')
            lbl_error.config(text="")   # Reset error label

    def _display_graph(self):
        """ Displays the instance of the party problem. """
        # Generate vertices
        self._vertices = []
        self._generate_vertices()

        # Draw vertices
        cnv_display = self.builder.get_object('cnv_display')
        for v in self._vertices:
            cnv_display.create_oval(v[0]-2.5, v[1] - 2.5, v[0] + 2.5, v[1] + 2.5)
        
    def _generate_vertices(self):
        """ Generates vertice coordinates for the defined problem. """
        cnv_display = self.builder.get_object('cnv_display')

        # Calculate properties for graph
        max_x = int(cnv_display.cget("width")) - 5
        max_y = int(cnv_display.cget("height")) - 5
        min_x = 5
        min_y = 5

        # Calculate center of graph
        center = ((max_x - min_x) / 2, (max_y - min_y) / 2)

        # Calculate X and Y values for each vertex
        deg_increment = 360 / len(self._party_problem.vertices)
        cur_deg = 0
        for v in self._party_problem.vertices:
            x = center[0] + (100 * sin(cur_deg))  # x = center's x + 5(sin(degree))
            y = center[1] + (100 * cos(cur_deg))  # y = center's y + 5(cos(degree))
            self._vertices.append((x, y))
            cur_deg = cur_deg + deg_increment

if __name__ == '__main__':
    root = tk.Tk()
    app = MainForm(root)
    root.resizable(width=False, height=False)
    root.mainloop()