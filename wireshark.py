import socket
import time
import signal
import sys


def run_program():
    sock_l = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_l.bind(('0.0.0.0', 12345)) #Putting all 0s means you can accept all kinds of network requests anywhere from any client (known routable address)
    sock_l.listen()
    while True:
        print('Waiting for connection')
        conn, addr = sock_l.accept()
        print('Connected')
        data = 1 #dummy value of 1
        while data is not None:
            data = conn.recv(1024)
            print(data.decode("utf-8"))      


if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit)
    run_program()
