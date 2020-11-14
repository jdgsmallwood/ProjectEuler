num_of_digits = 1000
index = 2


fnum = 1
fnum_prev = 1
storage = 0

while len(str(fnum))<num_of_digits:
    storage = fnum
    fnum = fnum_prev + fnum
    fnum_prev = storage
    index +=1


print(fnum)
print('Index is %i' % index)


# I think the answer is 4782.