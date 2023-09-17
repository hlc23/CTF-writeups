# Crypto101
## CRY1
> 底下是加密過的密文(ciphertext) :  
xyzqc{t3_qelrdeq_t3_k33a3a_lk3_lc_qe3p3}  
你可以解密她嗎?  
本題來自國外ABCTF的題目  
凱撒密碼:維基百科  
https://en.wikipedia.org/wiki/Caesar_cipher  
https://zh.wikipedia.org/wiki/凱撒密碼  
線上解題需特別注意有那些沒有被處理 
你可以試試看看有沒不同  
https://planetcalc.com/1434/  
http://md5decrypt.net/en/Caesar/  
https://www.xarg.org/tools/caesar-cipher/

### solution
brute force caesar cipher and find the flag start with `ABCTF{`  
## CRY2_凱撒密碼part2
> Pxevhfx mh tgzlmkhfvmy. Px ahix rhn xgchr hnk vmy. tvmy{utvd_mh_max_ynmnkx}.  
線上解題需特別注意有那些沒有被處理  
你可以試試看看有沒不同  
https://planetcalc.com/1434/  
http://md5decrypt.net/en/Caesar/  
https://www.xarg.org/tools/caesar-cipher/  
### solution
brute force caesar cipher and find the flag contain `CTF{`  
## CRY3_ROT13
> ROT13的奧秘  
OernxNYYPGS{kg_gvzr_V'yy_gel_2_ebha_ZNMldSDw}
### solution
ROT13 the ciphertext
## CRY4_ SCYTCRYPTO 密碼棒破密
> Decrypt this strange word: ERTKSOOTCMCHYRAFYLIPL  
本題目來自國外EKOPARTY CTF的題目  
解答也就會有相關文字
### solution
use scytale to decrypt the ciphertext  
and find the flag contain `EKO`
## CRY5_Vigenère cipher
> Crack the cipher: vhixoieemksktorywzvhxzijqni  
Your clue is:  
"caesar is everything. But he took it to the next level."  
Vigenère cipher  
https://en.wikipedia.org/wiki/Vigenère_cipher  
參考看看: https://www.guballa.de/vigenere-solver
### solution
"caesar is everything" means the key is `caesar`
decrypt the ciphertext with key `caesar`

## CRY6_頻率分析法
> There's an authorization code for some Thyrin Labs information here, along with someone's favorite song.
But it's been encrypted! Find the authorization code.
encrypted.txt  
Hint:  
You may want to look at what the relative frequencies of letters in english text are.  
底下網站有用:  
http://quipqiup.com/  

### file
[encrypted.txt](./encrypted.txt)
### solution
use frequency analysis to decrypt the ciphertext then flag is in the content

## CRY7_Rail Fence Cipher
> 你會Rail Fence Cipher 籬笆式位移密碼嗎?  
跟著Wiki學Rail fence cipher https://en.wikipedia.org/wiki/Rail_fence_cipher  
解底下題目吧! 密文如下:  
Ta _7N6DE7hlg:W3D_H3C31N__BD4ef sHR053F38N43D47 i33___NC 
<br></br>
使用四層籬笆(rail fence with 4 rails)  
答案格式:BreakAllCTF{flag}  
https://www.dcode.fr/rail-fence-cipher  

### solution
use rail fence cipher to decrypt the ciphertext

## CRY8_ROT47
> 你知道下列文字如何解密嗎？
<br></br>
qC62<p{{r%uL(92E0`D0#_%cfnm]kN

### solution
ROT47 the ciphertext


