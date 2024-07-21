# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 12:59:33 2021

@author: xpess
"""

class Eleve : 
    """ Définition d'un élève """
    def __init__(self,eleve,annee,classe,el_id=None):
        self.nom = eleve[0]
        self.prenom = eleve[1]
        self.num = eleve[2]
        self.num_ano = eleve[3]
        self.mail = eleve[4]
        self.annee = annee
        self.classe = classe
        self.id = el_id
              
    @classmethod
    def from_sql(cls,el):
        """
        Requete permettant d'avoir un élève 
        req = "SELECT id,nom,prenom,num,num_ano,annee,classe,mail FROM eleves WHERE"+\
            " annee="+str(annee)+\
            " AND classe ='"+classe+"'"+" ORDER BY num"
        el=res[i]
            
        """
        el_id,nom,prenom,num,ano,annee,classe,mail = el
        elev = [nom,prenom,num,ano,mail]
        return cls(elev,annee,classe,el_id)
    
    def make_req(self):
        req = 'INSERT INTO eleves\
            (nom,prenom,num,num_ano,annee,mail,classe)VALUES ("'+\
                self.nom+'","'+\
                self.prenom+'","'+\
                str(self.num)+'","'+\
                str(self.num_ano)+'","'+\
                str(self.annee)+'","'+\
                self.mail+'","'+\
                self.classe+'" )'
                           
        return req
    
    def get_num(self):
        if self.num < 10 :
            return '0'+str(self.num)
        else :
            return str(self.num)