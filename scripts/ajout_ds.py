# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 22:03:05 2021

@author: Xavier Pessoles
"""
## Paramètres 
classe = 'PSIe'
annee = "2022" # Année de passage du concours
bdd = "BDD_Evaluation.db"
type_eval = "DS"
num_eval  = "1"
date_eval = "16/12/2021"
dossier_notes = "Competences"
fichier_notes = "Eleves_PSIe.xlsx"

## Import de bibliothèques
import openpyxl
from pathlib import Path
import sqlite3


class Evaluation : 
    """ Définition d'un élève """
    def __init__(self,classe,type_eval,num_eval,date_eval):
        self.classe = classe
        self.type_eval = type_eval
        self.num_eval = num_eval
        self.date_eval = date_eval
             
    def make_req(self):
        req = 'INSERT INTO evaluations\
            (type,date,classe,numero) \
                VALUES ("'+self.type_eval+'",\
                        "'+self.date_eval+'",\
                        "'+self.classe+'",\
                        "'+self.num_eval+'" )'
                           
        return req
    
class Question :
    """ Définition d'une question """
    def __init__(self):
        self.id_eval = 0
        self.num_ques = 0
        self.id_comp = []
        self.note = 0
        self.poids = 0
        
class Question_Eleve :
    """ Définition d'une question pour un élève"""
    def __init__(self):
        self.id_eleve = 0
        self.id_ds = 0
        self.id_ques = 0
        self.note = 0
        



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
        list(Competence).

    """
    # Lire un fichier de notes       
    
    xlsx_file = Path(dossier_notes, fichier_notes)
    wb_obj = openpyxl.load_workbook(xlsx_file) 
    
    # Lecture du bareme
    # Read the active sheet:
    sheet = wb_obj.active
    nb_ligne = sheet.max_row
    #nb_col = sheet.max_column
    
    barreme = []
    for row in sheet.iter_rows(max_row=nb_ligne):
        ligne = []
        for cell in row:
            ligne.append(cell.value)
        

          
        
    return eleves


def ajout_eleves_bdd(eleves : list):
    # On vide la table
    conn = sqlite3.connect(bdd)
    c = conn.cursor()
    req = "DELETE FROM eleves WHERE classe = '"+classe+\
              "' AND annee = '"+annee+"'"
    c.execute(req)
    conn.commit()
    conn.close()  
    
    conn = sqlite3.connect(bdd)
    for eleve in eleves : 
        req = eleve.make_req()
        c = conn.cursor()
        c.execute(req)
        conn.commit()
    conn.close()
    
    
    
all_eleves  = read_file_competences(dossier_eleve, fichier_eleve)
ajout_eleves_bdd(all_eleves)