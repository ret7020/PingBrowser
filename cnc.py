import icmp
import threading
from pathlib import Path
import socket

def process_requests(data: str):
    print(data)



if __name__ == "__main__":
    while True:
        icmp.recv(process_requests)
