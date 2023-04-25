
def count_substr2(dna, search_string):
    total = 0
    for dna_i in range(len(dna)):
        if dna[dna_i] == search_string[0]:
            str_found = 1
            int = 1
            
            for dna_char in range(1, len(search_string)):
                # print('debug 3:', dna_char, int, dna_i)
                if dna_i + int < len(dna):
                    # print('debug 1:', dna[dna_i + int], search_string[dna_char], dna_char, int, dna_i)
                    if dna[dna_i + int] == search_string[dna_char]:
                        # print('debug 2:', dna_char, int, dna_i)
                        str_found +=1
                int +=1
                        
                            
                        
                if str_found == len(search_string):
                        total +=1
    return total


def easy_count_substr(dna, search_string):
    return dna.count(search_string)

                        


print(count_substr2('ACZTTACGGAACGG', 'ACGG'))
print(easy_count_substr('ACZTTACGGAACGG', 'ACGG'))

