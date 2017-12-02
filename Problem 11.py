probleminputfile = open('textinputs/Problem 11 input.txt')
probleminputlines = probleminputfile.readlines()
data = {}
for i in range(len(probleminputlines)):
    numbers = []
    for l in probleminputlines[i].split(' '):
        numbers.append(int(l.replace('\n','')))
    data[i] = numbers


largesth = 0
largestv = 0
largestdtl = 0
largestdbl = 0
n = 4
#Horizontal
for i in range(len(probleminputlines)):
    for j in range(len(data[i])-n+1):
        prod = 1
        for k in range(n):
            prod *= data[i][j+k]
        if prod > largesth:
            largesth = prod


#Vertical
for j in range(len(probleminputlines)):
    for i in range(len(data[i])-n+1):
        prod = 1
        for k in range(n):
            prod*=data[i+k][j]
        if prod > largestv:
            largestv = prod


#Diagonal Top Left - Bottom Right
for i in range(len(probleminputlines)-n):
    for j in range(len(probleminputlines) - n+1):
        prod = 1
        for k in range(n):
            prod *= data[i+k][j+k]
        if prod > largestdtl:
            largestdtl = prod


#Diagonal Top Right - Bottom Left
for j in range(len(probleminputlines)-n+1):
    for i in range(n-1,len(probleminputlines)):
        prod = 1
        for k in range(n):
            prod *= data[i-k][j+k]
        if prod > largestdbl:
            largestdbl = prod

print(largestv)
print(largesth)
print(largestdtl)
print(largestdbl)

largest = max(largestv, largesth, largestdbl, largestdtl)
print("largest is %i" % largest)



#I think the answer is 51267216