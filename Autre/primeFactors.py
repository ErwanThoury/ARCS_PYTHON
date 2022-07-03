def primefactors(x):
    lRetour = []
    def recu(n, lRetour, i):
        if n == i:
            lRetour.append(n)
            return lRetour
        if n % i == 0:
            return recu(i, lRetour, 2), recu(int(n/i), lRetour, 2)
        return recu(n, lRetour, i + 1)
        
    return recu(x, lRetour, 2)[0] 
    
    
