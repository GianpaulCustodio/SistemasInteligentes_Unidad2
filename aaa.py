import urllib.request
from bs4 import BeautifulSoup

url=input("Ingresa URL: ")
datos = urllib.request.urlopen(url).read().decode() 
soup = BeautifulSoup(datos).encode("utf-8")
a=str(soup)
TextoURL = open("URL.txt","w")
TextoURL.write(a)
TextoURL.close()