# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 13:42:08 2022

@author: xavier.pessoles2
"""

import pyqrcode as pyqr
import qrtools 

#CODER
"""
eleve = pyqr.create("ALSKDJFSDLKJF SLDKJFLKSDJFLKSDJFLKSDJF LDSKJF LSKDJF SDLKJF ")
eleve.png("test.png",scale=2)
"""

# DECODER
"""qr = qrtools.QR()
qr.decode('FEUILLE.png')
"""

from pyzbar.pyzbar import decode
from PIL import Image
a=decode(Image.open('FEUILLE.png'))