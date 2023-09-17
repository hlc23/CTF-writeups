# Linux 102
此大題需ssh連線至指定的主機，並且使用指定的帳號密碼登入
```
$ ssh 120.114.62.209 -p 2200 -l lab
lab@120.114.62.209's password: 
Last login: Sun Sep 17 11:25:11 2023 from 150.116.151.33
lab@6efabf09ad73:~$ 
```

## Linux CTF 6
你知道如何找到Linux正在執行的服務嗎?
提示 : 2111 Port
### solution
use `ps aux` to find the service
```shell
$ ps aux              
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0  65512  5996 ?        Ss   Sep12   0:00 /usr/sbin/sshd -D
root        25  0.0  0.0  24368  2804 ?        S    Sep12   0:00 socat TCP-LISTEN:2111,reuseaddr,fork EXEC:/bin/flag
root       173  0.0  0.0  71576  4104 ?        Ss   Sep15   0:07 /usr/sbin/apache2 -k start
www-data   178  0.0  0.0 360804  4568 ?        Sl   Sep15   0:56 /usr/sbin/apache2 -k start
www-data   179  0.0  0.0 360804  4568 ?        Sl   Sep15   0:55 /usr/sbin/apache2 -k start
root      3099  0.0  0.0  65512  6128 ?        Ss   12:57   0:00 sshd: lab [priv]
lab       3101  0.3  0.0  66824  4892 ?        D    12:57   0:05 sshd: lab@pts/1
lab       3102  0.0  0.0  18256  3388 pts/1    Ss   12:57   0:00 -bash
lab       3320  0.0  0.0  34424  2892 pts/1    R+   13:24   0:00 ps aux
```
in the result, we can see that the service is listening on port 2111, and there is a path `bin/flag`
```shell
$ strings /bin/flag | grep {
BreakALLCTF{YUA7D5D0k4elbQ1XqH14}
```
## Linux CTF 7
你知道如何找到Linux正在執行的網路服務嗎?
提示 : 80 Port
### solution
use `netstat -ano` to find the service
```shell
$ netstat -ano
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       Timer
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      off (0.00/0/0)
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      off (0.00/0/0)
tcp        0      0 0.0.0.0:2111            0.0.0.0:*               LISTEN      off (0.00/0/0)
tcp        0    216 172.17.0.33:22          101.137.72.221:6462     ESTABLISHED on (0.30/0/0)
tcp6       0      0 :::22                   :::*                    LISTEN      off (0.00/0/0)
Active UNIX domain sockets (servers and established)
Proto RefCnt Flags       Type       State         I-Node   Path
unix  3      [ ]         STREAM     CONNECTED     1944072  
unix  3      [ ]         STREAM     CONNECTED     1944071  
unix  3      [ ]         DGRAM                    78228    
unix  3      [ ]         DGRAM                    78229 
```
so the port 80 is opened and that probably is a web service, so try use `curl`.
```shell
$ curl localhost:80
<!DOCTYPE html>
<html>
<head>
<title>BreakALLCTF</title>
</head>
<body>
BreakALLCTF{Ef94iSQPRI66Ws4ECqV9}
</body>
</html>
```
## Linux CTF 8
> 你知道如何在Linux下載並解壓縮ForYou檔案嗎?  
下載連結:  
http://120.114.62.217/ForYou.tar.gz
### file
[ForYou.tar.gz](./ForYou.tar.gz)
### solution
just download and extract it at local
```shell
$ wget --no-check-certificate 'http://120.114.62.217/ForYou.tar.gz' -O ForYou.tar.gz
$ tar -xf ./ForYou.tar.gz
$ cat ForYou
```
## Linux CTF 9
> 你知道如何在Linux下載TobeExe檔案嗎?  
下載連結:  
http://120.114.62.217/TobeExe

### file
[TobeExe](./TobeExe)
### solution
just download it
```shell
$ wget --no-check-certificate 'http://120.114.62.217/TobeExe' -O TobeExe
$ strings ./TobeExe | grep {
```
## Linux CTF 10
> 在Linux上只有執行檔你如何顯示重要資訊?  
下載連結:  
http://120.114.62.217/reverse

### file
[reverse](./reverse)
### solution
```shell
$ wget --no-check-certificate 'http://120.114.62.217/reverse' -O reverse
$ strings ./reverse | grep {
```
