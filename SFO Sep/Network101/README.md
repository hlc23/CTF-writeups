# Network101
## NET1
> 題目來自CSAW Quals CTF 2013: Networking 1
<br></br>
file
<br></br>
strings

### file
[networkingOK.pcap](./networkingOK.pcap)
### solution
```bash
$ strings ./networkingOK.pcap 
38400,38400
XTERM
Ubuntu 12.04.2 LTS
hockeyinjune-virtual-machine login: 
Password: 
flag{d316759c281bf925d600be698a4973d5}
Login incorrect
hockeyinjune-virtual-machine login: 
```

## NET2
> Someone intercepted a chat between illustris and codelec
<br></br>
BITSCTF 2017 : woodstock-1-10

### file
[ws1_2.pcapng](./ws1_2.pcapng)
### solution
```bash
$ strings ./ws1_2.pcapng | grep CTF
$MyPass BITSCTF{such_s3cure_much_w0w}|
```
## NET3_Wireshark封包分析
> The shark won't bite you. Don't worry, it's wired!
<br></br>
答案格式:IW{xxxxxxxxxxxxxxx}
<br></br>
題目來源:Internetwache-CTF-2016:Network Forensic(MUST)

### file
- [dump.pcap](./dump.pcap)
- [flag.zip](./flag.zip)
### solution
open dump.pcap with wireshark and look for the http packet
![Alt text](image.png)
look for the packet with `GET /flag.zip`  
```http packet
Frame 61: 540 bytes on wire (4320 bits), 540 bytes captured (4320 bits)
Ethernet II, Src: 00:00:00_00:00:00 (00:00:00:00:00:00), Dst: 00:00:00_00:00:00 (00:00:00:00:00:00)
Internet Protocol Version 4, Src: 192.168.1.41, Dst: 192.168.1.41
Transmission Control Protocol, Src Port: 53968, Dst Port: 8080, Seq: 1, Ack: 1, Len: 474
Hypertext Transfer Protocol
    GET /flag.zip HTTP/1.1\r\n
    Host: 192.168.1.41:8080\r\n
    Connection: keep-alive\r\n
    Authorization: Basic ZmxhZzphenVsY3JlbWE=\r\n
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n
    Upgrade-Insecure-Requests: 1\r\n
    User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36\r\n
    DNT: 1\r\n
    Referer: http://192.168.1.41:8080/\r\n
    Accept-Encoding: gzip, deflate, sdch\r\n
    Accept-Language: en-US,en;q=0.8,ht;q=0.6\r\n
    \r\n
    [Full request URI: http://192.168.1.41:8080/flag.zip]
    [HTTP request 1/1]
    [Response in frame: 83]
```
at the Authorization field, we can see the base64 encoded string `ZmxhZzphenVsY3JlbWE=`  
decode it and we get `flag:azulcrema`  
open the flag.zip with the password `azulcrema` and we get the flag.txt

## NET4_Special Agent User(MUST)
> We can get into the Administrator's computer with a browser exploit.  
But first, we need to figure out what browser they're using.  
Perhaps this information is located in a network packet capture we took: data3.pcap.  
Enter the browser and version as "BrowserName BrowserVersion".
<br></br>
NOTE: We're just looking for up to 3 levels of subversions for the browser version (ie. Version 1.2.3 for Version 1.2.3.4) and ignore any 0th subversions (ie. 1.2 for 1.2.0)
<br></br>
PicoCTF_2017: Special Agent User(MUST)  
Hint:  
Where can we find information on the browser in networking data?  
Maybe try reading up on user-agent strings.

### file
[data3.pcap](./data3.pcap)
### solution
open `data3.pcap` with wireshark.
find user-agent which is about the browser information.
![Alt text](image-1.png)
so the flag will be `Chrome 36.0.1985`

