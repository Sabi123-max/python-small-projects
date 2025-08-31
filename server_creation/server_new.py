import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = '127.0.0.1'
    port = 8080
    s.bind((host, port))
    s.listen()
    print(f"seerver lisining on {host}:{port}")
    while True:
        client, addr = s.accept()
        print(f"client {addr} connected")
        msg = client.recv(1024).decode()
        print(f"received {msg}")
        client.send("hello wolrd".encode())
        client.close()