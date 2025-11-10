from struct import *

packed_data = pack('iif', 6, 19, 4.73)
print(packed_data)


print(calcsize("i")) 


## unpack b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'
original = unpack('iif', packed_data)
print('iif ', packed_data)

print(unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'))