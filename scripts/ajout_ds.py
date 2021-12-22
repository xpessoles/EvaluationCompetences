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
from evaluation.fonctions import add_evaluation_bdd
from evaluation.fonctions import read_notes,add_notes_bdd
from evaluation.fonctions import is_eval_exist
from evaluation.fonctions import get_eleves,get_questions_eval
from evaluation.fonctions import get_questions_eleve,insert_comp_bdd
from evaluation.fonctions import calc_note_eval,insert_note_eval_bdd
from evaluation.fonctions import classement_eval,ecriture_notes_eleves_tex
from evaluation.fonctions import plot_notes_brute
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


# On ajoute l'EVAL
add_evaluation_bdd(evaluation,bdd)
# On lit le bareme
bareme = read_bareme(dossier_notes, fichier_notes, evaluation,bdd)
# On ajoute le bareme a la BDD
add_bareme_bdd(bareme,filiere, bdd)

# On ajoute les notes de chacun des élèves
notes = read_notes(dossier_notes, fichier_notes, evaluation, bdd)

add_notes_bdd(notes,evaluation,bareme,bdd)



# Génération des bilans

# Récupération des élèves
eleves = get_eleves(classe,annee,bdd)
id_eval = is_eval_exist(evaluation,bdd)

bilan_evals = []


for eleve in eleves : 
    # Récup du bareme Liste de Questions
    bareme = get_questions_eval(id_eval,bdd)
    
    # Récupération des notes d'un élève
    # Dictionnaire de notes d'un éleve
    notes_eleve = get_questions_eleve(evaluation,eleve,bdd)
    
    # Calcul de l'élève
    note_eval_eleve = calc_note_eval(bareme,notes_eleve)
    # On écrit ca dans la base de données
    insert_note_eval_bdd(eleve.id,id_eval,note_eval_eleve,bdd)
    
    # On ajoute les compétences évaluées dans la base.
    insert_comp_bdd(eleve,id_eval,notes_eleve,bareme,filiere,bdd)
    
    bilan_evals.append(note_eval_eleve)


liste_evals = classement_eval(bilan_evals)

for eleve in eleves : 
    # Ecriture fichier tex
    print(eleve.nom)
    ecriture_notes_eleves_tex(eleve,notes_eleve,id_eval,bareme,liste_evals,"compil/f1.tex",bdd)
    plot_notes_brute(eleve.id,bilan_evals,"compil/histo.pdf")
    os.chdir("compil")
    os.system("pdflatex FicheDS.tex")
    os.system("pdflatex FicheDS.tex")
    fichier_eleve = eleve.get_num()+"_"+\
                    eleve.nom+"_"+\
                    eleve.prenom+"_"+\
                    evaluation.type_eval+"_"+\
                    str(evaluation.num_eval)+".pdf"
    os.rename("FicheDS.pdf",fichier_eleve)
    os.chdir("..")