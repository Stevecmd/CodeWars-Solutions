# 1.
def is_pangram(s):
    return len(set(filter(lambda x: x.isalpha(),s.lower()))) == 26

# len checks if the words are 26 since the alphabet contains 26 letters,
# set puts it all in a block so as to be filtered