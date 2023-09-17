# 隱寫術101
## STEG1_STEG(必)
> 你知道駭客如何將隱藏的訊息藏到Word中嗎?
本題任務是請你找出以下Word中隱藏的flag。
<br></br>
隱寫術(Steganography)是一種訊息隱藏的技術，所謂訊息隱藏指的是不讓接收者之外的任何人看到隱藏訊息的內容。
有各種類型的隱寫術:
Document Stegonagraphy:各種文件類型的隱寫術[本題示範文件類型的隱藏術]
Image Stegonagraphy:隱藏在圖片的機密
Audio Stegonagraphy:隱藏在聲音的機密
Video Stegonagraphy:隱藏在影片的機密
<br></br>
CTF是藏flag在各種再體
壞蛋是藏木馬和惡意程式在word/ppt/pdf/jpg/Mp3/Mp4
所以不要隨便下載咚咚!危險!

### file
[chapter1.docx](./chapter1.docx)
### solution
upload to microsoft word online

## STEG2_Secret in PDF
> 文件隱寫術之PDF可以藏詩文
### file
[steg2.pdf](./steg2.pdf)
### solution
`ctrl+a` to select all text in pdf and copy to notepad

## STEG3
> 圖片裡確實有你要的Flag  
把她找出來吧!
<br></br>
本題出自國外CTF題目
<br></br>
[解答格式]ABCTF{XXXXXXXXXXXXXXX}
<br></br>
Linux有許多指令可以看看  
file  
strings

### file
[just_open_it.jpg](./just_open_it.jpg)
### solution
```bash
strings ./just_open_it.jpg | grep {
```

## STEG4
> Carter喜歡登山去吃香蕉,有圖為證!  
聽說這張圖片藏了機密  
Can you find it?  
圖片隱藏術  

### file
[carter.jpg](./carter.jpg)
### solution
use `binwalk` to check file
```
$ binwalk -e -r ./carter.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
382           0x17E           Copyright string: "Copyright (c) 1998 Hewlett-Packard Company"
3192          0xC78           TIFF image data, big-endian, offset of first image directory: 8
140147        0x22373         JPEG image data, JFIF standard 1.01
140177        0x22391         TIFF image data, big-endian, offset of first image directory: 8
```
the result show there are two image in this file  
the second image is shifted by 140147 bytes  
use `dd` to extract image
```
$ dd if=carter.jpg of=flag skip=140147 bs=1
```
the flag is in the second image

## STEG5_Flag in Black & White
> chal.png  
stegsolve
### file
[chal.png](./chal.png)
### solution
Use online tool like [this](https://stegonline.georgeom.ne) to check the image  
In `LSB Half` tab, we can see the flag
