# Big Zip
## Problem
> Unzip this archive and find the flag.

[link](https://play.picoctf.org/practice/challenge/322)
### Source
- [big-zip-files.zip](./big-zip-files.zip)
## Solution
```shell
binwalk -er big-zip-files.zip
grep -r picoCTF ./
```
## flag
`picoCTF{gr3p_15_m4g1c_ef8790dc}`