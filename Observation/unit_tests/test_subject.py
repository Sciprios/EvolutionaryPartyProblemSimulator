from unittest.mock import Mock, call, patch
from unittest import TestCase
from Observation.Subject import Subject
from Observation.Observer import Observer

class TestSubject(TestCase):
    """ Ensures the subject object's methods. """

    def test_init(self):
        """ Ensures the constructor initialises an empty list of observers. """
        s = Subject()
        assert s._observers == []
    
    def test_subscribe(self):
        """ Ensures the subscription route only allows observers to subscribe. """
        s = Subject()
        o = Observer()
        x = "Not an observer"   # Create a non-observer
        s.subscribe(o)
        assert s._observers[0] is o
        s.subscribe(x)
        assert len(s._observers) == 1
    
    def test_unsubscribe(self):
        """ Ensures a subscriber is unsubscribed when required. """
        s = Subject()
        o = Observer()  # One to be subscribed
        o2 = Observer() # One not to be subscribed
        s.subscribe(o)
        s.unsubscribe(o2)   # Ensure nothing is removed as o2 isn't subscribed.
        assert s._observers[0] is o
        s.unsubscribe(o)
        assert s._observers == []


    def test_notify(self):
        """ Ensures the notify observers method throws an error. """
        s = Subject()
        try:
            s._notify_observers()
            assert False
        except NotImplementedError:
            assert True