#!/usr/bin/python

import flag
import flag_functions
import functions
import instruction
import register


class CPU:

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        if 'instructions' in kwargs:
            self.instructions = {i.name: i for i in kwargs['instructions']}
        if 'flags' in kwargs:
            self.flags = {f.name: f for f in kwargs['flags']}
        if 'registers' in kwargs:
            self.registers = {r.name: r for r in kwargs['registers']}
        
    def __str__(self):
        result = ''
        result = result + 'CPU: ' + self.name + '\n'
        result = result + 'REGISTERS:\n'
        for r_name in self.registers:
            result = result + str(self.registers[r_name]) + '\n'
        result = result + str(self.flags) + '\n'
        result = result + str(self.instructions) + '\n'
        result += '\n'
        return result
        
    def execute(self, i_name, reg1, reg2):
        self.instructions[i_name].execute(reg1, reg2)
        
    def load_registers(reg_array):
        self.registers = {r.name: r for r in reg_array}
        
    def load_flags(flag_array):
        self.flags = {f.name: f for f in flag_array}
        
    def load_instructions(inst_array):
        self.instructions = {i.name: i for i in inst_array}


if __name__ == '__main__':
    XOR = instruction.Instruction('XOR', functions.func_xor)
    ZF = flag.Flag('ZF')
    AX = register.Register('AL', size=8)
    
    cpu = CPU(
        name='x86',
        instructions=[XOR, ],
        flags=[ZF, ],
        registers=[AX, ],
    )
    print cpu
