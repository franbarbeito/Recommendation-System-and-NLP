# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'franbarbeitofase1.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Inicio(object):
    def setupUi(self, Inicio):
        Inicio.setObjectName("Inicio")
        Inicio.resize(1122, 879)
        self.centralwidget = QtWidgets.QWidget(Inicio)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.searchBut = QtWidgets.QCommandLinkButton(self.page)
        self.searchBut.setGeometry(QtCore.QRect(70, 710, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.searchBut.setFont(font)
        self.searchBut.setObjectName("searchBut")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(360, 230, 411, 401))
        self.label_3.setObjectName("label_3")
        self.similiBut = QtWidgets.QCommandLinkButton(self.page)
        self.similiBut.setGeometry(QtCore.QRect(880, 700, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.similiBut.setFont(font)
        self.similiBut.setObjectName("similiBut")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(340, 50, 421, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(79, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 1021, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(390, 30, 361, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(140, 130, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.consulta1 = QtWidgets.QLineEdit(self.page_2)
        self.consulta1.setGeometry(QtCore.QRect(230, 130, 711, 20))
        self.consulta1.setObjectName("consulta1")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(140, 200, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.topn = QtWidgets.QComboBox(self.page_2)
        self.topn.setGeometry(QtCore.QRect(210, 200, 51, 22))
        self.topn.setObjectName("topn")
        self.topn.addItem("")
        self.topn.addItem("")
        self.topn.addItem("")
        self.topn.addItem("")
        self.topn.addItem("")
        self.topn.addItem("")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(400, 200, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.filtrarpor = QtWidgets.QComboBox(self.page_2)
        self.filtrarpor.setGeometry(QtCore.QRect(470, 200, 111, 22))
        self.filtrarpor.setObjectName("filtrarpor")
        self.filtrarpor.addItem("")
        self.filtrarpor.addItem("")
        self.filtrarpor.addItem("")
        self.filtrarpor.addItem("")
        self.btnBuscarNoticia = QtWidgets.QPushButton(self.page_2)
        self.btnBuscarNoticia.setGeometry(QtCore.QRect(830, 190, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.btnBuscarNoticia.setFont(font)
        self.btnBuscarNoticia.setObjectName("btnBuscarNoticia")
        self.listaRanking = QtWidgets.QListWidget(self.page_2)
        self.listaRanking.setGeometry(QtCore.QRect(390, 270, 361, 81))
        self.listaRanking.setObjectName("listaRanking")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(530, 240, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.textoNoticia = QtWidgets.QTextEdit(self.page_2)
        self.textoNoticia.setGeometry(QtCore.QRect(40, 380, 401, 431))
        self.textoNoticia.setObjectName("textoNoticia")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(190, 350, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_19 = QtWidgets.QLabel(self.page_2)
        self.label_19.setGeometry(QtCore.QRect(700, 460, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.listaRanking_2 = QtWidgets.QListWidget(self.page_2)
        self.listaRanking_2.setGeometry(QtCore.QRect(610, 490, 361, 221))
        self.listaRanking_2.setObjectName("listaRanking_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setGeometry(QtCore.QRect(410, 0, 331, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        font.setItalic(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.page_3)
        self.label_11.setGeometry(QtCore.QRect(290, 50, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page_3)
        self.label_12.setGeometry(QtCore.QRect(540, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.page_3)
        self.label_13.setGeometry(QtCore.QRect(840, 10, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page_3)
        self.label_14.setGeometry(QtCore.QRect(550, 160, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.previewSimi = QtWidgets.QTextEdit(self.page_3)
        self.previewSimi.setGeometry(QtCore.QRect(210, 190, 751, 161))
        self.previewSimi.setObjectName("previewSimi")
        self.topSimi = QtWidgets.QComboBox(self.page_3)
        self.topSimi.setGeometry(QtCore.QRect(400, 390, 51, 22))
        self.topSimi.setObjectName("topSimi")
        self.topSimi.addItem("")
        self.topSimi.addItem("")
        self.topSimi.addItem("")
        self.topSimi.addItem("")
        self.topSimi.addItem("")
        self.topSimi.addItem("")
        self.label_15 = QtWidgets.QLabel(self.page_3)
        self.label_15.setGeometry(QtCore.QRect(330, 390, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.buscarSimi = QtWidgets.QPushButton(self.page_3)
        self.buscarSimi.setGeometry(QtCore.QRect(460, 380, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.buscarSimi.setFont(font)
        self.buscarSimi.setObjectName("buscarSimi")
        self.filtrarSimi = QtWidgets.QComboBox(self.page_3)
        self.filtrarSimi.setGeometry(QtCore.QRect(230, 390, 81, 22))
        self.filtrarSimi.setObjectName("filtrarSimi")
        self.filtrarSimi.addItem("")
        self.filtrarSimi.addItem("")
        self.filtrarSimi.addItem("")
        self.label_16 = QtWidgets.QLabel(self.page_3)
        self.label_16.setGeometry(QtCore.QRect(170, 390, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.rankingSimi = QtWidgets.QListWidget(self.page_3)
        self.rankingSimi.setGeometry(QtCore.QRect(190, 460, 331, 131))
        self.rankingSimi.setObjectName("rankingSimi")
        self.label_17 = QtWidgets.QLabel(self.page_3)
        self.label_17.setGeometry(QtCore.QRect(320, 440, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.textoSimiResult = QtWidgets.QTextEdit(self.page_3)
        self.textoSimiResult.setGeometry(QtCore.QRect(190, 650, 751, 161))
        self.textoSimiResult.setObjectName("textoSimiResult")
        self.label_18 = QtWidgets.QLabel(self.page_3)
        self.label_18.setGeometry(QtCore.QRect(510, 610, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.medioSimi = QtWidgets.QListWidget(self.page_3)
        self.medioSimi.setGeometry(QtCore.QRect(250, 80, 131, 61))
        self.medioSimi.setObjectName("medioSimi")
        self.categoriaSimi = QtWidgets.QListWidget(self.page_3)
        self.categoriaSimi.setGeometry(QtCore.QRect(520, 80, 131, 61))
        self.categoriaSimi.setObjectName("categoriaSimi")
        self.noticiasSimi = QtWidgets.QListWidget(self.page_3)
        self.noticiasSimi.setGeometry(QtCore.QRect(710, 40, 331, 131))
        self.noticiasSimi.setObjectName("noticiasSimi")
        self.listaRanking_3 = QtWidgets.QListWidget(self.page_3)
        self.listaRanking_3.setGeometry(QtCore.QRect(710, 400, 361, 221))
        self.listaRanking_3.setObjectName("listaRanking_3")
        self.label_20 = QtWidgets.QLabel(self.page_3)
        self.label_20.setGeometry(QtCore.QRect(800, 370, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.stackedWidget.addWidget(self.page_3)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        Inicio.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Inicio)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 21))
        self.menubar.setObjectName("menubar")
        Inicio.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Inicio)
        self.statusbar.setObjectName("statusbar")
        Inicio.setStatusBar(self.statusbar)

        self.retranslateUi(Inicio)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Inicio)

    def retranslateUi(self, Inicio):
        _translate = QtCore.QCoreApplication.translate
        Inicio.setWindowTitle(_translate("Inicio", "MainWindow"))
        self.searchBut.setText(_translate("Inicio", "B??SQUEDA"))
        self.label_3.setText(_translate("Inicio", "<html><head/><body><p><img src=\":/prefijoNuevo/app.jpg\"/></p></body></html>"))
        self.similiBut.setText(_translate("Inicio", "SIMILITUD"))
        self.label.setText(_translate("Inicio", "BIENVENIDO A LA APLICACI??N"))
        self.label_2.setText(_translate("Inicio", "En esta aplicaci??n se le ofrece la b??squeda de noticias sobre una amplia variedad, as?? como la posibilidad de comprar las mismas."))
        self.label_4.setText(_translate("Inicio", "B??SQUEDA DE NOTICIAS"))
        self.label_5.setText(_translate("Inicio", "Consulta"))
        self.label_6.setText(_translate("Inicio", "TOP-N:"))
        self.topn.setItemText(0, _translate("Inicio", "5"))
        self.topn.setItemText(1, _translate("Inicio", "6"))
        self.topn.setItemText(2, _translate("Inicio", "7"))
        self.topn.setItemText(3, _translate("Inicio", "8"))
        self.topn.setItemText(4, _translate("Inicio", "9"))
        self.topn.setItemText(5, _translate("Inicio", "10"))
        self.label_7.setText(_translate("Inicio", "Filtrar:"))
        self.filtrarpor.setItemText(0, _translate("Inicio", "Ciencia"))
        self.filtrarpor.setItemText(1, _translate("Inicio", "Todos"))
        self.filtrarpor.setItemText(2, _translate("Inicio", "Salud"))
        self.filtrarpor.setItemText(3, _translate("Inicio", "Tecnologia"))
        self.btnBuscarNoticia.setText(_translate("Inicio", "Buscar"))
        self.label_8.setText(_translate("Inicio", "Ranking:"))
        self.label_9.setText(_translate("Inicio", "Texto Noticia:"))
        self.label_19.setText(_translate("Inicio", "Quiz?? te interese:"))
        self.label_10.setText(_translate("Inicio", "SIMILITUD DE NOTICIAS"))
        self.label_11.setText(_translate("Inicio", "Medio:"))
        self.label_12.setText(_translate("Inicio", "Categor??a:"))
        self.label_13.setText(_translate("Inicio", "Noticias:"))
        self.label_14.setText(_translate("Inicio", "Preview:"))
        self.topSimi.setItemText(0, _translate("Inicio", "5"))
        self.topSimi.setItemText(1, _translate("Inicio", "6"))
        self.topSimi.setItemText(2, _translate("Inicio", "7"))
        self.topSimi.setItemText(3, _translate("Inicio", "8"))
        self.topSimi.setItemText(4, _translate("Inicio", "9"))
        self.topSimi.setItemText(5, _translate("Inicio", "10"))
        self.label_15.setText(_translate("Inicio", "TOP-N:"))
        self.buscarSimi.setText(_translate("Inicio", "Buscar"))
        self.filtrarSimi.setItemText(0, _translate("Inicio", "El_Mundo"))
        self.filtrarSimi.setItemText(1, _translate("Inicio", "El_Pais"))
        self.filtrarSimi.setItemText(2, _translate("Inicio", "20_minutos"))
        self.label_16.setText(_translate("Inicio", "Filtrar"))
        self.label_17.setText(_translate("Inicio", "Ranking:"))
        self.label_18.setText(_translate("Inicio", "Texto de la noticia"))
        self.label_20.setText(_translate("Inicio", "Quiz?? te interese:"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Inicio()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())