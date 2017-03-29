from PartyProblemSimulator.Solvers.Organisms.Genes.Gene import Gene
from random import randint

ENCODINGS = {
    "a": [0, 1],
    "b": [1, 0],
    "c": [0, 0],
    "d": [1, 1],
    "e": [1],
    "f": [0]
}

class SubMatrixGene(Gene):
    """ Represents a section of an adjacency matrix consisting of component genes. """

    def __init__(self, contents):
        """ Initialises the components of this sub-matrix. """
        Gene.__init__(self, contents)     # Contents is a string grammatical representation.
    
    def get_information(self):
        """ Decodes the grammatical data and returns a bit string. """
        bit_string = []
        for symbol in self.get_data():  # For each component in this sub-matrix
            bit_string.extend(ENCODINGS[symbol])
        return bit_string
    
    def mutate(self):
        """ Mutates itself """
        new_data = ""
        count = 0
        OLD_COUNT = len(self.get_data())
        for symbol in self.get_data():
            mutated_symbol = None
            # Decide whether to mutate to a, b, c or d.
            encoding = randint(0, 3)
            if encoding == 0:
                mutated_symbol = "a"
            elif encoding == 1:
                mutated_symbol = "b"
            elif encoding == 2:
                mutated_symbol = "c"
            else:
                mutated_symbol = "d"
            new_data = new_data + mutated_symbol
            count = count + 1
        self.set_data(new_data)
