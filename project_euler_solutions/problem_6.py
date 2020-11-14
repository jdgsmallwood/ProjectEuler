n = 100

sumsq = 0
sum = 0
for i in range(n+1):
    sumsq += i**2
    sum += i

diff = sum**2 - sumsq
print(diff)



