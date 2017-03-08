class PartyProblem(object):
    """ This class represents a Party Problem which can be represented in many ways. """

    def __init__(self, clique_size, graph_size):
        """ Initialises the main properties of a Party Problem. """
        self.clique_size = clique_size
        self.graph_size = graph_size
        self.vertices = []
        self.adjacency_matrix = []
        self._generate_vertices()
    
    def _generate_vertices(self):
        """ Generates the vertice dictionaries. """
        cnt = 0
        while (cnt < self.graph_size):
            self.vertices.append({
                'id': cnt
            })
            cnt = cnt + 1

    def set_clique_size(size):
        """ Sets the clique size. """
        if size is not None:
            if size >= 2:
                self.clique_size = size
    
    def set_graph_size(size):
        """ Sets the graph's size. """
        if size is not None:
            if size >= 2:
                self.graph_size = size
