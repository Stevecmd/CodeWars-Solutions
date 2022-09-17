def is_valid_walk(walk):
    '''Returns whether a walk is equal to 10 minutes based on directions travelled
    and number of increments'''
    a =  walk.count('n') == walk.count('s') 
    b =  walk.count('e') == walk.count('w')
    length = len(walk) == 10
    return a and b and length