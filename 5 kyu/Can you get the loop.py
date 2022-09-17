def loop_size(node):
    index = 0 
    nodes = {}
    while node not in nodes: 
        nodes[node] = index #getting the index of the current node
        node = node.next #moving to next node
        index += 1 #incrementing the node count
    return index - nodes[node] #Getting the length of the loop
    pass