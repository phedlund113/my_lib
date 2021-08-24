#
# pylint: disable=unused-wildcard-import, method-hidden
#

""" data_validation
get_lib_version() Show numeric version of library.
get_lib_full_version()  Show numeric version and library filename.
checksum_8(pkt) Returns 8 byte checksum of all bytes in pkt
checksum_16(pkt) Returns 16 byte checksum of all bytes in pkt
crc16( st, crc) Given a binary string and starting CRC, Calc a final CRC-16
crc16_CCITT(data : bytearray, offset , length)
    Given a binary string and offset and length Calc a final CRC-16 CCITT

"""


from tkinter import messagebox

name_about    = 'data_validation.py'
version_about = '1.0.0'
date_about    = '07/16/21'
author_about  = 'Peter A. Hedlund'

LIB_NAME = name_about
LIB_VERSION = version_about
LIB_DATE = date_about
LIB_AUTHOR = author_about


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




INITIAL_DF1 = 0x0000

table = (
0x0000, 0xC0C1, 0xC181, 0x0140, 0xC301, 0x03C0, 0x0280, 0xC241,
0xC601, 0x06C0, 0x0780, 0xC741, 0x0500, 0xC5C1, 0xC481, 0x0440,
0xCC01, 0x0CC0, 0x0D80, 0xCD41, 0x0F00, 0xCFC1, 0xCE81, 0x0E40,
0x0A00, 0xCAC1, 0xCB81, 0x0B40, 0xC901, 0x09C0, 0x0880, 0xC841,
0xD801, 0x18C0, 0x1980, 0xD941, 0x1B00, 0xDBC1, 0xDA81, 0x1A40,
0x1E00, 0xDEC1, 0xDF81, 0x1F40, 0xDD01, 0x1DC0, 0x1C80, 0xDC41,
0x1400, 0xD4C1, 0xD581, 0x1540, 0xD701, 0x17C0, 0x1680, 0xD641,
0xD201, 0x12C0, 0x1380, 0xD341, 0x1100, 0xD1C1, 0xD081, 0x1040,
0xF001, 0x30C0, 0x3180, 0xF141, 0x3300, 0xF3C1, 0xF281, 0x3240,
0x3600, 0xF6C1, 0xF781, 0x3740, 0xF501, 0x35C0, 0x3480, 0xF441,
0x3C00, 0xFCC1, 0xFD81, 0x3D40, 0xFF01, 0x3FC0, 0x3E80, 0xFE41,
0xFA01, 0x3AC0, 0x3B80, 0xFB41, 0x3900, 0xF9C1, 0xF881, 0x3840,
0x2800, 0xE8C1, 0xE981, 0x2940, 0xEB01, 0x2BC0, 0x2A80, 0xEA41,
0xEE01, 0x2EC0, 0x2F80, 0xEF41, 0x2D00, 0xEDC1, 0xEC81, 0x2C40,
0xE401, 0x24C0, 0x2580, 0xE541, 0x2700, 0xE7C1, 0xE681, 0x2640,
0x2200, 0xE2C1, 0xE381, 0x2340, 0xE101, 0x21C0, 0x2080, 0xE041,
0xA001, 0x60C0, 0x6180, 0xA141, 0x6300, 0xA3C1, 0xA281, 0x6240,
0x6600, 0xA6C1, 0xA781, 0x6740, 0xA501, 0x65C0, 0x6480, 0xA441,
0x6C00, 0xACC1, 0xAD81, 0x6D40, 0xAF01, 0x6FC0, 0x6E80, 0xAE41,
0xAA01, 0x6AC0, 0x6B80, 0xAB41, 0x6900, 0xA9C1, 0xA881, 0x6840,
0x7800, 0xB8C1, 0xB981, 0x7940, 0xBB01, 0x7BC0, 0x7A80, 0xBA41,
0xBE01, 0x7EC0, 0x7F80, 0xBF41, 0x7D00, 0xBDC1, 0xBC81, 0x7C40,
0xB401, 0x74C0, 0x7580, 0xB541, 0x7700, 0xB7C1, 0xB681, 0x7640,
0x7200, 0xB2C1, 0xB381, 0x7340, 0xB101, 0x71C0, 0x7080, 0xB041,
0x5000, 0x90C1, 0x9181, 0x5140, 0x9301, 0x53C0, 0x5280, 0x9241,
0x9601, 0x56C0, 0x5780, 0x9741, 0x5500, 0x95C1, 0x9481, 0x5440,
0x9C01, 0x5CC0, 0x5D80, 0x9D41, 0x5F00, 0x9FC1, 0x9E81, 0x5E40,
0x5A00, 0x9AC1, 0x9B81, 0x5B40, 0x9901, 0x59C0, 0x5880, 0x9841,
0x8801, 0x48C0, 0x4980, 0x8941, 0x4B00, 0x8BC1, 0x8A81, 0x4A40,
0x4E00, 0x8EC1, 0x8F81, 0x4F40, 0x8D01, 0x4DC0, 0x4C80, 0x8C41,
0x4400, 0x84C1, 0x8581, 0x4540, 0x8701, 0x47C0, 0x4680, 0x8641,
0x8201, 0x42C0, 0x4380, 0x8341, 0x4100, 0x81C1, 0x8081, 0x4040 )



