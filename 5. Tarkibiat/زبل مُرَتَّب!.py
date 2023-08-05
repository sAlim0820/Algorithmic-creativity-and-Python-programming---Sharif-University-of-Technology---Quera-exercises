def fact(n):

    result = 1

    for i in range(1, n+1):

        result *= i

    return result


def P(n, r):
    fact_n = fact(n)
    fact_r = fact((n-r))

    return fact_n / fact_r

n_input = int(input())
r_input = int(input())

print(int(P(n_input,r_input)))