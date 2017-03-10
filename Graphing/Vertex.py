from Graphing.Component import Component

class Vertex(Component):
    """ A point within a graph. """

    def __init__(self, identifier, location_x=0, location_y=0):
        """ Initialises a vertex with the given properties. """
        super().__init__(identifier)
        self._set_id(identifier)
        self._set_location(location_x, location_y)
    
    def _set_location(self, x=0, y=0):
        """ Sets the location of this vertex on a graph; defaults to (0,0) """
        if not isinstance(x, int):
            x = 0
        if not isinstance(y, int):
            y = 0
        self._location = (x, y)
    
    def get_location(self):
        """ Retrieves the location of this vertex. """
        return self._location