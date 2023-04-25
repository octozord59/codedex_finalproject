# #01 of Modules

import random

symbols = [ '🍒', '🍇', '🍉', '7️⃣']

def play():
    
    for i in range(50):
        win = False
        results = random.choices(symbols, k = 3)
        print(f'{results[0]} \t | \t {results[1]} \t | \t {results[2]}')

        # if results == ['7️⃣', '7️⃣', '7️⃣']:
        #     win = True

        win = results == ['7️⃣', '7️⃣', '7️⃣']

        if win:
            print('Jackpot! 💰')
            
            break

        # else:
        #     results = random.choices(symbols, k = 3)      
                 

answer = 'Y'

while answer.upper() != 'N':
    play()
    answer = input('Do you want to keep playing Y/N?  ').upper()

print('Thanks for playing!')