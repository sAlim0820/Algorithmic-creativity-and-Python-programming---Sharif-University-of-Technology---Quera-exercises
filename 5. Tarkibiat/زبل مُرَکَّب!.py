def fact(n):

    result = 1

    for i in range(1, n+1):

        result *= i

    return result

def P(n, k):

    return fact(n)/fact(n-k)

def C(n, k):
    return P(n,k) / fact(k)


n_input = int(input())
k_input = int(input())

print(int(C(n_input,k_input)))