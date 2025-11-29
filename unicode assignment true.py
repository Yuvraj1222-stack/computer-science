# Rough Work / Notes
# program to convert a Unicode to UTF-8 ,Assignment.
# Yuvraj Saini

# function to convert hex letter to decimal
# sample input = U+20AC
# expected output = UTF-8
# breaking input into array
# loop through array and call corresponding func
# rearrange it to UTF-8
# print UTF-8

# ----------------------------------------
# Actual Code Starts Here

def myfunc(i):
    if i == 'A': return 10
    if i == 'B': return 11
    if i == 'C': return 12
    if i == 'D': return 13
    if i == 'E': return 14
    if i == 'F': return 15
    return int(i)

def to4bit(n):
    bits = ""
    for _ in range(4):
        bits = str(n % 2) + bits
        n //= 2
    return bits

# get Unicode input
y = input("Enter a Unicode (example: U+20AC): ")[2:]

# break the input into hex digits and convert to 4-bit binary
binary_digits = []
for ch in y:
    decimal = myfunc(ch)
    binary_digits.append(to4bit(decimal))

# combine all 4-bit groups into full binary string
full_binary = ''.join(binary_digits)
print("Binary from the hex table from class(4 bits per digit):", ' '.join(binary_digits))

# convert to UTF-8 bytes
decimal_value = int(full_binary, 2)
UTF8 = []
if decimal_value <= 0x7F:
    UTF8.append(decimal_value)
elif decimal_value <= 0x7FF:
    UTF8.extend([0b11000000 | (decimal_value >> 6),
                 0b10000000 | (decimal_value & 0b00111111)])
else:
    UTF8.extend([0b11100000 | (decimal_value >> 12),
                 0b10000000 | ((decimal_value >> 6) & 0b00111111),
                 0b10000000 | (decimal_value & 0b00111111)])

# print UTF-8 in binary
def to8bit(n):
    bits = ""
    for _ in range(8):
        bits = str(n % 2) + bits
        n //= 2
    return bits

UTF8_binary = [to8bit(b) for b in UTF8]
print("UTF-8 encoding/rearrange :", ' '.join(UTF8_binary))

