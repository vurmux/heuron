#!/usr/bin/python


def func_xor(op1, op2):
    if len(op1) != len(op2):
        raise ValueError
    res = [op1[i] ^ op2[i] for i in range(len(op1))]
    return res
