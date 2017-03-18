#!/usr/bin/python
#-*- coding:utf-8 -*-

# Import the random module

import random
import json


# Liste de questions vide au depart"

qr_liste = []

#Definition de la fonction permettant d'importer les questions depuis le fichier questions.js

def questions_import(nom_fichier_json):
	"""Cette fonction permet de charger les questions depuis le fichier json"""
	global qr_liste
	with open(nom_fichier_json) as f:
		donnees = json.load(f)
		for entree in donnees:
			qr_liste.append(entree)

# On importe les question dans une liste (qr_liste)

questions_import("questions.json")

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
