from itertools import islice
import re

texto="Texto.txt"
secuencia = r'\w*temporada1\w*'
busqueda = re.findall(secuencia, texto)
print(texto)
# with open(texto,'r',encoding="utf-8") as f:
#     #r1 = re.findall("policia",texto)
#     for l in islice(f,5):
#         print(l)