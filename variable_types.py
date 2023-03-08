
"""
The types of Variables in Python include:
    1.  Integer
    2.  Float 
    3.  String
    4.  Boolean (True or False)
    5.  List 
    6.  Tuple 
    7.  Dictionary 
    8.  Set 
"""


""" 1.  Integer - An integer is negative and positive whole number include 0  """
number = 12
count = -10000

print(number)
print(type(number))
print(type(count))


""" 2.  Float - A floats can be thought of as a number with decimal point """
number1 = 12.0
salary_rate = 12.45

print(number1)
print(type(number1))


""" 3.  String - A string is a colloection of some characters with no numerical value. 
        We represent strings by putting them within a quotation (' ' or " ")  """
my_name = "Peter Zorve"
sentence = 'I am very hungry and tired'

print(my_name)
print(type(sentence))


""" 4.  Boolean - A boolean is just True of False. In Python, we use the keywords True or False """
hungry = True
print(hungry)
print(type(hungry))


""" 5.  List - A list is a collection of items. We represent a list by putting them in a square parenthesis, [] """
my_list = [10, 12, 23, 50, 80] 
my_list_2 = ['Peter', 'Kwame', 'name', 50., 18, 0.001]

print(my_list)
print(type(my_list)) 

print(my_list_2)
print(type(my_list_2))


""" 6.  Tuple - A tuple is like a list. Also a collection of items. We tuple is defined with a parenthesis, ()  
        We will discuss the difference between a list and a tuple later """

my_tuple = (10, 'Kwame', 10.082128, True, False, 'shoes')
print(my_tuple)
print(type(my_tuple))



""" 7.  Dictionary - A dictionary comes in the form of a keys and value pair. Think of it as the dictionary we know - 
        Words (Key), and their meaning (Value). We write dictionaries with curly parenthesis, {}  """

my_dict = {'name': 'Peter Zorve', 'age' : 15, 'salary' : 150.20, 12 : 'I am very tired'} 
print(my_dict)
print(type(my_dict))


""" 8.  Set - A set is also a collection of items. We represent a set using curly parenthesis, but the 
        elements are not key-value pairs """

my_set = {'name', 'hungry', 'tired', 'happy', 'name', 'name'}
print(my_set)
print(type(my_set))



