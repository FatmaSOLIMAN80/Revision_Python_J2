s1="Automatisation de tests"
s2='Test manuel'
s3="""
Test automatisé 
avec Selenium
"""
s4='''
Tests automatisé 
avec RobotFramework
'''
print(type(s1))
print(type(s2))
print(type(s3))
print(type(s4))

print(s1)
print(s2)
print(s3)
print(s4)

s5="L'hiver prochain il va faire chaud"
s6='Cet hiver est "excessivement" froid'
s7='L\'hiver prochain il va faire chaud'

#Slicing, découpage de chaine de caractères
s1="Automatisation de tests"
print(len(s1))

#indexation d'une liste de caractères, récupérer une lettre
print(s1[0])
print(s1[8])
print(s1[22])
print(s1[1])

#parcours inverse
print(s1[-1])
print(s1[-2])

s1="Automatisation de tests"
s2='Test manuel'
s8=s1+" "+s2
print(s8)

s9=s1*9
print(s9)

