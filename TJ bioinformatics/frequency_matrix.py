def freq_lists(dna_list):
    n = len(dna_list[0])
    A = [0]*n
    T = [0]*n
    G = [0]*n
    C = [0]*n
    for dna in dna_list:
        for index, base in enumerate(dna):
            if base == 'A':
                A[index] += 1
            elif base == 'C':
                C[index] += 1
            elif base == 'G':
                G[index] += 1
            elif base == 'T':
                T[index] += 1
    return A, C, G, T


dna_list = ['GGTAG', 'GGTAC', 'GGTGC']
A, C, G, T = freq_lists(dna_list)
print (A)
print (C)
print (G)
print (T)


# for i in dna_list:
#     for i_char in i:
#         print (i_char, )


for a in range(len(dna_list)):
    for b in dna_list[a]:
        print(a, b)

for index, string in enumerate(dna_list):
    print(index, string)
    for index2, string2 in enumerate(string):
        print(index, string2)

# temp_string = 'LALWOIUDLKJ'

# for i in temp_string:
#     print(i)

            
