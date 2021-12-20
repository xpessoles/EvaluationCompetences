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
req = "SELECT id,nom,prenom,num,num_ano,annee,classe,mail FROM eleves WHERE"+\
    " annee="+str(annee)+\
    " AND classe ='"+classe+"'"+" ORDER BY num"
res = exec_select(bdd,req)
print('ELEVE')
print(res[0])

id_eval = is_eval_exist(evaluation,bdd)

#Synthèse d'un élève
eleve = Eleve.from_sql(res[4])
req = "SELECT id_eleve,id_eval,id_question,note_question FROM questions_eleves"+\
    " WHERE id_eval="+str(id_eval)+" AND id_eleve="+str(eleve.id)+" ORDER BY id_question"
res = exec_select(bdd,req)
print(req)
print('EVAL')
print("id_eleve,id_eval,id_question,note_question")
for r in res : print(r)
notes_eleve = res
# Récup des questions
req = "SELECT nom,num_ques,index_question,poids_comp,"+\
      " note_ques,code FROM questions "+\
          "JOIN competences ON questions.id_comp=competences.id "+\
              " WHERE id_eval="+str(id_eval)+" ORDER BY questions.id"
res = exec_select(bdd,req)
print(req)
print("nom,num_ques,index_question,poids_comp,note_ques,code")
for r in res : print(r)

bareme = res
# Calcul de la moyenne par eleve
note_brute=0
total_brut = 0
note_traitee=0
total_traite = 0
for i in range(len(bareme)):
    note_quest = notes_eleve[i][3]
    poids_question = bareme[i][3]
    note_quest_bareme = bareme[i][4]
    if note_quest!="NT":
        note_traitee += float(note_quest)*note_quest_bareme
        total_traite += note_quest_bareme*poids_question
    else : 
        note_quest = 0
       
    note_brute += float(note_quest)*note_quest_bareme
    total_brut += note_quest_bareme*poids_question

print(note_brute,total_brut,note_brute*20/total_brut)
print(note_traitee,total_traite,note_traitee*20/total_traite)