from huff_tools import MAXBITS
import huff_codes

freqs = dict()
buff = list()    
tupes = list()

f = open("data.1", "rb")
try:
    byte = f.read(1)
    while byte != "":
        # Do stuff with byte.
        buff.append(byte)
        if freqs.has_key(byte):
            freqs[byte] += 1
        else:
            freqs[byte] = 1
            
        byte = f.read(1)
finally:
    f.close()

tups = freqs.items()
huff_table = huff_codes.getCodes(tups)  


print freqs
print buff
print tups
print huff_table

