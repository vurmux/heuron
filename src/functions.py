#!/usr/bin/python

def func_xor(op1, op2, **kwargs):
    if len(op1) != len(op2):
        raise Exception
    res = [op1[i] ^ op2[i] for i in op1]
    return (res, {})
