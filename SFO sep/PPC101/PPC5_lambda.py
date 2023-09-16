from pwn import remote

r = remote('120.114.62.209', 5124)

def f0(x):
    return 3*x*x+x+3
def f1(x):
    return 5*x*x+8
def f2(x):
    return 4*x*x*x+6*x+6
def f3(x):
    return 7*x*x*x+5*x*x
def f4(x):
    return x*x+4*x+3

r.recvlines(12)

for _ in range(100):
    print(_)
    r.recvline(1)
    call = int(r.recvuntil(b'\n').decode().replace('\n', '').split(' ')[-1])
    x = int(r.recvuntil(b'\n').decode().replace('\n', '').split(' ')[-1])
    if call == 0:
        ans = f0(x)
    elif call == 1:
        ans = f1(x)
    elif call == 2:
        ans = f2(x)
    elif call == 3:
        ans = f3(x)
    elif call == 4:
        ans = f4(x)
    r.sendline(str(ans).encode())
r.interactive()