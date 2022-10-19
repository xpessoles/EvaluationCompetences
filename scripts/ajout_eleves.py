# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 22:03:05 2021

@author: Xavier Pessoles
"""
## Paramètres 
dossier_eleve = "Competences"
fichier_eleve = "Eleves_PTSI2_2022_2023.xlsx"#"Eleves_PSIe_2022_2023.xlsx"
classe = "PTSI2"#"MPSI1"#'PSIe'
annee = "2023" # Année de passage du concours
bdd = "BDD_2022_2023.db"
    
from evaluation.fonctions import read_file_eleves,ajout_eleves_bdd 
    
all_eleves  = read_file_eleves(dossier_eleve, fichier_eleve,annee,classe)
ajout_eleves_bdd(all_eleves,bdd,classe,annee)