import socket
import select

# Задаем адрес сервера
SERVER_ADDRESS = ('157.230.91.217', 9878)

HOST = '157.230.91.217'  # Standard loopback interface address (localhost)
PORT = 9878        # Port to listen on (non-privileged ports are > 1023)

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
            conn.close()