Char , step = input().split()
step = int(step)

ascii_first = ord(Char)

sum = ascii_first + step
while sum >= 122:
    a = sum - 122
    sum = 96 + a


print(chr(sum))