#!/usr/bin/python

import curses, traceback, string, os, time, json
import sys
sys.path.append('./src/')

import cpu
import flag
import flag_functions
import functions
import instruction
import register
import memory

def create_subwindow(x, y, w, h, border_list, header):
    res = stdscr.subwin(12,14,0,0)
    res = stdscr.subwin(h,w,y,x)
    b1, b2, b3, b4, b5, b6, b7, b8 = border_list
    res.border(b1, b2, b3, b4, b5, b6, b7, b8)
    #inbox_w = w - 2
    res.addstr(1, 1, header)
    res.hline(2, 1, chr(45), w-2)
    return res

def create_suface():
    reg_window = create_subwindow(
        0, 0, 18, 12,
        [0, 0, 0, 0,
         0, curses.ACS_TTEE, curses.ACS_PLUS, curses.ACS_PLUS],
        'REGISTERS')
    flags_window = create_subwindow(
        0, 11, 18, 12,
        [0, 0, 0, 0,
         curses.ACS_PLUS, curses.ACS_PLUS, 0, curses.ACS_BTEE],
        'FLAGS'
    )
    instr_window = create_subwindow(
        17, 0, 20, 12,
        [0, 0, 0, 0,
         curses.ACS_TTEE, curses.ACS_TTEE, curses.ACS_PLUS, curses.ACS_RTEE],
        'INSTRUCTIONS'
    )
    asm_window = create_subwindow(
        17, 11, 20, 12,
        [0, 0, 0, 0,
         curses.ACS_PLUS, curses.ACS_RTEE, curses.ACS_BTEE, curses.ACS_BTEE],
        'ASSEMBLER'
    )
    memo_window = create_subwindow(
        36, 0, 43, 23,
        [0, 0, 0, 0,
         curses.ACS_TTEE, 0, curses.ACS_BTEE, 0],
        'MEMO DUMP'
    )
    return (reg_window, flags_window, instr_window, asm_window, memo_window)

def update_registers(reg_window, registers):
    i = 3
    for reg in registers:
        reg_window.addstr(i, 1, reg + ' ' + str(registers[reg]))
        i += 1
        
def update_flags(flags_window, flags):
    i = 3
    for flag in flags:
        flags_window.addstr(i, 1, str(flags[flag]))
        i += 1

def refresh_cpu_screen(cpu, screen, **kwargs):
    registers = cpu.registers
    flags = cpu.flags
    update_registers(kwargs['reg_window'], registers)
    update_flags(kwargs['flags_window'], flags)
    screen.refresh()


if __name__=='__main__':
    try:
        stdscr=curses.initscr()
        curses.noecho() ; curses.cbreak()
        screen = stdscr.subwin(23, 79, 0, 0)
        screen.box()
        screen.refresh()
        stdscr.keypad(1)

        (reg_window,
         flags_window,
         instr_window,
         asm_window,
         memo_window) = create_suface()

        cpu_registers = register.load_from_file('./examples/x86/registers.json')
        cpu_instructions = instruction.load_from_file('./examples/x86/instructions.json')
        cpu_flags = flag.load_from_file('./examples/x86/flags.json')
        cpu_memory = memory.MemoryPage(2048)
        cpu_memory.write_ord(0, eval(open('./examples/memory.txt').read()))

        cpu = cpu.CPU(
            name='x86',
            instructions=cpu_instructions,
            flags=cpu_flags,
            registers=cpu_registers,
            ip_register='EIP',
            memory=cpu_memory
        )
            
        program = [
            "cpu.registers['EAX'].set_int_value(415)",
            "cpu.registers['EBX'].set_int_value(342)",
            "cpu.execute('XOR', cpu.registers['EAX'], cpu.registers['EBX'])",
            "cpu.execute('XOR', cpu.registers['EAX'], cpu.registers['EAX'])",
        ]
        
        for instruction in program:
            eval(instruction)
            refresh_cpu_screen(
                cpu,
                screen,
                reg_window=reg_window,
                flags_window=flags_window
            )
            c = screen.getch()

        stdscr.keypad(0)
        curses.echo() ; curses.nocbreak()
        curses.endwin()
    except:
        stdscr.keypad(0)
        curses.echo() ; curses.nocbreak()
        curses.endwin()
        traceback.print_exc()
