"""16 segment alphanumeric line display 
    get_lib_version() Show numeric version of library.
    get_lib_full_version()  Show numeric version and library filename.
    class seg16Digit() creates 1 character of a 16 segment display
        show()  displays numeric value in character
    class strDisp() creates multiple 16 segment display characters
        show() displays the sting 
    NOTE: Characters 0x20 to 0x7e have been encoded.  
    Characters 0x80 - 0x8E are for making animations 
    the show method of the strDisp class will automatically subtract
    0x20 from the characters in the string. 
    """
import tkinter as tk

# Order 16 segments  or british flag display.
#
#   --a1-- --a2-- 
#  | \    |    / |
#  f  h   i   j  b
#  |   \  |  /   |
#  |    \ | /    |
#   --g1-- --g2--
#  |     /|\     |
#  |    / | \    |
#  e   m  l  k   c
#  |  /   |   \  |
#   --d1-- --d2--  
#    
# clockwise from top left, with crossbar last.
# Coordinates of each segment are (x0, y0, x1, y1) 
# given as offsets from top left measured in segment lengths.

offsets = (
    (0, 0, 1, 0),  # a1 top
    (1, 0, 2, 0),  # a2 top
    (2, 0, 2, 1),  # b upper right
    (2, 1, 2, 2),  # c lower right
    (1, 2, 2, 2),  # d2 bottom
    (0, 2, 1, 2),  # d1 bottom
    (0, 1, 0, 2),  # e lower left
    (0, 0, 0, 1),  # f upper left
    (0, 1, 1, 1),  # g1 middle
    (1, 1, 2, 1),  # g2 middle
    (0, 0, 1, 1),  # h left diag top
    (1, 0, 1, 1),  # i ctr vert top
    (2, 0, 1, 1),  # j right diag top
    (1, 1, 2, 2),  # k right diag btm
    (1, 1, 1, 2),  # l ctr vert btm
    (1, 1, 0, 2),  # m left diag btm

)

