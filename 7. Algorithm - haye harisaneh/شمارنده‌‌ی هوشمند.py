try:
    names_list = []
    while True:
        n = input()
        if (not n == "ERROR") and (not n == "BEBRASE BOZORG"):
            names_list.append(n)
        elif n == "BEBRASE BOZORG":
            names_list.append(n)
            print(len(names_list))
            break
        elif n == "ERROR":
            print("KHARABE!")
            break

except:
    exit(0)