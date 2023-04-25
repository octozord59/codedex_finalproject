credit = int(input('Credits:'))
height = int(input('Height in centimeters:'))
taller_person = 0

if credit >= 10:
    if height >= 137:
        print("Enjoy the ride!")
    elif height < 137 and height >= 100:
        print('Are you with a taller person? (1 for yes 2 for no)')
        taller_person = int(input(''))

        if taller_person == 1:
            print("Enjoy the ride!")
        else:
            print("You cannot go on this ride.")
    else:
        print("You cannot go on this ride.")
else:
        print("You don't have enough credits to go on this ride.")


