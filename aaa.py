# import re
# frase = 'Pepe pica papas con un pico, picopapas pepe pepas pica papas repapas hola papas epapasd'
# secuencia = r'\w*papas\w*'
# busqueda = re.findall(secuencia, frase)
# busqueda = re.findall()
# print(busqueda)

#Librería para leer página en html
import urllib.request
#Librería para leer htlm y extraer datos de ello
import sys
from bs4 import BeautifulSoup
#Librería para buscar
import re
import requests

url = 'https://www.todamateria.com/celula/'
page = requests.get(url)
soup = BeautifulSoup(page.text)
filas = soup.select("tr")
equipos = soup.findAll("td",{"class": "biologia"})
print(biologia[0])



#Buscar Palabras    
# secuencia = r'\w*biologia\w*'
# busqueda = re.findall(secuencia, datos)

#Abrir .txt
# import codecs
# resumenTxt = codecs.open("Texto.txt","r","utf-8")
# lectura = resumenTxt.read()
# aa="Texto.txt"