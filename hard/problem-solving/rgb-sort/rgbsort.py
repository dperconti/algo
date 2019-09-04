def sortRGB(a):
    cont = True
    while cont:
        cont = False
        for i, v in enumerate(a):
            if v != "R":
                if len(a) > i + 1:
                    if v == "B" and a[i + 1] == "G":
                        a = swap(a, i, i + 1)
                        cont = True
                    if a[i + 1] == "R":
                        a = swap(a, i, i + 1)
                        cont = True
    return a

def swap(list, pos1, pos2): 
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

assert(sortRGB(['G', 'B', 'R', 'R', 'B', 'R', 'G']) == ['R', 'R', 'R', 'G', 'G', 'B', 'B'])
assert(sortRGB(["G", "B", "R", "G", "R", "B", "R", "G", "R", "B", "R", "G", "R", "B", "R", "G", "R"]) == ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'G', 'G', 'G', 'G', 'G', 'B', 'B', 'B', 'B'])
assert(sortRGB(["R", "R", "R", "R", "R", "R", "R", "R", "R", "G", "B"]) == ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'G', 'B'])


