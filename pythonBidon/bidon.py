class Bidon:
    zaz = "je suis un pro du python"

    def __init__(self, unTxt: str, unNum = 42, **kwargs):

        self.txt = unTxt
        self.num = unNum
        for k, v in kwargs.items():
            setattr(Bidon, k, v)    

def var2listsort(*args):
    listeTriee = []
    for x in args:
        listeTriee.append(x)
    bo = True
    while bo == True:
        bo = False
        for i in range(1, len(listeTriee), 1):
            if listeTriee[i-1] > listeTriee[i]:
                temp = listeTriee[i-1]
                listeTriee[i-1] = listeTriee[i]
                listeTriee[i] = temp
                #print("on permute", listeTriee[i-1], "et", listeTriee[i])
                bo = True
    return listeTriee

#var2listsort(40.3, 40.0, 39.8, 38.7, 39.9, 40.1, 38.80, 38.69)
        
