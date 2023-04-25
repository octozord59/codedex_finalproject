# input()
# max()
# min()
# len()
# range()

num1 = input('First random value:')
num2 = input('Second random value:')
num3 = input('Third random value:')
num4 = input('Fourth random value:')
num5 = input('Fifth random value:')

all_num = [num1, num2, num3, num4, num5]

print("Your numbers:")

for i in range(len(all_num)):
    print(all_num[i])


print("Statistics:")

print('Highest number: ', max(all_num))
print('Lowest number:  ', min(all_num))
print('Amount of numbers:  ', len(all_num))



