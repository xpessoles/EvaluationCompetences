# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 22:33:00 2021

@author: xpess
"""

class Competence : 
    """ Définition d'une compétence """
    def __init__(self,filiere,discipline):
        # Code défini par le programme
        self.code = ""
        # Type : macro compétence ou compétence
        self.type = ""
        self.discipline = discipline # Info/SII
        # Nom des compétences
        self.nom_long = ""
        self.nom_court = ""
        self.semestre = ""
        self.filiere = filiere
        
    
    def creer_comp(self,ligne:list):
        # compter le nombre de None
        nb_none = 0
        for e in ligne : 
            if e==None :
                nb_none +=1
        if nb_none == 0 :
            self.type = "Compétence"
            self.code = ligne[0]
            self.nom_long = ligne[1]
            self.nom_court = ligne[2]
            self.semestre = ligne[3]
        if nb_none == 1 :
            self.type = "Macro Compétence"
            self.code = ligne[0]
            self.nom_long = ligne[1]
            self.nom_court = ligne[2]
            
    def make_req(self):
        req = 'INSERT INTO competences \
            (discipline,filiere,code,nom_long,nom_court,semestre) \
                VALUES ("'+self.discipline+'",\
                        "'+self.filiere+'",\
                        "'+self.code+'",\
                        "'+self.nom_long+'",\
                        "'+self.nom_court+'",\
                        "'+str(self.semestre)+'" )'
                            
        return req