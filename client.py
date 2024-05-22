import threading
import socket
import time
import random


#linux IP : 192.168.21.128
#windows IP : 192.168.1.130

print("whats your IP")
ipv4_address = input()
print("what IP adress you looking for")
HOST = input()
count: int = 0
print("what port you looking for")
PORT = int(input())
connecet: bool = False
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ipv4_address, PORT))
    s.listen()
    while not connecet:
        if count > 10:
            break
        wait = random.uniform(1, 3)
        print(wait)
        s.settimeout(wait)
        try:
            conn, addr = s.accept()
        except:
            print("failed")
            count = count + 1
            try:
                s.connect((HOST, PORT))
            except:
                print("failed to connect the other computer")
            else:
                print("i made connection")
                with s:
                    connecet = True
                    print(f"Connected by {HOST}")
                    while True:
                        print("waiting for input")
                        massege = input()
                        conn.send(massege.encode("utf-8"))
                        if "exit" in str(massege):
                            break
                        print("waiting for incoming massege")
                        data = conn.recv(1024).decode("utf-8")
                        print(data)
                        if "exit" in str(data):
                            break
                        if not data:
                            break
        else:
            print("i recived a connection")
            with conn:
                connecet = True
                print(f"Connected by {HOST}")
                while True:
                    print("waiting for incoming massege")
                    data = conn.recv(1024).decode("utf-8")
                    print(data)
                    if "exit" in str(data):
                        break
                    if not data:
                        break
                    print("waiting for input")
                    # print("enter x")
                    # x = int(input())
                    # print("enter y")
                    # y = int(input())
                    # s.send((Point.Point(y, x)).encode('utf-8'))
                    massege = input()
                    conn.send(massege.encode("utf-8"))
                    if "exit" in str(massege):
                        break




















