import icmp
import threading
from pathlib import Path
import socket

def process_requests(data: str):
    print(data)
    data = data.strip()
    content = "" # Response
    if data.startswith("GET"):
        path = data.replace("GET ", "")
        print(f"GET: {path}")
        if path == "/simple":
            print("Sending builtin test page")
            content = Path("./misc/send_me.html").read_text()
            # Optimize size
            content = content.replace("\n", " ")
        print(content)
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        icmp.send(sock, "192.168.1.8", data)
        sock.close()



if __name__ == "__main__":
    while True: # Listen for incoming data transfer requests
        icmp.recv(process_requests)
