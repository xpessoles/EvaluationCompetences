# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 12:57:07 2021

@author: xpess
"""

class Evaluation : 
    """ Définition d'un élève """
    def __init__(self,classe,type_eval,num_eval,date_eval):
        self.classe = classe
        self.type_eval = type_eval
        self.num_eval = num_eval
        self.date_eval = date_eval
             
    def make_req_insertion(self) -> str :
        """
        Création d'une requête peremttant d'ajouter une évaluation 
        dans une base de données SQL.
        Returns
        -------
        str 
            Requete SQL

        """
        req = 'INSERT INTO evaluations '+\
            '(type,date,classe,numero) '+ \
                'VALUES ("'+self.type_eval+'",'+\
                         '"'+self.date_eval+'",'+\
                         '"'+self.classe+'",'+\
                         '"'+str(self.num_eval)+'" )'
        return req
    
    def make_req_exist(self) -> str :
        """
        Création d'une requête permettant de savoir si une évaluation existe
        dans une BDD de donnée SQL.

        Returns
        -------
        str 
            requete SQL.

        """
        req = "SELECT id FROM evaluations WHERE "+\
            "type = '"+ self.type_eval+\
            "' AND numero = "+ str(self.num_eval)+\
            " AND date = '"+ self.date_eval+\
            "' AND classe = '"+ self.classe+"'" 
        return req
    
    def make_req_del_eval(self) -> str :
        req = "DELETE FROM evaluations WHERE  "+\
            "type = '"+ self.type_eval+\
            "' AND numero = "+ str(self.num_eval)+\
            " AND date = '"+ self.date_eval+\
            "' AND classe = '"+ self.classe+"'"
        return req