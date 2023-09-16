from pwn import remote

r = remote('120.114.62.209', 5127)

r.recvlines(5)
for _ in range(100):
    r.recvline()
    x = int(r.recvline().decode().replace("\n", '').split(' ')[-1])
    ans = str((x-32)*5)+'/'+str(9)
    r.sendline(ans.encode())

r.interactive()