import math
def get_divisors(n):
    divisors = []
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)

    divisors2 = []
    for i in divisors:
        divisors2.append(int(n / i))

    divisors = set(divisors + divisors2)
    return divisors

control = True
sum = 0
i=1
while control:
    sum += i
    div = get_divisors(sum)
    if len(div) > 500:
        control = False
        print(sum)
        break
    i+=1






