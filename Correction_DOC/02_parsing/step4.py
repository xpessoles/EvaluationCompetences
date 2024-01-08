#! /Users/ghaberer/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-

from os import listdir, mkdir
from shutil import copyfile

f = open ("./tmp/premieres_pages.txt")
etudiant = -1
k = -1
for line in f:
    k += 1
    numero = str(k)    
    zeros = "0"*(4-len(numero))
    if "QR-Code" in line:
        etudiant += 1
        netudiant = line[17:-1]
        try : 
            mkdir('./copie_'+netudiant)
        except FileExistsError:
            print("Suivant...")
        print("Je traite l'étudiant {}".format(netudiant))
    copyfile('./page_'+zeros+numero+'.pdf', './copie_'+netudiant+'/page_'+zeros+numero+'.pdf')


