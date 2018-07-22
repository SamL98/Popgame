with open('cities1000.txt') as f:
    with open('cities.txt', 'w') as out:
        for line in f:
            terms = line.split('\t')
            del terms[3]
            del terms[5]
            del terms[5]
            for _ in range(5):
                del terms[6]
            
            terms = terms[:-4]
            if int(terms[-1]) == 0:
                continue

            out.write('\t'.join(terms))
            out.write('\n')
