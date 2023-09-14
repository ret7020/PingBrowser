import struct
import socket
import random
import time

def checksum(source_string):
    sum_ = 0
    count_to = len(source_string) - 1
    count = 0
    while count < count_to:
        this_val = source_string[count + 1]*256+source_string[count]
        sum_ = sum_ + this_val
        sum_ = sum_ & 0xffffffff
        count = count + 2
    if count_to < len(source_string):
        sum_ += source_string[len(source_string) - 1]
        sum_ = sum_ & 0xffffffff
    sum_ = (sum_ >> 16) + (sum_ & 0xffff)
    sum_ = sum_ + (sum_ >> 16)
    answer = ~sum_
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer


def create_packet(id_, payload):
    ICMP_ECHO_REQUEST = 8 # icmp echo
    header = struct.pack('bbHHh', ICMP_ECHO_REQUEST, 0, 0, id_, 1)

    my_checksum = checksum(header + payload)
    header = struct.pack('bbHHh', ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), id_, 1)
    return header + payload


def send(s, dest_addr, payload):
    packet_id = random.randint(0, 65535)
    payload = payload.encode("utf-8")
    packet = create_packet(packet_id, payload)
    
    while packet:
        sent = s.sendto(packet, (dest_addr, 1))
        packet = packet[sent:]

    return packet_id

def recv(callback):
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
    while True:
        data, addr = s.recvfrom(1024)
        if data:
            icmp_header = data[20:28]
            icmp_type, code, checksum, p_id, sequence = struct.unpack('bbHHh', icmp_header)
            callback(icmp_type, data[28:].decode("utf-8"))

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    while True:
        send(sock, "192.168.1.8", input(">"))
        print("Packet sent")
        time.sleep(1)
