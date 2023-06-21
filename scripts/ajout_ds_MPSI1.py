# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 22:03:05 2021

@author: Xavier Pessoles
"""


## Import de bibliothèques
#import matplotlib.pyplot as plt
import os
from evaluation.class_evaluation import Evaluation

from evaluation.fonctions import read_bareme,add_bareme_bdd
from evaluation.fonctions import add_evaluation_bdd,del_evaluation_bdd
from evaluation.fonctions import read_notes,add_notes_bdd,get_eleves
from evaluation.fonctions import generation_bilan_eval_indiv
from evaluation.fonctions import generation_bilan_competences


## Paramètres
classe = 'MPSI1'
filiere = "All"
discipline = 'Info'
annee = "2023" # Année de passage du concours
bdd = "BDD_2022_2023.db"
type_eval = "DS"
num_eval  = 10
date_eval = "09/06/2023"
dossier_notes = "2022_2023"
fichier_notes = "MPSI1_Info_DS_10.xlsx"

COEF_DS = 1

evaluation = Evaluation(classe,annee,type_eval,num_eval,date_eval)

# # On ajoute l'EVAL à la BDD
add_evaluation_bdd(evaluation,bdd)

# # On lit le bareme
bareme = read_bareme(dossier_notes, fichier_notes, evaluation,bdd)

# # On ajoute le bareme a la BDD
add_bareme_bdd(bareme,filiere, bdd)

# # On ajoute les notes de chacun des élèves dans la base de donnée
notes = read_notes(dossier_notes, fichier_notes, evaluation, bdd)
add_notes_bdd(notes,evaluation,bareme,bdd)

# # # Génération des bilans indivisualisés
generation_bilan_eval_indiv(classe,annee,filiere,evaluation,bdd,COEF_DS)

# # Génération du bilan de compétences
#eleves = get_eleves(classe,annee,bdd)
#eleve = eleves[0]
#generation_bilan_competences(eleve,classe,filiere,discipline,bdd)