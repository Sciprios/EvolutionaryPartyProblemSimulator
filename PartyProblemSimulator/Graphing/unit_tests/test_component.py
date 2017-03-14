from unittest.mock import Mock, call, patch
from unittest import TestCase
from PartyProblemSimulator.Graphing.Component import Component

class TestComponent(TestCase):
    """ Ensures s component meets the requirements. """

    @patch('PartyProblemSimulator.Graphing.Component.Component._set_id')
    def test_init(self, set_id):
        """ Ensure the constructor initialises this components id. """
        c = Component(5)
        set_id.assert_called_with(5)

    @patch('PartyProblemSimulator.Graphing.Component.Component._set_id')
    def test_get_id(self, set_id):
        """ Tests the retrieval of the id. """
        component = Component(None)
        component._id = 0
        assert component.get_id() == 0
        component._id = 1000
        assert component.get_id() == 1000

    def test_set_id(self):
        """ Ensures the setting of id protects the instance variable. """
        component = Component(0)
        assert component._id == 0

        component._set_id(None)    # id should default to -1
        assert component._id == -1

        component._set_id(0.1)
        assert component._id == -1