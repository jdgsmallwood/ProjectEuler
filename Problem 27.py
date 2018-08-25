from Helpers import get_primes

max_mod_a = 1000
max_mod_b = 1000

max_a = 0
max_b = 0
largest_num_of_primes = 0

generate_primes = 1000000







primes = get_primes(generate_primes)

for a in range(-max_mod_a+1,max_mod_a):
    for b in range(max(-1 - a, 1),max_mod_b+1):
        print(a)
        print(b)
        control = True
        n=0
        while control:
            num = n**2 + a*n + b
            if num <= 0:
                control = False
                break
            elif num < generate_primes and num in primes:
                n += 1
            elif num > generate_primes:
                print("Higher generate_primes needed")
            else:
                if n > largest_num_of_primes:
                    largest_num_of_primes = n
                    max_a = a
                    max_b = b
                control = False
                break

print(largest_num_of_primes)
print(max_a)
print(max_b)
print(max_a * max_b)


