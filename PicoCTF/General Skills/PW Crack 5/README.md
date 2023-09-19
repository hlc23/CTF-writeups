# PW Crack 5
## Problem
> Can you crack the password to get the flag?
Download the password checker here and you'll need the encrypted flag and the hash in the same directory too. Here's a dictionary with all possible passwords based on the password conventions we've seen so far.

[link](https://play.picoctf.org/practice/challenge/249)
### Source
- [level5.py](./level5.py)
- [level5.flag.txt.enc](./flag.txt.enc)
- [level5.hash.bin](./level5.hash.bin)
- [dictionary.txt](./dictionary.txt)
## Solution
Rewrite the code to brute force the possible password.
```python
# level_5_pw_check()

for line in open('./dictionary.txt', mode="r"):
    line = line.strip()
    if hash_pw(line) == correct_pw_hash:
        print("Password is: " + line)
        print("Flag is: " + str_xor(flag_enc.decode(), line))
        break
```
## flag
