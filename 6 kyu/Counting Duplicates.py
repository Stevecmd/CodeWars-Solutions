def duplicate_count(text):
    text = text.lower() #this changes every character to lower case
    count = {i: text.count(i) for i in set(text)} #frequency of each character in the text
    count = sorted(count.values()) #Counting how many times the specific letters appear in the array.
    result = 0 #initialize the count at 0
    for i in count:
        if i > 1: #for every element thats counted, increase the count by 1
            result += 1
    return result # display the results