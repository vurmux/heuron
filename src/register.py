#!/usr/bin/python

import json


class Register:

    def __init__(self, name, size=32):
        self.name = name
        self.size = size
        self.value = [0] * self.size
        
    def __str__(self):
        return (self.name +
                ' ' +
                ''.join(str(b) for b in self.value.__reversed__())
        )
    
    def reset(self):
        self.value = [0] * self.size
    
    def set_str_value(self, value):
        self.reset()
        if len(value) > len(self.value):
            raise LongValueError
        pos = 0
        for b in value[:: -1]:
            if b not in ('0', '1'):
                raise ValueError
            self.value[pos] = int(b)
            pos += 1

    def set_int_value(self, value):
        self.reset()
        bin_value = bin(value)[2: ]
        self.set_str_value(bin_value)


def load_from_file(filename):
    reg_file = open(filename)
    reg_str = reg_file.read()
    reg_file.close()
    registers = json.loads(reg_str)
    result = []
    for register in registers:
        result.append(Register(register['name'], register['size']))
    return result
    

if __name__ == '__main__':
    ax = Register('AX')
    ax.set_str_value('101101101')
    print ax
    ax.set_int_value(17)
    print ax
    ax.reset()
    print ax
    print [str(elem) for elem in load_from_file('../examples/x86/registers.json')]
