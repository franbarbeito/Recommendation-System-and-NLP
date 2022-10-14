from franbarbeitofase1vista import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import glob
import csv
import re
import string
import unicodedata
import math
import os
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from PyQt5 import QtWidgets
import numpy as np




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Inicio()
        self.ui.setupUi(self)
        self.ui.searchBut.clicked.connect(self.goBuscar)
        self.ui.similiBut.clicked.connect(self.goBuscar1)
        self.ui.btnBuscarNoticia.clicked.connect(self.cargarDatos)
        self.ui.listaRanking.itemClicked.connect(self.cargarTexto)
        self.ui.categoriaSimi.itemClicked.connect(self.cargarPreview)
        self.ui.noticiasSimi.itemClicked.connect(self.cargarPreview1)
        self.ui.rankingSimi.itemClicked.connect(self.cargarTexto1)
        self.ui.buscarSimi.clicked.connect(self.cargarDatosSimi)





    def goBuscar(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def cargarDatos(self):
        
        self.ui.listaRanking.clear()
        busqueda = self.ui.consulta1.text()
        if busqueda == "":
            buttonReply = QtWidgets.QMessageBox.information(self, 'Error', "Porfavor introduce una noticia.", QtWidgets.QMessageBox.Ok)
        else:
            fuentes = ["20_minutos", "el_mundo", "el_pais"]
            categorias_array = ["ciencia", "salud", "tecnologia"]
            noticias_salud = []
            query = []
            results = []
            lista_final = []
            categoria = self.ui.filtrarpor.currentText().lower()
            top_n = self.ui.topn.currentText()



            
        #Tras comprobar si hemos introducido una query, ahora vamos a procesar todo el contenido de los archivos de las noticias.
        
        #Como hemos indicado, procesamos todo lo relacionado con salud
            for folder in range(1):
                if(categoria!="todos"):
                    for i in range(len(fuentes)):
                        files = glob.glob('*/' + categoria + '/*.txt')
                else:
                    print("No Implementado")
                for news_file in files:
                    new = open(news_file,  encoding="utf8")
                    archivo = new.read()
                    if archivo != None:
                        minus = archivo.lower()
                        re_punc = re.compile('[%s]' % re.escape(string.punctuation,))
                    
                        words = minus.split()
                        strip = [re_punc.sub('', w) for w in words]
                        sinpuntos = " ".join(strip)
                        sinpreguntas = sinpuntos.replace("¿", "")
                        apostrofes = sinpreguntas.replace("'","")
                        apostrofes = apostrofes.replace("\"","")
                        apostrofes = apostrofes.replace("`","")
                    
                        apostrofes = apostrofes.replace("´", "")
                        apostrofes = apostrofes.replace("‘", "")
                        apostrofes = apostrofes.replace("’", "")
                        apostrofes = apostrofes.replace("[", "")
                        apostrofes = apostrofes.replace("]", "")
                        apostrofes = apostrofes.replace("“", "")
                    
                        apostrofes = apostrofes.replace("”", "")
                        words = word_tokenize(apostrofes)
                        stop_words = set(stopwords.words('spanish'))
                        words = [w for w in words if not w in stop_words]
                        porter = PorterStemmer()
                        stemmed = [porter.stem(word) for word in words]
                        noticias_salud.append(stemmed)
            for n in noticias_salud:
                clean = str(n).replace("[","")
                clean = clean.replace("]","")
                clean = clean.replace("'","")
                clean = clean.replace(" ","")
                clean = clean.replace(",", ";")
            vectorizer = TfidfVectorizer()
            #Ahora realizamos el mismo proceso para la query introducida, para poder vectorizarla y hayar el coseno.

            minus1 = busqueda.lower()
            re_punc1 = re.compile('[%s]' % re.escape(string.punctuation,))
            words1 = minus1.split()
            strip1 = [re_punc1.sub('', w) for w in words1]
            sinpuntos1 = " ".join(strip1)
            
            sinpreguntas1 = sinpuntos1.replace("¿", "")
            apostrofes1 = sinpreguntas1.replace("'","")
            apostrofes1 = apostrofes1.replace("\"","")
            apostrofes1 = apostrofes1.replace("`","")
            apostrofes1 = apostrofes1.replace("´", "")
            
            apostrofes1 = apostrofes1.replace("‘", "")
            apostrofes1 = apostrofes1.replace("’", "")
            apostrofes1 = apostrofes1.replace("[", "")
            
            apostrofes1 = apostrofes1.replace("]", "")
            apostrofes1 = apostrofes1.replace("“", "")
            apostrofes1 = apostrofes1.replace("”", "")
            words1 = word_tokenize(apostrofes1)
            wordsFiltered = []
            stopWords = set(stopwords.words('spanish'))
            for w in words1:
                if w not in stopWords:
                    wordsFiltered.append(w)
            porter1 = PorterStemmer()
            stemmed1 = [porter1.stem(word) for word in wordsFiltered]
            for i in stemmed1:
                        for word in i.split():
                            query.append(word)
            for n in query:
                clean = str(n).replace("[","")
                clean = clean.replace("]","")
                clean = clean.replace("'","")
                clean = clean.replace(" ","")
                clean = clean.replace(",", ";")

                ##

            prueba = ""
            prueba1 = ""
            for i in noticias_salud:
                for j in i:
                    prueba = prueba + " " + j
                for k in query:
                    prueba1 = prueba1 + " " + k
                vector = vectorizer.fit_transform([prueba])
                vector1 = vectorizer.transform([prueba1])
                result = cosine_similarity(vector, vector1)
                result_list = result.tolist()
                for i in result_list:
                    results.append(i)
            
            for i in range(len(files)):
                asignacion = {'file': files[i], 'value': results[i]}
                lista_final.append(asignacion)
            def func_aux(e):
                return e['value']
            lista_final.sort(reverse=True, key=func_aux)
            
            n = len(lista_final)
             
            for i in range(1, int(top_n)+1 ):
                archivo1 = str(lista_final[i]['file'])
                valor = lista_final[i]['value'][0]
                valor = valor * 100
                objeto = "Valor: " + str(valor) + "%" + " Archivo: " + str(archivo1)
                self.ui.listaRanking.addItem(objeto)

    def cargarTexto(self):
        self.ui.previewSimi.clear()
        self.ui.listaRanking_2.clear()
        archivo = self.ui.listaRanking.currentItem().text()
        categoria = self.ui.filtrarpor.currentText().lower()


        fuentes = ["20_minutos", "el_mundo", "el_pais"]
        array_tags =[]
        array_aux = []
        array_similitudes = []
        lista_final1 = []

        
        codificar = (archivo).encode('utf-8')
        decodificar = (codificar).decode('utf8')
        
        peticion = re.compile("Archivo: ([\s\S]*)")
        search = peticion.search(decodificar)
        archivo1 = str(str(search.group(1)))
        resultado = open(archivo1, encoding="utf8")
        archivo2 = resultado.read()
        self.ui.textoNoticia.setText(archivo2)

        f = open(archivo1, encoding="utf8")
        tags_first = f.readline().replace("\n", "")
        y = tags_first.split(" ")  
        
        for folder in range(1):
            
            for i in range(len(fuentes)):
                files = glob.glob('*/' + categoria + '/*.txt')
            for news_file in files:
                contador = 0
                new = open(news_file,  encoding="utf8")
                evadir = new.readline()
                tags_second = new.readline().replace("\n", "").split(" ")
                array_tags.append(tags_second)
                for i in array_tags:
                    for j in i:
                        array_aux.append(j)

                for w in y:
                    for h in array_aux:
                        if w.lower()==h.lower():
                            contador = contador + 1
                dividendo = 2 * contador
                
                valor_conjunto1 = len(y)
                valor_conjunto2 = len(array_aux)
                divisor = valor_conjunto1 +  valor_conjunto2
                similitud = dividendo/divisor
                array_similitudes.append(similitud)

        for i in range(len(files)):
            asignacion = {'file': files[i], 'value': array_similitudes[i]}
            lista_final1.append(asignacion)
        def func_aux(e):
            return e['value']
        lista_final1.sort(reverse=True, key=func_aux)
        
        top_n1 = self.ui.topn.currentText()

        n = len(lista_final1)
        
        for i in range(0, int(top_n1) ):
            archivo1 = str(lista_final1[i]['file'])
            valor = lista_final1[i]['value']
            objeto = "Valor: " + str(valor) + " Archivo: " + str(archivo1)
            self.ui.listaRanking_2.addItem(objeto)

        


    def goBuscar1(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.medioSimi.addItem("El_Mundo",)
        self.ui.medioSimi.addItem("El_Pais")
        self.ui.medioSimi.addItem("20_Minutos")
        self.ui.categoriaSimi.addItem("Ciencia")
        self.ui.categoriaSimi.addItem("Salud")
        self.ui.categoriaSimi.addItem("Tecnologia")

    def cargarPreview(self):
        self.ui.noticiasSimi.clear()
        medio = self.ui.medioSimi.currentItem().text().lower()
        categoria = self.ui.categoriaSimi.currentItem().text().lower()
        noticias_salud = []
        fuentes = [medio]
        query = []
        results = []
        lista_final = []
        
        for i in range(len(fuentes)):
            files = glob.glob(medio + '/' + categoria + '/*.txt')
            
            
            for news_file in files:
                new = open(news_file,  encoding="utf8")
                archivo = new.read()
                if(len(archivo)!=0):
                    self.ui.noticiasSimi.addItem(news_file)

    def cargarPreview1(self):
        self.ui.previewSimi.clear()

        archivo = self.ui.noticiasSimi.currentItem().text()
        
        codificar = (archivo).encode('utf-8')
        decodificar = (codificar).decode('utf8')
        
        peticion = re.compile("([\s\S]*)")
        search = peticion.search(decodificar)
        archivo1 = str(str(search.group(1)))
        resultado = open(archivo1, encoding="utf8")
        archivo2 = resultado.read()
        if(len(archivo2)!=0):
            self.ui.previewSimi.setText(archivo2)

    def cargarDatosSimi(self):
        self.ui.rankingSimi.clear()
        categoria = self.ui.filtrarSimi.currentText().lower()
        busqueda = self.ui.previewSimi.toPlainText()
        fuentes = ["20_minutos", "el_mundo", "el_pais"]
        categorias_array = ['ciencia', 'salud', 'tecnologia']
        noticias_salud = []
        query = []
        results = []
        lista_final = []
        top_n = self.ui.topSimi.currentText()

        for folder in range(1):
           
            for j in range(len(fuentes)):
                files = glob.glob(categoria + '/' + '*' + '/*.txt')
                    
            for news_file in files:
                new = open(news_file,  encoding="utf8")
                archivo = new.read()
                if archivo != None:
                    minus = archivo.lower()
                    re_punc = re.compile('[%s]' % re.escape(string.punctuation,))
                
                    words = minus.split()
                    strip = [re_punc.sub('', w) for w in words]
                    sinpuntos = " ".join(strip)
                    sinpreguntas = sinpuntos.replace("¿", "")
                    apostrofes = sinpreguntas.replace("'","")
                    apostrofes = apostrofes.replace("\"","")
                    apostrofes = apostrofes.replace("`","")
                
                    apostrofes = apostrofes.replace("´", "")
                    apostrofes = apostrofes.replace("‘", "")
                    apostrofes = apostrofes.replace("’", "")
                    apostrofes = apostrofes.replace("[", "")
                    apostrofes = apostrofes.replace("]", "")
                    apostrofes = apostrofes.replace("“", "")
                
                    apostrofes = apostrofes.replace("”", "")
                    words = word_tokenize(apostrofes)
                    stop_words = set(stopwords.words('spanish'))
                    words = [w for w in words if not w in stop_words]
                    porter = PorterStemmer()
                    stemmed = [porter.stem(word) for word in words]
                    noticias_salud.append(stemmed)
        for n in noticias_salud:
            clean = str(n).replace("[","")
            clean = clean.replace("]","")
            clean = clean.replace("'","")
            clean = clean.replace(" ","")
            clean = clean.replace(",", ";")

        vectorizer = TfidfVectorizer()

        minus1 = busqueda.lower()
        re_punc1 = re.compile('[%s]' % re.escape(string.punctuation,))
        words1 = minus1.split()
        strip1 = [re_punc1.sub('', w) for w in words1]
        sinpuntos1 = " ".join(strip1)
        
        sinpreguntas1 = sinpuntos1.replace("¿", "")
        apostrofes1 = sinpreguntas1.replace("'","")
        apostrofes1 = apostrofes1.replace("\"","")
        apostrofes1 = apostrofes1.replace("`","")
        apostrofes1 = apostrofes1.replace("´", "")
        
        apostrofes1 = apostrofes1.replace("‘", "")
        apostrofes1 = apostrofes1.replace("’", "")
        apostrofes1 = apostrofes1.replace("[", "")
        
        apostrofes1 = apostrofes1.replace("]", "")
        apostrofes1 = apostrofes1.replace("“", "")
        apostrofes1 = apostrofes1.replace("”", "")
        words1 = word_tokenize(apostrofes1)
        wordsFiltered = []
        stopWords = set(stopwords.words('spanish'))
        for w in words1:
            if w not in stopWords:
                wordsFiltered.append(w)
        porter1 = PorterStemmer()
        stemmed1 = [porter1.stem(word) for word in wordsFiltered]
        for i in stemmed1:
                    for word in i.split():
                        query.append(word)
        for n in query:
            clean = str(n).replace("[","")
            clean = clean.replace("]","")
            clean = clean.replace("'","")
            clean = clean.replace(" ","")
            clean = clean.replace(",", ";")

            ##

        prueba = ""
        prueba1 = ""
        for i in noticias_salud:
            for j in i:
                prueba = prueba + " " + j
            for k in query:
                prueba1 = prueba1 + " " + k
            vector = vectorizer.fit_transform([prueba])
            vector1 = vectorizer.transform([prueba1])
            result = cosine_similarity(vector, vector1)
            result_list = result.tolist()
            for i in result_list:
                results.append(i)
        
        for i in range(len(files)):
            asignacion = {'file': files[i], 'value': results[i]}
            lista_final.append(asignacion)
        def func_aux(e):
            return e['value']
        lista_final.sort(reverse=True, key=func_aux)
        
        n = len(lista_final)
            
        for i in range(1, int(top_n)+1 ):
            archivo1 = str(lista_final[i]['file'])
            valor = lista_final[i]['value'][0]
            valor = valor * 100
            objeto = "Valor: " + str(valor) + "%" + " Archivo: " + str(archivo1)
            self.ui.rankingSimi.addItem(objeto)
    def cargarTexto1(self):
        self.ui.textoSimiResult.clear()
        self.ui.listaRanking_3.clear()

        archivo = self.ui.rankingSimi.currentItem().text()
        medio = self.ui.filtrarSimi.currentText().lower()


        fuentes = ["20_minutos", "el_mundo", "el_pais"]
        array_tags =[]
        array_aux = []
        array_similitudes = []
        lista_final1 = []
        
        codificar = (archivo).encode('utf-8')
        decodificar = (codificar).decode('utf8')
        
        peticion = re.compile("Archivo: ([\s\S]*)")
        search = peticion.search(decodificar)
        archivo1 = str(str(search.group(1)))
        resultado = open(archivo1, encoding="utf8")
        archivo2 = resultado.read()
        self.ui.textoSimiResult.setText(archivo2)

        f = open(archivo1, encoding="utf8")
        tags_first = f.readline().replace("\n", "")
        y = tags_first.split(" ")  
        
        for folder in range(1):
            
            for i in range(len(fuentes)):
                files = glob.glob('*/' + '*' + '/*.txt')
            for news_file in files:
                contador = 0
                new = open(news_file,  encoding="utf8")
                evadir = new.readline()
                tags_second = new.readline().replace("\n", "").split(" ")
                array_tags.append(tags_second)
                for i in array_tags:
                    for j in i:
                        array_aux.append(j)

                for w in y:
                    for h in array_aux:
                        if w.lower()==h.lower():
                            contador = contador + 1
                dividendo = 2 * contador
                
                valor_conjunto1 = len(y)
                valor_conjunto2 = len(array_aux)
                divisor = valor_conjunto1 +  valor_conjunto2
                similitud = dividendo/divisor
                array_similitudes.append(similitud)

        for i in range(len(files)):
            asignacion = {'file': files[i], 'value': array_similitudes[i]}
            lista_final1.append(asignacion)
        def func_aux(e):
            return e['value']
        lista_final1.sort(reverse=True, key=func_aux)
        
        top_n1 = self.ui.topn.currentText()

        n = len(lista_final1)
        
        for i in range(0, int(top_n1) ):
            archivo1 = str(lista_final1[i]['file'])
            valor = lista_final1[i]['value']
            objeto = "Valor: " + str(valor) + " Archivo: " + str(archivo1)
            self.ui.listaRanking_3.addItem(objeto)


        







        



                
        



       






if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()