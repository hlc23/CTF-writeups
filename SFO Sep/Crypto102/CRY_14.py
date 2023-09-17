raw_text = "91 322 57 114 40 406 272 147 239 285 353 272 77 110 296 262 299 323 255 337 150 102".split(" ")
for i in range(len(raw_text)):
    raw_text[i] = int(raw_text[i])%37

for i in raw_text:
    if i == 36:
        print("_", end="")
    elif i < 26:
        print(chr(i+65), end="")
    else:
        print(i-26, end="")