# ascii character 0x20 through 0x7e
# offset to numbers is 0x20, offset to letters is 0x20
# Segments used for each digit; 0, 1 = off, on.
digits = (
   # a1 a1 b  c  d2 d1 e  f  g1 g2 h  i  j  k  l  m 
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),  # 0x20 space
    (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0),  # 0x21 !    
    (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),  # 0x22 "
    (0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0),  # 0x23 #
    (1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0),  # 0x24 $
    (0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1),  # 0x25 %
    (1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0),  # 0x26 &
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),  # 0x27 '
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0),  # 0x28 (
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1),  # 0x29 )
    (0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1),  # 0x2A *
    (0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0),  # 0x2B +
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),  # 0x2C ,
    (0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x2D -
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),  # 0x2E .
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1),  # 0x2F /
    (1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1),  # 0x30 0
    (0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),  # 0x31 1
    (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x32 2
    (1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x33 3
    (0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x34 4
    (1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x35 5
    (1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x36 6
    (1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),  # 0x37 7 
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x38 8
    (1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x39 9
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0),  # 0x3A :
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1),  # 0x3B ;
    (0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1),  # 0x3C <
    (0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x3D =
    (0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0),  # 0x3E >
    (1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0),  # 0x3F ?
    (1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0),  # 0x40 @
   # a1 a1 b  c  d2 d1 e  f  g1 g2 h  i  j  k  l  m 
    (1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x41 A
    (1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0),  # 0x42 B
    (1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0),  # 0x43 C
    (1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0),  # 0x44 D
    (1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x45 E
    (1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x46 F
    (1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0),  # 0x47 G
    (0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x48 H
    (1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0),  # 0x49 I
    (0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),  # 0x4A J
    (0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0),  # 0x4B K
    (0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0),  # 0x4C L
    (0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0),  # 0x4D M
    (0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0),  # 0x4E N
    (1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0),  # 0x4F O
    (1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x50 P
    (1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0),  # 0x51 Q
    (1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0),  # 0x52 R
    (1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0),  # 0x53 S
    (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0),  # 0x54 T
    (0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0),  # 0x55 U
    (0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1),  # 0x56 V
    (0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1),  # 0x57 W
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1),  # 0x58 X
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0),  # 0x59 Y
    (1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1),  # 0x5A Z
   # a1 a1 b  c  d2 d1 e  f  g1 g2 h  i  j  k  l  m 
    (0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0),  # 0x5B [
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0),  # 0x5C \
    (1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0),  # 0x5D ]    
    (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0),  # 0x5E ^    
    (0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),  # 0x5F _    
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),  # 0x60 `    

   # a1 a1 b  c  d2 d1 e  f  g1 g2 h  i  j  k  l  m 
    (1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x61 a
    (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x62 b
    (0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x63 c
    (0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x64 d
    (1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x65 e
    (0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0),  # 0x66 f
    (1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x67 g
    (0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x68 h
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),  # 0x69 i
    (0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),  # 0x6A j
    (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0),  # 0x6B k
    (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0),  # 0x6C l
    (0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0),  # 0x6D n
    (0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x6E m
    (0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x6F o
    (1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0),  # 0x70 p
    (1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0),  # 0x71 q
    (0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x72 r
    (0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0),  # 0x73 s
    (0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0),  # 0x74 t
    (0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),  # 0x75 u
    (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0),  # 0x76 v
    (0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1),  # 0x77 w
    (0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1),  # 0x78 x
    (0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x79 y
    (0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1),  # 0x7A z
    (0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0),  # 0x7B {
    (0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0),  # 0x7C |
    (1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0),  # 0x7D }
    (0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0),  # 0x7E ~
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),  # 0x7f 

   #  Diagnostics / animation frames 0x80 and 0x87
    (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),  # 0x80 top horiz Bar
    (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),  # 0x81 Top Right Vert
    (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),  # 0x82 Bot right Vert
    (0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),  # 0x83 Bot horiz
    (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),  # 0x84 Bot Left Vert
    (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),  # 0x85 Top Left Vert
    (0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0),  # 0x86 Ctr horiz bar
    (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),  # 0x87 ctr left horiz
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),  # 0x88 top left slant
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),  # 0x89 top ctr vert
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),  # 0x8a top right slant
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),  # 0x8b ctr right vert
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0),  # 0x8c bot right slant
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),  # 0x8d bot ctr vert
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),  # 0x8e bot left slant
)
name_sixteen_seg    = 'sixteen_seg.py'
version_sixteen_seg = '1.0.0'
date_sixteen_seg    = '02/05/21'
author_sixteen_seg  = 'Peter A. Hedlund'

LIB_NAME = name_sixteen_seg
LIB_VERSION = version_sixteen_seg
LIB_DATE = date_sixteen_seg
LIB_AUTHOR = author_sixteen_seg

# LIB_NAME = 'sixteen_seg.py'
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
# 16 Segment Line DISPLAY SECTION
#

class seg16Digit:
    """Creates a 16 segment line type display (one alphanumeric character)"""
    def __init__(self, canvas, *, x=10, y=10, length=23, width=3, 
                myfill='green'):
        self.canvas = canvas
        self.myfill = myfill
        l = length
        w = length/2
        self.segs = []
        for x0, y0, x1, y1 in offsets:
            self.segs.append(canvas.create_line(
                x + x0*w, y + y0*l, x + x1*w, y + y1*l,
                width=width, state = 'hidden', fill=myfill))


    def show(self, num, color='green'):
        """Show the character number num  on the single character line
        16 segment display in the designated color"""
        for iid, on in zip(self.segs, digits[num]):
            self.canvas.itemconfigure(iid, state = 'normal' if on else 'hidden',
                                      fill = color)


class StrDisp:
    """Creates a set of 16 segment line style (dig = num characters)"""
    def __init__(self, canvas, *, x=10, y=10, dig=4, myfill='green'):
        self.canvas = canvas
        self.dig = dig 
        self.poss=[]
        for w in range(0, self.dig):
            self.poss.append(seg16Digit(canvas, x = w*32 + x, y=y, myfill=myfill))


    def show(self, st, color='green'):
        """Shows the string converted to uppercase in the display in the designated
           color."""
        ep = self.dig
        if len(st) < ep:
            ep = len(st)
        for q in range(0, ep):
            v = ord(st[q])
            self.poss[q].show(v - 0x20, color)


if __name__ == "__main__":

    import time

    def update():
        global a, b, n, toc
        a = (a+1) % 15
        toc = (toc+1) % 10
        if toc == 0:
            n = (n+1) % 30
            b = (b+1) % 0x41
        dig1.show(0x60 + a, 'red')
        dig2.show( b, 'red')
        digx.show(0x41 + n, 'cyan')
        tm = time.localtime()
        str1 = time.strftime('%H %M %S', tm)
        dsp6.show(str1, 'royalblue')
        root.after(100, update)
   

    def quit_prog():
        root.destroy()


    root = tk.Tk()
    screen = tk.Canvas(root, bg='black', width=430, height=200)
    screen.grid(column=0, row=0, columnspan=5)
    bt = tk.Button(root, text='   Quit   ', command=quit_prog)
    bt.grid(column=0, row=1)
    screen2 = tk.Canvas(root, bg='gray10', width=430, height=70)
    screen2.grid(column=0, row=2, columnspan=5)
    n = 0;  a = 0;  b = 0; toc = 0
    # 4 character line 7 segment display the hard way
    dig1 = seg16Digit(screen, x=395)
    dig1.show(0x41, 'red')
    dig2 = seg16Digit(screen, x=395, y=120)
    dig2.show(0x48, 'red')
    digx = seg16Digit(screen, x=395, y=64)
    digx.show(0x61, 'red')
    dsp3 = StrDisp(screen, dig=12)
    dsp3.show('ABCDEFGHIJK')
    dsp4 = StrDisp(screen, y=64, dig=12)
    dsp4.show('LMNOPQRSTUV','yellow')
    dsp5 = StrDisp(screen, y=120, dig=12)
    dsp5.show('WXYZ()[]  ')
    dsp6 = StrDisp(screen2, x=10, y=19, dig=13)
    dsp6.show('NCC-1701 TIME', 'royalblue')
    root.after(1000, update)
    root.mainloop()
