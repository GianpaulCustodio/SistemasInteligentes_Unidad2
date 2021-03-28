#Librería para leer página en html
import urllib.request
#Librería para leer htlm y extraer datos de ello
import sys
import codecs
from bs4 import BeautifulSoup
#Librería para buscar
import re

def UrlToHTML():
    url=input("Ingresa URL: ")
    datos = urllib.request.urlopen(url).read().decode()
    soup = BeautifulSoup(datos).encode("utf-8")
    a=str(soup)
    TextoURL = open("HTML.txt","w")
    TextoURL.write(a)
    TextoURL.close()
    LinksBusqueda(url)

def LinksBusqueda(url):
    datos = urllib.request.urlopen(url).read().decode()
    soup =  BeautifulSoup(datos)
    tags = soup('a')
    texto=''
    n = input('Ingrese palabra: ')
    c=0
    ficheros = open("Ficheros.txt","w")
    for tag in tags:
        texto = tag.get('href')
        if type(texto) == str:
            if texto.count(n)>=1 and re.search('^[h]', texto):
                c+=1
                ficheros.write(str(c) + ". "+ texto + "\n")
    ficheros.close()


UrlToHTML()
