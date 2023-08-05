x = int(input())

Number_of_bills_required = 0

num100 = x // 100

left = x - (num100 * 100)

num20 = left // 20

left -= (num20 * 20)

num10 = left // 10

left -= (num10 * 10)

num5 = left // 5

left -= (num5 * 5)

num1 = left // 1

left -= (num1 * 1)

result = num100 + num20 + num10 + num5 + num1

print(result)