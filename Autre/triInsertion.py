def placement(x, l):
    i = 0
    boo = False
    po = len(l)
    while i != po and boo == False:
        #print(i, " est différent de ", len(l))
        if x < l[i]:
            l = l[:i] + [x] + l[i:]
            boo = True
        i += 1
    if boo == False:
        l.append(x)
    return l

def tri(l):
    lRetour = []
    i = 0
    while i != len(l):
        #print("on place ", l[i], " dans ", lRetour, "\n")
        lRetour = placement(l[i], lRetour) 
        i += 1
    return lRetour
