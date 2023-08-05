def app (input_list,status_code):
    if status_code == 0:
        input_list.sort()
        input_list.reverse()
    if status_code == 1:
        input_list.sort()

    print(input_list)



in_list = list(map(int,input().split()))
status_in = int(input())

app(in_list,status_in)
