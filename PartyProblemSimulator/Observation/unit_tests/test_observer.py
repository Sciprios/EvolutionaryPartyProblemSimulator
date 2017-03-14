from unittest.mock import Mock, call, patch
from unittest import TestCase
from PartyProblemSimulator.Observation.Observer import Observer

class TestObserver(TestCase):
    """ Ensures the observer object throws an error if unimplemented. """

    def test_update(self):
        """ Ensures the update method throws an error. """
        o = Observer()
        try:
            o.update(0)
            assert False
        except NotImplementedError:
            assert True