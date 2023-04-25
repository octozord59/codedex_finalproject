gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0


print('Q1) Do you like Dawn or Dusk?  ')
print('    1) Dawn')
print('    2) Dusk')
Q1 = int(input(''))

if Q1 == 1:
    gryffindor = gryffindor + 1
    ravenclaw = ravenclaw + 1
elif Q1 == 2:
  hufflepuff = hufflepuff + 1
  slytherin = slytherin + 1
else:
  print('Wrong input.')

print("Q2) When I'm dead, I want people to remember me as:")
print("    1) The Good")
print("    2) The Great")
print("    3) The Wise")
print("    4) The Bold")
Q2 = int(input(''))

if Q2 == 1:
    hufflepuff = hufflepuff + 1
elif Q2 == 2:
    slytherin = slytherin + 1
elif Q2 == 3:
    ravenclaw = ravenclaw + 1
elif Q2 == 4:
    gryffindor = gryffindor + 1
else:
    print('Wrong Input.')

print("Q3) Which kind of instrument most pleases your ear?")
print("    1) The violin")
print("    2) The trumpet")
print("    3) The piano")
print("    4) The drum")
Q3 = int(input(''))

if Q3 == 1:
    slytherin = slytherin + 1
elif Q3 == 2:
    hufflepuff = hufflepuff + 1
elif Q3 == 3:
    ravenclaw = ravenclaw + 1
elif Q3 == 4:
    gryffindor = gryffindor + 1
else:
    print('Wrong input.')

if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
    print("Gryffindor")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
    print("Ravenclaw")
elif hufflepuff > gryffindor and hufflepuff > ravenclaw> hufflepuff > slytherin:
    print("Hufflepuff")
elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
    print('Slytherin')
else:
    print("It was a tie!")






