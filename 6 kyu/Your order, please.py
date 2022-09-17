def order(sentence):
    words = sentence.split() #splitting the string into words
    string = [] #initializing the strings
    for n in range(1,10): #Defining a range of numbers for the words
        for a in words: 
            if str(n) in a : string.append(a) #If the input string is empty, return an empty string. 
    return " ".join(string) #Joining the results