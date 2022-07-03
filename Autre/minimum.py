def minimum(l):
    mini = 0
    i =  1
    while i != len(l):
        if l[i] < l[mini]:
            mini = i
        i += 1
    return mini

def triSelection(l):
    i = 0
    while i != len(l):
        
        place = minimum(l[i:]) + i
        temp = l[i]
        l[i] = l[place]
        l[place] = temp
        
        i += 1

    return l
