from PartyProblemSimulator.Solvers.Organisms.Genes.Gene import Gene

ENCODINGS = {
    "a": [0, 1],
    "b": [1, 0],
    "c": [0, 0],
    "d": [1, 1]
}

class SubMatrixGene(Gene):
    """ Represents a section of an adjacency matrix consisting of component genes. """

    def __init__(self, contents):
        """ Initialises the components of this sub-matrix. """
        Gene.__init__(contents)     # Contents is a string grammatical representation.
    
    def get_information(self):
        """ Decodes the grammatical data and returns a bit string. """
        bit_string = []
        for symbol in self.get_data():  # For each component in this sub-matrix
            for value in ENCODINGS[symbol]: # Generate bit string from known values
                bit_string.append(value)
        return bit_string