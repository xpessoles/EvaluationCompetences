# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 22:03:05 2021

@author: Xavier Pessoles
"""


## Import de bibliothèques
from evaluation.class_evaluation import Evaluation
from evaluation.class_eleve import Eleve

from evaluation.fonctions import read_bareme,add_bareme_bdd
from evaluation.fonctions import add_evaluation_bdd,del_evaluation_bdd
from evaluation.fonctions import read_notes,add_notes_bdd
from evaluation.fonctions import exec_select,is_eval_exist
from evaluation.fonctions import get_eleves,get_questions_eval
from evaluation.fonctions import get_questions_eleve
from evaluation.fonctions import calc_note_eval,insert_note_eval_bdd

## Paramètres 
classe = 'PSIe'
filiere = "PCSI-PSI"
annee = "2022" # Année de passage du concours
bdd = "BDD_Evaluation.db"
type_eval = "DS"
num_eval  = 1
date_eval = "16/12/2021"
dossier_notes = "Competences"
fichier_notes = "DS_N.xlsx"


evaluation = Evaluation(classe,annee,type_eval,num_eval,date_eval)
#del_evaluation_bdd(evaluation,bdd)
"""
# On ajoute l'EVAL
add_evaluation_bdd(evaluation,bdd)
# On lit le bareme
bareme = read_bareme(dossier_notes, fichier_notes, evaluation,bdd)
# On ajoute le bareme a la BDD
add_bareme_bdd(bareme,filiere, bdd)

# On ajoute les notes de chacun des élèves
notes = read_notes(dossier_notes, fichier_notes, evaluation, bdd)

add_notes_bdd(notes,evaluation,bareme,bdd)
"""

# Génération des bilans

# Récupération des élèves
eleves = get_eleves(classe,annee,bdd)
eleve = eleves[4]


# Récupération des notes d'un élève
# dictionnaire de notes
notes_eleve = get_questions_eleve(evaluation,eleve,bdd)
id_eval = is_eval_exist(evaluation,bdd)

# Récup du bareme Liste de Questions
bareme = get_questions_eval(id_eval,bdd)

note_eval_eleve = calc_note_eval(bareme,notes_eleve)
# On écrit ca dans la base de données
insert_note_eval_bdd(eleve.id,id_eval,note_eval_eleve,bdd)



# bareme = res
# # # Calcul de la moyenne par eleve
# note_brute=0
# total_brut = 0
# note_traitee=0
# total_traite = 0
# for i in range(len(bareme)):
#     note_quest = notes_eleve[i][3]
#     poids_question = bareme[i][3]
#     note_quest_bareme = bareme[i][4]
#     if note_quest!="NT":
#         note_traitee += float(note_quest)*note_quest_bareme
#         total_traite += note_quest_bareme*poids_question
#     else : 
#         note_quest = 0
       
#     note_brute += float(note_quest)*note_quest_bareme
#     total_brut += note_quest_bareme*poids_question

# print(note_brute,total_brut,note_brute*20/total_brut)
# print(note_traitee,total_traite,note_traitee*20/total_traite)