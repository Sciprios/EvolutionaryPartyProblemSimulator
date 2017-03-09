class ProblemSubject(object):
    """ A subscribable object which can notify ProblemObservers. """
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
    
    def _notify_observers(self, graph, gen, evalsfinished):
        """ Notifies observers that something has happened. """
        for o in self._observers:
            o._update(graph, gen, evals, fin)