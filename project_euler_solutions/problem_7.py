def get_primes(n):
    primes = [False,False]+[True for i in (range(2,n+1))]
    for num in range(2,n+1):
        print(num)
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
    print(primes3)
    return primes3




print(get_primes(200000)[10000])