from PartyProblemSimulator.Solvers.Organisms.Genes.Gene import Gene

class BinaryGene(Gene):
    """ Represents a gene which can either be true of false. """

    def __init__(self, value):
        """ Instantiates this binary gene with the given value. """
        Gene.__init__(self, value)
    
    def get_information(self):
        """ For binary genes the information is the same as the raw data (a boolean). """
        return self.get_data()