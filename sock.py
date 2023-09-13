import socket
import struct

def listen():
    s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
    s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
    while 1:
        data, addr = s.recvfrom(1024)
        if data:
            icmp_header = recPacket[20:28]
            icmp_type, code, checksum, p_id, sequence = struct.unpack('bbHHh', icmp_header)


            print(data, end="\n-----\n")

if __name__ == "__main__":
    listen()
