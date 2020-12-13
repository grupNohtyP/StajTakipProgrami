from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class OgretmenKontrol_MainWindow(object):
    
    def kabulEt(self):
        pass
    
    def reddet(self):
        pass
    
    def ara(self):
        pass
    
    def tumunuGoster(self):
        pass

    def kapat(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = OgretmenKontrol_MainWindow()
        self.ui.setupUi(self.window)
        MainWindow.close()
        
    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(968, 598)
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
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
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
"}\n"
"\n"
"QPlainTextEdit{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.defterliste = QtWidgets.QGroupBox(self.centralwidget)
        self.defterliste.setGeometry(QtCore.QRect(10, 30, 381, 561))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.defterliste.setFont(font)
        self.defterliste.setObjectName("defterliste")
        self.tblwDefter = QtWidgets.QTableWidget(self.defterliste)
        self.tblwDefter.setGeometry(QtCore.QRect(10, 100, 361, 411))
        self.tblwDefter.setRowCount(15)
        self.tblwDefter.setColumnCount(3)
        self.tblwDefter.setObjectName("tblwDefter")
        item = QtWidgets.QTableWidgetItem()
        self.tblwDefter.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwDefter.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwDefter.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwDefter.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwDefter.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwDefter.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwDefter.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwDefter.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwDefter.setItem(1, 2, item)
        self.cboxAylar = QtWidgets.QComboBox(self.defterliste)
        self.cboxAylar.setGeometry(QtCore.QRect(110, 60, 251, 21))
        self.cboxAylar.setObjectName("cboxAylar")
        self.cboxAylar.addItem("")
        self.cboxAylar.addItem("")
        self.cboxAylar.addItem("")
        self.cboxAylar.addItem("")
        self.cboxAylar.addItem("")
        self.cboxAylar.addItem("")
        self.cboxAylar.addItem("")
        self.cboxAylar.addItem("")
        self.cboxAylar.addItem("")
        self.cboxAylar.addItem("")
        self.cboxAylar.addItem("")
        self.cboxAylar.addItem("")
        self.lblAySec = QtWidgets.QLabel(self.defterliste)
        self.lblAySec.setGeometry(QtCore.QRect(20, 60, 81, 21))
        self.lblAySec.setObjectName("lblAySec")
        self.lineOgrenciTc = QtWidgets.QLineEdit(self.defterliste)
        self.lineOgrenciTc.setGeometry(QtCore.QRect(110, 30, 201, 20))
        self.lineOgrenciTc.setObjectName("lineOgrenciTc")
        self.lblOgrenciTc = QtWidgets.QLabel(self.defterliste)
        self.lblOgrenciTc.setGeometry(QtCore.QRect(20, 30, 81, 21))
        self.lblOgrenciTc.setObjectName("lblOgrenciTc")
        self.btnAra = QtWidgets.QPushButton(self.defterliste)
        self.btnAra.setGeometry(QtCore.QRect(320, 30, 51, 21))
        self.btnAra.setObjectName("btnAra")
        self.btnTumunuGoster = QtWidgets.QPushButton(self.defterliste)
        self.btnTumunuGoster.setGeometry(QtCore.QRect(200, 520, 171, 31))
        self.btnTumunuGoster.setObjectName("btnTumunuGoster")
        self.defteronay = QtWidgets.QGroupBox(self.centralwidget)
        self.defteronay.setGeometry(QtCore.QRect(400, 30, 561, 561))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.defteronay.setFont(font)
        self.defteronay.setStyleSheet("")
        self.defteronay.setObjectName("defteronay")
        self.btnKabul = QtWidgets.QPushButton(self.defteronay)
        self.btnKabul.setGeometry(QtCore.QRect(300, 30, 121, 21))
        self.btnKabul.setObjectName("btnKabul")
        self.btnRed = QtWidgets.QPushButton(self.defteronay)
        self.btnRed.setGeometry(QtCore.QRect(430, 30, 121, 21))
        self.btnRed.setObjectName("btnRed")
        self.lblOGrenciTc2 = QtWidgets.QLabel(self.defteronay)
        self.lblOGrenciTc2.setGeometry(QtCore.QRect(10, 30, 101, 21))
        self.lblOGrenciTc2.setObjectName("lblOGrenciTc2")
        self.lineOgrenciTc2 = QtWidgets.QLineEdit(self.defteronay)
        self.lineOgrenciTc2.setGeometry(QtCore.QRect(120, 30, 171, 20))
        self.lineOgrenciTc2.setObjectName("lineOgrenciTc2")
        self.defterdetay = QtWidgets.QGroupBox(self.defteronay)
        self.defterdetay.setGeometry(QtCore.QRect(10, 60, 541, 491))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.defterdetay.setFont(font)
        self.defterdetay.setObjectName("defterdetay")
        self.lineOgrenciTc3 = QtWidgets.QLineEdit(self.defterdetay)
        self.lineOgrenciTc3.setGeometry(QtCore.QRect(140, 30, 131, 20))
        self.lineOgrenciTc3.setObjectName("lineOgrenciTc3")
        self.lblOgrenciTc3 = QtWidgets.QLabel(self.defterdetay)
        self.lblOgrenciTc3.setGeometry(QtCore.QRect(20, 30, 111, 21))
        self.lblOgrenciTc3.setObjectName("lblOgrenciTc3")
        self.lineBaslamaTarihi = QtWidgets.QLineEdit(self.defterdetay)
        self.lineBaslamaTarihi.setGeometry(QtCore.QRect(140, 60, 131, 20))
        self.lineBaslamaTarihi.setText("")
        self.lineBaslamaTarihi.setObjectName("lineBaslamaTarihi")
        self.lblBaslamaTarihi = QtWidgets.QLabel(self.defterdetay)
        self.lblBaslamaTarihi.setGeometry(QtCore.QRect(20, 60, 111, 21))
        self.lblBaslamaTarihi.setObjectName("lblBaslamaTarihi")
        self.lblBitirmeTarihi = QtWidgets.QLabel(self.defterdetay)
        self.lblBitirmeTarihi.setGeometry(QtCore.QRect(280, 60, 111, 21))
        self.lblBitirmeTarihi.setObjectName("lblBitirmeTarihi")
        self.lineBitirmeTarihi = QtWidgets.QLineEdit(self.defterdetay)
        self.lineBitirmeTarihi.setGeometry(QtCore.QRect(400, 60, 131, 20))
        self.lineBitirmeTarihi.setText("")
        self.lineBitirmeTarihi.setObjectName("lineBitirmeTarihi")
        self.lblCalismaSuresi = QtWidgets.QLabel(self.defterdetay)
        self.lblCalismaSuresi.setGeometry(QtCore.QRect(20, 90, 111, 21))
        self.lblCalismaSuresi.setObjectName("lblCalismaSuresi")
        self.lineCalismaSuresi = QtWidgets.QLineEdit(self.defterdetay)
        self.lineCalismaSuresi.setGeometry(QtCore.QRect(140, 90, 71, 20))
        self.lineCalismaSuresi.setText("")
        self.lineCalismaSuresi.setObjectName("lineCalismaSuresi")
        self.lblGirilenTarih = QtWidgets.QLabel(self.defterdetay)
        self.lblGirilenTarih.setGeometry(QtCore.QRect(280, 90, 111, 21))
        self.lblGirilenTarih.setObjectName("lblGirilenTarih")
        self.lineGirilenTarih = QtWidgets.QLineEdit(self.defterdetay)
        self.lineGirilenTarih.setGeometry(QtCore.QRect(400, 90, 131, 20))
        self.lineGirilenTarih.setText("")
        self.lineGirilenTarih.setObjectName("lineGirilenTarih")
        self.label = QtWidgets.QLabel(self.defterdetay)
        self.label.setGeometry(QtCore.QRect(20, 130, 511, 21))
        self.label.setObjectName("label")
        self.textYapilanIslemler = QtWidgets.QPlainTextEdit(self.defterdetay)
        self.textYapilanIslemler.setGeometry(QtCore.QRect(20, 150, 511, 91))
        self.textYapilanIslemler.setStyleSheet("#yapilanisler{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.textYapilanIslemler.setObjectName("textYapilanIslemler")
        self.label_10 = QtWidgets.QLabel(self.defterdetay)
        self.label_10.setGeometry(QtCore.QRect(20, 250, 511, 21))
        self.label_10.setObjectName("label_10")
        self.textKabulEdilenDefter = QtWidgets.QPlainTextEdit(self.defterdetay)
        self.textKabulEdilenDefter.setGeometry(QtCore.QRect(20, 270, 511, 91))
        self.textKabulEdilenDefter.setStyleSheet("#yapilanisler{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.textKabulEdilenDefter.setObjectName("textKabulEdilenDefter")
        self.textReddedilenDefter = QtWidgets.QPlainTextEdit(self.defterdetay)
        self.textReddedilenDefter.setGeometry(QtCore.QRect(20, 390, 511, 91))
        self.textReddedilenDefter.setStyleSheet("#yapilanisler{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.textReddedilenDefter.setPlainText("")
        self.textReddedilenDefter.setObjectName("textReddedilenDefter")
        self.label_11 = QtWidgets.QLabel(self.defterdetay)
        self.label_11.setGeometry(QtCore.QRect(20, 370, 511, 21))
        self.label_11.setObjectName("label_11")
        self.uyari_2 = QtWidgets.QLabel(self.defterdetay)
        self.uyari_2.setGeometry(QtCore.QRect(220, 90, 41, 21))
        self.uyari_2.setStyleSheet("QLabel {\n"
"    border: none;\n"
"    padding: 0;\n"
"    \n"
"    background-color: beige;\n"
"}")
        self.uyari_2.setObjectName("uyari_2")
        self.btnKapat = QtWidgets.QPushButton(self.centralwidget)
        self.btnKapat.setGeometry(QtCore.QRect(904, 10, 51, 23))
        self.btnKapat.setObjectName("btnKapat")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.btnAra.clicked.connect(self.ara)
        self.btnKabul.clicked.connect(self.kabulEt)
        self.btnRed.clicked.connect(self.reddet)
        self.btnTumunuGoster.clicked.connect(self.tumunuGoster)
        self.btnKapat.clicked.connect(MainWindow.close)
        
        MainWindow.setWindowFlags(Qt.WindowType.WindowSystemMenuHint);
        MainWindow.setWindowIcon(QIcon("icon/python1.png"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ogretmen Kontrol"))
        self.defterliste.setTitle(_translate("MainWindow", "Detaylı Görüntülemek için defter seçin"))
        item = self.tblwDefter.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Öğrenci TC"))
        item = self.tblwDefter.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Başlama Tarihi"))
        item = self.tblwDefter.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Bitirme Tarihi"))
        __sortingEnabled = self.tblwDefter.isSortingEnabled()
        self.tblwDefter.setSortingEnabled(False)
        item = self.tblwDefter.item(0, 0)
        item.setText(_translate("MainWindow", "11111111111"))
        item = self.tblwDefter.item(0, 1)
        item.setText(_translate("MainWindow", "14/12/2020"))
        item = self.tblwDefter.item(0, 2)
        item.setText(_translate("MainWindow", "14/01/2021"))
        item = self.tblwDefter.item(1, 0)
        item.setText(_translate("MainWindow", "2222222222"))
        item = self.tblwDefter.item(1, 1)
        item.setText(_translate("MainWindow", "28/12/2020"))
        item = self.tblwDefter.item(1, 2)
        item.setText(_translate("MainWindow", "28/01/2021"))
        self.tblwDefter.setSortingEnabled(__sortingEnabled)
        self.cboxAylar.setItemText(0, _translate("MainWindow", "Ocak"))
        self.cboxAylar.setItemText(1, _translate("MainWindow", "Şubat"))
        self.cboxAylar.setItemText(2, _translate("MainWindow", "Mart"))
        self.cboxAylar.setItemText(3, _translate("MainWindow", "Nisan"))
        self.cboxAylar.setItemText(4, _translate("MainWindow", "Mayıs"))
        self.cboxAylar.setItemText(5, _translate("MainWindow", "Haziran"))
        self.cboxAylar.setItemText(6, _translate("MainWindow", "Temmuz"))
        self.cboxAylar.setItemText(7, _translate("MainWindow", "Ağustos"))
        self.cboxAylar.setItemText(8, _translate("MainWindow", "Eylül"))
        self.cboxAylar.setItemText(9, _translate("MainWindow", "Ekim"))
        self.cboxAylar.setItemText(10, _translate("MainWindow", "Kasım"))
        self.cboxAylar.setItemText(11, _translate("MainWindow", "Aralık"))
        self.lblAySec.setText(_translate("MainWindow", "Ay Seçiniz"))
        self.lblOgrenciTc.setText(_translate("MainWindow", "Öğrenci TC:"))
        self.btnAra.setText(_translate("MainWindow", "Ara"))
        self.btnTumunuGoster.setText(_translate("MainWindow", "Tümünü Göster"))
        self.defteronay.setTitle(_translate("MainWindow", "Staj Defteri Onayı"))
        self.btnKabul.setText(_translate("MainWindow", "Kabul Et"))
        self.btnRed.setText(_translate("MainWindow", "Reddet"))
        self.lblOGrenciTc2.setText(_translate("MainWindow", "Öğrenci TC:"))
        self.defterdetay.setTitle(_translate("MainWindow", "Staj Defteri Detay"))
        self.lblOgrenciTc3.setText(_translate("MainWindow", "Öğrenci TC:"))
        self.lblBaslamaTarihi.setText(_translate("MainWindow", "Başlama Tarihi:"))
        self.lblBitirmeTarihi.setText(_translate("MainWindow", "Bitirme Tarihi:"))
        self.lblCalismaSuresi.setText(_translate("MainWindow", "Çalışma Süresi"))
        self.lblGirilenTarih.setText(_translate("MainWindow", "Girilen Tarih:"))
        self.label.setText(_translate("MainWindow", "Yapılan İşler"))
        self.textYapilanIslemler.setPlainText(_translate("MainWindow", "Ram değiştirildi"))
        self.label_10.setText(_translate("MainWindow", "Kabul Edilen Staj Defteri"))
        self.textKabulEdilenDefter.setPlainText(_translate("MainWindow", "Anakart değiştirildi."))
        self.label_11.setText(_translate("MainWindow", "Reddedilen Staj Defteri"))
        self.uyari_2.setText(_translate("MainWindow", "Gün"))
        self.btnKapat.setText(_translate("MainWindow", "Kapat"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = OgretmenKontrol_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())
