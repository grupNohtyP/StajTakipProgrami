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
from Frm_OgrtKayit import *
from tkinter import messagebox
from PyQt5.QtWidgets import *

#----------------------UYGULAMA OLUŞTUR-------------------#
#---------------------------------------------------------#
Uygulama=QApplication(sys.argv)
penAna=QMainWindow()
ui=Ui_dialog()
ui.setupUi(penAna)
penAna.show()



#----------------------VERİTABANI OLUŞTUR-----------------#
#---------------------------------------------------------#
import sqlite3
global curs
global conn

conn=sqlite3.connect('stjyrtkp.sqlite')
curs=conn.cursor()
global mesaj

    
def TEMIZLE():
    ui.txtTcno.clear()
    ui.txtBrans.clear()
    ui.txtMail.clear()
    ui.txtSifre.clear()
    ui.txtAdSoyad.clear()
    ui.txtTcno.setEnabled(True)
    ui.btnGuncelle.setEnabled(False)
    ui.btnSil.setEnabled(False)

def GirisKontrol():
    _ogrTCno=ui.txtTcno.text()
    _ogrAdiSoyadi=ui.txtAdSoyad.text()
    _ogrSifre=ui.txtSifre.text()
    _ogrBrans=ui.txtBrans.text()
    _ogrMail=ui.txtMail.text()
    global mesaj
    deger=True
    if len(_ogrTCno)!=11 or _ogrTCno.isdigit()==False or int(_ogrTCno[0])==0:
        mesaj+="Tc No "
        deger=False
    if _ogrAdiSoyadi.isdigit==True or len(_ogrAdiSoyadi)<2:
        mesaj+="Adı Soyadı "
        deger=False
    if len(_ogrSifre)<6:
        mesaj+="Sifre "
        deger=False
    if len(_ogrBrans)<3:
        mesaj+="Branş "
        deger=False
    if len(_ogrMail)<5 or _ogrMail.find('@')==-1:
        mesaj+="Mail"
        deger=False
    return deger

def EKLE():  
    global mesaj
    _ogrTCno=ui.txtTcno.text()
    _ogrAdiSoyadi=ui.txtAdSoyad.text()
    _ogrSifre=ui.txtSifre.text()
    _ogrBrans=ui.txtBrans.text()
    _ogrMail=ui.txtMail.text()
    mesaj=" "
    if len(_ogrTCno)!=11 or _ogrTCno.isdigit()==False or int(_ogrTCno[0])==0:
       messagebox.showinfo("Hata", "Girişleri kontrol ediniz:")
    else:
        curs.execute("SELECT * FROM ogretmen WHERE ogretmen_tcno = %s"%(_ogrTCno))
        veriler=curs.fetchone()
        if veriler:    
            messagebox.showinfo("Hata", "Kayıtlı bir TC Numarası girdiniz.")
        else:
            if GirisKontrol()==False:
                messagebox.showinfo("Hata", "Girişleri kontrol ediniz:" + mesaj)
            else:
                curs.execute("INSERT INTO ogretmen \
                     (ogretmen_tcno,ogretmen_AdSoyad,ogretmen_Sifre,ogretmen_Alan,ogretmen_email) \
                     VALUES (?,?,?,?,?)", \
                     (_ogrTCno,_ogrAdiSoyadi,_ogrSifre,_ogrBrans,_ogrMail))
                conn.commit()         
                TEMIZLE()
                messagebox.showinfo("Kayıt İşlemi", "Kayıt işlemi gerçekleşti.")

def GETIR():
    global mesaj
    _ogrTCno=ui.txtTcno.text()   
    _ogrSifre=ui.txtSifre.text()
    mesaj=" "
    curs.execute("SELECT * FROM ogretmen WHERE ogretmen_tcno = ? AND ogretmen_Sifre =?",(_ogrTCno,_ogrSifre))
    veriler=curs.fetchone()
    if veriler:
        ui.txtAdSoyad.setText(veriler[1])
        ui.txtBrans.setText(veriler[3])
        ui.txtMail.setText(veriler[4])
        ui.btnGuncelle.setEnabled(1)
        ui.txtTcno.setEnabled(False)
        ui.btnGuncelle.setEnabled(True)
        ui.btnSil.setEnabled(True)
    else:
        messagebox.showinfo("Hata", "Kullanıcı bulunamadı / Hatalı giriş")
        ui.btnGuncelle.setEnabled(False)
        ui.btnSil.setEnabled(False)
                 
    
def GUNCELLE():
    cevap=QMessageBox.question(penAna,"KAYIT GÜNCELLE","Kaydı güncellemek istediğinize emin misiniz?",\
                         QMessageBox.Yes | QMessageBox.No)
    if cevap==QMessageBox.Yes:
        try:
            _ogrTCno=ui.txtTcno.text()
            _ogrAdiSoyadi=ui.txtAdSoyad.text()
            _ogrSifre=ui.txtSifre.text()
            _ogrBrans=ui.txtBrans.text()
            _ogrMail=ui.txtMail.text()
            curs.execute("UPDATE ogretmen SET ogretmen_AdSoyad=?, ogretmen_Sifre=?, ogretmen_Alan=?, ogretmen_email=? WHERE ogretmen_tcno=?", (_ogrAdiSoyadi,_ogrSifre,_ogrBrans,_ogrMail,_ogrTCno))
            conn.commit()
            messagebox.showinfo("Güncelleme", "Kayıt Güncelleme Başarılı")
            TEMIZLE()
        except Exception as Hata:
            messagebox.showinfo("Hata", str(Hata))
            
    else:
        messagebox.showinfo("Hata", "Güncellme iptal edildi")

def SIL():
    GETIR()
    cevap=QMessageBox.question(penAna,"KAYIT SİL","Kaydı silmek istediğinize emin misiniz?",\
                         QMessageBox.Yes | QMessageBox.No)
    if cevap==QMessageBox.Yes:
        silinecek=ui.txtTcno.text()
        try:
            curs.execute("DELETE FROM ogretmen WHERE ogretmen_tcno='%s'" %(silinecek))
            conn.commit()
            TEMIZLE()         
        except Exception as Hata:
            messagebox.showinfo("Hata", str(Hata))
    else:
        messagebox.showinfo("Silme İşlemi","Kayıt silindi")
        TEMIZLE()
        


ui.btnTemizle.clicked.connect(TEMIZLE)
ui.btnKaydet.clicked.connect(EKLE)
ui.btnGuncelle.clicked.connect(GUNCELLE)
ui.btnKytGetir.clicked.connect(GETIR)
ui.btnSil.clicked.connect(SIL)
ui.txtSifre.setMaxLength(11)
ui.txtTcno.setMaxLength(11)
ui.btnGuncelle.setEnabled(False)
ui.btnSil.setEnabled(False)


def CIKIS():
    cevap=QMessageBox.question(penAna,"ÇIKIŞ","Programdan çıkmak istediğinize emin misiniz?",QMessageBox.Yes | QMessageBox.No)
    if cevap==QMessageBox.Yes:
        conn.close()
        sys.exit(Uygulama.exec_())
    else:
        penAna.show()

sys.exit(Uygulama.exec_())

