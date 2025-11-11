from struct import *

packed_data = pack('iif', 6, 19, 4.73)
print(packed_data)


print(calcsize("i")) 


## unpack b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'
original = unpack('iif', packed_data)
print('iif ', packed_data)

print(unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'))

## BITWISE 

# ...... Binary AND .......
a = 50    # 110010
b = 25    # 011001

c = a & b # 010000
print(c)

# ...... Binary RIGTH SHIFT .......
x = 240     # 11110000
y = x >> 2  # 00111100

print(y)
  
