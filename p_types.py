# p_types.py 
"""C style type definitions for python structures"""

name_p_types    = 'p_types.py'
version_p_types = '1.0.0'
date_p_types    = '04/22/21'
author_p_types  = 'Peter A. Hedlund'

# ============================================
# C type casting for use in python structures
# ============================================

char8_   = 'b'      # Bytes 1
uchar8_  = 'B'      # Bytes 1
bool_    = '?'      # Bytes 1
int16_   = 'h'      # Bytes 2
uint16_  = 'H'      # Bytes 2
int32_   = 'i'      # Bytes 4
uint32_  = 'I'      # Bytes 4
int64_   = 'q'      # Bytes 8
uint64_  = 'Q'      # Bytes 8
float32_ = 'f'      # Bytes 4
float64_ = 'd'      # Bytes 8
str_     = 's'      # Bytes ? put number before str_
bpacked_ = '='      # Bytes 0

