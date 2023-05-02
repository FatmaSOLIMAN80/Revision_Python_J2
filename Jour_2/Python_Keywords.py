#Retrouvez les mots réservés de Python(Keywords)
import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))
a=25
#identifiants doivent être différents de Python Keywords
#ex: as=25 (as est un keyword Python)

#123somme=25
#les identifiants ne doivent pas commencer par un nombre
somme123=25

#somme$=25
#Les identifiants ne doivent pas contenir un caractère spécial
somme=25

_somme=25
#Les identifiants peuvent commencer par une underscore

def maFonction():
    pass