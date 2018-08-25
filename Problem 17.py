def write_number_in_words(n):
    if len(str(n)) == 1:
        return identify_digit(n,1)

    elif len(str(n)) == 2:
        if str(n)[0]=='1':
            return identify_teen(n)
        else:
            return identify_digit(str(n)[0],2) + ' ' + identify_digit(str(n)[1],1)

    elif len(str(n))==3:
        if str(n)[1:3] == '00':
            return identify_digit(str(n)[0],1) + ' hundred'

        elif str(n)[1] == '1':
            return identify_digit(str(n)[0],1) + ' hundred and ' + identify_teen(str(n)[1:3])

        else:
            return identify_digit(str(n)[0],1) + ' hundred and ' + identify_digit(str(n)[1],2) + ' ' + identify_digit(str(n)[2],1)



    elif len(str(n)) == 4:
        return 'one thousand'

def identify_teen(i):
    i = int(i)

    if i == 10:
        return 'ten'
    elif i == 11:
        return 'eleven'
    elif i == 12:
        return 'twelve'
    elif i == 13:
        return 'thirteen'
    elif i ==14:
        return 'fourteen'
    elif i==15:
        return 'fifteen'
    elif i==16:
        return 'sixteen'
    elif i==17:
        return 'seventeen'
    elif i==18:
        return 'eighteen'
    elif i==19:
        return 'nineteen'


def identify_digit(i,place):
    i = int(i)
    if i == 1 and place == 1:
        return 'one'

    elif i ==2 and place == 1:
        return 'two'

    elif i==2 and place ==2:
        return 'twenty'

    elif i==3 and place == 1:
        return 'three'

    elif i==3 and place ==2:
        return 'thirty'

    elif i==4 and place == 1:
        return 'four'

    elif i==4 and place ==2:
        return 'forty'

    elif i ==5 and place ==1:
        return 'five'

    elif i==5 and place ==2:
        return 'fifty'

    elif i==6 and place == 1:
        return 'six'

    elif i==6 and place ==2:
        return 'sixty'

    elif i ==7 and place == 1:
        return 'seven'

    elif i==7 and place ==2:
        return 'seventy'

    elif i==8 and place == 1:
        return 'eight'

    elif i==8 and place ==2:
        return 'eighty'

    elif i==9 and place == 1:
        return 'nine'

    elif i==9 and place ==2:
        return 'ninety'

    elif i == 0:
        return ''


sum = 0
n=1000
for i in range(1,n+1):
    sum += len(write_number_in_words(i).replace(' ', ''))

print(sum)