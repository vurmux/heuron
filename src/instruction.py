#!/usr/bin/python

import joint


class Instruction:
    
    def __init__(self, name, function):
        self.name = name
        self.function = function
        
    def execute(self, *operands):
        self.result = None
        result = self.function(*operands)
        return result

    def get_joint(self, joint):
        self.joint = joint
