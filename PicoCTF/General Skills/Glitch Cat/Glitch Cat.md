# Glitch Cat
## Problem
> Our flag printing service has started glitching!  
`$ nc saturn.picoctf.net 52682`

[link](https://play.picoctf.org/practice/challenge/242)
### Source
## Solution
1. ```sh
    $ nc saturn.picoctf.net 52682
    ```
    get output `'picoCTF{gl17ch_m3_n07_' + chr(0x62) + chr(0x64) + chr(0x61) + chr(0x36) + chr(0x38) + chr(0x66) + chr(0x37) + chr(0x35) + '}'`
2. write simple [python script](./script.py)
    ```py
    print('picoCTF{gl17ch_m3_n07_' + chr(0x62) + chr(0x64) + chr(0x61) + chr(0x36) + chr(0x38) + chr(0x66) + chr(0x37) + chr(0x35) + '}')
    ```
## flag
`picoCTF{gl17ch_m3_n07_bda68f75}`