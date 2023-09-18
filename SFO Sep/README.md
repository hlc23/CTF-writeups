# Security Focus Online 2023 9月場 課程內容
# 目錄
- [數字系統](#數字系統)
- [編碼與解碼 (Encoding & Decoding)](#編碼與解碼-encoding--decoding)
  - [線上工具](#線上工具)
    - [延伸內容](#延伸內容)
- [網路安全入門 (Web Security)](#網路安全入門-web-security)
    - [HTTP Request Sample](#http-request-sample)
    - [HTTP Response Sample](#http-response-sample)
    - [開發者工具](#開發者工具)
    - [robots.txt](#robotstxt)
    - [curl (CommandLine URL)](#curl-commandline-url)
- [古典密碼學 (Classical Cryptography)](#古典密碼學-classical-cryptography)
    - [密碼學的基本術語](#密碼學的基本術語)
    - [替換式密碼 (Substitution Cipher)](#替換式密碼-substitution-cipher)
        - [凱薩密碼 (Caesar Cipher)](#凱薩密碼-caesar-cipher)
        - [ROT13 / ROT47](#rot13--rot47)
        - [仿射密碼 (Affine cipher)](#仿射密碼-affine-cipher)
        - [維吉尼亞密碼 (Vigenère cipher)](#維吉尼亞密碼-vigenère-cipher)
        - [維吉尼亞密碼表](#維吉尼亞密碼表)
        - [頻率分析 (Frequency analysis)](#頻率分析-frequency-analysis)
    - [置換式密碼 (Transposition Cipher)](#置換式密碼-transposition-cipher)
        - [密碼棒 (Scytale)](#密碼棒-scytale)
        - [柵欄密碼 (Rail Fence Cipher)](#柵欄密碼-rail-fence-cipher)
- [Linux](#linux)
- [隱寫術(Steganography)](#隱寫術steganography)
    - [LSB](#lsb)
    - [解題方法](#解題方法)
- [鑑識分析(Forensics)](#鑑識分析forensics)
    - [wireshark](#wireshark)
- [Python 基礎語法](#python-基礎語法)
- [Python 資安應用](#python-資安應用)
  - [base64 編碼/解碼](#base64-編碼解碼)

我寫到linux的部份看到那一推指令就決定改成只寫我學到的  
前面寫好的就算了 lol

# 數字系統
- 10進位(Decimal): 0~9
- 2進位(Binary): 0~1
- 8進位(Octal): 0~7
- 16進位(Hexadecimal): 0~9 + A~F
# 編碼與解碼 (Encoding & Decoding)
- ASCII
- morse code
- base64
- base32
- unicode
- URL
## 線上工具
- [CyberChef](https://gchq.github.io/CyberChef/)
### 延伸內容
- 曼徹斯特編碼
- 霍夫曼編碼

# 網路安全入門 (Web Security)
- HTTP Requests method:  
    GET、POST、PUT、TRACE、DELETE、HEAD、OPTIONS、CONNECT
- HTTP Response status code:
    - 1xx: Informational
    - 2xx: Success
    - 3xx: Redirection
    - 4xx: Client Error 
    - 5xx: Server Error
### HTTP Request Sample
Use curl
```
> GET / HTTP/1.1           // 使用 GET 方法
> Host: google.com         // 設定 Host
> User-Agent: curl/7.81.0  // 設定 User-Agent
> Accept: */*    
```
### HTTP Response Sample
```
< HTTP/1.1 301 Moved Permanently            // HTTP Response status code
< Location: http://www.google.com/          // 來源網址
< Content-Type: text/html; charset=UTF-8
< Content-Security-Policy-Report-Only: object-src 'none';base-uri 'self';script-src 'nonce-Ed_ycpTSJ8g610VRdkYF4Q' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
< Date: Mon, 18 Sep 2023 13:57:12 GMT
< Expires: Wed, 18 Oct 2023 13:57:12 GMT
< Cache-Control: public, max-age=2592000
< Server: gws
< Content-Length: 219
< X-XSS-Protection: 0
< X-Frame-Options: SAMEORIGIN
<                                           // 以下為內文
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>
```
## 開發者工具
F12
## robots.txt
規範搜尋引擎爬蟲對整個網站的存取限制  
通常置於網站的公開資料夾下  
有些雖然上面寫不行但有能力的爬蟲還是會爬  
## curl (CommandLine URL)
在 Command Line 的環境下，透過 HTTP 協定及利用 URL 規則進行資訊傳遞的工具。  
curl 指令格式：`curl [參數] <網址>`。
|參數說明如下  ||
|-|-|
|-v| 輸出更多的訊息方便 debug  |
|-X \<Request method> | 使用指定的 http method 來發出 http request  |
|-u| 攜帶使用者帳號、密碼  | 
|-O| 依原始檔名下載  |
|-d| 攜帶 HTTP POST Data  |
[參考資源](https://blog.techbridge.cc/2019/02/01/linux-curl-command-tutorial/)
### sample
使用 curl 發送 OPTIONS 請求 來檢查該網站支援的請求方法
```shell
curl -X OPTIONS https://www.google.com
< HTTP/2 405 
< allow: GET, HEAD
< date: Mon, 18 Sep 2023 14:07:51 GMT
< content-type: text/html; charset=UTF-8
< server: gws
< content-length: 1592
< x-xss-protection: 0
< x-frame-options: SAMEORIGIN
< alt-svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
< 
* TLSv1.2 (IN), TLS header, Supplemental data (23):
<!DOCTYPE html>
...
```
在Allow中可以看到該網站只支援`GET`、`HEAD`方法
# 古典密碼學 (Classical Cryptography)
古典與現代的差別:
- 古典密碼學: 以數學為基礎, 利用旋轉、替換、位移等方式進行加密
- 現代密碼學: 以電腦科學為基礎, 基於位元運算的加密方式
## 密碼學的基本術語
- 明文(Plaintext): 未加密的訊息
- 密文(Ciphertext): 加密後的訊息
- 加密(Encryption): 將明文轉換成密文的過程
- 解密(Decryption): 將密文轉換成明文的過程
## 替換式密碼 (Substitution Cipher)
### 凱薩密碼 (Caesar Cipher)
將明文中的每個字母都替換成字母表中固定位移的字母
### ROT13 / ROT47
ROT13: 將字母表中的每個字母都替換成字母表中固定位移13的字母  
ROT47: 將ASCII表中的每個字元都替換成ASCII表中固定位移47的字元
```
ROT13: 
ABCDEFGHIJKLMNOPQRSTUVWXYZ

ROT47:
!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO
PQRSTUVWXYZ[\]^_\`abcdefghijklmnopqrstuvwxyz{|}~
```
### 仿射密碼 (Affine cipher)
依字元位置 x 乘上函數後再做模運算，取得新的位置即為加密後字元。
$$
e(x) = ax + b \pmod{m} \\
d(x) = a^{-1}(x - b) \pmod{m}
$$
其中 a、m 互質，m 為字元集合大小，b 為位移量。
### 維吉尼亞密碼 (Vigenère cipher)
將明文中的每個字母都替換成字母表中固定位移的字母，但位移量會隨著明文的位置而改變。  
明文：`ATTACKATDAWN`  
密鑰：`LEMONLEMONLE`  
密文：`LXFOPVEFRNHR`  
以明文第2個字母T說明: $P_i$ = 19、對應密鑰字母為`E`: $K_i$ = 4，所以加密後 $C_i$ = 23，其對應字母為 `X` 
#### 維吉尼亞密碼表
![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Vigen%C3%A8re_square.svg/450px-Vigen%C3%A8re_square.svg.png)
### 頻率分析 (Frequency analysis)
利用語言中字母及單字出現的頻率來破解密文  
[線上工具](https://quipqiup.com/)
## 置換式密碼 (Transposition Cipher)
### 密碼棒 (Scytale)
[我找到的範例影片](https://www.youtube.com/watch?v=_vIb6Y45ERQ)  
密碼棒是個可使的傳遞訊息字母順序改變的工具，由一條加工過、且有夾帶訊息的載體繞在一個木棒所組成。  
### 柵欄密碼 (Rail Fence Cipher)
將明文中的字母依照一定的規則填入矩陣中，再將矩陣中的字母依照一定的規則讀出來。
#### sample
```
W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . A . . . I . . . V . . . D . . . E . . . N . .
```
Plaintext:`WEAREDISCOVEREDFLEEATONCE`  
Ciphertext:`WECRLTEERDSOEEFEAOCAIVDEN`
# Linux 
一些常用指令、檔案結構、權限等等
# 隱寫術(Steganography)
## LSB
最低有效位元(Least Significant Bit)  
利用人眼對RGB的感受度, 改變圖片中像素的最低有效位元, 來儲存訊息  
[線上工具](https://stegonline.georgeom.net/upload)
## 解題方法
- binwalk
- dd
- strings
- exiftool
# 鑑識分析(Forensics)
## wireshark
是一個免費開源的網路封包分析(network protocol analyzer)軟體。  
最常見功能就是截取(capture)網路封包，並盡可能顯示出最為詳細的網路封包資料。
![](https://media.geeksforgeeks.org/wp-content/uploads/20220812133910/ws.jpg)
# Python 基礎語法
~~你怎麼覺得我會寫東西在這~~
# Python 資安應用
## base64 編碼/解碼
```python
import base64
>>> base64.b64decode(b'TWFu')
b'Man'
>>> base64.b64encode(b'ABCD') 
b'QUJDRA=='
```