#!/usr/bin/python


class Joint:

    def __init__(self, j_from):
        self.j_from = j_from
        self.j_to = None

    def __str__(self):
        return str(self.j_from) + '->' + str(self.j_to)

    def connect(self, target):
        self.j_to = target
        target.set_joint(self)

    def bend(self, func, *args):
        if not self.j_to:
            raise ValueError
        func(*args)
