a=10
print(type(a))
#système numérique: décimal
#On peut représenter le système numérique en plusieurs formes: décimal, binaire, hexadecima et octal

#représentation binaire
#0b ou 0B pour dire que la variable est présentée en binaire 0 et 1
somme=0b01111
total=0B11110001
print(somme)
print(total)

#représentation octal
#base octale de 1 à 7
#0o ou 0O
b=0o3175642
print(b)
c=0O54732
print(c)
#représentation hexadecimale de 0 à 9 et de a à f
#ox ou oX
d=0xface
print(d)
e=0Xface9
print(e)

#conversion de base
#commentaire1: conversion binaire
k=25
print(bin(k))
#commentaire2: conversion octale
print(oct(k))
#commentaire3: conversion hexadecimale
print(hex(k))