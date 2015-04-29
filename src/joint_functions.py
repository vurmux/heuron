#!/usr/bin/python


def set_flag(flag, flag_function, *ff_args):
    flag.state = flag_function(*ff_args)
