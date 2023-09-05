# Mind your Ps and Qs
## Problem
> In RSA, a small e value can be problematic, but what about N? Can you decrypt this?  [values](https://mercury.picoctf.net/static/51d68e61bb41207a55f24e753f07c5a3/values)

[link](https://play.picoctf.org/practice/challenge/162)
### Source
[values](./values)
## Solution
1. find the phi of N from this [web](https://www.alpertron.com.ar/ECM.HTM)  
`phi = 1280678415822214057864524798453297819181234364596418 349127352680639289550089776560`
2. write a [script](./sol.py) to decrypt the message
## flag
`picoCTF{sma11_N_n0_g0od_05012767}`