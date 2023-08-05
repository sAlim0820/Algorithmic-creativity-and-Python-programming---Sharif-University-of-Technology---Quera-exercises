def app(input_list,number):
    input_list.sort()
    input_list.reverse()

    print(input_list[number-1])


in_list = list(map(int,input().split()))
req_num = int(input())

app(in_list,req_num)