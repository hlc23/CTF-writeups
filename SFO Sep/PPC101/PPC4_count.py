from pwn import struct, remote

r = remote('120.114.62.209', 2403)

r.recvlines(3)
for i in range(1, 101):
    r.recvlines(2)
    r.sendline(str(i).encode())

r.interactive()