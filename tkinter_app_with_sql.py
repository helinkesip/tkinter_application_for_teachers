import sqlite3
from tkinter import *
from tkinter import messagebox

def ÖğrenciEkleme():
    lbOgrenciler.insert(END, inputNo.get() + ' ' +  inputAd.get() + ' ' + inputSoyad.get())
    baglanti.execute("INSERT INTO Ogrenciler VALUES(?,?,?)",
                     [inputNo.get(), inputAd.get(), inputSoyad.get()])
    baglanti.commit()

def ÖğrenciSilme():
    if messagebox.askyesno("UYARI", "Seçili Kayıtları silmek istediğinize emin misiniz?"):
        for i in range(lbOgrenciler.size(), -1, -1):
            if lbOgrenciler.select_includes(i):
                baglanti.execute("DELETE FROM Ogrenciler WHERE OgrNo=?",
                                 [lbOgrenciler.get(i).split(' ')[0]])
                baglanti.commit()
                lbOgrenciler.delete(i)

def DersEkleme():
    lbDersler.insert(END, inputDersKod.get() + ' ' +  inputDersAd.get())
    baglanti.execute("INSERT INTO Dersler VALUES(?,?)",
                     [inputDersKod.get(), inputDersAd.get()])
    baglanti.commit()

def DersSilme():
    if messagebox.askyesno("UYARI", "Seçili Kayıtları silmek istediğinize emin misiniz?"):
        for i in range(lbDersler.size(), -1, -1):
            if lbDersler.select_includes(i):
                baglanti.execute("DELETE FROM Dersler WHERE DersKodu=?",
                                 [lbDersler.get(i).split(' ')[0]])
                baglanti.commit()
                lbDersler.delete(i)

def NotEkleme():
    if lbOgrenciler.curselection() and lbDersler.curselection():
        ÖğrenciNo = lbOgrenciler.get(ACTIVE).split()[0]
        DersKodu = lbDersler.get(ACTIVE).split()[0]
        lbNotlar.insert(END, ÖğrenciNo + ' ' + DersKodu + ' ' +  inputVize.get() + ' ' + inputFinal.get())
        baglanti.execute("INSERT INTO Notlar VALUES(?,?,?,?)",
                         [ÖğrenciNo, DersKodu, inputVize.get(), inputFinal.get()])
        baglanti.commit()
    else:
        messagebox.showwarning("HATA", "Bir ders ve bir öğrenci seçmelisiniz")

def NotSilme():
    if messagebox.askyesno("UYARI", "Seçili Kayıtları silmek istediğinize emin misiniz?"):
        for i in range(lbNotlar.size(), -1, -1):
            if lbNotlar.select_includes(i):
                baglanti.execute("DELETE FROM Notlar WHERE OgrNo=? AND DersKodu=?",
                                 [lbNotlar.get(i).split(' ')[0], lbNotlar.get(i).split(' ')[1]])
                baglanti.commit()
                lbNotlar.delete(i)

pencere = Tk()

solFrame = Frame(highlightthickness=5, bd=5, relief=GROOVE)
solFrame.grid(row=0, column=0)
ortaFrame = Frame(highlightthickness=5, bd=5, relief=GROOVE)
ortaFrame.grid(row=0, column=1)
sağFrame = Frame(highlightthickness=5, bd=5, relief=GROOVE)
sağFrame.grid(row=0, column=2)


lblOgrenciler = Label(solFrame, text="ÖĞRENCİLER", font="Calibri 24")
lblOgrenciler.grid(row=0, column=0, columnspan=2)

lblNo = Label(solFrame, text="ÖğrNo :", font="Calibri", width=7, anchor="e")
inputNo = Entry(solFrame, font="Calibri")
lblNo.grid(row=1, column=0)
inputNo.grid(row=1, column=1)

lblAd = Label(solFrame, text="Adı :", font="Calibri", width=7, anchor="e")
inputAd = Entry(solFrame, font="Calibri")
lblAd.grid(row=2, column=0)
inputAd.grid(row=2, column=1)

