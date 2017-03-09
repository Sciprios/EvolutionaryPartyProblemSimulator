class Vertex(object):
    """ A point within a graph. """

    def __init__(self, identifier, location_x=0, location_y=0):
        """ Initialises a vertex with the given properties. """
        self._set_id(identifier)
        self._set_location(location_x, location_y)
    
    def _set_id(self, id):
        """ Safely sets the identifier of this vertex. """
        if isinstance(id, int):
            self._id = id
        else:
            self._id = -1
    
    def _set_location(self, x=0, y=0):
        """ Sets the location of this vertex on a graph; defaults to (0,0) """
        if not isinstance(x, int):
            x = 0
        if not isinstance(y, int):
            y = 0
        self._location = (x, y)
    
    def get_id(self):
        """ Retrieve the id of this vertex. """
        return self._id
    
    def get_location(self):
        """ Retrieves the location of this vertex. """
        return self._location