"""Seven Segment display This library consists of 7 segment line characters
as well as 7 segment led characters. Digits 0 -9 and a-f are supported along 
with characters 16-22 which are individual segments. (16 is a, 17 is b ... )

    get_lib_version() Show numeric version of library.
    get_lib_full_version()  Show numeric version and library filename.
    class Digit() creates line type 7 segment display character
        show()  displays numeric value in character
    class Counter() creates line type 7 segment display with dig characters 
        and base of 10 or 16 (decimal or hex)
        num() displays the number on the counter display 1000 on a 3 digit
        display is 000 
    Class Counter_Dp() creates a counter of dig characters with a decimal
        point at char dp and dp+1  
        num() displays the number on the counter display with the whole number
            on the left side of the decimal point and the fractional number
            on the right side of the decimal point. 
            display is 000
    class Clock() Creates a 7 segment line clock mode=0 = HH:MM mode=1
        = HH:MM:SS. 
        num() Pass H, M and S to routinte to dispay time
    class Digit_Led() creates led type 7 segment display character
        show()  displays numeric value in character 
    class Counter_Led() creates Led type 7 segment display with dig 
        characters and base of 10 or 16 (decimal or hex)
        num() displays the number on the counter display 1000 on a 3 digit
            display is 000
    Class Counter_Led_Dp() creates a counter of dig characters with a decimal
        point at char dp and dp+1  
        num() displays the number on the counter display with the whole number
            on the left side of the decimal point and the fractional number
            on the right side of the decimal point. 
            display is 000
    class Clock_Led() Creates a 7 segment LED clock mode=0 = HH:MM mode=1
        = HH:MM:SS. 
        num() Pass H, M and S to routinte to dispay time
        """
'''Seven segment display of hex digits.'''
import tkinter as tk

# DONE Add Clock face to LED Display
# DONE Add Update_time to LED_Clock
# DONE Add Clock face to line display
# DONE Add update_time to Line display clock
# DONE Add Counter with Decimal Point to LED Display
# DONE Add Show to decimal LED display
# DONE Add Counter with Decimal Point to Line Display
# DONE Add Show to decimal line display

segments = (
    (0, 3, 4, 0, 16, 0, 20, 3, 16, 7, 4, 7), # a
    (20, 4, 23, 8, 23, 20, 20, 24, 17, 20, 17, 8 ), # b
    (20,24, 23, 28, 23, 40,20, 44, 17, 40, 17, 28), # c
    (20,45, 16, 48, 4, 48, 0, 45, 4, 42, 16,42), # d
    (0, 44, -3, 40, -3, 28, 0, 24, 3, 28, 3, 40), # e
    (0, 4, 3, 8, 3, 20, 0, 24, -3, 20, -3, 8), #f
    (20, 24, 16, 21, 4, 21, 0, 24, 4, 27, 15, 27), #g
)

# Order 7 segments clockwise from top left, with crossbar last.
# Coordinates of each segment are (x0, y0, x1, y1) 
# given as offsets from top left measured in segment lengths.

