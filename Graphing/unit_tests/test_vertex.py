from unittest.mock import Mock, call, patch
from unittest import TestCase
from Graphing.Vertex import Vertex

class TestVertex(TestCase):
    """ Tests the vertex class. """

    @patch('Graphing.Vertex.Vertex._set_location')
    @patch('Graphing.Vertex.Vertex._set_id')
    def test_init(self, set_id, set_loc):
        """ Ensure initializing the Vertex sets the right properties. """
        vertex = Vertex(0, 1, 2)
        set_id.assert_called_with(0)
        set_loc.assert_called_with(1, 2)

    @patch('Graphing.Vertex.Vertex._set_location')
    def test_set_id(self, set_loc):
        """ Ensures the setting of id protects the instance variable. """
        vertex = Vertex(0, 1, 2)
        assert vertex._id == 0

        vertex._set_id(None)    # id should default to -1
        assert vertex._id == -1

        vertex._set_id(0.1)
        assert vertex._id == -1
    
    @patch('Graphing.Vertex.Vertex._set_id')
    def test_set_location(self, set_id):
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
    @patch('Graphing.Vertex.Vertex._set_id')
    def test_get_id(self, set_id, set_loc):
        """ Tests the retrieval of the id. """
        vertex = Vertex(None, None, None)
        vertex._id = 0
        assert vertex.get_id() == 0
        vertex._id = 1000
        assert vertex.get_id() == 1000
    
    @patch('Graphing.Vertex.Vertex._set_location')
    @patch('Graphing.Vertex.Vertex._set_id')
    def test_get_location(self, set_id, set_loc):
        """ Tests the retrieval of the location. """
        vertex = Vertex(None, None, None)
        vertex._location = (0, 0)
        assert vertex.get_location() == (0, 0)
        vertex._location = (1000, 1000)
        assert vertex.get_location() == (1000, 1000)