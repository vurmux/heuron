#!/usr/bin/python

import json


class Flag:

    def __init__(self, name, function):
        self.name = name
        self.state = False
        self.function = function

    def __str__(self):
        return self.name + ' ' + str(int(self.state))

    def set_joint(self, joint):
        self.joint = joint

    def set(self):
        self.state = True

    def reset(self):
        self.state = False


def load_from_file(filename):
    flag_file = open(filename)
    flag_str = flag_file.read()
    flag_file.close()
    flags = json.loads(flag_str)
    result = []
    for flag in flags:
        result.append(Flag(flag['name'], flag['function']))
    return result
