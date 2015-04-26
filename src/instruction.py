#!/usr/bin/python

import joint
import functions
import flag_functions
import json


class Instruction:
    
    def __init__(self, name, mnemonic, operands, result, function_name, bound):
        self.name = name
        self.mnemonic = mnemonic
        self.operands = operands
        self.result = result
        self.function_name = function_name
        self.joints = {}
	for elem in bound.split(' '):
            self.joints[elem] = joint.Joint(self)
            
    def __str__(self):
        return self.name + ' ' + self.mnemonic
            
    def check_correctness(self):
        if self.operands != '-':
            for operand in self.operands:
                if operand not in self.mnemonic:
                    return False
        if self.result != '-' and self.result not in self.mnemonic:
            return False
        return True
            
    # TODO: Ugly code. Refactor it!
    def execute(self, *operands):
        result = getattr(functions, self.function_name)(*operands)
        for joint_name in self.joints:
            if self.joints[joint_name].j_to:
                self.joints[joint_name].bend(getattr(flag_functions, self.joints[joint_name].j_to.function))
        return result

    def set_joint(self, joint):
        self.joint = joint


def load_from_file(filename):
    inst_file = open(filename)
    inst_str = inst_file.read()
    inst_file.close()
    instructions = json.loads(inst_str)
    result = []
    for instruction in instructions:
        result.append(
            Instruction(
                instruction['name'],
                instruction['mnemonic'],
                instruction['operands'],
                instruction['result'],
                instruction['function'],
                instruction['bound']
            )
        )
    return result
