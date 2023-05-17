#!/usr/bin/env python3
import sys

ip, port = sys.argv[1], sys.argv[2]

ip = ip.split('.')
ip.reverse()

enc_ip = []

for i in ip:
    enc_ip.append(hex(int(i))[2:].zfill(2))

enc_ip = ''.join(enc_ip)
port = hex(int(port))[2:].zfill(4)

enc_port = ''.join([port[i:i+2] for i in range(0, len(port), 2)])

encoded_ip = int(enc_ip, 16)
encoded_port = int(enc_port, 16)

print("Encoded BigIP Cookie: %s.%s.0000" % (encoded_ip, encoded_port))
