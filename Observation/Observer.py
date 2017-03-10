class Observer(object):
    """ An Entity which can observe a subject. """

    def update(self, args):
        """ To be implemented to update this object based on the args dictionary provided. """
        raise NotImplementedError("The update method has not been inherited by the class {}".format(type(self)))