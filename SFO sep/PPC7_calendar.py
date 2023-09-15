from pwn import struct, remote

shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"

def p32(x):
    return struct.pack('I', x)
def p64(x):
    return struct.pack('Q', x)

def leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

r = remote('120.114.62.209', 2402)
r.recvlines(9)
for _ in range(100):
    r.recvline()
    year = r.recvline().decode().split(' ')[-1]
    r.sendline(str('leap' if leap(int(year)) else 'ordinary').encode())


r.interactive()