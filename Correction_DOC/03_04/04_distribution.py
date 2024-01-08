#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from shutil import copyfile

num_DS = "02"
# Lire fichier eleve
file_eleve = "Eleves_MP_2023_2024.csv"

def lire_fichier_eleve(file):
    """Parser un fichier sous la forme 
    Nom, Prénom, Trinome, adresse, numero"""
    
    fid = open(file,'r')
    data = fid.readlines()
    fid.close()
    
    eleves = []
    cpt = 0
    for ligne in data :
        if cpt <= 9 : 
            scpt = "0"+str(cpt)
        else :
            scpt = str(cpt)
        ligne = ligne.rstrip()
        ligne = ligne.split(";")
        eleve = [ligne[0],ligne[1],ligne[3],ligne[4],scpt]
        eleves.append(eleve)
    return eleves


def make_rep(eleves):
    "Creation d'un repertoire par eleve, et copie du fichier htaccess"
    for eleve in eleves : 
        rep = 'www\\'+eleve[3]
        try :
            os.mkdir(rep)
        except FileExistsError:
            print(rep,"Fichier existant")
        copyfile(".htaccess",rep+'\\.htaccess')

def distribution_ds(ds:str,eleves):
    """ds : numéro du DS. (str: 01,...)
    Les copies doivent être dans le répertoire DS_ds 
    les élèves sont numérotés de 00 à nn.
    Les noms de copies doivent être de la forme psi_ds_nn
    """
    ds_dir = "DS_"+ds
   
    # On fait la liste des PDF
    liste_file = os.listdir(ds_dir)
    liste_pdf = []
    for file in liste_file : 
        if ".pdf" in file :
            liste_pdf.append(file)
           
    # On copie les PDF
    for pdf in liste_pdf : 
        # On cherche le numéro :
        num = pdf.split("_")
        # On supprime l'extension
        num = num[0]
        # On récupère le numéro d'anonymat
        num_ano = eleves[int(num)-1][3]
        print(num,num_ano)
        #On crée le dossier www\\num_ano\\DS_ds\\
        rep_DS = "www\\"+num_ano+"\\DS_"+ds
        print(rep_DS)
        try :
            os.mkdir(rep_DS)
        except FileExistsError:
            print(rep_DS,"Fichier existant")
            
        print("ICI")
        dest = "www\\"+num_ano+"\\DS_"+ds+"\\"+pdf
        src = ds_dir+"\\"+pdf
        print(src+" >> "+dest)
        copyfile(src,dest)
         
    
    
eleves = lire_fichier_eleve(file_eleve)
make_rep(eleves)
distribution_ds(num_DS,eleves)