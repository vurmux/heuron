#!/usr/bin/python


import string
import functions

class MemoryPage:
    
    def __init__(self, size):
        self.size = size
        self.value = [0] * size
        
    def __str__(self):
        width = 64
        pos = 0
        result = ''
        for byte in self.value:
            # [:-5] cuts \t\n\r\x0b\x0c
            result += chr(byte) if chr(byte) in string.printable[:-5] else '.'
            pos += 1
            if pos == width:
                result += '\n'
                pos = 0
        return result

    def list(self):
        width = 40
        pos = 0
        result = []
        temp = ''
        for byte in self.value:
            # [:-5] cuts \t\n\r\x0b\x0c
            temp += chr(byte) if chr(byte) in string.printable[:-5] else '.'
            pos += 1
            if pos == width:
                result.append(temp)
                temp = ''
                pos = 0
        return result

    def write_chr(self, address=0, data_string=''):
        writing_string = data_string[:self.size-address-len(data_string)]
        pos = address
        for char in writing_string:
            self.value[pos] = ord(char)
            pos += 1
            
    def write_ord(self, address=0, data_list=[]):
        writing_list = data_list[:self.size-address]
        pos = address
        for byte in writing_list:
            self.value[pos] = byte
            pos += 1
            
    def get_list(self, address, length):
        return self.value[address: address+length]
    
    def get_int(self, address, length):
        target_list = self.get_list(address, length)
        return sum(target_list[::-1][i] * 255**i for i in range(len(target_list)))
    
    def get_bin(self, address, byte_length):
        return functions.int_to_list(self.get_int(address, byte_length))


class Memory:
    
    def __init__(page_size=4096):
        self.page_size = page_size
        self.pages = {}
    
    def create_page(page_id):
        self.pages[page_id] = MemoryPage(self.page_size)
    
    def write_page(page_id, data_string):
        pass

    def print_page(page_id):
        return


if __name__ == '__main__':
    page = MemoryPage(128)
    print page
    page.write_chr(120, '1234567890')
    page.write_ord(5, [23, 42, 89])
    print page.get_list(2, 5)
    print page.get_int(4, 3)
    print page
