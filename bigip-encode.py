import sys

ip, port = sys.argv[1], sys.argv[2]
ip = ip.split('.')
ip.reverse()
enc_ip = []

for i in ip:
    enc_ip.append(hex(int(i))[2:])

enc_ip = ''.join(map(lambda x: x.zfill(2), enc_ip))
port = hex(int(port))[2:]
enc_port = []

for i in range(0, len(port), 2):
    enc_port.append(str(port[i:i+2]))

enc_port.reverse()
enc_port = ''.join(enc_port)

print("Encoded BigIP Cookie: %s.%s.0000" % (int(enc_ip, 16), int(enc_port, 16)))