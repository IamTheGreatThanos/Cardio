b = int.from_bytes(b'\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00', byteorder='big')
# print(b)
a = str(b'\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00')
# print(a[2:len(a)-1])

import binascii
a = str(b'\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00')
# a = a.split("x")[1:]
a = a[2:len(a)-1]
l = len(a)
bb = []
s = 0
for i in range(12,l+12,12):
    t = a[s:i].split("\\x")
    st = ""
    st = st.join(t)
    h = int(st, 16)
    bb.append(h)
    s=i
print(bb)
# print(bytearray.fromhex('deadbeef'))

#!/usr/bin/env python

# import socket

# with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

#     message = b'800000800008000008000080000080000'
#     # addr = ("157.230.91.217", 9879)
#     addr = ("localhost", 9879)

#     s.sendto(message, addr)

#     # data, address = s.recvfrom(1024)
#     # print(data.decode())