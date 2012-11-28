# 1. fatorial
# 2. fibonacci
# 3. maioria


def factorial(num):
    fact = 1
    while num > 1:
        fact *= num
        num -= 1
    return fact


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# def vetor_maioria(arr, index):
#     arr_maioria = filter(lambda i: i == arr[index], arr)
#     return len(arr_maioria) > len(arr) / 2


def div_by_three_or_five(arr):
    cond = lambda el: el % 3 == 0 or el % 5 == 0
    return reduce(lambda res, el: res + el, filter(cond, arr))


def primo(num, arr):
    return len(filter(lambda el: num % el == 0, arr)) == 2


def elemento_maioria(arr, index):
    return len(filter(lambda el: el == arr[index], arr)) > len(arr) / 2


def vetor_maioria(arr):
    return True in map(lambda elemento:
            len(filter(lambda el_maioria:
                el_maioria == elemento, arr)) > len(arr) / 2, arr)
