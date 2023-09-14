import socket
import struct

def listen():
    s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
    s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
    while 1:
        data, addr = s.recvfrom(1024)
        if data:
            # Header processing
            icmp_header = data[20:28]
            icmp_type, code, checksum, p_id, sequence = struct.unpack('bbHHh', icmp_header)
            if icmp_type == 0: # Read only ICMP ECHO REQUESTS; For listen for ICMP ECHO sent by us use 8
                print(data[28:].decode("utf-8"))

if __name__ == "__main__":
    listen()
