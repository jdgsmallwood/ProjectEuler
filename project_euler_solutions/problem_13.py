probleminputfile = open('../textinputs/Problem 13 input.txt')
probleminputlines = probleminputfile.readlines()
numbers = []

for l in probleminputlines:
    numbers.append(int(l.replace('\n','')))
print(str(sum(numbers))[0:10])

#I think the answer is 5537376230