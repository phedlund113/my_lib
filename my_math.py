#
# pylint: disable=unused-wildcard-import, method-hidden
#
"""My_Math.py My math routines 
    get_lib_version() Show numeric version of library.
    get_lib_full_version()  Show numeric version and library filename.
    inside()       returns true / false depening if value is within limits. 
    outsied()      returns true / false depending if value is ouside limits
    re-scale()     returns scaled value based on limits and new range
    c_to_f()       returns c from f
    f_to_c()       returns f from c
    sec_2_hms()    returns hh:mm:ss string from seconds passed
    current_time() returns hh:mm:ss string of current time
    filter_float() returned filtered value based on coeficcent.
"""
import time

name_my_math    = 'my_math.py'
version_my_math = '1.2.0'
date_my_math    = '05/19/21'
author_my_math  = 'Peter A. Hedlund'

LIB_NAME = name_my_math
LIB_VERSION = version_my_math
LIB_DATE = date_my_math
LIB_AUTHOR = author_my_math
    
# LIB_NAME = 'my_math.py'
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

def inside(lo, hi, ck):
    """Checks that ck is within lo to hi range returns 1 if true 0 if false"""
    if lo < ck and hi > ck:
        return 1
    return 0


def outside(lo, hi, ck):
    """Checks that ck is ouside of lo to hi range returns 1 if true 0 if
    false"""
    if lo > ck and hi < ck:
        return 1
    return 0


def re_scale(lo, hi, rng, val):
    """Scale value val to range rng bases on lo and hi limits """
    x = (hi - lo) / rng
    ov = val / x
    return ov


def f_to_c(f_val):
    """ Returns  celsius from fahrenheit"""
    return (f_val-32) * 5.0 / 9.0


def c_to_f(c_val):
    """ Returns  fahrenheit from celsius"""
    return (c_val * 9 / 5) + 32.0


def sec_2_hms(seconds):
    """Convert seconds to HH:MM:SS string"""
    seconds = int(seconds)
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return f'{h:02}:{m:02}:{s:02}'


def current_time():
    """returns current time in a string HH:MM:SS."""
    tm = time.localtime()
    str1 = time.strftime('%H:%M:%S',tm)
    return str1


def filter_float( old_value, new_value, filter_coe):
    """ Filter Function  (old value, new value, filter coeffecient)"""
    if filter_coe >= 1.0:
        output = old_value
    else:
        if filter_coe <= 0.0:
            output = new_value
        else:
            output = ( old_value * filter_coe ) + ( new_value * ( 1  - filter_coe ) )
    return output

#
# Testing Library Function
#


if __name__ == "__main__":
    from tkinter import *
    from tkinter import ttk
    import mylib.scrn_log as scrn

    def send_str(txt, wstr):
        txt.insert(END,wstr)
        txt.index(END)
        txt.see(END)
        txt.update()

    root = Tk()
    #  prevent window resizing.
    root.resizable(0, 0)
    # Replace tk icon with your own.
    root.title('Dual LED Test Program DEMO')
    mainframe = ttk.Frame(root, padding="3", height=420, width=440)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.grid_propagate(0)
    raw=[10,15,5,20,20,10]
    log = scrn.scrn_log(mainframe, 50, 23, 'black', 'light grey', 0, 0, 2, 10)
    log.log_scrn_color('MyMath Library Test\n', 'green')
    log.log_scrn_color('[TESTING Inside]\n', 'blue')
    log.log_scrn(f'15 inside range 10-20 {inside(10,20,15)} (expect 1)\n')
    log.log_scrn(f'25 inside range 10-20 {inside(10,20,25)} (expect 0)\n')
    log.log_scrn_color('[TESTING Outside]\n', 'blue')
    log.log_scrn(f'25 outside range 10-20 {outside(10,20,25)} (expect 1)\n')
    log.log_scrn(f'15 outside range 10-20 {outside(10,20,15)} (expect 0)\n')
    log.log_scrn_color('[TESTING re_scale]\n', 'blue')
    log.log_scrn(f'45 re_scaled from range 0-90 {re_scale(0,90,50,45)}'
            ' (expect 25)\n')
    log.log_scrn(f'22.5 re_scaled from range 0-90 {re_scale(0,90,50,22.5)}'
            ' (expect 12.5)\n')
    log.log_scrn(f'67.5 re_scaled from range 0-90 {re_scale(0,90,50,67.5)}'
            ' (expect 37.5)\n')
    log.log_scrn_color('[Testing sec_to_hms]\n', 'blue')
    log.log_scrn(' 4166 seconds is 01:09:26\n')
    st = sec_2_hms(4166)
    log.log_scrn(f'Return of sec_2_hms(4166) is {st}\n')
    log.log_scrn_color('[Testing current_time]\n', 'blue')
    log.log_scrn(f'Current time is {current_time()}\n')
    log.log_scrn_color('[Testing filter_float]\n', 'blue')
                
    log.log_scrn(f'Raw Data = {raw}\n')
    filt = []
    filt.append(0)
    
    for x in range(1,len(raw)):
        filt.append(filter_float(filt[x-1], raw[x], .80))
    log.log_scrn(f'Filtering with a coeffiencent of .80\n')
    log.log_scrn(f'Filtered data = \n         ')
    for x in range(0,len(filt)):
        b = int(filt[x]*100) / 100
        log.log_scrn(f'{b}, ')
    
    log.log_scrn(f'\n')
    log.log_scrn(f'expected 0.0, 2.99, 3.39, 6.71, 9.37, 9.5\n')
    
    for child in root.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()

