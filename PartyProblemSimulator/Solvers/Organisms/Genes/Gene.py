class Gene(object):
    """ A gene represents s section of a genome. """

    def __init__(self, data):
        """ Initialises the data to be stored within this gene. """
        self.set_data(data)
    
    def set_data(self, data):
        """ Safely sets the data of this gene. """
        self._data = data
    
    def get_data(self):
        """ Retrieves the data which this gene represents. """
        return self._data
    
    def get_information(self):
        """ Retrieves the information encoded in this gene. """
        raise NotImplementedError("The get_data method has not been inherited by the base class {}".format(type(self)))