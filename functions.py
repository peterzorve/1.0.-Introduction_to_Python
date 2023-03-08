
""" Functions """

number1 = 10
number2 = 20 

add = 10
summation = number1 + number2 

print(number1, ' + ', number2,  ' = ', summation)



def samuel_boateng(num1=0, num2=0):
    result = num1 + num2 
    print(num1, '+', num2,  '=', result)
    return 

samuel_boateng(30, 40)
samuel_boateng(10, 20)
samuel_boateng(80, 60)
samuel_boateng(100, 80)



# Question 1. Write a function that accepts a number and print a square based on that number 
# For example, with a function named square 
# square(number, unit='cm')

def square(number, unit):

    

    for num in range(number):
        if num == 0:
            print('*  ' * number, '      ')
        
        elif num < number: 
            print('*  ', '   ' * (number - 2), '* ')

        
        if num == (number-1):
            print('*  ' * number, '      ')
    
    print('   ' * int(number/2) , number, unit)


    return 

square(15, 'cm')


def backtosender(ewiase):

    length = len(ewiase)  
    reverse = ''

    for number in range(length):
        character = ewiase[length - (number + 1 )]  
        reverse = reverse + character

    return reverse

backtosender('where are you going today?')


"""
Question 3. Write a function to extract the first name, second name and date of birth from the data below. 

my_dictionary = {   'emails'    :  ['peter.zorve25@gmail.com', 'lara.funke125@gmail.com', 'faith.edem@yahoo.com', 'kenny.edem12@yahoo.com', 'kojo.sammy235@gmail.com', 'ama.lara16@yahoo.com', 'adeyele.kumi999999@yahoo.com', 'bismark.asamoah@yahoo.com', 'john.mireku@uef.fi', 'youth.agam@uef.fi', 'entry.james@uef.fi', 'kofi.antwi@uef.fi'], 
                    'id_number' :  ['27021990-THN', '28021990-IHE', '28121990-THE', '28021990-OHE', '28121990-JKE', '28061990-RHE', '27021980-POE', '28121990-ABC', '28021890-FGE', '28021990-LZE', '28021990-NAE', '28021990-THE' ]}


OUTPUT 

Peter Zorve       -  27.02.1990
Lara Funke        -  28.02.1990
Faith Edem        -  28.12.1990
Kenny Edem        -  28.02.1990
Kojo Sammy        -  28.12.1990
Ama Lara          -  28.06.1990
Adeyele Kumi      -  27.02.1980
Bismark Asamoah   -  28.12.1990
John Mireku       -  28.02.1890
Youth Agam        -  28.02.1990
Entry James       -  28.02.1990
Kofi Antwi        -  28.02.1990

"""

david = {   'emails'    :  ['peter.zorve25@gmail.com', 'lara.funke125@gmail.com', 'faith.edem@yahoo.com', 'kenny.edem12@yahoo.com', 'kojo.sammy235@gmail.com', 'ama.lara16@yahoo.com', 'adeyele.kumi999999@yahoo.com', 'bismark.asamoah@yahoo.com', 'john.mireku@uef.fi', 'youth.agam@uef.fi', 'entry.james@uef.fi', 'kofi.antwi@uef.fi'], 
            'id_number' :  ['27021990-THN', '28021990-IHE', '28121990-THE', '28021990-OHE', '28121990-JKE', '28061990-RHE', '27021980-POE', '28121990-ABC', '28021890-FGE', '28021990-LZE', '28021990-NAE', '28021990-THE' ]}


all_emails = david['emails']


for asamoah in all_emails:
    philip = asamoah.split('.')
    khoby = philip[0]
    peter = philip[1].split('@')
    daniel = peter[0]

    print(khoby, daniel)


for item in david['emails']:
    name = ''
    for character in item: 
        #  
        if not character.isdigit(): 
            name = name + character
            # break 
    print(name)




david = {   'emails'    :  ['peter.zorve25@gmail.com', 'lara.funke125@gmail.com', 'faith.edem@yahoo.com', 'kenny.edem12@yahoo.com', 'kojo.sammy235@gmail.com', 'ama.lara16@yahoo.com', 'adeyele.kumi999999@yahoo.com', 'bismark.asamoah@yahoo.com', 'john.mireku@uef.fi', 'youth.agam@uef.fi', 'entry.james@uef.fi', 'kofi.antwi@uef.fi'], 
            'id_number' :  ['27021990-THN', '28021990-IHE', '28121990-THE', '28021990-OHE', '28121990-JKE', '28061990-RHE', '27021980-POE', '28121990-ABC', '28021890-FGE', '28021990-LZE', '28021990-NAE', '28021990-THE' ]}

def extract(david):

    first_last_name = []
    date_of_birth = []

    for item in david['emails']:
        name = item.split('@')[0]

        full_name = ''
        for i in name: 
            if not i.isdigit():
                full_name = full_name + i 
        
        full_name = full_name.replace('.', ' ').title()

        first_last_name.append(full_name)

    for item in david['id_number']:
        id = item[:2]+ '-' + item[2:4] + '-' + item[4:8]
        date_of_birth.append(id)

    for item in range(len(first_last_name)):
        print(f"{first_last_name[item]:15}  -  {date_of_birth[item]}")
    
    return 









