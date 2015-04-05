#!/usr/bin/python

import flag-functions as ff
import flag


def bound(function, flag):
    def decorator(func):
        def wrapper(op1, op2):
            result = func(op1, op2)
            flag.state = function(result)
            return result
        return wrapper
    return decorator
    

@bound(ff.zero_function, ZF)
def func_xor(op1, op2):
    if len(op1) != len(op2):
        raise ValueError
    res = [op1[i] ^ op2[i] for i in op1]
    return (res, {})