offsets = (
    (0, 0, 1, 0),  # top
    (1, 0, 1, 1),  # upper right
    (1, 1, 1, 2),  # lower right
    (0, 2, 1, 2),  # bottom
    (0, 1, 0, 2),  # lower left
    (0, 0, 0, 1),  # upper left
    (0, 1, 1, 1),  # middle
)
# Segments used for each digit; 0, 1 = off, on.
digits = (
    (1, 1, 1, 1, 1, 1, 0),  # 0
    (0, 1, 1, 0, 0, 0, 0),  # 1
    (1, 1, 0, 1, 1, 0, 1),  # 2
    (1, 1, 1, 1, 0, 0, 1),  # 3
    (0, 1, 1, 0, 0, 1, 1),  # 4
    (1, 0, 1, 1, 0, 1, 1),  # 5
    (1, 0, 1, 1, 1, 1, 1),  # 6
    (1, 1, 1, 0, 0, 0, 0),  # 7
    (1, 1, 1, 1, 1, 1, 1),  # 8
    (1, 1, 1, 1, 0, 1, 1),  # 9
    (1, 1, 1, 0, 1, 1, 1),  # 10=A
    (0, 0, 1, 1, 1, 1, 1),  # 11=b
    (1, 0, 0, 1, 1, 1, 0),  # 12=C
    (0, 1, 1, 1, 1, 0, 1),  # 13=d
    (1, 0, 0, 1, 1, 1, 1),  # 14=E
    (1, 0, 0, 0, 1, 1, 1),  # 15=F
    (1, 0, 0, 0, 0, 0, 0),  # Top horiz Bar
    (0, 1, 0, 0, 0, 0, 0),  # Top Right Vert
    (0, 0, 1, 0, 0, 0, 0),  # Bot right Vert
    (0, 0, 0, 1, 0, 0, 0),  # Bot horiz
    (0, 0, 0, 0, 1, 0, 0),  # Bot Left Vert
    (0, 0, 0, 0, 0, 1, 0),  # Top Left Vert
    (0, 0, 0, 0, 0, 0, 1),  # Ctr horiz bar
)
name_seven_seg    = 'seven_seg.py'
version_seven_seg = '1.0.0'
date_seven_seg    = '02/05/21'
author_seven_seg  = 'Peter A. Hedlund'

LIB_NAME = name_seven_seg
LIB_VERSION = version_seven_seg
LIB_DATE = date_seven_seg
LIB_AUTHOR = author_seven_seg

# LIB_NAME = 'seven_seg.py'
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

# 
# 7 Segment LED DISPLAY SECTION
#
class Digit_Led:
    """ Creates a 7 segment led type display (one character)"""
    def __init__(self, canvas, *, x=10, y=10, length=20, width=3, 
                myfill='red'):
        self.canvas = canvas
        self.segs7 = []
        for x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6 in segments:
            self.segs7.append(canvas.create_polygon(
                x+x1, y+y1, x+x2, y+y2, x+x3, y+y3, x+x4, y+y4, x+x5, y+y5,
                x+x6, y+y6,x+x1, y+y1, fill = myfill, state='hidden'))


    def show(self, num):
        """ Show the number num on the single character led 7 segment display
        """
        for iid, on in zip(self.segs7, digits[num]):
            self.canvas.itemconfigure(iid, state = 'normal' if on else 'hidden')

    
class Counter_Led:
    """Creates a set of 7 segment led style (dig = num characters)"""
    def __init__(self, canvas, *, x=10, y=10, dig=4, base=10, myfill='red'):
        self.canvas = canvas
        self.dig = dig 
        self.base = base
        self.poss=[]
        for w in range(0, self.dig):
            self.poss.append(Digit_Led(canvas, x = w*30 + x, y=y, 
                            myfill=myfill))


    def num(self, n):
        """ Shows the number on counter created if number > digits
        number wraps around 3 digits 1000 is 000, 1001 is 001"""
        div = (1000000, 100000, 10000,1000,100,10,1)
        div_h = (16777216, 1048576, 65536, 4096, 256, 16, 1)
        st = len(div) - self.dig
        for q in range(0, self.dig):
            if self.base == 16:
                self.poss[q].show(int(n/div_h[st+q]) % 16)
            else:
                self.poss[q].show(int(n/div[st+q]) % 10)
            
class Counter_Led_Dp:
    """Creates a set of 7 segment led style (dig = num characters, dp 
    location of decimal point)"""
    def __init__(self, canvas, *, x=10, y=10, dig=4, base=10, dp=1, 
                myfill='red'):
        self.canvas = canvas
        self.dig = dig 
        self.base = base
        self.dp = dp
        self.poss=[]
        for w in range(0, self.dig):
            self.poss.append(Digit_Led(canvas, x = w*34 + x, y=y, myfill=myfill))
        if dp > 0:
            x1 = x-10 + ((dig - dp) * 34)
            x2 = x1 + 5
            canvas.create_oval(x1, y + 31, x2, y + 37,  fill=myfill) 


    def num(self, n):
        """ Shows the number on counter created if number > digits
        number wraps around 3 digits 1000 is 000, 1001 is 001"""
        mul = (10,100,1000,10000)
        i = int(n)
        r = n - i 
        ad = int(r * mul[self.dp-1])
        v = '00000000' + str(i) + str(ad)
        ln = len(v)
        for x in range(0, self.dig):
            self.poss[x].show(int(v[ln - self.dig + x]))



