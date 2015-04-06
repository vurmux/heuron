#!/usr/bin/python


class Flag:
    
    def __init__(self, name):
        self.name = name
        self.state = False
        
    def __str__(self):
        return self.name + ' ' + str(int(self.state))


ZF = Flag('ZF')
