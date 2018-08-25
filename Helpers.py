def digit_sum(n):
    array = str(n)
    sum = 0
    for i in range(len(array)):
        sum += int(array[i])
    return sum


def factorial(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod


def get_primes(n):
    primes = [False,False]+[True for i in (range(2,n+1))]
    for num in range(2,n+1):
        if primes[num]:
            control = True
            i=0
            while control:
                if num**2+i*num <= n:
                    primes[num**2+i*num] = False
                    i+=1
                else:
                    control = False

    primes3 = [i for i in range(0,n-1) if primes[i]]
    return primes3