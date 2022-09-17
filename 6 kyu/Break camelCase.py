def solution(s):
    '''Solution returns the formatted string'''
    return  ''.join(list(map(upper, list(s))))
    
def upper(letter):
    '''Finds capital letters and returns it plus a space otherwise ignores'''
    return ' ' + letter if letter.isupper() else letter