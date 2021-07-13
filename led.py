#
# pylint: disable=unused-wildcard-import, method-hidden
#

""" LED library for round leds, 1, 2, 4 and 8 wide
    Single LED ONLY
    get_lib_version() Show numeric version of library.
    get_lib_full_version()  Show numeric version and library filename.
    make_led_1r   Makes a single led with a text label on the side
    set_led_1r    Sets the led to a color
    get_led_1r    Gets the current color of the led
    BANK LEDS ONLY
    make_led_2r  creates a bank of leds
    make_led_4r
    make_led_8r
    led2num_2r    Sets the leds in the bank the binary values
    led2num_4r          colors are light grey off and red on
    led2num_8r
    set_leds_r    sets the led to a color at an index
    get_leds_r    Gets the color of the led at an indes
"""

from tkinter import *
import tkinter as tk
name_led    = 'led.py'
version_led = '2.0.0'
date_led    = '02/05/21'
author_led  = 'Peter A. Hedlund'

LIB_NAME = name_led
LIB_VERSION = version_led
LIB_DATE = date_led
LIB_AUTHOR = author_led

# LIB_NAME = 'led.py'
# LIB_VERSION = "2.0.0"
# LIB_DATE = '02/05/21'


def get_lib_version():
    """Returns version information only."""
    return LIB_VERSION


def get_full_lib_version():
    """Returns version information and library name."""
    msg = get_lib_version()
    rs = 'Library Name : ' + LIB_NAME + '\nVersion : ' + msg
    rs = rs + '\nDate : ' + LIB_DATE
    rs = rs + '\nAuthor : ' + LIB_AUTHOR + '\n' 
    return rs


def make_led_1r(mf, label):
    """Creates a single round led widget with a label next to it. """
    lsize = 18

    scratch = Canvas()
    id = scratch.create_text((0, 0), text=label,anchor=tk.W)
    size = scratch.bbox(id)
    # size is a tuple: (x1, y1, x2, y2)
    # since x1 and y1 will be 0, x2 and y2 give the string width and height

    tw = size[2]-size[0]
    w = Canvas(mf,
               width=lsize + tw + 2,
               height=lsize)
    y = int(lsize) - 2
    led = w.create_oval(2, 2, y-2, y-2, fill='lightgrey')
    w.create_text(18, 8, text=label,anchor=tk.W)
    return w, led


def set_led_1r(w, led, color):
    """Sets the single led to the defined color. """
    w.itemconfig(led, fill=color)


def get_led_1r(c, led):
    """Gets the color of the led widget. """
    return c.itemcget(led, 'fill')


def make_led_r(mf, sz, leds, num):
    """Creates Multiple Round LEDs """    
    c = Canvas(mf, height=(sz * 2) + 2, width=sz * num + 2)
    c.create_rectangle(2, 2, sz*num, sz*2)
    for x in range(0, num):
        coord = sz * x + 3, 4, sz * (x + 1) - 2, sz - 2
        leds.insert(x, c.create_oval(coord, fill='lightgrey'))
        c.create_text(x * sz + 10, sz * 2 - 8, text=str(num - 1 - x))
#    c.tag_raise(g)
    leds.reverse()
    return c, leds


def leds2num_r(c, leds, val, num):
    """Set array of leds in one function. """
    for x in range(0, num):
        cl = 'lightgrey'
        if val & (1 << x):
            cl = 'red'
        set_leds_r(c, leds, x, cl)


def set_leds_r(c, leds, ndx, color):
    """Set individual leds in a multiple led widget """
    c.itemconfig(leds[ndx], fill=color)


def get_leds_r(c, leds, ndx):
    """Gets the status of one led in an array of leds. """
    return c.itemcget(leds[ndx], 'fill')


def make_led_2r(mf, sz, leds):
    """Makes 2 led's side by side """
    c, leds = make_led_r(mf, sz, leds, 2)
    return c, leds


def led2num_2r(c, leds, val):
    """Set individual leds in a multiple led widget """
    leds2num_r(c, leds, val, 2)


def make_led_4r(mf, sz, leds):
    """Makes 4 led's side by side """
    c, leds = make_led_r(mf, sz, leds, 4)
    return c, leds


def led2num_4r(c, leds, val):
    """Set individual leds in a multiple led widget """
    leds2num_r(c, leds, val, 4)


def make_led_8r(mf, sz, leds):
    """Makes 8 led's side by side """
    c, leds = make_led_r(mf, sz, leds, 8)
    return c, leds


def led2num_8r(c, leds, val):
    """Set individual leds in a multiple led widget """
    leds2num_r(c, leds, val, 8)


if __name__ == "__main__":
    from tkinter import *
    from tkinter import ttk


    def led_1_stat(level):
        if level:
            led1stat.configure(text='LED ON ')
        else:
            led1stat.configure(text='LED OFF')

    Red_c = 'red'
    Dark_c = 'lightgrey'


    def led_on():
        global lval
        if lval == 0:
            lval = 1
        set_led_1r(w, ind, Red_c)
        led_1_stat(get_led_1r(w, ind) == Red_c)
#        print lval
        led2num_2r(w2, ind2, lval % 4)
        led2num_4r(w4, ind4, lval % 16)
        led2num_8r(w8, ind8, lval % 256)
#        x = get_leds_r(w2, ind2, 0)
#        if x == Red_c:
#            print 'Bank2 bit 0 is on '
#        else:
#            print 'Bank2 bit 0 is off'
        lbl_count.config(text='Count=' + str(lval))
        lval = lval * 2
        lval = lval % 256


    def led_off():
        global lval
        set_led_1r(w, ind, Dark_c)
        led_1_stat(get_led_1r(w, ind) == Dark_c)
        led2num_2r(w2, ind2, 0)
        led2num_4r(w4, ind4, 0)
        led2num_8r(w8, ind8, 0)
        lval = 0
        lbl_count.config(text='Count=' + str(lval))


    root = Tk()
    #  prevent window resizing.
    root.resizable(0, 0)
    # Replace tk icon with your own.
    root.title('LED Test Program')

    mainframe = ttk.Frame(root, padding="3", height=300, width=300)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.grid_propagate(0)
    lval = 1
    w, ind = make_led_1r(mainframe, 'BUSY')
    w.grid(column=0, row=1)
    led1stat = ttk.Label(mainframe, text='LED OFF')
    led1stat.grid(column=1, row=1)
    leds2 = []
    w2, ind2 = make_led_2r(mainframe, 18, leds2)
    w2.grid(column=0, row=2)
    lbl_count = ttk.Label(mainframe, text='Count=0')
    lbl_count.grid(column=1, row=2)
    leds4 = []
    w4, ind4 = make_led_4r(mainframe, 18, leds4)
    w4.grid(column=0, row=3)
    leds8 = []
    w8, ind8 = make_led_8r(mainframe, 18, leds8)
    w8.grid(column=0, row=4)

    opn_prt = ttk.Button(mainframe, text="LED ON", command=led_on, width=15)
    opn_prt.grid(column=0, row=0, padx=15, pady=5)
    cse_prt = ttk.Button(mainframe, text="LED OFF", command=led_off, width=15)
    cse_prt.grid(column=1, row=0, padx=15, pady=5)
    s = 'Filename : Version [' + get_full_lib_version() + ']\n'
    lab2 = Label(mainframe,text=s)
    lab2.grid(column=0,row=5, columnspan=2)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()
