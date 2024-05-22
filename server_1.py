import socket

HOST = '192.168.1.130'  # Standard loopback interface address (localhost)
PORT = 9091  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("p")
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print("a")
    with conn:
        print(f"Connected by {addr}")
        data = conn.recv(1024).decode("utf-8")
        print(data)
        conn.send('i accept this connection'.encode('utf-8'))
        while True:
            data = conn.recv(1024).decode("utf-8")
            print(data)
            if "exit" in str(data):
                break
            if not data:
                break
            conn.send(data.encode("utf-8"))


