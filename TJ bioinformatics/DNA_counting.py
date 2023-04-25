#  ATGGCATTA

def dna_counter():

    total = 0
    DNA_string = input('DNA string:   ')

    for i in DNA_string:
        
        if i == 'A' or i == 'a':
            total += 1
        # print(i)
    print('Number of As:  ', total)

    print ('%s appears %d times in %s' % ('A', DNA_string, total))

dna_counter()

# # printf-style formatting
# print '%s appears %d times in %s' % (base, n, dna)

# # or (new) format string syntax
# print '{base} appears {n} times in {dna}'.format(
#     base=base, n=n, dna=dna)

