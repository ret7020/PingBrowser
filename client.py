import icmp
import threading
import socket

def collect_server_responses(data):
    print(data)
    #sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    #icmp.send(sock, "192.168.1.8", data)
    #sock.close()


if __name__ == "__main__":
    threading.Thread(target=lambda: icmp.recv(collect_server_responses)).start()
    request_sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    icmp.send(request_sock, "192.168.1.8", "GET /simple")

    


