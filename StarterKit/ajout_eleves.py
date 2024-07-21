# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 22:03:05 2021

@author: Xavier Pessoles
"""
## Paramètres
dossier_eleve = "2023_2024"
fichier_eleve ="Eleves_PSIe_2023_2024.xlsx"


classe = "PSIe"#PSIe"#PTSI1"#PTSI2"#"MPSI1"#'PSIe'
annee = "2025" # Année de passage du concours des spés
bdd = "BDD_Evaluation.db"

from evaluation.fonctions import read_file_eleves,ajout_eleves_bdd

all_eleves  = read_file_eleves(dossier_eleve, fichier_eleve,annee,classe)
ajout_eleves_bdd(all_eleves,bdd,classe,annee)