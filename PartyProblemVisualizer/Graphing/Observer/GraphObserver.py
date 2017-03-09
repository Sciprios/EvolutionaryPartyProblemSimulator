class GraphObserverObserver(object):
    """ Observes a Problem subject for changes. """
    def update(self, edges, gen, evals, fin):
        """ Updates the sub class with the edges present. """
        raise NotImplementedError("The update method has not been inherited by the base class {}".format(type(self)))