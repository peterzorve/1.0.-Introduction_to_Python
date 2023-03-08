# Arithmetic Operation 

number_1 = 50 
number_2 = 15 

# Addition 
result = number_1 + number_2 
print(number_1, ' + ', number_2, ' = ',  result)

# Substraction 
result = number_1 - number_2 
print(number_1, ' - ', number_2, ' = ',  result)

# Multiplication  
result = number_1 * number_2 
print(number_1, ' * ', number_2, ' = ',  result)


# Division   
result = number_1 / number_2 
print(number_1, ' / ', number_2, ' = ',  result)


# Modulus   
result = number_1 % number_2 
print(number_1, ' % ', number_2, ' = ',  result)


# Modulus   
result = number_1 ** number_2 
print(number_1, ' ** ', number_2, ' = ',  result)

# Floor Division    
result = number_1 // number_2 
print(number_1, ' // ', number_2, ' = ',  result)





# COMPARISON OPERATION 

number_3 = 10
number_4 = 12
number_5 = 30 

# Equal to 
print('1 : ',  number_3 == number_4)

# Not equal to 
print('2 : ',  number_3 != number_4)

# Less than 
print('3 : ',  number_3 < number_4)

# Greater than 
print('4 : ',  number_3 > number_4)

# less than or equal to  
print('4 : ',  number_3 <= number_4)

# greater than or equal to  
print('4 : ',  number_3 >= number_4)





# LOGICAL OPERATION 

number_6 = 5
number_7 = 2
number_8 = 10

# AND 
print('1 : ', number_6 > number_7 and number_6 < number_8)

                    # True          and          True             ----->  True 
                    # False         and          False            ----->  True  
                    # True          and          False            ----->  False 
                    # False         and          True             ----->  False  


# OR 
print('2 : ', number_6 > number_8 or number_6 < number_8)
                    # False         or    True 

                    # True          or          True             ----->    False 
                    # False         or          False            ----->    False 
                    # True          or          False            ----->    True
                    # False         or          True             ----->    Truw 

# NOT  
print('3 : ', not (number_6 > number_7 and number_6 < number_8))
print('2 : ', not (number_6 > number_8 or number_6 < number_8))

number_6 = 5
number_7 = 2
number_8 = 10

print('1 : ', (not (number_8 > number_7)) or number_8 < number_8)
                        #  False           or          False 

print('2 : ', not (number_8 > number_7) and (not (number_6 < number_7)))
                        # False                        True  

print('3 : ', (not (number_6 > number_7)) and (number_8 < number_8) and  (not (number_6 < number_7) )) 
                        # False                        False                        True  



