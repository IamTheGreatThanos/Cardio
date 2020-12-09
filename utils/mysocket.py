import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    host = "back.cardioservice.com.kz"
    port = 13

    s.connect((host, port))
    s.sendall(b'')
    print(str(s.recv(4096), 'utf-8'))