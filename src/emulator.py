#!/usr/bin/python


import cpu

class Emulator:
    
    def __init__(self, cpu):
        labels = []
        self.cpu = cpu
        self.program = None
    
    def parse_code(self):
        pass
    
    def load_program(self, program):
        pass

    def execute_program(self):
        for instruction in self.program:
            self.cpu.execute(self.cpu.match_instruction(instruction))
