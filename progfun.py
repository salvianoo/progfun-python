# 1. fatorial
# 2. fibonacci
# 3. maioria


def factorial(num):
    fact = 1
    while (num > 1):
        fact = fact * num
        num = num - 1
    return fact


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def vetor_maioria(vet, index):
    item_maioria = vet[index]
    count = 0
    for item in vet:
        if item_maioria == item:
            count = count + 1
    if count > (len(vet) / 2):
        return True
    return False
