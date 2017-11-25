def is_valid(num,n):
    print("Checking validity.")
    ran = range(1, n + 1)
    for i in ran:
        if num % i != 0:
            return False
    return True


n = 20
prod = 1
ran = list(range(2,n+1))
for i in ran:
    prod *= i

for j in range(len(ran)):
    print(prod/ran[-j])
    print(prod)
    if int(prod/ran[-j]) == prod/ran[-j]:
        control = is_valid(int(prod / ran[-j]),n)
        print("Finished checking validity.")
        while control:
            print(prod)
            print(ran[-j])
            prod = prod / ran[-j]
            if not is_valid(int(prod / ran[-j]),n) and int(prod/ran[-j]) == prod/ran[-j]:
                control = False




print(prod)



# 20 allows division by 20,10,5,4,2,1
# 19 allows division by 19
# 18 allows division by 18, 9, 6, 3 and 2
# 17 allows division by 17
# 16 allows division by 16,8,4,2
# 15 allows division by 15
#14 allows division by 14, 7 and 2
# 13 allows division by 13
# 12 allows divsiion by 12, 6, 4, 3, 2
#11 allows division by 11






