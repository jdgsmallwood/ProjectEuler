
def is_palindrome(n):
    m = int(str(n)[::-1])
    if n == m:
        return True
    else:
        return False

largest = 0
for num in range(100,1000):
    for num2 in range(100, 1000):
        if is_palindrome(num*num2) and num*num2 > largest:
            largest = num*num2


print("The largest palindrome number made up of a product of 3 digit numbers is %d." % largest)



