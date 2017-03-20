class Genome(object):
    """ A collection of genes. """

    def __init__(self):
        """ Initialises the required attributes for a genome. """
        self._genes = []
    
    def evaluate(self, equation):
        """ Evaluates this genome against the given equation. """

    def add_gene(self, gene):
        """ Adds the given gene to this genome. """
        self._genes.append(gene)
    
    def remove_gene(self, gene):
        """ Removes the given gene from the genome. """
        self._genes.remove(gene)

    def get_genes(self):
        """ Retrieves the genes from this genome. """
        return self._genes