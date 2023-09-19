# chrono
## Problem
> How to automate tasks to run at intervals on linux servers?

[link](https://play.picoctf.org/practice/challenge/347)
## Solution
先`ssh`連到題目給的機器
```shell
ssh <IP> -p <PORT> -l <USERNAME>
```
linux 有個內建的排程工具`crontab`(我不知道那啥)  
`crontab`的設定檔在`/etc/crontab`
```shell
cat /etc/crontab
```
## flag
`picoCTF{Sch3DUL7NG_T45K3_L1NUX_1b4d8744}`