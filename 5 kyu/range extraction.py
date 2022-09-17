# My solution
def solution(args):
    ans, tmp = [], []
    for x in args:
        if len(tmp) == 0:
            tmp.append(x)
        elif len(tmp) < 3: 
            if x - tmp[-1] == 1:
                tmp.append(x)
            else:
                ans.extend(map(str, tmp))
                tmp = [x]
        else:
            if x - tmp[-1] == 1:
                tmp.append(x)
            else:
                ans.append(str(tmp[0]) + '-' + str(tmp[-1]))
                tmp = [x]
    if len(tmp) != 0:
        if len(tmp) < 3:
            ans.extend(map(str, tmp))
        else:
            ans.append(str(tmp[0]) + '-' + str(tmp[-1]))
    return ",".join(ans)

    # Interesting solution 1
    # def solution(args):
    # result = ""

    # while len(args) > 0:
    #     first = last = args.pop(0)
    #     while (len(args) > 0) and (args[0] == last + 1):
    #         last = args.pop(0)

    #     if first == last:
    #         result += f"{first},"
    #     elif last - first == 1:
    #         result += f"{first},{last},"
    #     else:
    #         result += f"{first}-{last},"
    
    # return result[:-1]


    # Interesting solution 2
    # def solution(args):
    # out = []
    # beg = end = args[0]
    
    # for n in args[1:] + [""]:        
    #     if n != end + 1:
    #         if end == beg:
    #             out.append( str(beg) )
    #         elif end == beg + 1:
    #             out.extend( [str(beg), str(end)] )
    #         else:
    #             out.append( str(beg) + "-" + str(end) )
    #         beg = n
    #     end = n
    
    # return ",".join(out)