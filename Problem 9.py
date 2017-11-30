target = 1000

#We're making an assumption without loss of generality that a < b < c
for a in range(1,1000):
    for b in range(a,1000):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            if a + b+ c == target:
                print('A: %f' % a)
                print('B: %f'% b)
                print("C: %f" % c)
                print(a*b*c)
                break

# I think the answer is 31875000