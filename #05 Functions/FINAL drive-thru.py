options = [ '🍔 Cheeseburger',
        '🍟 Fries',
        '🥤 Soda',
        '🍦 Ice Cream',
        '🍪 Cookie' ]



def welcome():
    print('Welcome to McDonalds!')
    print('This is the menu:')   
    # print('1. 🍔 Cheeseburger')
    # print('2. 🍟 Fries')
    # print('3. 🥤 Soda')
    # print('4. 🍦 Ice Cream')
    # print('5. 🍪 Cookie')
    
    # for i in options:
    #     print(i)

    for i in range(len(options)):
        print( i + 1, options[i])

def get_item(x):
    # if x == 1:
    #     return '🍔 Cheeseburger'
    # elif x == 2:
    #     return '🍟 Fries'
    # elif x == 3:
    #     return '🥤 Soda'
    # elif x == 4:
    #     return '🍦 Ice Cream'
    # elif x == 5:
    #     return '🍪 Cookie'
    # else:
    #     return'That item is not on the menu!'
    
    if choice > len(options):
        return "Not a valid choice."
    else:
        return options[x - 1]



welcome()

choice = int(input('What would you like to get today?  '))
print(get_item(choice))




