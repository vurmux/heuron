#!/usr/bin/python

import re

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
        self.ip_register = None
        if 'ip_register' in kwargs:
            self.ip_register = kwargs['ip_register']
        self.joints = []
        self.make_joint_topology()
        
    def __str__(self):
        result = ''
        result = result + 'CPU: ' + self.name + '\n'
        result = result + 'REGISTERS:\n'
        for r_name in self.registers:
            result = result + r_name + ': ' + str(self.registers[r_name]) + '\n'
        for f_name in self.flags:
            result = result + str(self.flags[f_name]) + '\n'
        for i_name in self.instructions:
            result = result + str(self.instructions[i_name]) + '\n'
        print self.joints
        for j in self.joints:
            result = result + str(j) + '\n'
        return result
        
    def execute(self, i_name, *operands):
        self.instructions[i_name].execute(*operands)
        if self.ip_register:
            self.registers[self.ip_register].value = functions.func_inc(
                self.registers[self.ip_register].value
            )
        
    def load_registers(reg_array):
        self.registers = {r.name: r for r in reg_array}
        
    def load_flags(flag_array):
        self.flags = {f.name: f for f in flag_array}
        
    def load_instructions(inst_array):
        self.instructions = {i.name: i for i in inst_array}
        
    def make_joint_topology(self):
        for instruction in self.instructions:
            for joint_name, joint in self.instructions[instruction].joints.iteritems():
                if joint_name == '-':
                    continue
                if joint_name in self.flags:
                    joint.connect(self.flags[joint_name])
                    self.flags[joint_name].set_joint(joint)
                    self.joints.append(self.flags[joint_name].joint)
                elif joint_name in self.registers:
                    joint.connect(self.registers[joint_name])
                    self.joints.append(self.registers[joint_name].joint)
                else:
                    raise AttributeError
                
    def match_instruction(self, string):
        instructions_regexps = {i.mnemonic: i for i in self.instructions.values()}
        for raw_regexp in instructions_regexps:
            regexp = re.compile(re.sub(r'\$\d+', '.*', raw_regexp))
            if regexp.match(string):
                return instructions_regexps[raw_regexp]
        return False


if __name__ == '__main__':
    cpu_registers = register.load_from_file('../examples/x86/registers.json')
    cpu_instructions = instruction.load_from_file('../examples/x86/instructions.json')
    cpu_flags = flag.load_from_file('../examples/x86/flags.json')
    
    cpu = CPU(
        name='x86',
        instructions=cpu_instructions,
        flags=cpu_flags,
        registers=cpu_registers,
        ip_register='EIP',
    )

    cpu.registers['EAX'].set_int_value(415)
    cpu.registers['EBX'].set_int_value(342)
    print cpu
    print '-' * 40 + '\n'
    cpu.execute('XOR', cpu.registers['EAX'], cpu.registers['EBX'])
    print cpu
    print '-' * 40 + '\n'
    cpu.execute('XOR', cpu.registers['EAX'], cpu.registers['EAX'])
    print cpu
    print '-' * 40 + '\n'
    cpu.execute('JMP', cpu.registers['EIP'], 0)
    print cpu
    print '-' * 40 + '\n'
    cpu.execute('MOV', cpu.registers['EAX'].value, cpu.registers['EBX'].value)
    print cpu
    print '-' * 40 + '\n'
    print cpu.match_instruction('XOR AX, BX')
    print cpu.match_instruction('XOR RAX, [RBX+1]')
    print cpu.match_instruction('NOP')
    print cpu.match_instruction('QWERTY A, B')
