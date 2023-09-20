# flag_shop
## Problem
> There's a flag shop selling stuff, can you buy a flag? Source.  
Connect with nc jupiter.challenges.picoctf.org 9745.

[link](https://play.picoctf.org/practice/challenge/49)
### Source
- [store.c](./store.c)
## Solution
shell 連線到 `jupiter.challenges.picoctf.org 9745` 摸索一下後發現  
能購買的選項有兩項 一項買不起, 推測要從另一項下手  
觀察程式碼後發現, 購買數量只能是正數, 好像可以嘗試溢位  
輸入一個足夠大的數字後, 金錢確實增加  
就可以拿去買flag了
## flag
Everyone's flag is different.