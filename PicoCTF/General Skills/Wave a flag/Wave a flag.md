# Name
## Problem
> Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/a14be2648c73e3cda5fc8490a2f476af/warm) has extraordinarily helpful information...

[link](https://play.picoctf.org/practice/challenge/170)
### Source
[warm](./warm)
## Solution
```bash
strings warm | grep picoCTF
```
## flag
`picoCTF{b1scu1ts_4nd_gr4vy_755f3544}`