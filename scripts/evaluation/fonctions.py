# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 12:54:46 2021

@author: xpess
"""
import openpyxl
from pathlib import Path
import sqlite3
from evaluation.class_competence import Competence
from evaluation.class_question import Question
from evaluation.class_evaluation import Evaluation
from evaluation.class_eleve import Eleve



##
def read_file_competences(dossier_comp, fichier_comp,filiere,discipline) -> list:
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
    # Lire un fichier de competences       
            
    xlsx_file = Path(dossier_comp, fichier_comp)
    wb_obj = openpyxl.load_workbook(xlsx_file) 
    
    # Read the active sheet:
    sheet = wb_obj.active
    nb_ligne = sheet.max_row
    #nb_col = sheet.max_column
    
    competences = []
    for row in sheet.iter_rows(max_row=nb_ligne):
        ligne = []
        for cell in row:
            ligne.append(cell.value)
        
        nb_none = 0
        for e in ligne : 
            if e==None :
                nb_none +=1
        if nb_none <= 1 :
            cp = Competence(filiere,discipline)
            cp.creer_comp(ligne)
            competences.append(cp)
        
    return competences


def ajout_competences_bdd(competences : list, filiere, discipline, bdd:str):
    # On vide la table
    req = "DELETE FROM competences WHERE filiere = '"+filiere+\
              "' AND discipline = '"+discipline+"'"
    res = exec_select(bdd,req)
    
    for competence in competences : 
        req = competence.make_req()
        res = exec_select(bdd,req)

       



def is_eval_exist(evaluation:Evaluation,bdd) -> str :
    """
    Renvoie -1 si l'évalation exite. 
    Renvoi l'ID si elle existe. 
    """
    req  = evaluation.make_req_exist()
    res = exec_select(bdd,req)

    
    if res ==[] or res[0][0]=="" :
        return -1
    else : 
        return res[0][0]        

def del_evaluation_bdd(evaluation:Evaluation,bdd):
    id_eval = is_eval_exist(evaluation,bdd)
    if id_eval >-1 : 
        # On supprime l'évaluation
        req = evaluation.make_req_del_eval()
        res = exec_select(bdd,req)

        
        # On supprime les questions liées l'évaluation
        req = evaluation.make_req_del_question(id_eval)
        res = exec_select(bdd,req)

        
        # On supprime les questions éleves liées à l'évaluation.
        req = evaluation.make_req_del_commentaires_eleves(id_eval)
        res = exec_select(bdd,req)

        req = evaluation.make_req_del_questions_eleves(id_eval)
        res = exec_select(bdd,req)

        
        
    

def add_evaluation_bdd(evaluation:Evaluation,bdd):
    # On crée l'évaluation
    req = evaluation.make_req_insertion()
    exec_select(bdd,req)

    
    
    # On garde l'id de l'évalution
    id_eval = is_eval_exist(evaluation,bdd)
    evaluation.set_id_eval(id_eval)
    
def ajout_eleves_bdd(eleves : list,bdd,classe,annee):
    # On vide la table
    req = "DELETE FROM eleves WHERE classe = '"+classe+\
              "' AND annee = '"+annee+"'"
    exec_select(bdd,req)
    
    for eleve in eleves : 
        req = eleve.make_req()
        exec_select(bdd,req)


def read_file_eleves(dossier_eleve, fichier_eleve,annee,classe) -> list:
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
    # Lire un fichier de competences       
            
    xlsx_file = Path(dossier_eleve, fichier_eleve)
    wb_obj = openpyxl.load_workbook(xlsx_file) 
    
    # Read the active sheet:
    sheet = wb_obj.active
    nb_ligne = sheet.max_row
    #nb_col = sheet.max_column
    
    eleves = []
    for row in sheet.iter_rows(max_row=nb_ligne):
        ligne = []
        for cell in row:
            ligne.append(cell.value)
        
        nb_none = 0
        for e in ligne : 
            if e==None :
                nb_none +=1
        if nb_none ==0 :
            
            # On numérote les élèves de 00 à nn.
            if ligne[2]<10:
                ligne[2]="0"+str(ligne[2])
            eleve = Eleve(ligne,annee,classe)
            eleves.append(eleve)
        
    return eleves




def read_bareme(dossier_notes, fichier_notes, evaluation:Evaluation,bdd) -> list:
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
    id_eval = evaluation.id_eval
    
    # Lire un fichier de notes       
    xlsx_file = Path(dossier_notes, fichier_notes)
    wb_obj = openpyxl.load_workbook(xlsx_file) 
    
    # Lecture du bareme
    # Read the active sheet:
    sheet = wb_obj['Bareme']
    nb_ligne = sheet.max_row
    #nb_col = sheet.max_column
    
    
    
    ## Récupérer le nombre d'item evalués et la liste des questions
    ###############################################################
    first_row = sheet[1] 
    nb_item=0
    ligne_Q = []
    for cell in first_row:
        if cell.value!=None and 'Q' in cell.value : 
            ligne_Q.append(cell.value)
            nb_item+=1

    # On ajoute le nombre d'itemes évalués 
    evaluation.set_nb_ques(nb_item)


    # Récupération des poids des questions
    poids_row = sheet[3]
    ligne_poids = []
    for cell in poids_row:
            ligne_poids.append(cell.value)

    ligne_poids=ligne_poids[2:2+nb_item]

    bareme = []


    for row in sheet.iter_rows(max_row=nb_ligne):

        ligne = []
        for cell in row:
             ligne.append(cell.value)
        
        # On vérifie que la ligne est une compétence évaluable
        if ligne[0]!=None and is_competence_evaluable(ligne[0],bdd) :
            code_comp = ligne[0]
            valeurs = ligne[2:2+nb_item]
            if sum(valeurs)>0 :
                index_q = -1
                for i in range(len(valeurs)):
                    if valeurs[i]!=0 :
                        index_q = i
                
                # On supprime le Q
                num_ques = int(ligne_Q[index_q][1:])
                note  = valeurs[index_q]
                poids = ligne_poids[index_q]
                nom = ligne_Q[index_q]
                q = Question(id_eval,num_ques,code_comp,note,poids,nom,index_q)
                bareme.append(q)
    return bareme


def is_competence_evaluable(comp:str,bdd) -> bool :
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
    req = "SELECT semestre FROM competences WHERE code = '"+ \
        comp+"'"
    res = exec_select(bdd,req)
    
    return res[0][0]!=""

def add_bareme_bdd(bareme:list,filiere, bdd) -> None:
    """
    bareme est une liste de question
    """
    index = 0
    for question in bareme : 
        # Détermination de l'id de la compétence  
        req = question.make_req_id_comp(filiere)
        res = exec_select(bdd,req)
        id_comp = res[0][0]
        
        # Ajout de la question
        req = question.make_req_insertion(id_comp)
        res = exec_select(bdd,req)
        index = index+1
        
        #Récupération de l'id de la question
        req = question.make_req_get_id() 
        res = exec_select(bdd,req)
        id_question = res[0][0]
        question.set_id_ques(id_question)
        
        
        
    
def read_notes(dossier_notes, fichier_notes, evaluation:Evaluation,bdd) -> list:
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
    sheet = wb_obj['Notes']
    nb_ligne = sheet.max_row
    #nb_col = sheet.max_column
    
    
    notes=[]    
    
    for row in sheet.iter_rows(max_row=nb_ligne):
        ligne = []
        for cell in row:
             ligne.append(cell.value)
        notes.append(ligne)
    
    # On récupère le nombre de lignes qui nous intéresse : 
    # de la 5ème au nombre d'élèves +5
    nb_eleves = get_nb_eleves(evaluation,bdd)
    notes = notes[4:4+nb_eleves]
    
    # On garde les lignes du nom au commentaire,
    # c'est à dire de l'index 0 à 2+nbQuesitons+1
    notes = [note[0:2+evaluation.nb_ques+1] for note in notes]    
    
    return notes

def get_nb_eleves(evaluation,bdd):
    
    classe = evaluation.classe
    annee = evaluation.annee
    req = "SELECT COUNT (id) FROM eleves WHERE "+\
        "classe='"+classe+"'"+\
        " AND annee='"+str(annee)+"'"
    res = exec_select(bdd,req)
    nb = res[0][0]
    return int(nb)


def add_notes_bdd(notes,evaluation:Evaluation,bareme,bdd):
    annee = evaluation.annee
    classe = evaluation.classe
    id_eval = evaluation.id_eval
    nb_quest = evaluation.nb_ques
    for note in notes :
        # On récupère l'id de l'élève
        num_el = note[1]
        req = "SELECT id from eleves WHERE"+\
            " num="+str(num_el) +\
            " AND"+" classe='"+classe +"'"+\
            " AND"+" annee="+str(annee)
        

        res = exec_select(bdd,req)
        
        id_eleve = res[0][0]
        
        # Pour chacune des questions on met la note
        for i in range(nb_quest):
            index_note = i+2
            id_question= bareme[i].id_ques
            n = note[index_note]
            # On ajoute la question à la BDD
            req = "INSERT INTO questions_eleves "+\
                "(id_eleve,id_eval,id_question,note_question) VALUES ("+\
                    str(id_eleve)+","+\
                    str(id_eval)+","+\
                    str(id_question)+",'"+\
                    str(n)+"')"
            
            
            exec_insert(bdd,req)
            
        # Pour chaque éval, on met le commentaire
        comment = note[-1]
        req = "INSERT INTO commentaires_eleves "+\
            "(id_eleve,id_eval,commentaire) VALUES ("+\
                str(id_eleve)+","+\
                str(id_eval)+",'"+\
                comment+"')"
        
        exec_insert(bdd,req)
    
       



def exec_insert(bdd,req):
    conn = sqlite3.connect(bdd)
    c = conn.cursor()
    c.execute(req)
    conn.commit()
    conn.close()
    
def exec_select(bdd,req):
    conn = sqlite3.connect(bdd)
    c = conn.cursor()
    c.execute(req)
    res = c.fetchall()
    conn.commit()
    conn.close()
    return res
    