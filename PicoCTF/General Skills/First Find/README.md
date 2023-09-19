# First Find
## Problem
> Unzip this archive and find the file named 'uber-secret.txt'
Download zip file

[link](https://play.picoctf.org/practice/challenge/320)
### Source
- [files.zip](./files.zip)
## Solution
```shell
binwalk -er ./files.zip 
find -name uber-secret.txt
cat <file>
```
## flag
`picoCTF{f1nd_15_f457_ab443fd1}`