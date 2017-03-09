class Vertex(object):
    """ A vertice within a graph. """

    def __init__(self, identifier, x=None, y=None):
        """ Initializes this vertex with the given idenifier. """
        self._id = identifier
        self.set_location = (x,y) # The location of the vertex can be empty.

    def get_id(self):
        """ Returns the identifier of this vertex. """
        return self._id

    def set_location(self, new_x=0, new_y=0):
        """ Safely sets the new location of this vertex. Defaults to (0, 0) """
        # Check values are integers
        if isinstance(new_x, int) and isinstance(new_y, int):
            self._location = (new_x, new_y)
        else:
            self._location = (0, 0)