class Clock_Led:
    """ Creates a 7 segment line clock in either HH:MM or HH:MM:SS. 
    mode 0 = HH:MM mode 1 = HH:MM:SS. """
    def __init__(self,canvas, *, x=10, y=10, mode=0, myfill='red'):
        self.canvas = canvas
        self.mode = mode 
        self.poss=[]
        dig = 4
        if self.mode==1:
            dig = 6
        for w in range(0, dig):
            self.poss.append(Digit_Led(canvas, x = w*34 + x, y=y, 
                myfill=myfill))

        x1 = x-10 + ((4 - 2) * 34)
        x2 = x1 + 5
        canvas.create_oval(x1, y + 11, x2, y + 17,  fill=myfill) 
        canvas.create_oval(x1, y + 31, x2, y + 37,  fill=myfill) 
        if mode == 1:
            x1 = x-10 + ((dig - 2) * 34)
            x2 = x1 + 5
            canvas.create_oval(x1, y + 11, x2, y + 17,  fill=myfill) 
            canvas.create_oval(x1, y + 31, x2, y + 37,  fill=myfill) 


    def num(self, h,m,s=0):
        """ Shows the time (Hh:MM:SS) """

        self.poss[0].show(int(h/10) % 10)
        self.poss[1].show((h) % 10)
        self.poss[2].show(int(m/10) % 10)
        self.poss[3].show(m % 10)

        if self.mode == 1:
            self.poss[4].show(int(s/10) % 10)
            self.poss[5].show(s % 10)

# 
# 7 Segment Line DISPLAY SECTION
#

class Digit:
    """ Creates a 7 segment line type display (one character)"""
    def __init__(self, canvas, *, x=10, y=10, length=23, width=3, 
                myfill='green'):
        self.canvas = canvas
        l = length
        self.segs = []
        for x0, y0, x1, y1 in offsets:
            self.segs.append(canvas.create_line(
                x + x0*l, y + y0*l, x + x1*l, y + y1*l,
                width=width, state = 'hidden', fill=myfill))


    def show(self, num):
        """ Show the number num on the single character line 7 segment display
        """
        for iid, on in zip(self.segs, digits[num]):
            self.canvas.itemconfigure(iid, state = 'normal' if on else 'hidden')


class Counter:
    """Creates a set of 7 segment line style (dig = num characters)"""
    def __init__(self, canvas, *, x=10, y=10, dig=4, base=10, myfill='green'):
        self.canvas = canvas
        self.dig = dig 
        self.base = base
        self.poss=[]
        for w in range(0, self.dig):
            self.poss.append(Digit(canvas, x = w*30 + x, y=y, myfill=myfill))


    def num(self, n):
        """ Shows the number on counter created if number > digits
        number wraps around 3 digits 1000 is 000, 1001 is 001"""
        div = (1000000, 100000, 10000,1000,100,10,1)
        div_h = (16777216, 1048576, 65536, 4096, 256, 16, 1)
        st = len(div) - self.dig
        for q in range(0, self.dig):
            if self.base == 16:
                self.poss[q].show(int(n/div_h[st+q]) % 16)
            else:
                self.poss[q].show(int(n/div[st+q]) % 10)


class Counter_Dp:
    """Creates a set of 7 segment line style (dig = num characters, dp 
    location of decimal point)"""
    def __init__(self, canvas, *, x=10, y=10, dig=4, base=10, dp=1, 
                myfill='green'):
        self.canvas = canvas
        self.dig = dig 
        self.base = base
        self.dp = dp
        self.poss=[]
        for w in range(0, self.dig):
            self.poss.append(Digit(canvas, x = w*34 + x, y=y, myfill=myfill))
        if dp > 0:
            x1 = x-8 + ((dig - dp) * 34)
            x2 = x1 + 5
            canvas.create_oval(x1, y + 31, x2, y + 37,  fill=myfill) 


    def num(self, n):
        """ Shows the number on counter created if number > digits
        number wraps around 3 digits 1000 is 000, 1001 is 001"""
        mul = (10,100,1000,10000)
        i = int(n)
        r = n - i 
        ad = int(r * mul[self.dp-1])
        v = '00000000' + str(i) + str(ad)
        ln = len(v)
        for x in range(0, self.dig):
            self.poss[x].show(int(v[ln - self.dig + x]))


