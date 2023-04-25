

def get_base_counts(dna,  pair):
    
    total = 0

    for dna_i in range(len(dna)):
        if dna[dna_i] == pair[0] and dna[dna_i + 1] == pair[1]:
            total += 1
    
    return total

    # for dna_i in range(len(dna)):
    #     if dna_i == dna[len(pair[0])] - 1 and dna_i == len(pair[1]):
    #         total += 1

print(get_base_counts('ACTGCATATCACATT', 'CA'))

# print ('%s appears %d times in %s' % ('A', DNA_string, total))

# print ( 'Total pairs is:   ', get_base_counts('ACTGCTATCCATT', 'AT') )







