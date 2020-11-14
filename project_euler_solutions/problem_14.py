# The sequence is defined by the following:
# n -> n/2 is n is even
# n -> 3n + 1 is n is odd
# We want the longest chain before it reaches one of starting numbers underneath 1 million.

n = 1000000
longest = 0
longesti = 0
for i in range(1,n):
    print(i)
    control = True
    m=i
    n=0
    while control:
        if m == 1:
            break
        elif m % 2 == 0:
            m /= 2
        else:
            m = 3*m + 1
        n+=1
    if n > longest:
        longest = n
        longesti = i

print(longest)
print(longesti)

#I think the answer is 837799

#This could be improved by ruling out all of the numbers that the sequence goes through as starting numbers as by definition it must be a shorter
#path, similar to the sieve of Erastothenes.
