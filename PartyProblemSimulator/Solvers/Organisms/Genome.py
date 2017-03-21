class Genome(object):
    """ A collection of genes. """

    def __init__(self, genome_size):
        """ Initialises the required attributes for a genome. """
        self._genes = []
        self._set_genome_size(genome_size)
        self._instantiate()
        
    def _instantiate(self):
        """ Initialises this genome with a random set of genes. """
        raise NotImplementedError("The instantiate method has not been inherited by the base class {}".format(type(self)))

    def evaluate(self, equation):
        """ Evaluates this genome against the given equation. """
        raise NotImplementedError("The evaluate method has not been inherited by the base class {}".format(type(self)))

    def add_gene(self, gene):
        """ Adds the given gene to this genome. """
        self._genes.append(gene)
    
    def remove_gene(self, gene):
        """ Removes the given gene from the genome. """
        self._genes.remove(gene)

    def get_genes(self):
        """ Retrieves the genes from this genome. """
        return self._genes

    def _set_genome_size(self, genome_size):
        """ Safely sets the gene count of this genome. """
        if genome_size > 0:
            self._genome_size = genome_size
        else:
            self._genome_size = 1
    
    def _get_genome_size(self):
        """ Retrieves the gene count for this genome. """
        return self._genome_size