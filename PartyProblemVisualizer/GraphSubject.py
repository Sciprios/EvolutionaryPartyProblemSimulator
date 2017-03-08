class GraphSubject(object):
    """ A subscribable object which can notify GraphObservers. """
    def __init__(self):
        """ Initialises a subscriber list. """
        self._observers = []
    
    def sub(self, observer):
        """ Subscribes the given observer. """
        if observer not in self._observers:
            self._observers.append(observer)
    
    def unsub(self, observer):
        """ Unsubscribes observer from this subject. """
        if observer in self._observers:
            self._observers.remove(observer)
    
    def _notify_observers(self, edges, gen, evals, fin):
        """ Notifies observers that something has happened. """
        for o in self._observers:
            o._update(edges, gen, evals, fin)