lblSoyad = Label(solFrame, text="Soyadı :", font="Calibri", width=7, anchor="e")
inputSoyad = Entry(solFrame, font="Calibri")
lblSoyad.grid(row=3, column=0)
inputSoyad.grid(row=3, column=1)

cmdEkle = Button(solFrame, text="Ekle", font="Calibri", command=ÖğrenciEkleme)
cmdEkle.grid(row=4, column=0, columnspan=2)

lbOgrenciler = Listbox(solFrame, font="Calibri", selectmode="extended", width=30, exportselection=0)
lbOgrenciler.grid(row=5, column=0, columnspan=2)

cmdSil = Button(solFrame, text="Seçili olanları sil", font="Calibri", command=ÖğrenciSilme)
cmdSil.grid(row=6, column=0, columnspan=2)


lblDersler = Label(ortaFrame, text="DERSLER", font="Calibri 24")
lblDersler.grid(row=0, column=0, columnspan=2)

lblDersKod = Label(ortaFrame, text="Ders Kodu :", font="Calibri", width=10, anchor="e")
inputDersKod = Entry(ortaFrame, font="Calibri")
lblDersKod.grid(row=1, column=0)
inputDersKod.grid(row=1, column=1)

lblDersAd = Label(ortaFrame, text="Ders Adı :", font="Calibri", width=10, anchor="e")
inputDersAd = Entry(ortaFrame, font="Calibri")
lblDersAd.grid(row=2, column=0)
inputDersAd.grid(row=2, column=1)

cmdEkle3 = Button(ortaFrame, text="Ekle", font="Calibri", command=DersEkleme)
cmdEkle3.grid(row=3, column=0, columnspan=2)

lbDersler = Listbox(ortaFrame, font="Calibri", selectmode="extended", width=32, exportselection=0)
lbDersler.grid(row=4, column=0, columnspan=2)

cmdSil3 = Button(ortaFrame, text="Seçili olanları sil", font="Calibri", command=DersSilme)
cmdSil3.grid(row=5, column=0, columnspan=2)


lblNotlar = Label(sağFrame, text="NOTLAR", font="Calibri 24")
lblNotlar.grid(row=0, column=0, columnspan=2)

lblVize = Label(sağFrame, text="Vize Notu :", font="Calibri", width=10, anchor="e")
inputVize = Entry(sağFrame, font="Calibri")
lblVize.grid(row=1, column=0)
inputVize.grid(row=1, column=1)

lblFinal = Label(sağFrame, text="Final Notu :", font="Calibri", width=10, anchor="e")
inputFinal = Entry(sağFrame, font="Calibri")
lblFinal.grid(row=2, column=0)
inputFinal.grid(row=2, column=1)

cmdEkle2 = Button(sağFrame, text="Ekle", font="Calibri", command=NotEkleme)
cmdEkle2.grid(row=3, column=0, columnspan=2)

lbNotlar = Listbox(sağFrame, font="Calibri", selectmode="extended", width=32, exportselection=0)
lbNotlar.grid(row=4, column=0, columnspan=2)

cmdSil2 = Button(sağFrame, text="Seçili olanları sil", font="Calibri", command=NotSilme)
cmdSil2.grid(row=5, column=0, columnspan=2)


baglanti = sqlite3.connect("data.db")

baglanti.execute("CREATE TABLE IF NOT EXISTS Ogrenciler(OgrNo, Ad, Soyad)")
baglanti.execute("CREATE TABLE IF NOT EXISTS Dersler(DersKodu, DersAdı)")
baglanti.execute("CREATE TABLE IF NOT EXISTS Notlar(OgrNo, DersKodu, Vize, Final)")

for kayıt in baglanti.execute("SELECT * FROM Ogrenciler"):
    lbOgrenciler.insert(END, kayıt[0] + ' ' + kayıt[1] + ' ' + kayıt[2])

for kayıt in baglanti.execute("SELECT * FROM Dersler"):
    lbDersler.insert(END, kayıt[0] + ' ' + kayıt[1])

for kayıt in baglanti.execute("SELECT * FROM Notlar"):
    lbNotlar.insert(END, kayıt[0] + ' ' + kayıt[1] + ' ' + kayıt[2] + ' ' + kayıt[3])

pencere.mainloop()
