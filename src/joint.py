#!/usr/bin/python


class Joint:
    """
    Implementation of Observer-like pattern.
    This pattern is very similar to Observer pattern. The main difference
    between them is that every Joint object is inside objects it connects
    unlike Observer objects.

    Class attributes:
    j_from - primary object that sends functions to the secondary
    j_to - secondary object that receives functions from the primary
    """

    def __init__(self, j_from):
        self.j_from = j_from
        self.j_to = None

    def __str__(self):
        return str(self.j_from) + '->' + str(self.j_to)

    def connect(self, target):
        """
        Connect current joint to target object.
        Every joint is created connected to one object so after calling this
        function current joint will be connected with two objects.

        Arguments:
        target - object current joint is connected to
        """
        self.j_to = target
        target.set_joint(self)

    def bend(self, func, *args):
        """
        Send a function from one object to another through the current joint.

        Arguments:
        func - target function
        args - arguments of target function
        """
        if not self.j_to:
            raise ValueError
        func(*args)
