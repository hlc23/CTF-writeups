# PPC101 writeup

## Index
- [PPC1_hello world](#ppc1_hello-world)
- [PPC2_3rd](#ppc2_3rd)
- [PPC3_beautify](#ppc3_beautify)
- [PPC4_count](#ppc4_count)
- [PPC5_lambda](#ppc5_lambda)
- [PPC6_money](#ppc6_money)
- [PPC7_calendar](#ppc7_calendar)
- [PPC8_temperature](#ppc8_temperature)

## PPC1_hello world
```bash
$ nc 120.114.62.209 2405
===== Welcome to CTF =====
You successfully reach this problem
Congratulation!!!
Wait for a few second, let me get you the flag

Here you go : CTF{Hel10WorLD123}
```

## PPC2_3rd
```bash
$ nc 120.114.62.209 2400
===== Welcome to 3rd Game =====
Can you help me find the 3rd largest number?
All numbers are unique
----- Example -----
numbers : 1 9 7 3 6 2
answer : 6
----- Now You Turn -----
numbers : 40150 86765 32378 12791 43304 45186 65988 92939 44460 62925 2904 89971 31789 41468 48104 90520 2588 97381 64981 284 7625 6980 71148 3037 20415 24263 73765 36813 50706 25676 40722 34975 63585 99784 4086 4698 48460 43906 66915 70961 4958 83750 32615 41838 78121 56093 7426 45883 20431 60039 42174 28044 57231 5861 13170 27579 2891 43194 14739 22206 40711 80634 30917 4094 86113 16953 81610 58377 18519 4330 78513 31239 78127 42511 69423 81637 19151 20214 61502 62385 81360 78650 317 88961 5738 32942 1159 36163 66253 1934 55351 72145 42510 77096 42386 86352 58348 58560 702 398
answer : 
```

### [script](./PPC2_3rd.py)
```python
from pwn import remote

r = remote('120.114.62.209', 2400)
r.recvlines(7)
data = r.recvuntil(b'\n').decode().replace('numbers : ', "")
data = [int(i) for i in data.split(' ')]
data.sort()
r.sendline(str(data[-3]).encode() + b'\n')

r.interactive()
```

## PPC3_beautify
> 幫我美化一下這句子  
規則1 : 把所有 ' -'和'_' 都換成 ' '  
規則2 : 把所有英⽂文字母換成小寫
```bash
$ nc 120.114.62.209 2401
===== Welcome to pretty shop =====
Can you help me beautify these sentences?
Rule 1 : change all ' -_' to ' '
Rule 2 : change all alphabet to lower case
----- Example -----
sentence : ThiS-iS_tEst tRY to BeautIfY_mE
answer : this is test try to beautify me
----- Now You Turn -----
sentence : INnoCent haND hUnteR mISS-TRAP sChOOL GIfT_neCK-Dip-OWE-DEFeAt aDmIrATIoN_CONFRoNTaTiON_reFEree coNtempt
answer : 
```

### [script](./PPC3_beautify.py)
```python
from pwn import remote

r = remote('120.114.62.209', 2401)
r.recvlines(8)
text = r.recvline().decode().replace('sentence : ', '').lower().replace('-', ' ').replace('_', ' ')
r.sendline(text)
r.interactive()
```

## PPC4_count
從一輸出到100
```bash
$ nc 120.114.62.209 2403
===== Welcome to counting game =====
You just need to count from 1 to 100 and get the flag
I will help you, just repeat after me
----- wave 1/100 -----
I say 1 you say?
```
### [script](./PPC4_count.py)
```py
from pwn import remote

r = remote('120.114.62.209', 2403)

r.recvlines(3)
for i in range(1, 101):
    r.recvlines(2)
    r.sendline(str(i).encode())

r.interactive()
```

## PPC5_lambda
```bash
$ nc 120.114.62.209 5124
===== Welcome to lambda =====
give you x, help us calculate f(x)
here is some functions f
f0(x) = 3x^2 + x + 3
f1(x) = 5x^2 + 8
f2(x) = 4x^3 + 6x + 6
f3(x) = 7x^3 + 5x^2
f4(x) = x^2 + 4x + 3
----- wave : example -----
function : 1
x = 2
f(x) = 28
----- wave : 1/100 -----
function : 1
x = 388
```
### [script](./PPC5_lambda.py)
```python
from pwn import struct, remote

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
```

## PPC6_money
```bash
===== Welcome to money game =====
Can you help me calculate bank interest
Give you total amount of money (will be multiple of 100) and annual interest rate
Give me the total amount of money I will have next year
----- Example -----
money : 10000
interest : 5%
answer : 10500
----- wave 1/100 -----
money : 648800
interest : 9%
answer : 
```

### [script](./PPC6_money.py)
```python
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
```

## PPC7_calendar
```bash
$ nc 120.114.62.209 2402
===== Welcome to Calendar Calculator =====
Can you help me determine which year is leap year in Gregorian Calendar?
According to Wikipedia : Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400. For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are.
----- Example -----
year : 2019
answer : ordinary
----- Example -----
year : 2020
answer : leap
----- wave 1/100 -----
year : 2918
answer : 
```
### [script](./PPC7_calendar.py)
```python
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
```

## PPC8_temperature
```bash
$ nc 120.114.62.209 5127
===== Welcome =====
I need you to transform from Fahrenheit to Celsius
----- wave : example -----
Fahrenheit : 10 (guarantee to be integer)
Celsius : -110/9
----- wave : 1/100 -----
Fahrenheit : 16
Celsius : 
```

### [script](./PPC8_temperature.py)
```python
from pwn import remote

r = remote('120.114.62.209', 5127)

r.recvlines(5)
for _ in range(100):
    r.recvline()
    x = int(r.recvline().decode().replace("\n", '').split(' ')[-1])
    ans = str((x-32)*5)+'/'+str(9)
    r.sendline(ans.encode())

r.interactive()
```
