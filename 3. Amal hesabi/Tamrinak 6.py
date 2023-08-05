Character , Length = input().split()
Length = int(Length)

for Width in range(1,6):
    if Width == 1 or Width == 5:
        print(Character * Length)
    else:
        print(Character+" "*(Length-2)+Character)