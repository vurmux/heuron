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
        self.make_joint_topology()
        
    def __str__(self):
        result = ''
        result = result + 'CPU: ' + self.name + '\n'
        result = result + 'REGISTERS:\n'
        for r_name in self.registers:
            result = result + str(self.registers[r_name]) + '\n'
        for f_name in self.flags:
            result = result + str(self.flags[f_name]) + '\n'
        for i_name in self.instructions:
            result = result + str(self.instructions[i_name]) + '\n'
        result += '\n'
        return result
        
    def execute(self, i_name, *operands):
        return self.instructions[i_name].execute(*operands)
        
    def load_registers(reg_array):
        self.registers = {r.name: r for r in reg_array}
        
    def load_flags(flag_array):
        self.flags = {f.name: f for f in flag_array}
        
    def load_instructions(inst_array):
        self.instructions = {i.name: i for i in inst_array}
        
    # TODO: Ugly code. Refactor it!
    def make_joint_topology(self):
        for instruction in self.instructions:
            for elem in self.instructions[instruction].joints:
                if elem == '-':
                    continue
                if elem in self.flags:
                    self.flags[elem].set_joint(self.instructions[instruction].joints[elem])
                elif elem in self.registers:
                    self.registers[elem].set_joint(self.instructions[instruction].joints[elem])
                else:
                    raise AttributeError


if __name__ == '__main__':
    cpu_registers = register.load_from_file('../examples/x86/registers.json')
    cpu_instructions = instruction.load_from_file('../examples/x86/instructions.json')
    cpu_flags = flag.load_from_file('../examples/x86/flags.json')
    
    cpu = CPU(
        name='x86',
        instructions=cpu_instructions,
        flags=cpu_flags,
        registers=cpu_registers,
    )

    cpu.registers['EAX'].set_int_value(415)
    cpu.registers['EBX'].set_int_value(342)
    print cpu
    print '-' * 40
    cpu.registers['EAX'].value = cpu.execute('XOR', cpu.registers['EAX'].value, cpu.registers['EBX'].value)
    print cpu
