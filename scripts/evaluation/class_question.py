# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 13:05:20 2021

@author: xpess
"""

class Question :
    """ Définition d'une question """
    def __init__(self,id_eval,num_ques,code_comp,note,poids,nom,index):
        self.id_eval = id_eval
        self.num_ques = num_ques
        self.code_comp = code_comp
        self.note = note
        self.poids = poids
        self.nom = nom
        self.index = index
    
    def set_id_ques(self,id_ques):
        self.id_ques = id_ques
    
    def make_req_id_comp(self,filiere):
        req = "SELECT id FROM competences WHERE "+\
            "code = '"+ self.code_comp+\
            "' AND filiere = '"+ filiere+"'"
        return req
    
    def make_req_insertion(self,id_comp):
        
        req = 'INSERT INTO questions '+\
            '(id_eval,num_ques,id_comp,note_ques,nom,index_question,poids_comp) '+ \
                'VALUES ("'+str(self.id_eval)+'",'+\
                         '"'+str(self.num_ques)+'",'+\
                         '"'+str(id_comp)+'",'+\
                         '"'+str(self.note)+'",'+\
                         '"'+str(self.nom)+'",'+\
                         '"'+str(self.index)+'",'+\
                         '"'+str(self.poids)+'" )'
        self.id_comp = id_comp
        return req
    
    def make_req_get_id(self):
        req = 'SELECT id FROM questions WHERE'+\
            " id_eval="+str(self.id_eval)+\
            " AND num_ques="+str(self.num_ques)+\
            " AND id_comp='"+str(self.id_comp)+"'"+\
            " AND note_ques="+str(self.note)+\
            " AND nom='"+str(self.nom)+"'"+\
            " AND index_question="+str(self.index)

        return req
    
    
    