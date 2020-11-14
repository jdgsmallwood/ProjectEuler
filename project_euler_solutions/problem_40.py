number = '0.'
i = 1
while len(number) < 1000002:
    number += str(i)
    i += 1

prod = 1
for j in range(7):
    prod *= int(str(number)[1+10**j])

print(prod)
