# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:07:52 2020

@author: etuna
"""



#----------------------KÜTÜPHANE--------------------------#
#---------------------------------------------------------#
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
#from MainWindowForm import *

#----------------------UYGULAMA OLUŞTUR-------------------#
#---------------------------------------------------------#
Uygulama=QApplication(sys.argv)
penAna=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()



#----------------------VERİTABANI OLUŞTUR-----------------#
#---------------------------------------------------------#
import sqlite3
global curs
global conn

conn=sqlite3.connect('veritabani.db')
curs=conn.cursor()
sorguCreTblogrenci=("CREATE TABLE IF NOT EXISTS ogrenci(                 \
                 Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,    \
                 TCNo TEXT NOT NULL UNIQUE,                        \
                 ogAdi TEXT NOT NULL,                          \
                 ogSoyadi TEXT NOT NULL,                       \
                 okulNo TEXT NOT NULL,                           \
                 sinifi TEXT NOT NULL,                              \
                 ogTelno TEXT NOT NULL)")
curs.execute(sorguCreTblogrenci)
conn.commit()

#----------------------KAYDET-----------------------------#
#---------------------------------------------------------#
def EKLE():
    
    _ogTCno=ui.ogTCno.text()
    _ogAdi=ui.ogAdi.text()
    _ogSoyadi=ui.ogSoyadi.text()
    _ogOklno=ui.ogOklno.text()
    _ogSinif=ui.ogSinif.text()
    _ogTelno=ui.ogTelno.text()
 
    
            
    curs.execute("INSERT INTO ogrenci \
                     (TCNo,ogAdi,ogSoyadi,okulNo,sinifi,ogTelno) \
                      VALUES (?,?,?,?,?,?)", \
                      (_ogTCno,_ogAdi,_ogSoyadi,_ogOklno,_ogSinif,_ogTelno))
    conn.commit()
    
    
    LISTELE()
#----------------------LİSTELE-----------------------------#
#---------------------------------------------------------#  
def LISTELE():
    
    ui.ogKayitlar.clear()
    
    ui.ogKayitlar.setHorizontalHeaderLabels(('No','TC Kimlik No','Öğr. Adı','Öğr.Soyadı','Okul No', 'Sınıfı', 'Telefon'))
    
    ui.ogKayitlar.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    
    curs.execute("SELECT * FROM ogrenci")
    
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate (satirVeri):
            ui.ogKayitlar.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
    ui.ogTCno.clear()
    ui.ogAdi.clear()
    ui.ogSoyadi.clear()
    ui.ogOklno.clear()
    ui.ogSinif.clear()
    ui.ogTelno.clear()

    


LISTELE()


#----------------------DOLDUR-----------------------------#
#---------------------------------------------------------#
def DOLDUR():
    secili=ui.ogKayitlar.selectedItems()
    ui.ogTCno.setText(secili[1].text())
    ui.ogAdi.setText(secili[2].text())
    ui.ogSoyadi.setText(secili[3].text())
    ui.ogOklno.setText(secili[4].text())
    ui.ogSinif.setText(secili[5].text())
    ui.ogTelno.setText(secili[6].text())
    



#----------------------SİL-----------------------------#
#---------------------------------------------------------# 
def SIL():
    cevap=QMessageBox.question(penAna,"KAYIT SİL","Kaydı silmek istediğinize emin misiniz?",\
                         QMessageBox.Yes | QMessageBox.No)
    if cevap==QMessageBox.Yes:
        secili=ui.ogKayitlar.selectedItems()
        silinecek=secili[1].text()
        try:
            curs.execute("DELETE FROM ogrenci WHERE TCNo='%s'" %(silinecek))
            conn.commit()
            
            LISTELE()
            mesaj="KAYIT SİLME İŞLEMİ BAŞARIYLA GERÇEKLEŞTİ..."
            ui.lblMesaj.setText(mesaj)
         
        except Exception as Hata:
           mesaj="Şöyle bir hata ile karşılaşıldı:"+str(Hata)
           ui.lblMesaj.setText(mesaj)
    else:
        mesaj="Silme işlemi iptal edildi..."
        ui.lblMesaj.setText(mesaj)
        
    
        
#----------------------ARAMA-----------------------------#
#---------------------------------------------------------# 

def ARA():
    aranan1=ui.ogTCno.text()
    aranan2=ui.ogAdi.text()
    aranan3=ui.ogSoyadi.text()
    curs.execute("SELECT * FROM ogrenci WHERE TCNo=? OR ogAdi=? OR ogSoyadi=? OR (ogAdi=? AND ogSoyadi=?)",  \
                 (aranan1,aranan2,aranan3,aranan2,aranan3))
    conn.commit()
    ui.ogKayitlar.clear()
    ui.ogKayitlar.setHorizontalHeaderLabels(('No','TC Kimlik No','Öğr. Adı','Öğr.Soyadı','Okul No', 'Sınıfı', 'Telefon'))
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate (satirVeri):
            ui.ogKayitlar.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))



#----------------------GÜNCELLE-----------------------------#
#---------------------------------------------------------#
def GUNCELLE():
    cevap=QMessageBox.question(penAna,"KAYIT GÜNCELLE","Kaydı güncellemek istediğinize emin misiniz?",\
                         QMessageBox.Yes | QMessageBox.No)
    if cevap==QMessageBox.Yes:
        try:
            secili=ui.ogKayitlar.selectedItems()
            _Id=int(secili[0].text())
            _ogTCno=ui.ogTCno.text()
            _ogAdi=ui.ogAdi.text()
            _ogSoyadi=ui.ogSoyadi.text()
            _ogOklno=ui.ogOklno.text()
            _ogSinif=ui.ogSinif.text()
            _ogTelno=ui.ogTelno.text()
 
          
            
            curs.execute("UPDATE ogrenci SET TCNo=?, ogAdi=?, ogSoyadi=?, okulNo=?, sinifi=?, ogTelno=? WHERE Id=?", (_ogTCno,_ogAdi,_ogSoyadi,_ogOklno,_ogSinif,_ogTelno,_Id))
            conn.commit()
            
            LISTELE()
            
        except Exception as Hata:
            mesaj="Şöyle bir hata meydana geldi"+str(Hata)
            ui.lblMesaj.setText(mesaj)
    else:
         mesaj="Güncellme iptal edildi"
         ui.lblMesaj.setText(mesaj)

        

#----------------------ÇIKIŞ-----------------------------#
#---------------------------------------------------------#  
def CIKIS():
    cevap=QMessageBox.question(penAna,"ÇIKIŞ","Programdan çıkmak istediğinize emin misiniz?",QMessageBox.Yes | QMessageBox.No)
    if cevap==QMessageBox.Yes:
        conn.close()
        sys.exit(Uygulama.exec_())
    else:
        penAna.show()
        


#----------------------SİNYAL-SLOT-----------------------------#
#---------------------------------------------------------#
ui.btnEkle.clicked.connect(EKLE)
ui.btnListele.clicked.connect(LISTELE)
ui.btnCikis.clicked.connect(CIKIS)
ui.btnSil.clicked.connect(SIL)
ui.btnAra.clicked.connect(ARA)
ui.btnGuncelle.clicked.connect(GUNCELLE)
ui.ogKayitlar.itemSelectionChanged.connect(DOLDUR)

sys.exit(Uygulama.exec_())
