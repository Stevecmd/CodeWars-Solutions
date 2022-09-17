def square_digits(num):
    answer = ''
    for num in map(int, str(num)): # Using a map to separate the digits and work on them
        answer += str(num**2)  # Only strings can be concatenated
    return int(answer) # return the final result of the concatenation


# Interesting solution 1
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))


# Simplest solution
def square_digits(num):
    stringnum = str(num)
    result = ""
    for digit in stringnum:
        result += str(int(digit) * int(digit))
    return int(result)