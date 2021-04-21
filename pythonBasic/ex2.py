def make_pair(lA: list, lB: list):

    retour = []
    
    if len(lA) < len(lB):
        maxi = lB
        mini = lA
        
    else:
        maxi = lA
        mini = lB
    taille = 0
    lMax = len(maxi)
    for i in range(0, lMax,1):
    #for i in maxi:
        
        if taille < len(mini):
            retour.append((lA[i], lB[i]))

        else:
            if mini == lB:
                retour.append((lA[i], None))
            else:
                retour.append((None, lB[i]))
        taille = taille + 1
    return retour

#a = [2, 4, 6, 8]
#b = [3, 6, 9]
#make_pair(b, a)

            
