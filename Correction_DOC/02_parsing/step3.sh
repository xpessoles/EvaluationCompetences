#!/bin/sh

# on convertit maintenant tous les pdf en png pour y repérer la pastille bleue/le qrcode
echo "Conversion des fichiers en png pour repérer les pastilles bleues/qrcode"
liste=$(find . -name "page*.pdf")
# echo $liste
for file in $liste
do	    
    #    echo $file
    jobname=$(echo $(echo "${file%.*}") | cut -c 3- )
    echo $jobname
    convert $file -colorspace RGB -alpha on 'z'$jobname'.png'
    result=$(zbarimg -q 'z'$jobname'.png')
    echo $jobname$result >> tmp/premieres_pages.txt    
done

sort tmp/premieres_pages.txt -o tmp/premieres_pages.txt

# ici, un fichier est créé avec les numéros des pages et les QR codes trouvés, le cas échéant.
# ce fichier est trié dans l'ordre des numéros de pages
