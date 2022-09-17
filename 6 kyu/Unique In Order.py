def unique_in_order(iterable):
    solution = []
    for x in iterable:
        if len(solution) == 0 or solution[-1] != x:
            solution.append(x)
    return solution

# In this program, the solution checks whether the array is empty, the elements appear only once, 
# after which they are appended to X which is then printed