from unittest.mock import Mock, call, patch
from unittest import TestCase
from Visualizer.Graphing.Edge import Edge
from Visualizer.Graphing.Vertex import Vertex

class TestEdge(TestCase):
    """ Tests the Edge class. """

    def setUp(self):
        """ Sets up a fake vertex for class based use. """
        self.vertex = Vertex(0, 0, 0)

    @patch('Visualizer.Graphing.Edge.Edge._set_origin')
    @patch('Visualizer.Graphing.Edge.Edge._set_target')
    @patch('Visualizer.Graphing.Edge.Edge.set_colour')
    def test_init(self, set_col, set_tar, set_or):
        """ Tests the initialisation of an Edge. """
        edge = Edge(0, self.vertex, self.vertex)
        set_or.assert_called_with(self.vertex)
        set_tar.assert_called_with(self.vertex)
        set_col.assert_called_with(0)

        o = "Origin"
        t = "Target"
        c = "Colour"
        edge = Edge(0, origin=o, target=t, colour=c)
        set_or.assert_called_with(o)
        set_tar.assert_called_with(t)
        set_col.assert_called_with(c)
    
    @patch('Visualizer.Graphing.Edge.Edge._set_target')
    def test_set_origin(self, set_tar):
        """ Ensures the origin instance variable is protected. """
        edge = Edge(0, self.vertex, None)
        assert edge._origin == self.vertex

        edge._origin = None # Reset
        edge._set_origin(self.vertex)
        assert edge._origin == self.vertex

        try:    # When not passing a vertex an error should be thrown.
            edge._origin = None
            edge._set_origin("Not an vertex")
            assert False
        except TypeError:
            assert True

    @patch('Visualizer.Graphing.Edge.Edge._set_origin')
    def test_set_target(self, set_or):
        """ Ensures the target instance variable is protected. """
        edge = Edge(0, None, self.vertex)
        assert edge._target == self.vertex

        edge._target = None # Reset
        edge._set_target(self.vertex)
        assert edge._target == self.vertex

        try:    # When not passing a vertex an error should be thrown.
            edge._target = None
            edge._set_target("Not an vertex")
            assert False
        except TypeError:
            assert True
    
    @patch('Visualizer.Graphing.Edge.Edge._set_origin')
    @patch('Visualizer.Graphing.Edge.Edge._set_target')
    def test_set_colour(self, set_tar, set_or):
        edge = Edge(0, None, None)

        edge.set_colour(555)
        assert edge._colour == 555

        try:    # When not passing an integer an error should be thrown.
            edge.set_colour("Not an integer")
            assert False
        except TypeError:
            assert True