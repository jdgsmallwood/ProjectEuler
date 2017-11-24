def divisible_by(x,y):
    '''
    Is x divisible by y?
    :param x: number to be divided
    :param y: divisor
    :return: true/false
    '''
    if x % y == 0:
        return True
    else:
        return False

sum = 0
for i in range(1,1000):
    if divisible_by(i,3) or divisible_by(i,5):
        sum += i

print("The sum is %d." % sum)
