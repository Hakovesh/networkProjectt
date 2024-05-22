import socket
import Point

HOST = '192.168.1.130'  # Standard loopback interface address (localhost)
PORT = 9091  # Port to listen on (non-privileged ports are > 1023)

def isfinish(data):
    if "exit" in str(data):
        return True


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
            if isfinish(data):
                break
            if not data:
                break
            massege = input()
            conn.send(massege.encode("utf-8"))
            if isfinish(massege):
                break


