from pwn import remote

r = remote('120.114.62.209', 2400)
r.recvlines(7)
data = r.recvuntil(b'\n').decode().replace('numbers : ', "")
data = [int(i) for i in data.split(' ')]
data.sort()
r.sendline(str(data[-3]).encode() + b'\n')

r.interactive()
