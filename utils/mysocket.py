from tornado.ioloop import IOLoop
from tornado.tcpserver import TCPServer
from tornado.iostream import IOStream, StreamClosedError

import struct
int_struct = struct.Struct("<i")
_UNPACK_INT = int_struct.unpack
_PACK_INT = int_struct.pack
class MyTCPServer(TCPServer):
    def handle_stream(self, stream, address):
        try:
            while True:
                # Read 4 bytes.
                header = stream.read_bytes(4)

                # Convert from network order to int.
                length = _UNPACK_INT(header)[0]

                msg = stream.read_bytes(1024)
                print('"%s"' % msg.decode())

                del msg  # Dereference msg in case it's big.
        except StreamClosedError:
            print("%s disconnected", address)

if __name__ == '__main__':
    server = MyTCPServer()
    server.listen(9876)
    IOLoop.instance().start()

# import socket
# import sys

# # Create a TCP/IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Connect the socket to the port where the server is listening
# # server_address = ('157.230.91.217', 10000)
# server_address = ('192.168.1.101', 10000)
# print(sys.stderr, 'connecting to %s port %s' % server_address)
# sock.connect(server_address)


# try:
#     # Send data
#     message = 'This is the message.  It will be repeated.'
#     print(sys.stderr, 'sending "%s"' % message)
#     sock.sendall(message)

#     # Look for the response
#     amount_received = 0
#     amount_expected = len(message)

#     while amount_received < amount_expected:
#         data = sock.recv(16)
#         amount_received += len(data)
#         print(sys.stderr, 'received "%s"' % data)

# finally:
#     print(sys.stderr, 'closing socket')
#     sock.close()