class Clock:
    """ Creates a 7 segment line clock in either HH:MM or HH:MM:SS. 
    mode 0 = HH:MM mode 1 = HH:MM:SS. """
    def __init__(self,canvas, *, x=10, y=10, mode=0, myfill='green'):
        self.canvas = canvas
        self.mode = mode 
        self.poss=[]
        dig = 4
        if self.mode==1:
            dig = 6
        for w in range(0, dig):
            self.poss.append(Digit(canvas, x = w*34 + x, y=y, myfill=myfill))
        x1 = x-8 + ((4 - 2) * 34)
        x2 = x1 + 5
        canvas.create_oval(x1, y + 11, x2, y + 17,  fill=myfill) 
        canvas.create_oval(x1, y + 31, x2, y + 37,  fill=myfill) 
        if mode == 1:
            x1 = x-8 + ((dig - 2) * 34)
            x2 = x1 + 5
            canvas.create_oval(x1, y + 11, x2, y + 17,  fill=myfill) 
            canvas.create_oval(x1, y + 31, x2, y + 37,  fill=myfill) 


    def num(self, h,m,s=0):
        """ Shows the time (Hh:MM:SS) """

        self.poss[0].show(int(h/10) % 10)
        self.poss[1].show((h) % 10)
        self.poss[2].show(int(m/10) % 10)
        self.poss[3].show(m % 10)

        if self.mode == 1:
            self.poss[4].show(int(s/10) % 10)
            self.poss[5].show(s % 10)



if __name__ == "__main__":
    
    def update():
        global n
        # update 4 individual line characters the hard way
        dig1.show(int(n/1000) % 10)
        dig2.show(int(n/100) % 10)
        dig3.show(int(n/10) % 10)
        dig4.show(n % 10)
        # update 4 individual led characters the hard way
        dig1L.show(int(n/1000) % 10)
        dig2L.show(int(n/100) % 10)
        dig3L.show(int(n/10) % 10)
        dig4L.show(n % 10)

        dig5.show((n % 6) + 16)
        dig5L.show((n % 6 ) + 16)
        # update 5 character line  display the easy way
        ctr4.num(n)
        # update 4 character led  display the easy way
        ctr5.num(n)

        tm.num(0,int(n/60) %60, n%60)
        n = (n+1) % 100000
        root.after(100, update)


    root = tk.Tk()
    screen = tk.Canvas(root, bg='black', width=430)
    screen.grid()

    # 4 character line 7 segment display the hard way
    dig1 = Digit(screen)
    dig2 = Digit(screen, x=40)
    dig3 = Digit(screen, x=70)
    dig4 = Digit(screen, x=100)
    dig5 = Digit(screen, x = 290)
    # 4 character led 7 segment display the hard way
    dig1L = Digit_Led(screen, x=150)
    dig2L = Digit_Led(screen, x=180)
    dig3L = Digit_Led(screen, x=210)
    dig4L = Digit_Led(screen, x=240)
    dig5L = Digit_Led(screen, x = 330)
    n = 0
    # 5 character line 7 segment display (decimal) the easy way
    ctr4 = Counter(screen, y=70, dig=5 )
    # 4 character led 7 segment display (hex) the easy way
    ctr5 = Counter_Led(screen, x=180, y=70, base=16, myfill='navy')
    tm = Clock(screen, y=140, mode=1 )
    tm.num(1,12,37)
    tm2 = Clock_Led(screen, x = 220, y=140, mode=1)
    tm2.num(5,22,37)
    ctr6 = Counter_Dp(screen, y = 210,dig=6, dp=2)
    ctr6.num(43.1450)
    ctr7 = Counter_Led_Dp(screen, x=225, y=210, dig=5, dp=2)
    ctr7.num(43.21435)

    root.after(100, update)
    root.mainloop()