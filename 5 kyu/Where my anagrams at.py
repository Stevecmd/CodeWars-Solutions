def anagrams(word, words):
    #your code here
    sort = sorted(word)
    return[item for item in words if sort == sorted(item)]