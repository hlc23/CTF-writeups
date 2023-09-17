# 編碼102
## Internetwache CTF 2016: The hidden message
> My friend really can’t remember passwords. So he uses some kind of obfuscation(代碼混淆).  
Can you restore the plaintext?  
Attachment: [misc50.zip](./misc50.zip)
### file
[misc50.zip](./misc50.zip)
### solution
使用`binwalk`檢查檔案並提取出來
```bash
$ binwalk -e ./misc50.zip 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Zip archive data, at least v1.0 to extract, name: task/
63            0x3F            Zip archive data, at least v2.0 to extract, compressed size: 120, uncompressed size: 268, name: task/README.txt
416           0x1A0           End of Zip archive, footer length: 22
```
解壓縮後得到`task/README.txt`，內容如下
```
0000000 126 062 126 163 142 103 102 153 142 062 065 154 111 121 157 113
0000020 122 155 170 150 132 172 157 147 123 126 144 067 124 152 102 146
0000040 115 107 065 154 130 062 116 150 142 154 071 172 144 104 102 167
0000060 130 063 153 167 144 130 060 113 012
0000071
```
猜測應為8進制 進行轉換得  
`V2VsbCBkb25lIQoKRmxhZzogSVd7TjBfMG5lX2Nhbl9zdDBwX3kwdX0K`  
base64解碼得到flag
```bash
echo V2VsbCBkb25lIQoKRmxhZzogSVd7TjBfMG5lX2Nhbl9zdDBwX3kwdX0K | base64 -d
```

## alexctf-2017: CR1: Ultracoded
> Fady didn't understand well the difference between encryption and encoding, so instead of encrypting some secret message to pass to his friend, he encoded it!  
Hint: Fady's encoding doens't handly any special character

### file
[zero_one.txt](./zero_one.txt)
### solution
open `zero_one.txt` see the content  
it's a ton of `zero` and `one` so turn it into binary with `zero` as `0` and `one` as `1` then convert to ASCII  
```
Li0gLi0uLiAuIC0uLi0gLS4tLiAtIC4uLS4gLSAuLi4uIC4tLS0tIC4uLi4uIC0tLSAuLS0tLSAuLi4gLS0tIC4uLi4uIC4uLSAuLS0uIC4uLi0tIC4tLiAtLS0gLi4uLi4gLiAtLi0uIC4tLiAuLi4tLSAtIC0tLSAtIC0uLi0gLQ==
```
looks like base64 so decode it  
```
.- .-.. . -..- -.-. - ..-. - .... .---- ..... --- .---- ... --- ..... ..- .--. ...-- .-. --- ..... . -.-. .-. ...-- - --- - -..- -
```
it is morse code so decode it  
```
ALEXCTFTH15O1SO5UP3RO5ECR3TOTXT
```
looks like a flag because of `ALEXCTF` so add `{}` and replace `O` with `_`

## SECCON CTF 2014: Easy Cipher
> 多元編碼方案  
試著解解看吧!
### file
[ciphertxt.txt](./ciphertxt.txt)
### solution
open `ciphertxt.txt` and it looks like a bunch of binary, octal, hex, ASCII
so convert them to ASCII  
[script](./main.py)