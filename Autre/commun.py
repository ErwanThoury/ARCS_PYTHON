def shared(l1, l2):
    comp = 0
    commun = []
    i = 0
    while i != len(l1):
        j = 0
        boo = False
        while j != len(l2) and boo == False:
            if l1[i] == l2[j]:
                commun.append(n)
                comp += 1
                boo = True
            j += 1
        i += 1
    return commun
