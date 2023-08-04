import itertools

def can_chain(dominoes):

    for combination in itertools.permutations(dominoes):
    
        chain = [combination[0]]

        for i in range(1, len(combination)):
        
            if combination[i][0] == chain[len(chain)-1][1]: 
                chain.append(combination[i])
            elif combination[i][1] == chain[len(chain)-1][1]: 
                chain.append(sorted(combination[i], reverse=True))
            else:
                None

        if len(chain) == len(dominoes) and chain[0][0] == chain[len(chain)-1][1]:
            return chain
    
print(can_chain([(1, 2), (2, 3), (3, 1), (1, 1), (2, 2), (3, 3)]))  