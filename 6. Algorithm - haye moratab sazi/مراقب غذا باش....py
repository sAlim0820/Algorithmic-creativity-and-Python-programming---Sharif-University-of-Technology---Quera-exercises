temps = []
_ = input().split()

for i in _:
    temps.append(int(i))

index_finder = temps.copy()

temps.sort()

if temps[-1] > 100:
    print(f"مراقب قابلمه {index_finder.index(temps[-1]) + 1} باش")

if temps[0] < 20:
    print(f"زیر قابلمه {index_finder.index(temps[0])+1} را زیاد کن")