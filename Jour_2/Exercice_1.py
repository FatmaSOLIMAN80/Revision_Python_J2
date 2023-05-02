#écrire un programme qui trouve le plus grand nombre parmi deux nombres en utilisant un prompt
#type casting
nbr1=int(input("Entrez le premier nombre"))
nbr2=int(input("Entrer le deuxième nombre"))
#print(type(nbr1),type(nbr2))
if nbr1>nbr2:
    print("Le plus grand nombre est: "+str(nbr1))
elif nbr2>nbr1:
    print("Le plus grand nombre est: "+str(nbr2))
else:
    print("Les deux nombres sont égaux")
