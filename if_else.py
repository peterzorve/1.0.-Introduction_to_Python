""" if and else """

count = 1

if count < 12:
    print(count, 'less than 12')

else: 
    print(count, 'greater or equal 12')
    print(count * 10)
    print(count)



count_1 = 10
count_2 = 15

if count_1 < count_2 and count_1 > 5:
    print(count_1, ' < ', count_2)

else: 
    print(count_1, ' >= ', count_2)




temperature = int(input('enter temperature : '))
# temperature = 10


if temperature < 15:
    print(temperature, 'it is very cold')

elif temperature < 20: 
    print(temperature, 'it is still cold')

elif temperature < 30:
    print(temperature, 'it is normal')

elif temperature < 40: 
    print(temperature, 'too is normal')

elif temperature < 50:
    print(temperature, 'it beginning to get hot')

else:
    print(temperature, 'it is very hot')

number_1 = 10
number_2 = 15

if number_1 > 10:
    print(number_1, 'is greater than 10')
else: 
    print(number_1, 'is equal to or less than 10')




number_2 = 1

if number_2 > 5:
    print('more than 5')
elif number_2 > 3:
    print('nore than 3')
elif number_2 > 0:
    print('more than 0')
else: 
    print('less than 0 or equal to 0')
