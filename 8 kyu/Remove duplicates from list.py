# My solution
def distinct(seq):
    seq = list(dict.fromkeys(seq))
    return(seq)

# Interestign solution 1
def distinct(seq):
    return sorted(set(seq), key = seq.index)


# Interestign solution 2
def distinct(seq):
    nl = []
    [nl.append(i) for i in seq if i not in nl]
    return nl


# Interestign solution 3
def distinct(seq):
    result = []
    for item in seq:
        if item not in result:
            result.append(item)

    return result