probleminputfile = open('textinputs/Problem 11 input.txt')
probleminputlines = probleminputfile.readlines()
data = {}
for i in range(len(probleminputlines)):
    numbers = []
    for l in probleminputlines[i].split(' '):
        numbers.append(int(l.replace('\n','')))
    data[i] = numbers


largest = 0
n = 4
#Horizontal
for i in range(len(probleminputlines)):
    for j in range(len(data[i])-n):
        prod = 1
        for k in range(n):
            prod *= data[i][j+k]
        if prod > largest:
            largest = prod


#Vertical
for j in range(len(probleminputlines)):
    for i in range(len(data[i])-n):
        prod = 1
        for k in range(n):
            prod*=data[i+k][j]
        if prod > largest:
            largest = prod


#Diagonal Top Left - Bottom Right
for i in range(len(probleminputlines)-n):
    for j in range(len([probleminputlines]) - n):
        prod = 1
        for k in range(n):
            prod *= data[i+k][j+k]
        if prod > largest:
            largest = prod


#Diagonal Top Right - Bottom Left
for j in range(len(probleminputlines)-n):
    for i in range(n-1,len([probleminputlines])):
        prod = 1
        for k in range(n):
            prod *= data[i-k, j+k]
        if prod > largest:
            largest = prod

print(largest)



#I think the answer is 51267216