num = 2 ** 1000
array = str(num)
sum = 0
print(array)
for i in range(len(array)):
    sum += int(array[i])

print(sum)