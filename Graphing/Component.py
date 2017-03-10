class Component(object):
    """ A component is a entity within a graph with a given identifier. """

    def __init__(self, id):
        """ Initialises the id of this component. """
        self._set_id(id)

    def _set_id(self, id):
        """ Safely sets the identifier of this component. """
        if isinstance(id, int):
            self._id = id
        else:
            self._id = -1

    def get_id(self):
        """ Retrieve the id of this component. """
        return self._id