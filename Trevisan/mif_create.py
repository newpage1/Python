__author__ = 'Owner'
input_text = str()
from random import *
input_text += 'WIDTH=1;\r\nDEPTH=4096;\r\nADDRESS_RADIX=HEX;\r\nDATA_RADIX=BIN;\r\nCONTENT BEGIN\r\n'
line_text = str()
for i in range(4096):
    address = hex(i)
    address = address[2:]
    address += ':'
    line_text += address
    for j in range(1):
        ran_text = str(randrange(2))
        line_text += ran_text
    line_text += ';\r\n'
    input_text += line_text
    line_text = str()

input_text += 'END;'

output = open('bit_ram_init.mif','wb')
output.write(input_text)
output.flush()
output.close()


