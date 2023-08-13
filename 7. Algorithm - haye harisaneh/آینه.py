try:
    n = list(input())

    reversed_n = n.copy()
    reversed_n.reverse()

    if n == reversed_n:
        print("AYNEH")
    else:
        print("NORMAL")
except:
    pass
