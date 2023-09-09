# PW Crack 3
## Problem
> Can you crack the password to get the flag?
Download the password checker here and you'll need the encrypted flag and the hash in the same directory too.
There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.


[link](https://play.picoctf.org/practice/challenge/247)
### Source
- [level3.py](./level3.py)  
- [level3.hash.bin](./level3.hash.bin)
- [level3.flag.txt.enc](./level3.flag.txt.enc)
## Solution
In the [level3.py](./level3.py) file, there is a list called `pos_pw_list` which contains all the possible passwords.  
Try all the passwords and find the correct one.  
## flag
`picoCTF{m45h_fl1ng1ng_2b072a90}`
