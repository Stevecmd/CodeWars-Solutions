def valid_parentheses(input):
    stack=[]
    brackets={'[':']','{':'}','(':')','<':'>'} 
    for element in input:
        if element in ['(','{','[','<']:
            stack.append(element)
        elif element in [')','}',']','>']:
            try: 
                last_element=stack.pop()
                if brackets.get(last_element) == element: #checking if the opening and closing elements are similar eg ()
                    continue
                else :
                    return False #if the elements are not similar eg )) return false
            except IndexError: #mandatory for try statements
                return False
    if stack:       
        return False # if everything is validated
    else:
        return True