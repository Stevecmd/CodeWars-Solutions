# def sum_for_list(lst):
#     # largest = find largest abs value in lst
#     def simple_abs(num):
#         return -num if num < 0 else num #making numbers less than 0 negative
#     abs_value_lst = []
#     for i in lst:
#         value = simple_abs(i) 
#         abs_value_lst.append(value) #making a new list with -ve numbers that can be worked on
        
#     largest = max(abs_value_lst) #Getting the largest number in the array
#     # p = [prime numbers], from 2 to largest number 
#     p = []
#     count = 2 #beginning the count at 2
    
#     while count < largest:
#         isprime = True
        
#         for x in range(2, int((count/2) + 1)):
#             if count % x == 0: 
#                 isprime = False 
#                 break
        
#         if isprime:
#             p.append(count) #if the number is a prime its added to the list
        
#         count += 1
#     # sum_list = factor, sum
#     sum_list = []
#     sum = 0
#     counter = 0
#     #loop through prime array
    
#     for j in p:
#         sum = 0
#         counter = 0
#         for i in lst:
#         # loop through lst
#             if not i % j:
#                 sum += i
#                 counter += 1
#         if counter:
#             sum_list.append([j, sum])
#     #return result
#     return sum_list

def prime_factors(n):
    i = 2
    factors = []
    if n < 0:
        n *= -1
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def combine(arr1, arr2):
    for a in arr1:
        if not a in arr2:
            arr2.append(a)
    return arr2

def sum_for_list(lst):
    factors = []
    sums = []
    for i in range(len(lst)):
        combine(prime_factors(lst[i]),factors)
    for i in range(len(factors)):
        msum = 0
        for j in range(len(lst)):
            if not lst[j]%factors[i]:
                msum += lst[j]
        sums.append([factors[i], msum])
    sums.sort(key=lambda factors:factors[0])
    return sums 