import urllib.request
import sys
from bs4 import BeautifulSoup
import re
datos = urllib.request.urlopen('https://elpais.com/america/').read().decode()
soup =  BeautifulSoup(datos)
tags = soup('a')
texto=''
n = input('Ingrese palabra: ')
for tag in tags:
  texto = tag.get('href')
  if type(texto) == str:
    if texto.count(n)>=1 and re.search('^[h]', texto):
      print(texto)