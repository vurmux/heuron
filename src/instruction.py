#!/usr/bin/python

import joint


class Instruction:
    
    def __init__(self, name, mnemonic, operands, result, function, bound):
        self.name = name
        self.mnemonic = mnemonic
        self.operands = operands
        self.result = result
        self.function = function
        self.bound = bound
        
    def execute(self, *operands):
        self.result = None
        result = self.function(*operands)
        return result

    def get_joint(self, joint):
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
