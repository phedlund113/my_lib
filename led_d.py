#
# pylint: disable=unused-wildcard-import, method-hidden
#
"""LED Library for dual leds (top green if on or bottom red if off).

    get_lib_version() Show numeric version of library.
    get_lib_full_version()  Show numeric version and library filename.
    make_led_dr   Makes 2 round led's On and off
    make_led_ds   Makes 2 square led's On and Off
    set_led       Sets the leds on = green / gray  off = gray / red
    get_led       Gets the current state of the led.
    """
 

from tkinter import *
name_led_d    = 'led_d.py'
version_led_d = '1.0.0'
date_led_d    = '02/05/21'
author_led_d  = 'Peter A. Hedlund'

LIB_NAME = name_led_d
LIB_VERSION = version_led_d
LIB_DATE = date_led_d
LIB_AUTHOR = author_led_d

# LIB_NAME = 'led_d.py'
# LIB_VERSION = "1.0.0"
# LIB_DATE = '02/05/21'

def get_lib_version(): 
    """    Returns version information only. """
    return LIB_VERSION 


def get_full_lib_version():
    """Returns version information and library name.""" 
    msg = get_lib_version()
    rs = 'Library Name : ' + LIB_NAME + '\nVersion : ' + msg
    rs = rs + '\nDate : ' + LIB_DATE
    rs = rs + '\nAuthor : ' + LIB_AUTHOR + '\n' 
    return rs

def make_led_dr(mf):
    """Creates 2 round leds one on top of the other. 
      The top led is grey for off and green for on. 
      The bottom led is grey for on or red for off"""
    lsize = 18

    scratch = Canvas()
    id = scratch.create_text((0, 0), text='on')
    size = scratch.bbox(id)
    # size is a tuple: (x1, y1, x2, y2)
    # since x1 and y1 will be 0, x2 and y2 give the string width and height

    tw = size[2]-size[0]
    w = Canvas(mf,
               width=lsize + tw + 2,
               height=lsize * 2)
    leda = w.create_oval(2, 5, 10 ,15, fill='lightgrey')
    ledb = w.create_oval(2, 20,10, 30, fill='red')
    w.create_text(22, 9, text='ON')
    w.create_text(22, 24, text='OFF')
    return w, leda, ledb


def make_led_ds(mf):
    """Creates 2 square leds one on top of the other. 
      The top led is grey for off and green for on. 
      The bottom led is grey for on or red for off"""
    lsize = 18

    scratch = Canvas()
    id = scratch.create_text((0, 0), text='on')
    size = scratch.bbox(id)
    # size is a tuple: (x1, y1, x2, y2)
    # since x1 and y1 will be 0, x2 and y2 give the string width and height

    tw = size[2]-size[0]
    w = Canvas(mf,
               width=lsize + tw + 2,
               height=lsize * 2)
    leda = w.create_rectangle(2, 5, 10 ,15, fill='lightgrey')
    ledb = w.create_rectangle(2, 20,10, 30, fill='red')
    w.create_text(22, 9, text='ON')
    w.create_text(22, 24, text='OFF')
    return w, leda, ledb


def set_led(w, led1, led2, state):
    """Turns the led on or off (state) If on top, led is green bottom is grey
       if off, top led is grey and bottom is red."""
    if state == 1:
        col1 = 'green'
        col2 = 'lightgrey'
    else:
        col1 = 'lightgrey'
        col2 = 'red'
    w.itemconfig(led1, fill=col1)
    w.itemconfig(led2, fill=col2)


def get_led(c, led):
    """Returns the status of the led."""
    return c.itemcget(led, 'fill')


#
# Testing Library Function
#


if __name__ == "__main__":
    from tkinter import *
    from tkinter import ttk

    print("you are here")

    def test_led_1_stat(level):
        if level:
            led1stat.configure(text='LED ON ')
        else:
            led1stat.configure(text='LED OFF')

    Red_c = 'red'
    Dark_c = 'lightgrey'


    def test_led_on():
        set_led(w, ind1, ind2, 1)
        test_led_1_stat(get_led(w, ind1) == 'green')


    def test_led_off():
        set_led(w, ind1, ind2, 0)
        test_led_1_stat(get_led(w, ind1) == 'green')
    
    
    def test_power():
        if pwr.get() == 0:
            set_led(w2, ind3, ind4, 1)
            pwr.set(1)
        else:
            set_led(w2, ind3, ind4, 0)
            pwr.set(0)
            set_led(w3, ind3, ind4, 0)
            shields.set(0)
            set_led(w4, ind3, ind4, 0)
            impulse.set(0)
            set_led(w5, ind3, ind4, 0)
            warp.set(0)


    def test_shieldp():
        if pwr.get() == 0:
            return
        if shields.get() == 0:
            set_led(w3, ind3, ind4, 1)
            shields.set(1)
        else:
            set_led(w3, ind3, ind4, 0)
            shields.set(0)


    def test_impulsep():
        if pwr.get() == 0:
            return
        if impulse.get() == 0:
            set_led(w4, ind3, ind4, 1)
            impulse.set(1)
        else:
            set_led(w4, ind3, ind4, 0)
            impulse.set(0)


    def test_warpp():
        if pwr.get() == 0:
            return
        if warp.get() == 0:
            set_led(w5, ind3, ind4, 1)
            warp.set(1)
        else:
            set_led(w5, ind3, ind4, 0)
            warp.set(0)


    root = Tk()
    #  prevent window resizing.
    root.resizable(0, 0)
    # Replace tk icon with your own.
    root.title('Dual LED Test Program DEMO')
    pwr = IntVar()
    shields = IntVar()
    impulse = IntVar()
    warp = IntVar()
    pwr.set(0)
    impulse.set(0)
    shields.set(0)
    warp.set(0)
    mainframe = ttk.Frame(root, padding="3", height=400, width=300)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.grid_propagate(0)
    
    w, ind1, ind2 = make_led_dr(mainframe)
    w.grid(column=0, row=1)
    led1stat = ttk.Label(mainframe, text='LED OFF')
    led1stat.grid(column=1, row=1)

    opn_prt = ttk.Button(mainframe, text="LED ON", command=test_led_on, width=15)
    opn_prt.grid(column=0, row=0, padx=15, pady=5)
    cse_prt = ttk.Button(mainframe, text="LED OFF", command=test_led_off, width=15)
    cse_prt.grid(column=1, row=0, padx=15, pady=5)
    s = 'Filename : Version [' + get_full_lib_version() + ']\n'
    lab2 = Label(mainframe,text=s)
    lab2.grid(column=0,row=5, columnspan=2)
    btns = ttk.Button(mainframe, text='Shields', command=test_shieldp)
    btns.grid(column=0, row=6, sticky='e')
    w3, ind3,ind4 = make_led_ds(mainframe)
    w3.grid(column=1, row=6, sticky='w')
    btni = ttk.Button(mainframe, text='Impulse', command=test_impulsep)
    btni.grid(column=0, row=7, sticky='e')
    w4, ind3,ind4 = make_led_ds(mainframe)
    w4.grid(column=1, row=7, sticky='w')
    btnw = ttk.Button(mainframe, text='Warp', command=test_warpp)
    btnw.grid(column=0, row=8, sticky='e')
    w5, ind3,ind4 = make_led_ds(mainframe)
    w5.grid(column=1, row=8, sticky='w')
    btn = ttk.Button(mainframe, text='Power', command=test_power)
    btn.grid(column=0, row=9, sticky='e')
    w2, ind3,ind4 = make_led_dr(mainframe)
    w2.grid(column=1, row=9, sticky='w')
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()
