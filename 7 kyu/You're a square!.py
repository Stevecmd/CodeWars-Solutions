import math
def is_square(n):  #n is the given integral number 
    if (n < 0): #automatically negating negative numbers as they are not eligible
        return False
    square = math.sqrt(n) #square if the square root of n
    z = int(square) #converting n to an integer
    return (z ** 2 == n) #checking if z squared by itself is equal to n