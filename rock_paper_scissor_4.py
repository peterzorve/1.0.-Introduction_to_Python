
import numpy as np  

def rock_paper_scissor():
    options = ['rock', 'paper', 'scissor']

    co_c, my_c = options[np.random.randint(0, 3)], options[np.random.randint(0, 3)] 

    if co_c == my_c: 
        outcome = f"Computer : {co_c :7}  -   Peter : {my_c :8}  ==>  Draw"

    if ((co_c == 'rock') and (my_c == 'scissor')) or ((co_c == 'scissor') and (my_c == 'paper')) or ((co_c == 'paper') and (my_c == 'rock')):
        outcome = f"Computer : {co_c :7}  -   Peter : {my_c :8}  ==>  Computer wins"
    
    if ((co_c == 'paper') and (my_c == 'scissor')) or ((co_c == 'scissor') and (my_c == 'rock')) or ((co_c == 'rock') and (my_c == 'paper')):
        outcome = f"Computer : {co_c :7}  -   Peter : {my_c :8}  ==>  Peter wins"

    return outcome


print()
for i in range(10):
    print(rock_paper_scissor())


