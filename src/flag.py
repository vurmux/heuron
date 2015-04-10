#!/usr/bin/python

import json


class Flag:
    
    def __init__(self, name):
        self.name = name
        self.state = False
        
    def __str__(self):
        return self.name + ' ' + str(int(self.state))
        
    def get_from_joint(self, joint):
        self.joint = joint
        self.joint.j_from = self

    def get_to_joint(self, joint):
        self.joint = joint
        self.joint.j_to = self


def load_from_file(filename):
    flag_file = open(filename)
    flag_str = flag_file.read()
    flag_file.close()
    flags = json.loads(flag_str)
    result = []
    for flag in flags:
        result.append(Flag(flag['name']))
    return result


ZF = Flag('ZF')
