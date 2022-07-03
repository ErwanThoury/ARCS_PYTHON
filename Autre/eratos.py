def era(n):
    l = [2]
    i =  3
    while i != n:
        boo = True
        for premier in l:
            if (i % premier) == 0:
                boo = False
        if boo == True:
            l.append(i)
        i += 1
    return l
            
