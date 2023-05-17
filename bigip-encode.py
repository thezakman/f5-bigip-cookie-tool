#!/usr/bin/env python3
import sys

def encode_port(port):
    enc_port = hex(int(port))[2:].zfill(4)
    return enc_port[2:] + enc_port[:2]

def encode_ip(ip):
    return str(int(''.join(format(int(part), '02x') for part in ip.split('.')[::-1]), 16))

ip, port = sys.argv[1], sys.argv[2]

encoded_ip = encode_ip(ip)
encoded_port = int(encode_port(port), 16)

print("Encoded BigIP Cookie: %s.%s.0000" % (encoded_ip, encoded_port))
