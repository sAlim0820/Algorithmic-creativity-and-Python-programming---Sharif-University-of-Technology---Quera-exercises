n = list(input())

yeakn = n[-1]
sadegan = n[-3]

n[-1] = sadegan
n[-3] = yeakn

final = ""
for item in n:
    final += item
print(final)