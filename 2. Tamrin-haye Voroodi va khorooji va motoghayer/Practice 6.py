try:
    gift = input()
    number_l = list(gift)
    number_l2 = number_l.copy()
    for item in number_l:
        if item != "0":
            break
        elif item == "0":
            number_l2.pop(0)

    result = ""
    for item_final in number_l2:
        result = result+item_final

    print(result)
except:
    pass
