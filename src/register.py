#!/usr/bin/python

import json


class Register:

    def __init__(self, name, size=32):
        self.name = name
        self.size = size
        self.value = [0] * self.size
        
    def __str__(self):
        hex_list = []
        result = ''
        for b in self.value:
            if len(hex_list) < 3:
                hex_list.append(str(b))
            else:
                hex_list.append(str(b))
                result += hex(int('0b' + ''.join(hex_list.__reversed__()), 2))[-1]
                hex_list = []
        if hex_list:
            result += hex(int('0b' + ''.join(hex_list.__reversed__()), 2))[-1]
        return result[::-1].upper()
                
    def binary_string(self):
        return (self.name +
                ' ' +
                ''.join(str(b) for b in self.value.__reversed__())
        )
    
    def get_byte_list_value(self):
        byte = 0
        byte_len = 0
        result = []
        for b in self.value:
            if byte_len < 7:
                byte += b * 2**(byte_len)
                byte_len += 1
            else:
                result.append(int(byte))
                byte_len = 0
                byte = 0
        if byte_len:
            result.append(int(byte))
        return result
    
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
        self.fit()

    def set_int_value(self, value):
        self.reset()
        bin_value = bin(value)[2: ]
        self.set_str_value(bin_value)
        self.fit()
        
    def get_int_value(self):
        return sum(self.value[i] * 2**i for i in range(len(self.value)))

    def set_joint(self, joint):
        self.joint = joint
        
    def fit(self):
        if len(self.value) > self.size:
            self.value = self.value[:self.size]
        if len(self.value) < self.size:
            self.value = self.value + [0] * (self.size - len(self.value))


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
