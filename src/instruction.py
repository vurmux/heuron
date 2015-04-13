#!/usr/bin/python

import joint


class Instruction:
    
    def __init__(self, name, function):
        self.name = name
        self.function = function
        
    def execute(self, op1, op2):
        self.result = None
        result = self.function(op1, op2)
        return result

    def get_joint(self, joint):
        self.joint = joint
