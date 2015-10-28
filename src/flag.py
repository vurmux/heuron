#!/usr/bin/python

import json


class Flag:
    """
    Implementation of simple 2-state flags.

    Class attributes:
    name - flag name
    state - flag state: True or False
    function - joint function of current flag (read Joint class description)
    """

    def __init__(self, name, function):
        self.name = name
        self.state = False
        self.function = function
 
    def __str__(self):
        return self.name + ' ' + str(int(self.state))
 
    def set_joint(self, joint):
        """
        Bind this flag with another element (read Joint class decription).
        """
        self.joint = joint

    def set(self):
        """Sets the flag state to True"""
        self.state = True

    def reset(self):
        """Resets the flag and sets it to False"""
        self.state = False


def load_from_file(filename):
    """
    Reads a JSON file with flags in it, creates and returns a list of them.
    """
    flag_file = open(filename)
    flag_str = flag_file.read()
    flag_file.close()
    flags = json.loads(flag_str)
    result = []
    for flag in flags:
        result.append(Flag(flag['name'], flag['function']))
    return result
