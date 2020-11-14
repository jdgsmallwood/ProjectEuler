# Sum under 10 should be 17
n = 2000000


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


primes = get_primes(n)
print(sum(primes))


# I think the answer is 142913828922