# Transformation
## Problem
> I wonder what this really is... [enc](https://mercury.picoctf.net/static/2b4cea9b07db22bf4f933fddd1b8caa9/enc) `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`

[link](https://play.picoctf.org/practice/challenge/104)
### Source
[enc](./enc)
## Solution
Use UTF16 to encode `enc`
## flag
`picoCTF{16_bits_inst34d_of_8_04c0760d}`