alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"

def caesar(input_string, rot):
    output_string = ""
    for i in range(len(input_string)):
        if input_string[i].isalnum():
            idx = (alphabet.find(input_string[i]) + rot) % len(alphabet)
            output_string += alphabet[idx]
        else:
            output_string += input_string[i]
    return output_string

enc = '7sj-ighm-742q3w4t'

for i in range(len(alphabet)):
    print(caesar(enc, i))