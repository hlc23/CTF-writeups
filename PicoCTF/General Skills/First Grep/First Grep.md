# First Grep
## Problem
> Can you find the [flag](https://jupiter.challenges.picoctf.org/static/515f19f3612bfd97cd3f0c0ba32bd864/file) in file? This would be really tedious to look through manually, something tells me there is a better way.

[link](https://play.picoctf.org/practice/challenge/85)
### Source
- [file](./file)
## Solution
`strings file | grep picoCTF`
## flag
`picoCTF{grep_is_good_to_find_things_5af9d829}`
