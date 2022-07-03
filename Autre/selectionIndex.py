Lorig = [3,1,2,4]

def cmp(x, y):
    return x <= y

def selection_sort_idx(L:list, cmp:"comp. fun."):
    
    def minimum(L:list, cmp:"comp. func"):
        mini = 0
        i =  1
        
        while i != len(L):
            if cmp(L[i],L[mini]):
                mini = i
            i += 1
        return mini
    def transfere(l, L):
        i = 0
        while i != len(L):
            l.append(L[i])
            i += 1
    l = []
    transfere(l, L)
    lRetour = []  
    i = 0
    while i != len(L):
            
        place = minimum(l[i:], cmp) + i
        temp = l[i]
        lRetour.append(L.index(l[place]))
        l[i] = l[place]
        
        l[place] = temp
        
        i += 1
    L = l
    return lRetour
print(selection_sort_idx(Lorig, cmp))
