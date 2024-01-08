#!/bin/sh

# Dans chaque sous dossier, on fusionne les pdf et on ramène chq copie dans le dossier principal
echo "Fusion des pdf par étudiant"
liste=$(find . -maxdepth 1 -name "copie*")
for etudiant in $liste
do    
    # echo $etudiant
    netudiant=$(echo $etudiant | cut -c 9-)
    echo $netudiant
    cd $etudiant && pdftk *.pdf cat output $netudiant'.pdf' && cd ..
    mv $etudiant'/'$netudiant'.pdf' ./
done

mv page* ./tmp/
mv zpage* ./tmp/
mv ./copie*/ tmp/
