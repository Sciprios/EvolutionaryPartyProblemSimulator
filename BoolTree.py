""" This module contains the classes required to make a boolean equation. """

class SimpleNode(object):
    """ A simple tree node which represents a single terminal. """

    def __init__(self, identifier):
        """ Initializes a Terminal. """
        self.id = identifier

    def evaluate(self, input_vector):
        """
        Evaluates the result of this node.
        Returns true if the input contains this variable as true.
        """
        if input_vector[self.id]:
            return True

class InverseSimple(object):
    """ Inverses a simple nodes evaluation. """

    def __init__(self, identifier):
        """ Initializes a Terminal. """
        self.id = identifier

    def evaluate(self, input_vector):
        """
        Evaluates the result of this node.
        Returns true if the input contains this variable as false.
        """
        if input_vector[self.id]:
            return False
        elif not input_vector[self.id]:
            return True

class AndNode(object):
    """ A node which 'Ands' the result of two inner nodes. """

    def __init__(self, node_one, node_two):
        """ Instantiates a instance variables containing the two nodes. """
        self.a = node_one
        self.b = node_two
    
    def evaluate(self, input_vector):
        """ Evaluates the result of the two inner nodes and produces the AND of them. """
        return self.a.evaluate(input_vector) and self.b.evaluate(input_vector)

class OrNode(object):
    """ A node which 'Ors' the result of two inner nodes. """

    def __init__(self, node_one, node_two):
        """ Instantiates a instance variables containing the two nodes. """
        self.a = node_one
        self.b = node_two

    def evaluate(self, input_vector):
        """ Evaluates the result of the two inner nodes and produces the OR of them. """
        return self.a.evaluate(input_vector) or self.b.evaluate(input_vector)
