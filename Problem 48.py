n = 1000
sum = 0
for i in range(1,n+1):
    sum += i ** i

print(str(sum)[-10:len(str(sum))])