from Visualizer.Observation.Observer import Observer
from Visualizer.Observation.Subject import Subject

class Simulator(Subject, Observer):
    """ A simulator to process party problems. """

    def __init__(self):
        """ Initializes a user interface and sets up callbacks. """
        pass
    
    def _notify_observers(self):
        """ Notifies observers of genetic parameters and graph. """
        args = {
            "generation": 0,
            "evaluations": 
        }