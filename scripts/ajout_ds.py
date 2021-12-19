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

id_eval = is_eval_exist(evaluation,bdd)

#Synthèse d'un élève
eleve = Eleve.from_sql(res[0])
req = "SELECT id_eleve,id_eval,id_question,note_question FROM questions_eleves"+\
    " WHERE id_eval="+str(id_eval)+" AND id_eleve="+str(eleve.id)+" ORDER BY id_question"
res = exec_select(bdd,req)
