# My first solution wasnt quite right
# def is_uppercase(inp):
#     my_list = ["!","@","#","$","%","^","&","*","(",")" ,"{", "}" ,"[", "]", ":", '/"', ";", "'/''", ",", ".", "<", ">"]
#     list  = [("^[A-Za-z0-9_-]*$")]
#     if any([char in inp for char in list]):
#         return True
#     if any([char in inp for char in my_list]):
#         return True
#     elif inp.isupper():
#         return True
#     return False

# Much better solution that passes all the tests
def is_uppercase(inp):
    return str(inp).upper()==str(inp)