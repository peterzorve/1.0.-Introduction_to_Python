
""" For Loop    """

name = 'Peter Zorve'
my_list = ['milk', 'sugars', 'salt', 'books', 'cake', '12', '15.1', '78']

print(name)

for i in name: 
    print(i * 5)

for item in my_list:
    if item.isdigit():
        print(item)

for item in my_list:
    if item.endswith('s') and item.startswith('s'):
        print(item)

# dir(int)





sammy = 'Sammy  is a hard 320 working guy who earns GHC 450 every 2 weeks. He gives GHC 30 to his friend who has 12 children'

tommy = sammy.split()
tommy_is_empty = ''

for item in tommy:
    if item.isdigit():
        tommy_is_empty = tommy_is_empty + item + ' '

print(tommy_is_empty)


sammy = 'Sammy  is a hard 320 working guy who earns GHC 450 every 2 weeks. He gives GHC 30 to his friend who has 12 children'
sammy_2 = ''
for number in sammy:
    if number.isdigit() or number == ' ':
        sammy_2 = sammy_2 + number

sammy_2 = sammy_2.strip()
sammy_2 = sammy_2.replace('  ', ' ')
sammy_2 = sammy_2.replace('  ', ' ')
sammy_2 = sammy_2.replace('  ', ' ')
print(sammy_2)



""" While Loop """
# While Loop 

count = 5 

while count < 50:
    print(count)
    count = count + 5


sentence = "Don't kill the fox"
count = len(sentence)
start = 0 
# print(count)

for stone in sentence: 
    print(stone * 12)


while start < count: 
    print(sentence[start] * 12)
    start = start + 1




