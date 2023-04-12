# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 17:04:45 2023

@author: xpess
"""

import mechanize
import http.cookiejar as cookielib
import requests


import maskpass
PWD = maskpass.advpass()
#PWD ="dddd"
SITE = "https://2022.scei-concours.fr/WebLycees/#professeur"
#SITE = 'https://lamartinieremonplaisir.prepas-plus.fr/'
LOGIN = "xavier.pessoles@ac-lyon.fr"


# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(False)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# User-Agent (this is cheating....)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0')]

# # The site we will navigate into, handling it's session
br.open(SITE)

# Select the first form
br.select_form(nr=0)



# User credentials
br.form['login'] = LOGIN # Enter your username here
br.form['password'] = PWD # This is NOT my actual password.
# 
# Login
br.submit()
print("Login : done")

URL = "https://2022.scei-concours.fr/WebLycees/AfficheListeAdmissibilites.do"
br.open(URL)

for f in br.forms() :
    print('=============')
    print(f)
# url = "https://2022.scei-concours.fr/WebLycees/ExporterExcelNotesEcrit.do?codeConcours=1&codeBanque=1&codeClasse=21&sousClasseCode=null"
# # Searching the first link in the Devoirs tab.
# devoir_links =  [l for l in br.links(url_regex='devoirs')]
# devoir_link =  devoir_links[0]
# # Follow the link # This comment is useless, isn't it ?
# br.follow_link(devoir_link)
# 
# #Searching the links to the different DS
# DS_links =  [l for l in br.links(url_regex='noter/(\d+)')]
# print("{} links found".format(len(DS_links)))

"""
tab=renvoyer_etudiant(bdd_classe)
conn=sqlite3.connect(bdd_classe)
c=conn.cursor()
for n_ds,numds in enumerate(listes_DS):
    #br.follow_link(DS_link)
    url="https://lamartinieremonplaisir.prepas-plus.fr/devoirs/noter2?pk="+str(num_DS_plusplus[n_ds])
    print("Opening DS {}".format(n_ds)) # change this if your DS are numbered pythonically
    br.open(url)
    br.select_form(nr=0)
    i=0
    for (id_etudiant,nom) in tab:
        note=renvoyer_note_ds(nom,numds,c)
        if type(note)==type(1.0):
            note=round(note,2)
        print(id_etudiant,nom,note)
        print('Filling form-{}-note with value {}'.format(nom,note))
        # br.form['form-{}-note'.format(id_etudiant-1)] = str(note)
        br.form['form-{}-note'.format(i)] = str(note)
    # Click on the "Envoyer" button
        i+=1
    br.submit()
        
conn.commit()
conn.close()
"""
