def app(input_list,operator_input):
    if operator_input < 1 or operator_input > 3:
        print(".لطفا بین ۱ تا ۳ وارد کنید")
        exit()


    if operator_input == 1:
        indexs = [x*2 for x in range(1,((len(input_list)) // 2)+1)]

        for i in indexs:
            input_list[i-1] -= 3

    elif operator_input == 2 :
        indexs = [(x*2) - 1 for x in range(1,((len(input_list)) // 2)+1)]

        for i in indexs:
            input_list[i-1] *=  input_list[i-1]

    elif operator_input == 3:
        indexs = [(x*4) - 3 for x in range(1,((len(input_list)) // 2))]

        for i in indexs:
            input_list[i-1] +=  input_list[i]

    final_list = ""
    for i in input_list:
        final_list += str(i)+" "

    print(final_list)

ope = int(input())
in_list = list(map(int,input().split()))

app(in_list,ope)