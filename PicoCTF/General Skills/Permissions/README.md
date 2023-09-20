# Permissions
## Problem
> Can you read files in the root file?

[link](https://play.picoctf.org/practice/challenge/363)
## Solution
1. `ssh` into the server
2. `cd` into the root directory
3. `ls` to see the files
```shell
picoplayer@challenge:/$ ls
bin   challenge  etc   lib    lib64   media  opt   root  sbin  sys  usr
boot  dev        home  lib32  libx32  mnt    proc  run   srv   tmp  var
```
we can see there is a folder called `challenge` but we dont have permission to enter it.
4. `sudo -l` to see what permissions we have.
```shell
picoplayer@challenge:/$ sudo -l
Matching Defaults entries for picoplayer on challenge:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User picoplayer may run the following commands on challenge:
    (ALL) /usr/bin/vi
```
5. use `vim` to enter `/challange/`.
```shell
sudo vi /challange/
```
6. and we can see a file `challenge/metadata.json` and flag in it.
## flag
`picoCTF{uS1ng_v1m_3dit0r_3dd6dcf4}`