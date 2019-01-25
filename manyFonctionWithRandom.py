from random import randint

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




