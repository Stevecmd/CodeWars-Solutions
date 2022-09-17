import string #to use to import an array of the alphabet
def rot13(message):
    alphabet = list(string.ascii_lowercase)
    result = ''
    for letter in message:
        if letter.lower() in alphabet:
            uppercase = letter.isupper() 
            index = alphabet.index(letter.lower()) #indexing the letters
            new_letter = alphabet[(index+13)%len(alphabet)] #indexing only latin/english letters 
            if uppercase:         
                new_letter = new_letter.upper()
            result += (new_letter)
        else:
            result += letter
    return result #instruction was to return result not print