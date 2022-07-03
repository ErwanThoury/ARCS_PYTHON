def triAbulle(l):
    booP = False
    while booP == False:
        i = 0
        boo = False
        while i != len(l) - 1:
            if(l[i] > l[i + 1]):
               temp = l[i]
               l[i] = l[i+1]
               l[i+1] = temp
               boo = True
            i += 1
        if boo != True:
               booP = True
    
            
            
        
        
