from PartyProblemSimulator.Solvers.Organisms.Genome import Genome
from random import randint

class BinaryGenome(Genome):
    """ A binary encoding of a genome consisting of bits. """

    def __init__(self, var_count):
        """ Initialises the number of variables required in this genome. """
        self._var_count = var
        Genome.__init__()

    def _instantiate(self):
        """ Initialises this genome with a random set of binary values. """
        count = 0
        while count < self._get_var_count():
            if randint(0, 100) < 50:        # Randomize the value to apply to the gene
                self.add_gene(False)
            else:
                self.add_gene(True)
            count = count + 1
    
    def evaluate(self, equation):
        """ Evaluates this genome against the given equation. """
        input_vector = {}
        count = 0   # Generate the input vector
        for gene in self.get_genes():
            var_id = "{" + str(count) + "}" # Generate the identifier for this variable in the equation.
            input_vector[var_id] = gene
            count = count + 1
        clausal_result = equation.get_clause_evaluation(input_vector)
        score = sum(clausal_result) / len(clausal_result)   # Calculate the percentage of clauses met.
        return score

    def _set_var_count(self, var_count):
        """ Safely sets the var count of this genome. """
        if var_count > 0:
            self._var_count = var_count
        else:
            self._var_count = 1
    
    def _get_var_count(self):
        """ Retrieves the variable count for this binary genome. """
        return self._var_count