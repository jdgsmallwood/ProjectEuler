import math
target_num = 600851475143
#target_num = 10

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



def largest_prime_factor(n):
    primes = get_primes(int(round(math.sqrt(n),0))+1)
    for i in range(len(primes)):
        if n % primes[-i] == 0:
            for m in primes:
                if (n/primes[-i]) % m == 0:
                    return primes[-i]
            return (n/primes[-i])





    return 0


factor = largest_prime_factor(target_num)
print("The largest prime factor is %d." % factor)