t = int(input())
h = t // 3600
m = (t % 3600) // 60
s = (t % 3600) % 60
print(h, ":", m, ":", s)