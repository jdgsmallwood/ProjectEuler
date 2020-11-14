fibs = [1,1]

loop = True

while(loop):
    sum2 = fibs[-1] + fibs[-2]
    if sum2 < 4000000:
        fibs.append(fibs[-1] + fibs[-2])
    else:
        loop = False

sum = 0
for num in fibs:
    if num % 2 == 0:
        sum+=num


print("The sum is %d." % sum)



