def get_base_counts(dna,  pair):
    
    total = 0

    for dna_i in range(len(dna)):
        if dna[dna_i] == pair[0]:
            i = 1
            count_found = 1
            for dna_char in pair[1 : len(pair)]:
                # print(dna[dna_i  + i], dna_char, dna_i, i)
                if (dna_i + i) <= len(dna) - 1 and dna[dna_i  + i] == dna_char:
                    count_found += 1
                i += 1   
            if count_found == len(pair):
                total +=1
        # print("Total", total, len(pair))
    return total

print(get_base_counts('ACZTTACGGAACG', 'ACGGAACG'))