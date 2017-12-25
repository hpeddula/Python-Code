from struct import *
packed_data=pack('ii',2,5)
print(packed_data)
print(unpack('ii',b'\x02\x00\x00\x00\x05\x00\x00\x00'))
print(calcsize('s'))
a=50
b=25
print(a & b)
x=240
print(x >> 2)