from bs4 import BeautifulSoup
import requests
import re
from datetime import date

page = requests.get("https://www.20minutos.es/tecnologia/")
soup = BeautifulSoup (page.content, 'html.parser')

cuerpo = soup.find("div", class_="home-boards")
links=[]
board1 = cuerpo.find("div", class_="board-d6")
noticiasb1 = board1.find("ul")
listab1 = noticiasb1.find_all("li")
for i in range(len(listab1)):
  linksb1 = listab1[i].find_next("h1")
  for a in linksb1.find_all('a', href=True): 
    if a.text: 
        links.append(a['href'])

board2 = cuerpo.find("div", class_="board-f4")
noticiasb2 = board2.find_next("ul")
listab2 = noticiasb2.find_all("li")

for i in range(len(listab2)):
  linksb2 = listab2[i].find_next("h1")
  for a in linksb2.find_all('a', href=True): 
    if a.text: 
        links.append(a['href'])

for i in range(len(links)):
  
  lista1=[]
  lista_tags = []
  ruta = "20_minutos\\tecnologia\\"
  datestr = date.today().strftime("%Y-%m-%d")
  archivo = open(ruta + "tecnologia." + datestr + "." + str(i) + ".txt", "w", encoding="utf-8")
  

  page1 = requests.get(links[i])
  soup1 = BeautifulSoup (page1.content, 'html.parser')
  articulo = soup1.find("main", class_="page-article")
  if articulo is not None:
    header = articulo.find("section", class_="article-titles")
    titulo = header.find_next("h1")
    textarea = articulo.find("div", class_="article-text")
    textos = textarea.find_all("p")

    tags = articulo.find_all("li", class_="tag")
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

  
