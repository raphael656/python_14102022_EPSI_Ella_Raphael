# exercice : Afficher un nombre aléatoire entre 1 et 10
import random
a = random.randrange(1,10)
print(a)


# EXERCICE 1 :

# Déclarer differentes type de variable
prenom = "Pierre"
age = 20
majeur = True
compte_en_banque = 20135,384
amis = ["Marie", "Julien", "Adrien"]
parents = ("Marc","Caroline")

print(prenom, ":" ,type(prenom) ,age,":" ,type(age) ,majeur,":" ,type(majeur),compte_en_banque,":" ,type(compte_en_banque),amis,":" ,type(amis),parents,":" ,type(parents))

#EXERCICE 2 :

# version corrigé
site_web = "google"

print(site_web)

# EXERCICE 3 :

a = "17"
b = int(a)
print("le nombre est :",b)


# EXERCICE 4

a = 3 
c = a
b=6
a=c 
b =7

print("la valeur de a est : ",c)

#EXERCICE 5
#afficher "a+b+c"
a = 2 
b = 6 
c = 3

print(a,b,c,sep = "+")

#EXERCICE 6

# list1 = range(3)
# list2 =  range(5)
# print(list1(list2))

# EXERCICE 7 

# verifier le type d'une variable 

prenom = "Vincent"

if type(prenom) == str :
    print("la variable est une chaine chaine de caractère")
if type(prenom) == int :
    print("la variable est un entier")
else :
    print("rien")
    
    


#Exercice 8

phrase = "Salut les dev"

phrase2 = phrase.replace("Salut","Bonsoir")
        
print(phrase2)

# remplacer un  termes double dans une phrase
phrase = "Salut les dev, salut le robot"

phrase2 = phrase.replace("Salut","Bonsoir")
        
print(phrase2) 
