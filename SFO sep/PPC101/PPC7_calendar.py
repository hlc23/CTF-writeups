from pwn import remote

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