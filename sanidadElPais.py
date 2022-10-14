from bs4 import BeautifulSoup
import requests
import re
from datetime import date

page = requests.get("https://elpais.com/noticias/sanidad/")
soup = BeautifulSoup (page.content, 'html.parser')

cuerpo = soup.find_all("article", class_="story_card")
links=[]
for i in range(len(cuerpo)):
  link1 = cuerpo[i].find_next("h2")
  for a in link1.find_all('a', href=True): 
    if a.text: 
        links.append("https://elpais.com" + a['href'])
for i in range(len(links)):

  lista1=[]
  lista_tags=[]
  ruta = "el_pais\\salud\\"
  datestr = date.today().strftime("%Y-%m-%d")
  archivo = open(ruta + "salud." + datestr + "." + str(i) + ".txt", "w", encoding="utf-8")

  page1 = requests.get(links[i])
  soup1 = BeautifulSoup (page1.content, 'html.parser')
  articulo = soup1.find("article")
  header = articulo.find_next("h1")
  div1 = articulo.find("div", class_="a_b")
  if div1 is not None:
    textos = div1.find_all("p")

    head = soup1.find('head')
    tags = head.find_all("meta",  property="article:tag")
    

    for i in tags:
      tag1 = str(i['content'])
      lista_tags.append(tag1)
    for z in lista_tags :
        archivo.write(z + ' ')
    print("tags saved")
    archivo.write('\n')
    lista1.append(header.get_text())
    for i in textos:
      lista1.append(i.get_text())
    for y in lista1:
      archivo.write(y + '\n')
    archivo.close()