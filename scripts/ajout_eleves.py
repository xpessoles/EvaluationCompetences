# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 22:03:05 2021

@author: Xavier Pessoles
"""
## Paramètres
dossier_eleve = "2025_2026"
#fichier_eleve = "Eleves_PTSI1_2022_2023.xlsx"
#"Eleves_MP_2022_2023.xlsx"
#fichier_eleve ="Eleves_MP_2024_2025.xlsx"
fichier_eleve ="Eleves_MP_2025_2026.xlsx"
#"Eleves_PTSI1_2023_2024.xlsx"
#"Eleves_PTSI2_2023_2024.xlsx"#"Eleves_MP_2023_2024.xlsx"#
classe = "MP"#PSIe"#PTSI1"#PTSI2"#"MPSI1"#'PSIe'
annee = "2026" # Année de passage du concours des spés
bdd = "2025_2026_BDD.db"

from evaluation.fonctions import read_file_eleves,ajout_eleves_bdd

all_eleves  = read_file_eleves(dossier_eleve, fichier_eleve,annee,classe)
ajout_eleves_bdd(all_eleves,bdd,classe,annee)