
__author__ = 'Owner'
from random import *
input_text = str()
result = str()
input_text = 'MEMORY_INITIALIZATION_RADIX=2;\r\nMEMORY_INITIALIZATION_VECTOR=\r\n'
input_text = input_text.lower()
for i in range(128):
    for j in range(32):
        result = result + choice(['0','1'])
    input_text = input_text + result + ',\r\n'
    result = str()

output = open('4k_rom_init.coe','wb')
output.write(input_text)
output.flush()
output.close()


