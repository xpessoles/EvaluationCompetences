#! /Users/ghaberer/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-


# étiquettes AVERY J7159 (63,5x33,9mm)

FILE_CSV = "liste_MP.csv"
REP_QR = "tmp_mp"
SUFFIXE = "_SII_MP_2023-2024_"
import qrcode
fid = open(FILE_CSV,encoding='utf-8')
data=fid.readlines()
fid.close()

les_eleves=[]
for ligne in data :
    eleve = ligne.replace(" ","-")
    eleve = eleve.replace("é","e")
    eleve = eleve.replace("'","-")
    eleve = eleve.rstrip()
    eleve = eleve.split(";")
    les_eleves.append(eleve)

index = 1
index = 1
with open('./'+REP_QR+'/qrcode.tex', "w",encoding="utf-8") as f:
    f.write('\\documentclass[a4paper,10pt]{article}\n')
    f.write('\\usepackage{graphicx}\n')
    f.write('\\usepackage[newdimens]{labels}\n')
    f.write('\\LabelCols=3%\n')
    f.write('\\LabelRows=8%\n')
    f.write('\\LeftPageMargin=7mm%\n')
    f.write('\\RightPageMargin=7mm%\n')
    f.write('\\TopPageMargin=13mm%\n')
    f.write('\\BottomPageMargin=13mm%\n')
    f.write('\\begin{document}\n')

    for eleve in les_eleves:

        indexstr = ""
        if index <10 :
            indexstr=("0"+str(index))
        else :
            indexstr = str(index)

        nom_devoir = indexstr+SUFFIXE+eleve[0]+"-"+eleve[1]
        print(nom_devoir)
        img = qrcode.make(nom_devoir)
        #print("./tmp/"+etudiant.nomsansespace+"-"+etudiant.prenom+".png")
        img.save('./'+REP_QR+"/"+eleve[0]+"-"+eleve[1]+".png")
        #f.write('\\addresslabel[]{\\raisebox{-12mm}{\\includegraphics[angle=0,width=30mm,height=30mm,keepaspectratio]{./tmp/'+etudiant.nomsansespace+'-'+etudiant.prenom+'.png'+'}}'+etudiant.nom+'}')
        Nom = eleve[0].upper()

        for i in range(1) : ### POUR FAIRE DES ETIQUETTES AVEC PLUSIEURS FOIS LE NOM
            f.write('\\addresslabel[]{\\raisebox{-12mm}{\\includegraphics[angle=0,width=30mm,height=30mm,keepaspectratio]{'+eleve[0]+'-'+eleve[1]+'.png'+'}}'+""+Nom+'}')
        index = index+1
        # f.write('\\begin{labels}')
        # f.write('\\begin{center}\n')
        # f.write('\\includegraphics[angle=0,width=30mm,height=30mm,keepaspectratio]{./tmp/'+etudiant.nomsansespace+'-'+etudiant.prenom+'.png'+'}\\\\\n')
        # f.write('\\small \\textsc{'+etudiant.nom.title()+'}\\\\\n')
        # f.write('\\scriptsize '+etudiant.prenom.title()+'\n')
        # f.write('\\end{center}')
        # f.write('\\end{minipage}\n')

    #f.write('\\\\\n')
    f.write('\\end{document}')
