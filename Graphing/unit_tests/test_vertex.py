from unittest.mock import Mock, call, patch
from unittest import TestCase
from Graphing.Vertex import Vertex

class TestVertex(TestCase):
    """ Tests the vertex class. """

    @patch('Graphing.Vertex.Vertex._set_location')
    def test_init(self, set_loc):
        """ Ensure initializing the Vertex sets the right properties. """
        vertex = Vertex(0, 1, 2)
        set_loc.assert_called_with(1, 2)

    def test_set_location(self):
        """ Ensures the setting of location is protected. """
        vertex = Vertex(0, 1, 2)
        assert vertex._location == (1, 2)

        vertex._set_location(5, "Not an integer")
        assert vertex._location == (5, 0)

        vertex._set_location("Not an integer", 5)
        assert vertex._location == (0, 5)

        vertex._set_location("Not an integer", "Not an integer")
        assert vertex._location == (0, 0)
    
    @patch('Graphing.Vertex.Vertex._set_location')
    def test_get_location(self, set_loc):
        """ Tests the retrieval of the location. """
        vertex = Vertex(None, None, None)
        vertex._location = (0, 0)
        assert vertex.get_location() == (0, 0)
        vertex._location = (1000, 1000)
        assert vertex.get_location() == (1000, 1000)