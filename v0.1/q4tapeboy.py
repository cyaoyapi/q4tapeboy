#!/usr/bin/python
#-*- coding:utf-8 -*-

# Import the random module

import random



# Créer une liste de dictionnaires contenant les "questions et reponses"
qr_liste = [
	{"q":"Quelle est la date de naissance de frère Branham ?","p":"\n1- 06 Avril 1906 \n2- 06 Mai 1909 \n3- 06 Avril 1909","j":3,"r":"3- 06 Avril 1909"},
	{"q":"Quelle est le nom des parents de frère Branham ?","p":"\n1- Charles et Meda Branham \n2- Charles et Ella Branham \n3- Charlin et Helena Branham","j":2,"r":"2- Charles et Ella Branham"},
	{"q":"En quelle année décéda Hope et Sharon Rose Branham ?","p":"\n1- 1937 \n2- 1933 \n3- 1955","j":1,"r":"1- 1937"},
	{"q":"Dans quelle ville la colonne a-t-elle été photographié en 1950 avec le frère Branham ?","p":"\n1- Tucson, Arizona \n2- Jeffersonville, Indianna \n3- Houston, Texas","j":3,"r":"3- Houston, Texas"},
	{"q":"Quel est l'animal qui est le petit ami de frère Branham","p":"\n1- l'Aigle \n2- La colombe \n3- Le rouge-gorge","j":3,"r":"3- Le rouge-gorge"},
	{"q":"J'ai peur des bruits de tonnerres, je veux un Dieu avec une peau","p":"\n1- Elie le Tshisbite \n2- Le petit Junior \n3- Jim Poole","j":2,"r":"2- Le petit Junior"},
	{"q":"Qui fut le premier pasteur associé de frère Branham au Branham Tabernacle","p":"\n1- Frère Orman Neville\n2- Frère DeArk \n3- Frère Graham Snelling","j":2,"r":"2- Le petit Junior"},
	{"q":"En quelle année frère Joseph a-t-il fondé VoGR ?","p":"\n1- 1990\n2- 1981 \n3- 1984","j":2,"r":"2- 1981"}
]

# Nombre de points
points = 0

# Nombre d'essais

essais = 0


# Definition de la fonction qui génére une question et réponse

def generer_qr():
  """ Cette fonction généère une question à partir de la liste des dictionnaires de questions et réponses"""
  global qr_liste
  global points
  global essais

  # génération aléatoire d'un index de question et réponse
  # Ancien Code commené de 2017-03617 : index_qr = random.randint(0, len(qr_liste) -1)
  question_ramene = random.choice(qr_liste)
  # On récupère la question
  # Ancien Code commené de 2017-03617 : question = qr_liste[index_qr]["q"]
  question = question_ramene["q"]

  # On récupère les propositions de choix
  # Ancien Code commené de 2017-03617 : propositions = qr_liste[index_qr]["p"]
  propositions = question_ramene["p"]
  # On récupère le numéro de la reponse juste
  # Ancien Code commené de 2017-03617 : num_reponse_juste = qr_liste[index_qr]["j"]
  num_reponse_juste = question_ramene["j"]
  # On récupère la reponse juste 
  # Ancien Code commené de 2017-03617 : reponse_juste = qr_liste[index_qr]["r"]
  reponse_juste = question_ramene["r"]

  print(question+propositions)

  reponse_joueur = -1

  while (reponse_joueur < 1) or (reponse_joueur > 3) :
  	reponse_joueur = raw_input("Entrez votre choix de reponse : \n")
  	if reponse_joueur.isdigit() == False:
  		print("Entrez un entier par les 3 choix proposés")
  		reponse_joueur = -1
  	elif int(reponse_joueur) < 1 or int(reponse_joueur) > 3:
  		print("Entrez un entier par les 3 choix proposés")
  		reponse_joueur = int(reponse_joueur)
  	else:
  		reponse_joueur = int(reponse_joueur)
  	

  essais += 1
  if(reponse_joueur == num_reponse_juste):
  	points += 1
  	print("Reponse juste.Bravo!\n")
  else:
  	print("Fausse réponse ! La réponse juste est : {}\n".format(reponse_juste))
  	
  print("Votre score est de : {} / {}".format(points,essais))

  # Ancien Code commené de 2017-03617 : del qr_liste[index_qr]

  qr_liste.remove(question_ramene)



quitter = ""

while (quitter.upper() != "Q") and (len(qr_liste) != 0):
  # Générer une question
  generer_qr()
  if(len(qr_liste) == 0):
    print("Vous avez essayé toutes les questions disponibles.\n")
    break
  quitter = raw_input("Tapez ENTREE pour continuer et Q pour quitter le jeu : \n")

print("Fin du programme.\nMerci et A bientôt!")
