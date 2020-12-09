import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8888        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

# from tornado.ioloop import IOLoop
# from tornado.tcpserver import TCPServer
# from tornado.iostream import IOStream, StreamClosedError

# class EchoServer(TCPServer):
#     async def handle_stream(self, stream, address):
#         while True:
#             try:
#                 data = await stream.read_until(b"bardima")
#                 d = await stream.read_bytes(4)
#                 print(d)
#                 await stream.write(data)
#             except StreamClosedError:
#                 break


# server = TCPServer()
# server.listen(8888)
# server.start(0)
# IOLoop.current().start()
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