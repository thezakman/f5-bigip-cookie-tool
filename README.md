# f5-bigip-decode
Python 3 script to encode/decode F5 BigIP cookies.

Based on instructions at: https://support.f5.com/csp/article/K6917

# Usage
-Decode
bigip-decode.py -c 0000000000.00000.000
Where -c is your F5 BigIP cookie.

```
❯ python3 bigip-decode.py -c 2684427692.51205.0000
F5 BigIP cookie:  2684427692.51205.0000
Decoded cookie (IP address:Port): 172.29.1.160:1480
```

-Encode
bigip-encode.py 127.0.0.1 80

```
❯ python3 bigip-encode.py 172.29.1.160 1480
Encoded BigIP Cookie: 2684427692.51205.0000
```


