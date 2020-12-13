

from PyQt5 import QtCore, QtGui, QtWidgets
from ogretmenKontrol import OgretmenKontrol_MainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import sqlite3

baglanti=sqlite3.connect('stjyrtkp.sqlite')
imlec=baglanti.cursor()
baglanti.commit()


def listele():
        
    ui.tblwOgrenciTalep.clear()
    
    ui.tblwOgrenciTalep.setHorizontalHeaderLabels(('Öğrenci Adı Soyadı','Alan','Başvuru Tarihi','Mesaj'))
    ui.tblwOgrenciTalep.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    imlec.execute("SELECT ogrenci_adsoyad,ogrenci_alani,basvuru_Tarihi,mesaj FROM firma_basvurular")
    for satirIndeks, satirVeri in enumerate(imlec):
        for sutunIndeks, sutunVeri in enumerate (satirVeri):
            ui.tblwOgrenciTalep.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
    baglanti.commit()        
    

class OgretmenEkrani_MainWindow(object):
    def kabulEt(self):
        liste=[]
        _onay="Onaylandı"
        secili=self.tblwOgrenciTalep.selectedItems()
        _adSoyad = secili[0].text()
        _ogrAlan = secili[1].text()
        _basTarih = secili[2].text()
        imlec.execute("SELECT firma_onay FROM firma_basvurular WHERE \
                      ogrenci_adsoyad=? and ogrenci_alani=? and basvuru_tarihi=?",\
                          [_adSoyad,_ogrAlan,_basTarih])
        for satirIndeks, satirVeri in enumerate(imlec):
                for sutunIndeks, sutunVeri in enumerate (satirVeri):
                    liste.append(str(sutunVeri))
        baglanti.commit()

        if liste[0][0:9] == "Onaylandı":      
            cevap=QMessageBox.question(MainWindow,"Başvuru Onaylama","Başvuruyu Onaylamak İstediğinize Emin misiniz?",\
                         QMessageBox.Yes | QMessageBox.No)
            if cevap== QMessageBox.Yes:
                try:       
                    
                    imlec.execute("UPDATE firma_basvurular SET staj_onay=? WHERE ogrenci_adsoyad=?",(_onay,_adSoyad))
                    baglanti.commit()
                    
                except Exception as Hata:
                    self.statusbar.showMessage("Şöyle bir hata meydana geldi"+str(Hata))
        else:
            QMessageBox.warning(MainWindow,"Onay Yapılamaz","Firma Staj Başvurusunu Onaylamamış")
            
    def reddet(self):
        cevap=QMessageBox.question(MainWindow,"Başvuru Reddetme","Başvuruyu Reddetmek İstediğinize Emin misiniz?",\
                         QMessageBox.Yes | QMessageBox.No)
        if cevap== QMessageBox.Yes:
            try:
                _onay="Reddedildi"
                secili=self.tblwOgrenciTalep.selectedItems()
                _adSoyad =secili[0].text()
                imlec.execute("UPDATE firma_basvurular SET staj_onay=? WHERE ogrenci_adsoyad=?",(_onay,_adSoyad))
                baglanti.commit()
                baglanti.close()
            except Exception as Hata:
                self.statusbar.showMessage("Şöyle bir hata meydana geldi"+str(Hata))

        
        
    def kapat(self):
        cevap=QMessageBox.question(MainWindow,"Kapat","Kapatmak İstediğinize Emin misiniz?",\
                         QMessageBox.Yes | QMessageBox.No)
        if cevap== QMessageBox.Yes:
            self.window = QtWidgets.QMainWindow()
            self.ui = OgretmenEkrani_MainWindow()
            self.ui.setupUi(self.window)
            MainWindow.close()
            
        
    def ogretmenKontrolAc(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = OgretmenKontrol_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.close()
     
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 261)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet(".QWidget {\n"
"   background-color: beige;\n"
"}\n"
"\n"
"/* Nice Windows-XP-style password character. */\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"/* We provide a min-width and min-height for push buttons\n"
"   so that they look elegant regardless of the width of the text. */\n"
"QPushButton {\n"
"    background-color: palegoldenrod;\n"
"    border-width: 2px;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 5;\n"
"    padding: 3px;\n"
"    min-width: 9ex;\n"
"    min-height: 2.5ex;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: khaki;\n"
"}\n"
"\n"
"/* Increase the padding, so the text is shifted when the button is\n"
"   pressed. */\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: #d0d67c;\n"
"}\n"
"\n"
"QLabel, QAbstractButton {\n"
"    font: bold;\n"
"}\n"
"\n"
"/* Mark mandatory fields with a brownish color. */\n"
".mandatory {\n"
"    color: brown;\n"
"}\n"
"\n"
"/* Bold text on status bar looks awful. */\n"
"QStatusBar QLabel {\n"
"   font: normal;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border-width: 1;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 2;\n"
"}\n"
"\n"
"QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView {\n"
"    background-color: cornsilk;\n"
"    selection-color: #0a214c; \n"
"    selection-background-color: #C19A6B;\n"
"    border-width: 2px;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* We reserve 1 pixel space in padding. When we get the focus,\n"
"   we kill the padding and enlarge the border. This makes the items\n"
"   glow. */\n"
"QLineEdit, QFrame {\n"
"    border-width: 2px;\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border-color: darkkhaki;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* As mentioned above, eliminate the padding and increase the border. */\n"
"QLineEdit:focus, QFrame:focus {\n"
"    border-width: 3px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"/* A QLabel is a QFrame ... */\n"
"QLabel {\n"
"    border: none;\n"
"    padding: 0;\n"
"    background: none;\n"
"}\n"
"\n"
"/* A QToolTip is a QLabel ... */\n"
"QToolTip {\n"
"    border: 2px solid darkkhaki;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"/* Nice to have the background color change when hovered. */\n"
"QRadioButton:hover, QCheckBox:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* Force the dialog\'s buttons to follow the Windows guidelines. */\n"
"QDialogButtonBox {\n"
"    button-layout: 0;\n"
"}\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: palegoldenrod(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"   border-width: 2px;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius:44px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background-color: palegoldenrod;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-width: 2px;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-bottom-color: #darkkhaki; /* same as pane color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"QFrame{\n"
"    background-color: khaki;\n"
"    border-width: 2px;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 5;\n"
"    \n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnDefterOnay = QtWidgets.QPushButton(self.centralwidget)
        self.btnDefterOnay.setGeometry(QtCore.QRect(10, 220, 121, 31))
        self.btnDefterOnay.setObjectName("btnDefterOnay")
        self.btnKabul = QtWidgets.QPushButton(self.centralwidget)
        self.btnKabul.setGeometry(QtCore.QRect(280, 220, 121, 31))
        self.btnKabul.setObjectName("btnKabul")
        self.btnRed = QtWidgets.QPushButton(self.centralwidget)
        self.btnRed.setGeometry(QtCore.QRect(410, 220, 121, 31))
        self.btnRed.setObjectName("btnRed")
        self.tblwOgrenciTalep = QtWidgets.QTableWidget(self.centralwidget)
        self.tblwOgrenciTalep.setGeometry(QtCore.QRect(10, 60, 521, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblwOgrenciTalep.sizePolicy().hasHeightForWidth())
        self.tblwOgrenciTalep.setSizePolicy(sizePolicy)
        self.tblwOgrenciTalep.setBaseSize(QtCore.QSize(0, 0))
        self.tblwOgrenciTalep.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tblwOgrenciTalep.setAutoFillBackground(False)
        self.tblwOgrenciTalep.setLineWidth(1)
        self.tblwOgrenciTalep.setMidLineWidth(0)
        self.tblwOgrenciTalep.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tblwOgrenciTalep.setAlternatingRowColors(True)
        self.tblwOgrenciTalep.setShowGrid(True)
        self.tblwOgrenciTalep.setGridStyle(QtCore.Qt.SolidLine)
        self.tblwOgrenciTalep.setWordWrap(True)
        self.tblwOgrenciTalep.setRowCount(10)
        self.tblwOgrenciTalep.setColumnCount(4)
        self.tblwOgrenciTalep.setObjectName("tblwOgrenciTalep")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblwOgrenciTalep.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblwOgrenciTalep.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblwOgrenciTalep.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        item.setFont(font)
        self.tblwOgrenciTalep.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwOgrenciTalep.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwOgrenciTalep.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwOgrenciTalep.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwOgrenciTalep.setItem(0, 3, item)
        self.tblwOgrenciTalep.horizontalHeader().setVisible(True)
        self.tblwOgrenciTalep.horizontalHeader().setCascadingSectionResizes(False)
        self.tblwOgrenciTalep.horizontalHeader().setDefaultSectionSize(118)
        self.tblwOgrenciTalep.horizontalHeader().setMinimumSectionSize(39)
        self.tblwOgrenciTalep.horizontalHeader().setSortIndicatorShown(False)
        self.tblwOgrenciTalep.verticalHeader().setDefaultSectionSize(30)
        self.tblwOgrenciTalep.verticalHeader().setMinimumSectionSize(23)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnKapat = QtWidgets.QPushButton(self.centralwidget)
        self.btnKapat.setGeometry(QtCore.QRect(464, 20, 51, 23))
        self.btnKapat.setObjectName("btnKapat")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        self.btnKabul.clicked.connect(self.kabulEt)
        self.btnRed.clicked.connect(self.reddet)
        self.btnDefterOnay.clicked.connect(self.ogretmenKontrolAc)
        self.btnKapat.clicked.connect(self.kapat)
        
        MainWindow.setWindowFlags(Qt.WindowType.WindowSystemMenuHint);
        MainWindow.setWindowIcon(QIcon("icon/python1.png"))
        listele()
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Öğretmen İşlemleri"))
        self.btnDefterOnay.setText(_translate("MainWindow", "Staj Defteri Onay"))
        self.btnKabul.setText(_translate("MainWindow", "Kabul Et"))
        self.btnRed.setText(_translate("MainWindow", "Reddet"))
        self.tblwOgrenciTalep.setSortingEnabled(False)
        item = self.tblwOgrenciTalep.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Öğrenci Adı"))
        item = self.tblwOgrenciTalep.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Alan"))
        item = self.tblwOgrenciTalep.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Başvuru Tarihi"))
        item = self.tblwOgrenciTalep.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Mesaj"))
        __sortingEnabled = self.tblwOgrenciTalep.isSortingEnabled()
        self.tblwOgrenciTalep.setSortingEnabled(False)
        item = self.tblwOgrenciTalep.item(0, 0)
        item.setText(_translate("MainWindow", "Aslı Kılıç"))
        item = self.tblwOgrenciTalep.item(0, 1)
        item.setText(_translate("MainWindow", "Bilişim"))
        item = self.tblwOgrenciTalep.item(0, 2)
        item.setText(_translate("MainWindow", "5/12/2020"))
        item = self.tblwOgrenciTalep.item(0, 3)
        item.setText(_translate("MainWindow", "Staj Başvuru Onayı"))
        self.tblwOgrenciTalep.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Öğrenci Talep Listesi"))
        self.btnKapat.setText(_translate("MainWindow", "Kapat"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = OgretmenEkrani_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
