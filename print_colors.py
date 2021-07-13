"""Print color and cursor commands
# Note : make sure the following code snippets is in your code to 
enable ansi escape codes.

from colorama import init
init()

Colors are for foreground, background, bright foreground, bright background

Cursor Functions

def pr_cursor_up(lines):
def pr_cursor_down(lines):
def pr_cursor_forward(ch):
def pr_cursor_back(ch):
def pr_cursor_next_ln(line):
def pr_cursor_prev_ln(line):
def pr_cursor_horiz(ch):
def pr_cursor_pos(x, y):
def pr_erase_in_dsp(n):
def pr_erase_in_line(n):
def pr_scroll_up(n):
def pr_scroll_down(n):
def pr_cursor_save():
def pr_corsor_restore():
def pr_cursor_show():
def pr_cursor_hide():
"""

name_print_colors    = 'print_colors.py'
version_print_colors = '1.0.0'
date_print_colors    = '07/02/21'
author_print_colors  = 'Peter A. Hedlund'

LIB_NAME = name_print_colors
LIB_VERSION = version_print_colors
LIB_DATE = date_print_colors
LIB_AUTHOR = author_print_colors

# Print Color setting commands

# Normal Foreground
pr_f_black   = '\033[30m'
pr_f_red     = '\033[31m'
pr_f_green   = '\033[32m'
pr_f_yellow  = '\033[33m'
pr_f_blue    = '\033[34m'
pr_f_magenta = '\033[35m'
pr_f_cyan    = '\033[36m'
pr_f_white   = '\033[37m'

# Normal Background
pr_b_black   = '\033[40m'
pr_b_red     = '\033[41m'
pr_b_green   = '\033[42m'
pr_b_yellow  = '\033[43m'
pr_b_blue    = '\033[44m'
pr_b_magenta = '\033[45m'
pr_b_cyan    = '\033[46m'
pr_b_white   = '\033[47m'

# Bright Foreground
pr_fb_black   = '\033[90m'
pr_fb_red     = '\033[91m'
pr_fb_green   = '\033[92m'
pr_fb_yellow  = '\033[93m'
pr_fb_blue    = '\033[94m'
pr_fb_magenta = '\033[95m'
pr_fb_cyan    = '\033[96m'
pr_fb_white   = '\033[97m'

# Bright Background
pr_bb_black   = '\033[100m'
pr_bb_red     = '\033[101m'
pr_bb_green   = '\033[102m'
pr_bb_yellow  = '\033[103m'
pr_bb_blue    = '\033[104m'
pr_bb_magenta = '\033[105m'
pr_bb_cyan    = '\033[106m'
pr_bb_white   = '\033[107m'

# Reset color to default
pr_normal     = '\x1b[0m'
pr_bold       = '\x1b[1m'
pr_italic     = '\x1b[2m'
pr_underline  = '\x1b[3m'

def pr_cursor_up(lines):
    """ Move cursor up <lines> number of lines."""
    return(f'\x1b[{lines}A')


def pr_cursor_down(lines):
    """ Move cursor down <lines> number of lines."""
    return(f'\x1b[{lines}B')


def pr_cursor_forward(ch):
    """ Move cursor forward <ch> number of characters."""
    return(f'\x1b[{ch}C')


def pr_cursor_back(ch):
    """ Move cursor backward <ch> number of characters."""
    return(f'\x1b[{ch}D')


def pr_cursor_next_ln(line):
    """ Move cursor to the beginning of next line (lines) down."""
    return(f'\x1b[{line}E')


def pr_cursor_prev_ln(line):
    """ Move cursor to the beginning of next line (lines) up."""
    return(f'\x1b[{line}F')


def pr_cursor_horiz(ch):
    """Place cursor at position ch on current line."""
    return(f'\x1b[{ch}G')


def pr_cursor_pos(x, y):
    """Place cursor at horizontal x, vertical y."""
    return(f'\x1b[{x},{y}H')


def pr_erase_in_dsp(n):
    """Erase in display n is 0-3."""
    return(f'\x1b[{n}J')


def pr_erase_in_line(n):
    """Erease in line n is 0-3."""    
    return(f'\x1b[{n}K')


def pr_scroll_up(n):
    """ Scroll screen up n lines."""
    return(f'\x1b[{n}S')


def pr_scroll_down(n):
    """ Scroll screen down n lines"""
    return(f'\x1b[{n}T')


def pr_cursor_save():
    """Save current cursor position."""
    return(f'\x1b[s')


def pr_corsor_restore():
    """Restore cursor position to last saved."""
    return(f'\x1b[t')


def pr_cursor_show():
    """Show Cursor."""
    return('\x1b[?25h')


def pr_cursor_hide():
    """Hide cursor."""
    return('\x1b[?25l')
