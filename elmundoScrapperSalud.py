from bs4 import BeautifulSoup
import requests
import re
from datetime import date

page = requests.get("https://www.elmundo.es/salud.html")
soup = BeautifulSoup (page.content, 'html.parser')

cuerpo = soup.find("main", class_="main")
links=[]
noticias = cuerpo.find_all("article", class_="ue-c-cover-content")
for i in range(len(noticias)):

  cuerpo1 = noticias[i].find_next("div", class_="ue-c-cover-content__main")
  cuerpo2 = cuerpo1.find_next("header", class_="ue-c-cover-content__headline-group")
  for a in cuerpo2.find_all('a', href=True):
    if a.text:
      links.append(a['href'])

for i in range(len(links)):

  lista1=[]
  lista_tags=[]

  ruta = "el_mundo\\salud\\"
  datestr = date.today().strftime("%Y-%m-%d")
  archivo = open(ruta + "salud." + datestr + "." + str(i) + ".txt", "w", encoding="utf-8")
  
  page1 = requests.get(links[i])
  soup1 = BeautifulSoup (page1.content, 'html.parser')
  articulo = soup1.find("div", class_="ue-l-article__inner")
  
  if articulo is not None:
    titulo = articulo.find_next("h1", class_="ue-c-article__headline")
    cuerpotexto = articulo.find_next("div", class_="ue-l-article__body")
    textos = cuerpotexto.find_all("p")
    tags = soup1.find_all('li', class_="ue-c-article__tags-item")
    
    for i in tags:
      tag1 = i.get_text().replace("\n", "")
      tag2 = tag1.replace(" ", "")
      print(str(tag2))
      lista_tags.append(tag2)
    for z in lista_tags:
        archivo.write(z + ' ')
    archivo.write('\n')

    lista1.append(titulo.get_text())
    for i in textos:
      lista1.append(i.get_text())
    for z in lista1:
      archivo.write(z + '\n')
    archivo.close()
