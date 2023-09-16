from pwn import remote

r = remote('120.114.62.209', 2407)

r.recvlines(8)
for _ in range(100):
    r.recvline(1)
    base = r.recvline().decode().split(" ")[-1].replace("\n", '')
    p = r.recvline().decode().split(" ")[-1].replace('%', '').replace("\n", '')
    r.recvuntil(b':')
    ans = int(int(base)*(int(p)+100)/100)
    r.sendline(str(ans).encode())

r.interactive()