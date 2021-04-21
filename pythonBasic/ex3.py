def count_char(phrase: str):
    retour = {}
    for caractere in phrase:
        if caractere not in retour:
            retour[caractere] = 1
        else:
            retour[caractere] = retour[caractere] + 1
    return retour

#count_char("this is a test")
#count_char("sushi cat and yakitori dog")
