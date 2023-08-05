try:
    vorodi = True
    number_list = []
    result = 0
    def sum_number_list(input_list):
        sum_numbers = 0

        for i in input_list:
            sum_numbers += i

        return sum_numbers


    while vorodi:
        n = int(input())
        if not n == 0:
            number_list.append(n)
        elif n ==0:
            result = sum_number_list(number_list)
            break

    print(result)



except:
    exit(0)