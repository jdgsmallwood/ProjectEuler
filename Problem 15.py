#It require 40 such moves to get to the bottom right corner starting at the top left, and so the
#number of possible paths is {40 choose 20}
#Can python do this automatically?

n = 20

num = 1
den = 1
for m in range(1,n+1):
    num *= (m+n)
    den *= m
print(num/den)


#I think the answer is 137846528820

#I could try to write a combinations function for this