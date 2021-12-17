# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 22:03:05 2021

@author: Xavier Pessoles
"""


## Import de bibliothèques
import openpyxl
from pathlib import Path
import sqlite3
from evaluation.class_evaluation import Evaluation
from evaluation.class_question import Question

## Paramètres 
classe = 'PSIe'
annee = "2022" # Année de passage du concours
bdd = "BDD_Evaluation.db"
type_eval = "DS"
num_eval  = 1
date_eval = "16/12/2021"
dossier_notes = "Competences"
fichier_notes = "DS_N.xlsx"

evaluation = Evaluation(classe,type_eval,num_eval,date_eval)
    
def is_eval_exist(evaluation) -> str :
    """
    Renvoie -1 si l'évalation exite. 
    Renvoi l'ID si elle existe. 
    """
    conn = sqlite3.connect(bdd)
    c = conn.cursor()
    req  = evaluation.make_req_exist()
    c.execute(req)
    res = c.fetchall()
    conn.commit()
    conn.close()
    if res ==[] or res[0][0]=="" :
        return -1
    else : 
        return res[0][0]        

def add_evaluation_bdd(evaluation:Evaluation):
    id_eval = is_eval_exist(evaluation)
    if id_eval >-1 : 
        # On supprime l'évaluation
        conn = sqlite3.connect(bdd)
        c = conn.cursor()
        req = evaluation.make_req_del_eval()
        print(req)
        c.execute(req)
        conn.commit()
        conn.close()
        # On supprime les compétences liées à l'évaluation.       
    
  
    # On crée l'évaluation
    conn = sqlite3.connect(bdd)
    c = conn.cursor()
    req = evaluation.make_req_insertion()
    print(req)
    c.execute(req)
    conn.commit()
    conn.close()
    
    

add_evaluation_bdd(evaluation)



def read_bareme(dossier_notes, fichier_notes) -> list:
    """
    Retourne la liste des competences contenu dans le fichier de competences
    Parameters
    ----------
    dossier_comp : TYPE
        DESCRIPTION.
    fichier_comp : TYPE
        DESCRIPTION.

    Returns
    -------
    list
        list(Questions).

    """
    
    
    # Lire un fichier de notes       
    xlsx_file = Path(dossier_notes, fichier_notes)
    wb_obj = openpyxl.load_workbook(xlsx_file) 
    
    # Lecture du bareme
    # Read the active sheet:
    sheet = wb_obj['Bareme']
    nb_ligne = sheet.max_row
    #nb_col = sheet.max_column
    
    
    
    # Récupérer le nombre d'item evalués
    first_row = sheet[1] 
    nb_item=0
    ligne_Q = []
    for cell in first_row:
        if cell.value!=None and 'Q' in cell.value : 
            ligne_Q.append(cell.value)
            nb_item+=1
    # Récupération des poids 
    poids_row = sheet[3]
    ligne_poids = []
    for cell in poids_row:
            ligne_poids.append(cell.value)
            

    ligne_poids=ligne_poids[2:2+nb_item]

    bareme = [0 for i in range(nb_item)]
    
    for row in sheet.iter_rows(max_row=nb_ligne):
        ligne = []
        for cell in row:
             ligne.append(cell.value)
        
        # On vérifie que la ligne est une compétence évaluable
        # Pour cela il faut :
            # qu'elle ait un semestre dans la BDD
            # qu'elle ne commence pas par None
        if ligne[0]!=None and is_competence_evaluable(ligne[0]) :         
            code_comp = ligne[0]
            val = ligne[2:2+nb_item]
            for i in range(len(val)) :
                if val[i]!=0:
                    print(val)
                    id_eval =  0 # TODO avec la bdd
                    num_ques = 0 # TODO avec ligne_q
                    note =     0 # TODO avec val ?
                    poids=     0 # TODO avec ligne_poids
                    bareme[i]=Question(
                        id_eval,num_ques,code_comp,note,poids)
            #print(ligne,val)
    return bareme


def is_competence_evaluable(comp:str) -> bool :
    """
    Renvoie True si une compétence est évaluable. 
    Elle est évaluable si elle est associée à un semestre dans la BDD

    Parameters
    ----------
    comp : str
        DESCRIPTION.

    Returns
    -------
    bool 
        DESCRIPTION.

    """
    conn = sqlite3.connect(bdd)
    c = conn.cursor()
    req = "SELECT semestre FROM competences WHERE code = '"+ \
        comp+"'"
    c.execute(req)
    res = c.fetchall()
    conn.commit()
    conn.close()
    return res[0][0]!=""





def get_eval_id():
    
    return True


# def ajout_eleves_bdd(eleves : list):
#     # On vide la table
#     conn = sqlite3.connect(bdd)
#     c = conn.cursor()
#     req = "DELETE FROM eleves WHERE classe = '"+classe+\
#               "' AND annee = '"+annee+"'"
#     c.execute(req)
#     conn.commit()
#     conn.close()  
    
#     conn = sqlite3.connect(bdd)
#     for eleve in eleves : 
#         req = eleve.make_req()
#         c = conn.cursor()
#         c.execute(req)
#         conn.commit()
#     conn.close()
    
    
# Création de l'évaluation dans la BDD

# a=is_eval_exist(type_eval, num_eval)
# print(a)
# #all_eleves  = read_bareme(dossier_notes, fichier_notes)
#ajout_eleves_bdd(all_eleves)