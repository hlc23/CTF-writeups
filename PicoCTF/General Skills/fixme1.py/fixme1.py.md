# fixme1.py
## Problem
> Fix the syntax error in this Python script to print the flag.
[Download Python script](https://artifacts.picoctf.net/c/27/fixme1.py)

[link](https://play.picoctf.org/practice/challenge/240)
### Source
- [fixme1.py](./fixme1.py)
## Solution
fix the syntax error in line 20
from
```py=19
flag = str_xor(flag_enc, 'enkidu')
  print('That is correct! Here\'s your flag: ' + flag)
```
to
```py=19
flag = str_xor(flag_enc, 'enkidu')
print('That is correct! Here\'s your flag: ' + flag)
```
## flag
`picoCTF{1nd3nt1ty_cr1515_182342f7}`