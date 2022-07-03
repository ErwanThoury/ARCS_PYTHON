def histo(s):
    l = [0] * 256
    for c in s:
        l[ord(c)] += 1
    return l

def dif(s):
    l = histo(s)
    comp = 0
    for i in l:
        if i != 0:
            comp += 1
    return comp

def fre(s):
    l = histo(s)
    maxiPos = 0
    maxi = 0
    i = 0
    while i != len(l):
        if l[i] > maxi:
            maxi = l[i]
            maxiPos = i
        i += 1
    if maxi == 0:
        return -1
    else:
        return (chr(maxiPos), maxi)
