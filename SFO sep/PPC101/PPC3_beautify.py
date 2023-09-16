from pwn import remote

r = remote('120.114.62.209', 2401)
r.recvlines(8)
text = r.recvline().decode().replace('sentence : ', '').lower().replace('-', ' ').replace('_', ' ')
r.sendline(text)
r.interactive()