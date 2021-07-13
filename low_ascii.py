# low_ascii.py
"""Character defnitions for ascii characters 0 - 31 """
name_low_ascii    = 'low_ascii.py'
version_low_ascii = '1.0.0'
date_low_ascii    = '04/22/21'
author_low_ascii  = 'Peter A. Hedlund'
# ====================================================
# ascii codes 0 = 31  are non printable control codes
# ====================================================

nul_  = 0x00        # null
soh_  = 0x01        # Start of heading
stx_  = 0x02        # Start of text
etx_  = 0x03        # End of text
eot_  = 0x04        # End of transmit
ack_  = 0x06        # acknowledge
bel_  = 0x07        # audible bell
bksp_ = 0x08        # backspace
ht_   = 0x09        # horizontal tab
lf_   = 0x0a        # line feed
vt_   = 0x0b        # vertical tab
ff_   = 0x0c        # form feed
cr_   = 0x0d        # carriage return
si_   = 0x0e        # Shift in
so_   = 0x0f        # shift out
dle_  = 0x10        # Data link escape
dc1_  = 0x11        # Device Control 1 
dc2_  = 0x12        # Device Control 2 
dc3_  = 0x13        # Device Control 3 
dc4_  = 0x14        # Device Control 4 
nak_  = 0x15        # Nag acknowledge
is_   = 0x16        # Synchronus idle
etb_  = 0x17        # End Trans Block
can_  = 0x18        # Cancel
eom_  = 0x19        # End of medium
sub_  = 0x1a        # Substution
esc_  = 0x1b        # Escape
fs_   = 0x1c        # File Seperator
gs_   = 0x1d        # group seperator
rs_   = 0x1e        # Record Seperator


pb_ = 0x5b          # [ 
pe_ = 0x5d          # ]
