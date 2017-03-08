from Subject import Subject
from itertools import combinations
from ..SatisfiabilitySimulator.equation.BoolTree import Equation

class PartyProblem(Subject):
    """ A party problem which controls the party problem visualiser. """

    def __init__(self, clique_size, graph_size, algorithm):
        """ Initialises the instances variables required. """
        super().__init__()
        self._vertices = self._generate_vertices(graph_size)        # The vertices present in this graph.
        self._edges = self._generate_edges(graph_size)              # The edges present and their corresponding vertices.
        self.equation = None                                        # The equation generated from this graph problem.
        self._method = algorithm                                    # The algorithm to be used in order to solve the equation.
            
    def _generate_vertices(self, graph_size):
        """ Generates the vertices based on the intended size of this graph. """
        vertices = []
        count = 0   # Give vertices the ids equal to integers
        while count < graph_size:
            vertices.append({ 'id': str(count)})
        return vertices
    
    def _generate_edges(self, graph_size):
        """ Generates the list of edges to be used for this graph. """
        edges = []
        count = 0
        start_index = 0
        while start_index < len(self._vertices):    # Work out one edge between each vertex
            cur_index = start_index + 1
            while cur_index < len(self._vertices):  # New edge required
                edges.append({
                    'vertex_one': self._vertices[start_index]['id'],
                    'vertex_two': self._vertices[cur_index]['id'],
                    'edge_id': str(count)
                })
                count = count + 1   # Increment counters
                cur_index = cur_index + 1
            start_index = start_index + 1      
        return edges

    def _generate_equation(self, clique_size):
        """ Generates a boolean equation based on the clique size provided and vertices. """
        # Get all combinations of clique size
        combs = combinations(self._vertices, clique_size)

        # Generate string equation equivalent
        bln_str = ""
        for c in combs:
            clause = "("    # Build a clause
            for item in c:
                clause = clause + "{" + item['id'] + "}"
            clause = clause + ")"
            clause.replace("}{", "}.{") # Put the AND symbols in
            bln_str = bln_str + "+" + clause  # Put clause on bln_str
        bln_str = bln_str[1:]   # Remove initial "+"

        # Generate tree equation
        eq = Equation(bln_str)
        return eq
