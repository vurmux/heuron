#!/usr/bin/python


class Joint:
    def __init__(self, j_from):
        self.j_from = j_from
        self.j_to = None

    def connect(self, target):
        self.j_to = target
        target.set_joint(self)
        
    def bend(self, func):
        if not self.j_to:
            raise ValueError
        func(self.j_to)
