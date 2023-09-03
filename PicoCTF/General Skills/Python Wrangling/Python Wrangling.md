# Python Wrangling
## Problem
> Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/ende.py) using [this password](https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/pw.txt) to get [the flag](https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/flag.txt.en)?

[link](https://play.picoctf.org/practice/challenge/166)
### Source
- [ende.py](./ende.py)
- [pw.txt](./pw.txt)
- [flag.txt.en](./flag.txt.en)
## Solution
```bash
cat ./pw.txt | python3 ende.py -d flag.txt.en
```
## flag
`picoCTF{4p0110_1n_7h3_h0us3_aa821c16}`