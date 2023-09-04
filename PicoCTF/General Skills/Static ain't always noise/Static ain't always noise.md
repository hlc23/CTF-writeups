# Static ain't always noise
## Problem
> Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/bc72945175d643626d6ea9a689672dbd/static)? This [BASH script](https://mercury.picoctf.net/static/bc72945175d643626d6ea9a689672dbd/ltdis.sh) might help!

[link](https://play.picoctf.org/practice/challenge/163)
### Source
[static](./static)
[ltdis.sh](./ltdis.sh)
## Solution
```bash
strings static | grep picoCTF
```
## flag
`picoCTF{d15a5m_t34s3r_1e6a7731}`