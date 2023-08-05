a,b,c,d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

e = a + b + c + d

def number_of_day(sum):
    if sum % 10 != 0:
        return int((sum // 10) + 1)
    else:
        return int(sum // 10)
    
print(number_of_day(e))