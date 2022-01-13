# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 13:10:17 2022

@author: xpess
"""

# Lecture d'un fichier de note d'écrit
import xlrd
import sqlite3


file = "2021_PSI_Etoile_CentraleSupelec_Oral.xls"
file = "2012_PSI_Etoile_CCINP_Ecrit.xls"


def lecture_notes(file:str) : #-> list[dict]:
    """
    A partir d'un fichier xls provenant de scei, renvoie une liste de dictionnaires
    Chaque dictionnaire etant constitué des notes des eleves d'une classe

    Parameters
    ----------
    file : str
        Fichier xls.

    Returns
    -------
    list[dict]
        DESCRIPTION.

    """
    
    myBook = xlrd.open_workbook(file)
    sheet = myBook.sheet_by_index(0)
    
    # Caractéristiques du concours
    carac = sheet.cell_value(2, 0) 
    carac = carac.split("   ")
    CONCOURS = carac[0]
    BARRE = carac[1]
    
    if "barre" in BARRE : 
        BARRE=BARRE.split(' ')[1]
        
    # Caractéristiques d'une ligne (en vue d'en faire un dictionnaire)
    titre_colonnes = sheet.row(3)
    titre_colonnes = [v.value for v in titre_colonnes]
    
    dico_notes = []
    # Création d'une liste de dictionnaires
    for i in range(4,sheet.nrows):
        eleve = {}
        ligne = sheet.row(i)
        ligne = [v.value for v in ligne]
        eleve["ecole"]=CONCOURS
        for j in range(len(ligne)):
            eleve[titre_colonnes[j]]=ligne[j]
        dico_notes.append(eleve)
    return dico_notes


def exec_req(bdd,req):
    conn = sqlite3.connect(bdd)
    c = conn.cursor()
    c.execute(req)
    res = c.fetchall()
    conn.commit()
    conn.close()
    return res

def is_eleve_existe(num_scei:int,annee:int,bdd:str) -> bool:
    """
    Verfie si un eleve existe dans la BDD
    """
    req = "SELECT id FROM eleves WHERE "+\
        "num_scei='"+str(num_scei)+"'" +\
        " AND annee='"+str(annee)+"'"
    res = exec_req(bdd,req)
    
    if res ==[] or res[0][0]=="" :
        return False
    else : 
        return True

def get_id_eleve(num_scei:int,annee:int,bdd:str) -> bool:
    """
    Verfie si un eleve existe dans la BDD
    """
    req = "SELECT id FROM eleves WHERE "+\
        "num_scei='"+str(num_scei)+"'" +\
        " AND annee='"+str(annee)+"'"
    res = exec_req(bdd,req)
    
    return res[0]
    
def creation_eleve_bdd(eleve:dict,redoublant,classe,annee,bdd:str) -> None:
    req = "INSERT INTO eleves "+\
        "(num_scei,nom_prenom,classe,redoublant,annee) VALUES ("+\
            eleve["N°"]+","+\
            eleve["Nom"]+","+\
            classe+",'"+\
            redoublant+",'"+\
            str(annee)+"')"
    exec_req(bdd,req)
    
def ecrire_notes_bdd(bdd,dico_notes,classe,annee):
    
    for eleve in dico_notes : 
        num_scei = eleve["N°"]
        # On regarde si l'eleve existe, sinon on le crée
        if not(is_eleve_existe(num_scei,bdd)):
            # Par défaut on met les élèves en 3/2
            creation_eleve_bdd(eleve, "Non", classe, annee, bdd)
        id_eleve = get_id_eleve(num_scei,annee)
        # On inscrit l'élève aux écoles, si c'est des notes d'écrit
        # Pour CCMP, CCINP, CCMT, quand on inscrit aux banques, on inscrit à toutes
        # les écoles de la banque 
        if eleve["ecole"]=='Concours Commun INP PSI':
            banque = "CCINP"
    