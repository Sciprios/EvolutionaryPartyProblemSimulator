from unittest.mock import Mock, call, patch
from unittest import TestCase
from Graphing.Edge import Edge
from Graphing.Vertex import Vertex

class TestEdge(TestCase):
    """ Tests the Edge class. """

    def setUp(self):
        """ Sets up a fake vertex for class based use. """
        self.vertex = Vertex(0, 0, 0)

    @patch('Graphing.Edge.Edge._set_origin')
    @patch('Graphing.Edge.Edge._set_target')
    def test_init(self, set_tar, set_or):
        """ Tests the initialisation of an Edge. """
        edge = Edge(self.vertex, self.vertex)
        set_or.assert_called_with(self.vertex)
        set_tar.assert_called_with(self.vertex)

        o = "Origin"
        t = "Target"
        edge = Edge(origin=o, target=t)
        set_or.assert_called_with(o)
        set_tar.assert_called_with(t)
    
    @patch('Graphing.Edge.Edge._set_target')
    def test_set_origin(self, set_tar):
        """ Ensures the origin instance variable is protected. """
        edge = Edge(self.vertex, None)
        assert edge._origin == self.vertex

        edge._origin = None # Reset
        edge._set_origin(self.vertex)
        assert edge._origin == self.vertex

        try:    # When not passing an integer an error should be thrown.
            edge._origin = None
            edge._set_origin("Not an integer")
            assert False
        except TypeError:
            assert True

    @patch('Graphing.Edge.Edge._set_origin')
    def test_set_target(self, set_or):
        """ Ensures the target instance variable is protected. """
        edge = Edge(None, self.vertex)
        assert edge._target == self.vertex

        edge._target = None # Reset
        edge._set_target(self.vertex)
        assert edge._target == self.vertex

        try:    # When not passing an integer an error should be thrown.
            edge._target = None
            edge._set_target("Not an vertex")
            assert False
        except TypeError:
            assert True