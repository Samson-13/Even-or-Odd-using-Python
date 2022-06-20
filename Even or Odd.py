def EvenorOdd(num):
    if (num % 2 == 0) or (num == 0):
        print('{} is an even number.'.format(num))
    elif num % 2 != 0:
        print('{} is an odd number.'.format(num))
    else:
        print('Enter a valid or positive number')

# main
num = int(input('Enter a number: '))
EvenorOdd(num)