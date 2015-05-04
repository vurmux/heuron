#!/usr/bin/python


import cpu

class Emulator:
    
    def __init__(self, cpu, execution_limit, ip_register='IP'):
        self.cpu = cpu
        self.program = []
        self.execution_limit = execution_limit
        self.ip_register = ip_register
    
    def load_program(self, program):
        self.program = program.readlines()

    def execute_program(self):
        tick = 0
        while True:
            if tick > self.execution_limit:
                break
            self.cpu.execute(
                self.cpu.match_instruction(
                    self.program[
                        self.cpu.registers[self.ip_register].get_int_value()
                    ]
                )
            )
