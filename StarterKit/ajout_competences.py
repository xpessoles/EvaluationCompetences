# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 22:03:05 2021

@author: Xavier Pessoles
"""
## Paramètres
dossier_comp = "2023_2024"
fichier_comp = "CompetencesXP_V3.xlsx"
onglet_comp  = "Competences"
filiere = 'PCSI-PSI' # Pour le choix du programme
discipline = "SII"
bdd = "BDD_Evaluation.db"

## Import de bibliothèques
from evaluation.fonctions import read_file_competences,ajout_competences_bdd


all_comp  = read_file_competences(dossier_comp, fichier_comp,filiere,discipline)
ajout_competences_bdd(all_comp, filiere, discipline, bdd)