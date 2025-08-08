import base64

base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/" # To get index of the second character

nibbles = [] # To store the nibbles
with open('based64.txt', 'r') as file:
    lines = file.readlines()[:-1] # We don't want the last line remember?
    for line in lines:
       second_char = line[1]
       index = base64_chars.index(second_char)
       last_4_bits = index & 0b1111  # Get the last 4 bits
       nibbles.append(last_4_bits)

pairs = list(zip(nibbles[::2], nibbles[1::2]))

flag=""
for pair in pairs:
    first_nibble, second_nibble = pair # Get the two nibbles
    ascii_bin=format(first_nibble, '04b')+format(second_nibble, '04b') # Convert both nibbles to binary and then concatenate em~~
    ascii_char = chr(int(ascii_bin, 2))  # Convert binary to decimal and then to ASCII character
    flag+=(ascii_char)

print(flag)
