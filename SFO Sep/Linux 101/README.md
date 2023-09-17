# Linux 101
此大題需ssh連線至指定的主機，並且使用指定的帳號密碼登入
```
$ ssh 120.114.62.209 -p 2200 -l lab
lab@120.114.62.209's password: 
Last login: Sun Sep 17 11:25:11 2023 from 150.116.151.33
lab@6efabf09ad73:~$ 
```

## Linux CTF 1
你知道如何安全連線到遠端伺服器嗎?
### solution

```shell
cat ./flag 
BreakALLCTF{Sobkjgd14VuIFBUtgVts}
```

## Linux CTF 2
你知道如何在Linux上找到隱藏檔案嗎?
```shell
ls -a
.  ..  .bash_logout  .bashrc  .hidden  .profile  base64.txt  flag  hex.txt
cat .hidden
BreakALLCTF{WucLSg4cxPNYuXFF5XxJ}
```

## Linux CTF 3
你知道如何在Linux上做16進位轉字串(hex to string)嗎?
### solution
I just cat the `hex.txt` and copy to decoder

## Linux CTF 4
你知道如何在Linux上做base64 解碼嗎?
### solution
```shell
cat ./base64.txt | base64 -d
```
or cat then copy to decoder

## Linux CTF 5
你知道如何在Linux上找到secret秘密檔案嗎?
```shell
$ find / -name secret
/opt/secret
$ cat /opt/secret
```
