#!/usr/bin/python


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self, element):
        if not self.stack:
            raise ValueError
        element = self.stack.pop()
