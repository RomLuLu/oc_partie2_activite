from random import randint, choice
import string 
def mix_letters(string):
    """ fonction qui renvoie le mot avec les lettre dans le désordre"""
    l_string = list(string)
    l_mixed = list()
    c= 0
    while c < len(string):
        index = randint(0, len(l_string)-1)
        letter = l_string.pop(index)
        l_mixed.append(letter)
    
        c+=1
    return "".join(l_mixed)


print(mix_letters("bonjour"))


def random_letter():
    liste_letters = list()
    for i in range(8):
        letter = choice(string.ascii_uppercase)
        liste_letters.append(letter)
    return '-'.join(liste_letters)

print(random_letter())

    








