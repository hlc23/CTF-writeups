# Crypto102

## CRY11_PythonCrypto
> 錒錒去參加BREAKALLCTF 練習賽, 其中有一題密碼學的破密分析 讓她昏頭  
你能教她如何解這題嗎?  
密文(ciphertext)如下  
cvqBeqacRtqazEigwiAobxrKobxrAobxrLwgk8Lwgk8CrtuiTzahfFreqc{bnjrZwgk8Ikgd4Pj85ePgb_e_rwqr7fvbmHjklo3tews_hmkogooyf0vbnk0ii87Drfgh_n kiwutfb0ghk9ro987k5tfb_hjiouo087ptfcv}

題目是源自BreakAll CTF 可以猜測flag開頭是BREAKAll  
觀察密文發現有些字母大寫似乎具有規律
除去前三個字母後 將後面的字元每五個為一組 並將每組的第一個字母取出

### [script](./CRY11.py)

## CRY12_變形caesar密碼
> 有一題RC3 CTF的題目困擾小梅許久,你能幫她解出來嗎?  
“The fault, dear Brutus, is not in our stars, but in ourselves.”
(I.ii.141) Julius Caesar in William Shakespeare’s Julius Caesar  
密文(CipherText): 7sj-ighm-742q3w4t

題目是源自RC3 CTF 可以猜測flag開頭是RC3  
密文中有數字 猜測字母表中應該包含數字
枚舉出所有可能的結果 並找出開頭為`RC3`的結果

### [script](./CRY12.py)

## CRY13_affine-cipher
> 巅巅去參加國外CTF競賽,其中有一題讓她困擾不已. 你能幫她解出來嗎?  
她只記得加密規則如下: for each letter of cipher text its position in the alphabet is the position of the original letter multiplied by 4 and shifted by 15 character  
shift over alphabet is cyclic, so 'z' shifted by 1 is _ and _ shifted by 1 is 'a'  
aplhabet consists of letters from 'a' to 'z' and symbol '_'  
letter 'a' has position 0, symbol '_' has position 26 (following 'z')  
密文如下: ifpmluglesecdlqp_rclfrseljpkq

### solution
使用affine cipher的解密工具解密
[like this](https://crypto.interactive-maths.com/affine-cipher.html)  
將 `_` 加入字母集, `a`設為4, `b`設為15  
進行解密

## CRY14_加密的奧義
> 阿義去參加CTF競賽,有一題困擾他許久,你能完成底下加密方法嗎?  
加密方法: 將每個數字 mod 37後所得到的答案依序轉成對應的字母: 0-25 對應到大寫的英文字母(0是A, 1是B,...依此類推), 26-35對應到0-9數字, 36 對應到底線('_').    
數字: 91 322 57 114 40 406 272 147 239 285 353 272 77 110 296 262 299 323 255 337 150 102  
答案格式:BreakallCTF{加密後的答案}

### [script](./CRY14.py)

