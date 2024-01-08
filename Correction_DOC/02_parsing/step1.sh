#!/bin/sh

# traitement des copies scannées.
# elles sont scannées en A3 ouvert, page du début en haut à droite avec pastille bleue dans le coin.
# le scan commence par la date, donc par deux mille : on en fait un seul fichier.
# UPDATE2022 : avec les nouveaux copieurs, la date est nulle : 12092022 pour le 12 septembre 2022...
# il faut modifier le script en conséquence.
# installation de pdftk : https://www.pdflabs.com/tools/pdftk-server/
echo "Fusion des scans en un seul fichier"
pdftk 1*.pdf cat output copiesA3.pdf
mkdir -p ./tmp
mv 1*.pdf ./tmp/

# on recoupe les a3 en a4
# installation de pdfposter : admin@bash-3.2$ pip install pdftools.pdfposter
echo "Découpage des a3 en a4"
pdfposter -p 2x1a4 copiesA3.pdf copiesA4tournees.pdf
mv copiesA3.pdf ./tmp/

# on tourne les pages, de la première à la dernière, vers l'ouest
# UPDATE2022 : les copies tournées sont déjà dans le bon sens
# echo "Rotation des pages a4"
# pdftk copiesA4tournees.pdf cat 1-endwest output copiesA4.pdf
# mv copiesA4tournees.pdf ./tmp/

# on sépare le tout en plein de pages
echo "Séparation en pages uniques"
# pdftk copiesA4.pdf burst
pdftk copiesA4tournees.pdf burst
mv copiesA4tournees.pdf ./tmp/



