# Tab, Tab, Attack
## Problem
> Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://mercury.picoctf.net/static/659efd595171e4c40378be6a2e9b7298/Addadshashanammu.zip)

[link](https://play.picoctf.org/practice/challenge/176)
### Source
[Addadshashanammu.zip](./Addadshashanammu.zip)
## Solution
1. `unzip Addadshashanammu.zip`
2. `cd` to deepest directory
3. `strings fang-of-haynekhtnamet | grep pico`
## flag
`picoCTF{l3v3l_up!_t4k3_4_r35t!_524e3dc4}`
