#! /Users/ghaberer/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-

####

# On renumérote ici les pages pour qu'elles soient dans l'ordre.

from os import listdir, rename

les_pages = [f for f in listdir('./') if f[:3] == 'pg_' and f[-3:] == "pdf"]
les_pages.sort()

nombre_de_pages = len(les_pages)
print("Il y a {} pages à traiter".format(nombre_de_pages))

les_pages_dans_lordre = []
for k in range(nombre_de_pages // 4):
    les_pages_dans_lordre.append(les_pages[1+4*k])
    les_pages_dans_lordre.append(les_pages[2+4*k])
    les_pages_dans_lordre.append(les_pages[3+4*k])
    les_pages_dans_lordre.append(les_pages[4*k])

print("Renumérotation des pages pour qu'elles soient dans l'ordre")    
for k, f in enumerate(les_pages_dans_lordre):
    numero = str(k)
    zeros = "0"*(4-len(numero))
    new_name = 'page_'+zeros+numero+'.pdf'
    # print('Je traite '+new_name)
    rename(f, new_name)
    