def checksum_8(pkt):
    """Returns 8 byte checksum of all bytes in pkt"""
    crc = 0
    for x in range(0, len(pkt)):
        crc += pkt[x]
    crc %= 256
    return crc

def checksum_16(pkt):
    """Returns 16 byte checksum of all bytes in pkt"""
    crc = 0
    for x in range(0, len(pkt)):
        crc += pkt[x]
    crc %= 65536
    return crc

def crc16( st, crc):
    """Given a binary string and starting CRC, Calc a final CRC-16 """
    for ch in st:
        crc = (crc >> 8) ^ table[(crc ^ ch) & 0xFF]
    return crc

def crc16_CCITT(data : bytearray, offset , length):
    """Given a binary string and offset and length Calc a final CRC-16 CCITT """
    if data is None or offset < 0 or offset > len(data)- 1 and offset+length > len(data):
        return 0
    crc = 0xFFFF
    for i in range(0, length):
        crc ^= data[offset + i] << 8
        for j in range(0,8):
            if (crc & 0x8000) > 0:
                crc =(crc << 1) ^ 0x1021
            else:
                crc = crc << 1
    return crc & 0xFFFF

#
# Testing Library Function
#


if __name__ == "__main__":
    from tkinter import *
    from tkinter import ttk
    import mylib.scrn_log as scrn

    def to_hex(bya):
        os = ''
        for x in bya:
            os = os + f'0x{x:02X} '
        return os

    def send_str(txt, wstr):
        txt.insert(END,wstr)
        txt.index(END)
        txt.see(END)
        txt.update()

    root = Tk()
    #  prevent window resizing.
    root.resizable(0, 0)
    # Replace tk icon with your own.
    root.title('Data Validation Test Program DEMO')
    mainframe = ttk.Frame(root, padding="3", height=420, width=460)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.grid_propagate(0)
    
    log = scrn.scrn_log(mainframe, 52, 23, 'black', 'light grey', 0, 0, 2, 10)
 
    ba = (0x02, 0x05, 0x5b, 0x00, 0x5d, 0x03)

    log.log_scrn_color('Data Validation Library Test\n', 'green')
    cs1 = checksum_8(ba)
    cs2 = checksum_16(ba)
    cs3 = crc16(ba,0)
    cs4 = crc16_CCITT(ba,0, len(ba))
    
    log.log_scrn_color(f'Data Packet {to_hex(ba)}\n\n', 'blue')
    log.log_scrn(f'checksum-8 shoud return  0xC2    actual is 0x{cs1:02X}\n')   
    log.log_scrn(f'checksum-16 shoud return 0x00C2  actual is 0x{cs2:04X}\n')   
    log.log_scrn(f'      crc16 shoud return 0x57A6  actual is 0x{cs3:04X}\n')   
    log.log_scrn(f'crc16_CCITT shoud return 0x85A3  actual is 0x{cs4:04X}\n')   
    log.log_scrn('\n')
    ba = (0x02 ,0x02, 0x5B, 0x04, 0x91, 0x62, 0x94, 0x95, 0x94, 0x0F,
      0x50, 0x47, 0x58, 0x34, 0x00, 0x40, 0x00, 0x5D, 0x03 )
    cs1 = checksum_8(ba)
    cs2 = checksum_16(ba)
    cs3 = crc16(ba,0)
    cs4 = crc16_CCITT(ba,0, len(ba))
    st = f'{to_hex(ba)}\n'
    log.log_scrn_color(f'Data Packet\n', 'blue')
    log.log_scrn_color(f'{st[0:50]}\n{st[50:100]}\n', 'blue')
    log.log_scrn(f'checksum-8 shoud return  0xE5    actual is 0x{cs1:02X}\n')   
    log.log_scrn(f'checksum-16 shoud return 0x04E5  actual is 0x{cs2:04X}\n')   
    log.log_scrn(f'      crc16 shoud return 0x4172  actual is 0x{cs3:04X}\n')   
    log.log_scrn(f'crc16_CCITT shoud return 0xEE66  actual is 0x{cs4:04X}\n')   
            
    
    for child in root.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()
