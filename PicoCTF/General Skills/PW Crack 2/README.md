# PW Crack 2
## Problem
> Can you crack the password to get the flag?
Download the password checker [here](https://artifacts.picoctf.net/c/15/level2.py) and you'll need the encrypted [flag](./https://artifacts.picoctf.net/c/15/level2.flag.txt.enc) in the same directory too.


[link](https://play.picoctf.org/practice/challenge/246)
### Source
- [level2.py](./level2.py)
- [level2.flag.txt.enc](./level2.flag.txt.enc)
## Solution
In the `level2.py`, there is a line 
```python
if( user_pw == chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65) ):
```
that means the password is `39ce`.
## flag
`picoCTF{tr45h_51ng1ng_502ec42e}`