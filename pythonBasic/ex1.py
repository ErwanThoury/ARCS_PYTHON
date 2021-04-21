def get_len_list(l: list):
    retour = []
    for i in l:
        if i != None:
            j = 0
            for y in i:
              j = j + 1
            retour.append(j)
        else:
            retour.append(0)
    return retour

#s = ["this", "is", "a", "simple", "test"]
#get_len_list(s)
        
