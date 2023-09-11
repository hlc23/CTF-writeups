# fixme2.py
## Problem
> Fix the syntax error in the Python script to print the flag.
[Download Python script](https://artifacts.picoctf.net/c/4/fixme2.py)

[link](https://play.picoctf.org/practice/challenge/241)
### Source
- [fixme2.py](./fixme2.py)
## Solution
fix the syntax error in line 22 from
```py
# Check that flag is not empty
if flag = "":
  print('String XOR encountered a problem, quitting.')
else:
  print('That is correct! Here\'s your flag: ' + flag)
```
to 
```py
# Check that flag is not empty
if flag == "":
  print('String XOR encountered a problem, quitting.')
else:
  print('That is correct! Here\'s your flag: ' + flag)
```
## flag
`picoCTF{3qu4l1ty_n0t_4551gnm3nt_e8814d03}`