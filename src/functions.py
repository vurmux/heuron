#!/usr/bin/python


# -- General functions ---

def list_to_int(lst):
    return sum(lst[i] * 2**i for i in range(len(lst)))

def int_to_list(value):
    bin_value = bin(value)[2: ]
    result = []
    for b in bin_value[:: -1]:
        result.append(int(b))
    return result

# --- ALU functions ---

def func_xor(op1, op2):
    if len(op1) != len(op2):
        raise ValueError
    res = [op1[i] ^ op2[i] for i in range(len(op1))]
    return res

def func_or(op1, op2):
    if len(op1) != len(op2):
        raise ValueError
    res = [op1[i] | op2[i] for i in range(len(op1))]
    return res

def func_and(op1, op2):
    if len(op1) != len(op2):
        raise ValueError
    res = [op1[i] & op2[i] for i in range(len(op1))]
    return res

def func_nop():
    pass

def func_add(op1, op2):
    int_op1 = list_to_int(op1)
    int_op2 = list_to_int(op2)
    int_result = int_op1 + int_op2
    return int_to_list(int_result)

def func_sub(op1, op2):
    int_op1 = list_to_int(op1)
    int_op2 = list_to_int(op2)
    int_result = int_op1 - int_op2
    return int_to_list(int_result)

def func_mul(op1, op2):
    int_op1 = list_to_int(op1)
    int_op2 = list_to_int(op2)
    int_result = int_op1 * int_op2
    return int_to_list(int_result)

def func_div(op1, op2):
    int_op1 = list_to_int(op1)
    int_op2 = list_to_int(op2)
    int_result = int(float(int_op1) / int_op2)
    return int_to_list(int_result)

def func_inc(op):
    int_op = list_to_int(op)
    int_result = int_op + 1
    return int_to_list(int_result)

def func_dec(op):
    int_op = list_to_int(op)
    int_result = int_op - 1
    return int_to_list(int_result)

def func_jmp(ip, label):
    ip.set_int_value(int(label))
