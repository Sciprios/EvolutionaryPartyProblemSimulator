from Observation.Observer import Observer

class Subject(object):
    """ A subject which can notify some observers of changes. """

    def __init__(self):
        """ Initialises the instance with an empty list of observers. """
        self._observers = []
    
    def subscribe(self, obs):
        """ Subscribes the given observer to this subject. """
        if isinstance(obs, Observer):
            self._observers.append(obs)
    
    def unsubscribe(self, obs):
        """ Unsubscribes the given observer from this subject. """
        if obs in self._observers:
            self._observers.remove(obs)
    
    def _notify_observers(self):
        """ To be implemented to notify observers with suitable information. """
        raise NotImplementedError("The _notify_observers method has not been inherited by the class {}".format(type(self)))