# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 13:05:20 2021

@author: xpess
"""

class Question :
    """ Définition d'une question """
    def __init__(self,id_eval,num_ques,id_comp,note,poids):
        self.id_eval = id_eval
        self.num_ques = num_ques
        self.id_comp = id_comp
        self.note = note
        self.poids = poids
