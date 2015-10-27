#!/usr/bin/python

import json


class Register:
    """
    Implementation of general registers.
    Each register is represented by the list of bits.

    Class attributes:
    name - register name
    size - register size in bits, not bytes
    value - initial value of the register
    """

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
                result += hex(int('0b' + ''.join(
                    hex_list.__reversed__()), 2))[-1]
                hex_list = []
        if hex_list:
            result += hex(int('0b' + ''.join(hex_list.__reversed__()), 2))[-1]
        return result[::-1].upper()

    def binary_string(self):
        """
        String representation for a curses interface in format `name`:`value`.
        """
        return (self.name +
                ' ' +
                ''.join(str(b) for b in self.value.__reversed__()))

    def get_byte_list_value(self):
        """This function returns the list of bytes, not bits."""
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
        """Resets the register - all bits are set to 0."""
        self.value = [0] * self.size

    def set_str_value(self, value):
        """Sets the register to given value represented by a string."""
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
        """Sets the register to given value represented by an integer."""
        self.reset()
        bin_value = bin(value)[2:]
        self.set_str_value(bin_value)
        self.fit()

    def get_int_value(self):
        """Returns the value of the register converted to an integer."""
        return sum(self.value[i] * 2**i for i in range(len(self.value)))

    def set_joint(self, joint):
        """
        Bind this register with another element (read Joint class decription).
        """
        self.joint = joint

    def fit(self):
        """
        Checks the equality of the register size and the bit list length.
        If the size is more than the list length, add zero bytes to the list.
        If less - crop the bit list.
        """
        if len(self.value) > self.size:
            self.value = self.value[:self.size]
        if len(self.value) < self.size:
            self.value = self.value + [0] * (self.size - len(self.value))


def load_from_file(filename):
    """
    Reads a JSON file with registers in it, creates and returns a list of them.
    """
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
    print [
        str(elem)
        for elem in load_from_file('../examples/x86/registers.json')
    ]
