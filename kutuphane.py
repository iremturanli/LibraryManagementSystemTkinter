from sre_parse import State
from tkinter import font, messagebox, ttk
from tkinter import*
from datetime import*
from tkcalendar import Calendar,DateEntry
import sqlite3
from openpyxl import Workbook
import os



db=sqlite3.connect("uyeler.db")

cursor=db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS uyeler(ID INT AUTO INCREMENT PRIMARY KEY,
                                                    TUR TEXT,
                                                    REFERANS TEXT,
                                                    ISIM TEXT,
                                                    SOYISIM TEXT,
                                                    TELEFON TEXT,
                                                    EMAIL TEXT,
                                                    ADRES TEXT,
                                                    DURUM TEXT,
                                                    BORC TEXT)
                                                                        """)


cursor.execute("""CREATE TABLE IF NOT EXISTS kitaplar(BARKOD TEXT,
                                                      BASLIK TEXT,
                                                      YAZAR TEXT, 
                                                      SAYI TEXT,
                                                      RAF TEXT,
                                                      ODUNC TEXT,
                                                      TESLIM TEXT,
                                                      KIME TEXT)
                                                                    """)
db.commit()



class Kutuphane(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.wm_geometry("600x400+400+100")
        self.wm_title("Kütüphane Yönetim Sistemi")
        self.wm_resizable(False,False)
        #yenitema
        combostyle=ttk.Style()
        combostyle.theme_create("combostyle",parent="alt",settings={"TCombobox":
                                                                    {"configure":
                                                                        {
                                                                            "fieldbackground":"#DBD0C0",
                                                                             "background":"#DBD0C0"
                                                                            }}})

        combostyle.theme_use("combostyle")
        self.frame1=Frame(self,height=150,bg="#DBD0C0")
        self.frame1.pack(fill=X)
        self.frame2=Frame(self,height=450,bg="#9E9D89")
        self.frame2.pack(fill=X)
        
        self.baslik=Label(self.frame1,text="KÜTÜPHANE",font=("Garamond",35,"bold"),bg="#DBD0C0")
        self.baslik.place(x=200,y=38)
        self.baslik=Label(self.frame1,text="YÖNETİM SİSTEMİ",font=("Garamond",33,"bold"),bg="#DBD0C0")
        self.baslik.place(x=170,y=85)


        self.dugme1=Button(self.frame2,text="ÜYELER",font=("Garamond",15,"bold"),bg='#C1A3A3',
                            activebackground='#886F6F',command=Uyeler)

        self.dugme1.place(x=200,y=60,width=200)

        self.dugme2=Button(self.frame2,text="KİTAPLAR",font=("Garamond",15,"bold"),bg='#C1A3A3',
                            activebackground='#886F6F',command=Kitaplar)

        self.dugme2.place(x=200,y=100,width=200)
        self.dugme3=Button(self.frame2,text="KİTAPLIK",font=("Garamond",15,"bold"),bg='#C1A3A3',
                            activebackground='#886F6F',command=Kitaplık)

        self.dugme3.place(x=200,y=140,width=200)


class Uyeler(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.wm_geometry("600x400+400+100")
        self.wm_title("Üyeler")
       
        style=ttk.Style()
        style.theme_use("combostyle")

        self.frame1=Frame(self,bg="#9E9D89",height=400,width=600)
        self.frame1.pack()

        Label(self.frame1,text="ÜYE BİLGİLERİ",bg="#9E9D89",font=("Garamond",25,"bold")).place(x=170)

        Label(self.frame1,text="Üyelik Türü",bg="#9E9D89",font=("Garamond",15,"bold")).place(x=50,y=55)
        Label(self.frame1,text="Referans No",bg="#9E9D89",font=("Garamond",15,"bold")).place(x=50,y=85)
        Label(self.frame1,text="İsim",bg="#9E9D89",font=("Garamond",15,"bold")).place(x=50,y=115)
        Label(self.frame1,text="Soyisim",bg="#9E9D89",font=("Garamond",15,"bold")).place(x=50,y=145)
        Label(self.frame1,text="Telefon",bg="#9E9D89",font=("Garamond",15,"bold")).place(x=50,y=175)
        Label(self.frame1,text="Email",bg="#9E9D89",font=("Garamond",15,"bold")).place(x=50,y=205)
        Label(self.frame1,text="Adres",bg="#9E9D89",font=("Garamond",15,"bold")).place(x=50,y=235)
        Label(self.frame1,text="Üyelik Durumu",bg="#9E9D89",font=("Garamond",15,"bold")).place(x=50,y=295)
        Label(self.frame1,text="Borç",bg="#9E9D89",font=("Garamond",15,"bold")).place(x=50,y=330)



        self.tur=ttk.Combobox(self.frame1,font=("Garamond",12,"bold"),state="readonly",
                               values=["Öğrenci","Normal","Kütüphane Görevlisi"])    
        self.tur.place(x=330,y=55,width=180)     

        self.referans=Entry(self.frame1,font=("Garamond",15,"bold"),bg="#DBD0C0") 
        self.referans.place(x=330,y=85,width=180)    

        self.isim=Entry(self.frame1,font=("Garamond",15,"bold"),bg="#DBD0C0") 
        self.isim.place(x=330,y=115,width=180)

        self.soyisim=Entry(self.frame1,font=("Garamond",15,"bold"),bg="#DBD0C0") 
        self.soyisim.place(x=330,y=145,width=180)    

        self.telefon=Entry(self.frame1,font=("Garamond",15,"bold"),bg="#DBD0C0") 
        self.telefon.place(x=330,y=175,width=180)

        self.email=Entry(self.frame1,font=("Garamond",15,"bold"),bg="#DBD0C0") 
        self.email.place(x=330,y=205,width=180)    
        #textbirdenfazlasatıraizinveriyor
        self.adres=Text(self.frame1,font=("Garamond",15,"bold"),bg="#DBD0C0",height=2) 
        self.adres.place(x=330,y=235,width=180)
        
     
        self.sayi=IntVar(self.frame1)
        self.durum0=Radiobutton(self.frame1,text="Aktif",variable=self.sayi,value=1,bg="#DBD0C0")
        self.durum0.place(x=330,y=295)
        self.durum1=Radiobutton(self.frame1,text="Beklemede",variable=self.sayi,value=2,bg="#DBD0C0")
        self.durum1.place(x=390,y=295)
        self.durum2=Radiobutton(self.frame1,text="İptal",variable=self.sayi,value=3,bg="#DBD0C0")
        self.durum2.place(x=490,y=295)

        self.borc=Entry(self.frame1,font=("Garamond",15,"bold"),bg="#DBD0C0")
        self.borc.place(x=330,y=330)


        Button(self.frame1,text="KAYDET",command=self.kaydet,bg="#C1A3A3",
               activebackground="#886F6F",font=("Garamond",15,"bold")).place(x=50,y=365,width=115)
        
        Button(self.frame1,text="GETİR",command=self.getir,bg="#C1A3A3",
               activebackground="#886F6F",font=("Garamond",15,"bold")).place(x=181,y=365,width=115)

        Button(self.frame1,text="GÜNCELLE",command=self.guncelle,bg="#C1A3A3",
               activebackground="#886F6F",font=("Garamond",15,"bold")).place(x=312,y=365,width=115)

        Button(self.frame1,text="MAİL",command=self.mail_gonder,bg="#C1A3A3",
               activebackground="#886F6F",font=("Garamond",15,"bold")).place(x=443,y=365,width=115)

    def kaydet(self):
        query="INSERT INTO uyeler(tur,referans,isim,soyisim,telefon,email,adres,durum) VALUES(?,?,?,?,?,?,?,?)"
        val=(self.tur.get(),self.referans.get(),self.isim.get(),self.soyisim.get(),self.telefon.get(),self.email.get(),self.adres.get('1.0',END),self.sayi.get())
        cursor.execute(query,val)
        db.commit()
        self.temizle()


    def getir(self):
        query="SELECT * FROM uyeler WHERE referans=?"
        val=(self.referans.get(),)
        cursor.execute(query,val)
        sonuc=cursor.fetchall()

        for i in sonuc:
            self.tur.set("")
            self.isim.delete(0,END)
            self.soyisim.delete(0,END)
            self.telefon.delete(0,END)
            self.email.delete(0,END)
            self.adres.delete("1.0",END) 
            self.sayi.set(0)

            self.tur.set(i[1])
            self.isim.insert(0,i[3])
            self.soyisim.insert(0,i[4])
            self.telefon.insert(0,i[5])
            self.email.insert(0,i[6])
            self.adres.insert("end",i[7])
            self.sayi.set(i[8])

    
        
    def temizle(self):
        messagebox.showinfo("Başarılı","İşlem Başarılı!")
        self.tur.set("")
        self.referans.delete(0,END)
        self.isim.delete(0,END)
        self.soyisim.delete(0,END)
        self.telefon.delete(0,END)
        self.email.delete(0,END)
        self.adres.delete("1.0",END)
        self.sayi.set(0)
        self.focus()

    def guncelle(self):
        query= """UPDATE uyeler SET  tur=?,isim=?,soyisim=?,telefon=?,email=?,adres=?,durum=?
                WHERE referans=? """ 
        val=(self.tur.get(),self.isim.get(),self.soyisim.get(),self.telefon.get(),self.email.get(),self.adres.get('1.0',END),self.sayi.get(),
            self.referans.get())
        
        cursor.execute(query,val)
        db.commit()
        self.temizle()
        

class Kitaplar(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.wm_geometry("600x400+400+100")
        self.wm_title("Kitap Bilgileri")

        style=ttk.Style()
        style.theme_use("combostyle")
       

        self.frame1=Frame(self,bg="#9E9D89",height=400,width=600)
        self.frame1.pack()

        Label(self.frame1,text="KİTAP BİLGİLERİ",bg="#9E9D89",font=("Garamond",25,"bold")).place(x=170)

        Label(self.frame1,text="Barkod",bg="#9E9D89",font=("Garamond",15,"bold")).place(x=50,y=55)
        Label(self.frame1,text="Başlık",bg="#9E9D89",font=("Garamond",15,"bold")).place(x=50,y=85)
        Label(self.frame1,text="Yazar",bg="#9E9D89",font=("Garamond",15,"bold")).place(x=50,y=115)
        Label(self.frame1,text="Durum",bg="#9E9D89",font=("Garamond",15,"bold")).place(x=50,y=145)
        Label(self.frame1,text="Raf",bg="#9E9D89",font=("Garamond",15,"bold")).place(x=50,y=175)
        Label(self.frame1,text="Kime",bg="#9E9D89",font=("Garamond",15,"bold")).place(x=50,y=205)
        Label(self.frame1,text="Ödünç Tarihi",bg="#9E9D89",font=("Garamond",15,"bold")).place(x=50,y=260)
        Label(self.frame1,text="Teslim Tarihi",bg="#9E9D89",font=("Garamond",15,"bold")).place(x=50,y=295)
        
        self.barkod=Entry(self.frame1,font=("Garamond",15,"bold"),bg="#DBD0C0")
        self.barkod.place(x=330,y=55)

        self.baslik=Entry(self.frame1,font=("Garamond",15,"bold"),bg="#DBD0C0")
        self.baslik.place(x=330,y=85)

        self.yazar=Entry(self.frame1,font=("Garamond",15,"bold"),bg="#DBD0C0")
        self.yazar.place(x=330,y=115)

        self.sayi=IntVar(self.frame1)
        self.durum0=Radiobutton(self.frame1,text="Rafta",variable=self.sayi,value=1,bg="#DBD0C0")
        self.durum0.place(x=330,y=145)
        self.durum1=Radiobutton(self.frame1,text="Ödünç Verildi",variable=self.sayi,value=2,bg="#DBD0C0")
        self.durum1.place(x=395,y=145)

        self.raf=Entry(self.frame1,font=("Garamond",15,"bold"),bg="#DBD0C0")
        self.raf.place(x=330,y=175)

        self.kime=ttk.Combobox(self.frame1,font=("Garamond",15,"bold"),values=["Teslim Al"])   

        self.kime.bind("<KeyRelease>",self.islemler) #herhangi bir tusa basılınca
        self.kime.bind("<Button-1>",self.islemler)#mouse ile tıklandığında
        self.kime.bind("<Return>",self.islemler)#enter tusuna basildiginda
        self.kime.bind("<<ComboboxSelected>>",self.islemler)#combobox ile islem yapildiginda
                                
        self.kime.place(x=330,y=205,width=198)         

        self.odunc=DateEntry(self.frame1,font=("Garamond",15,"bold"),bg="#DBD0C0",locale="tr_TR",
                            selectbacground="#E4CDA7",weekendbackground="#E4CDA7",state="disabled")
        self.odunc.place(x=330,y=260,width=198)                   

        self.teslim=DateEntry(self.frame1,font=("Garamond",15,"bold"),bg="#DBD0C0",locale="tr_TR",
                            selectbacground="#E4CDA7",weekendbackground="#E4CDA7",state="disabled")
        self.teslim.place(x=330,y=295,width=198)  

        self.borc=Label(self.frame1,font=("Garamond",15,"bold"),bg="#DBD0C0")
        self.borc.place(x=330,y=330)
                                                                    
        
     
        Button(self.frame1,text="KAYDET",command=self.kaydet,bg="#C1A3A3",
               activebackground="#886F6F",font=("Garamond",15,"bold")).place(x=50,y=365,width=115)
        
        Button(self.frame1,text="GETİR",command=self.getir,bg="#C1A3A3",
               activebackground="#886F6F",font=("Garamond",15,"bold")).place(x=181,y=365,width=115)

        Button(self.frame1,text="GÜNCELLE",command=self.guncelle,bg="#C1A3A3",
               activebackground="#886F6F",font=("Garamond",15,"bold")).place(x=312,y=365,width=115)

        Button(self.frame1,text="SİL",command=self.sil,bg="#C1A3A3",
               activebackground="#886F6F",font=("Garamond",15,"bold")).place(x=443,y=365,width=115)

        self.onceki_borc=0

    def islemler(self,event):
        if len (self.kime.get())!=0:#kime kısmı bos birakilmamıssa
            if (self.kime.get())!="Teslim Al":
                 self.sayi.set(2)
                 self.odunc.config(state='normal')
                 self.teslim.config(state='normal')
                 self.teslim_tarihi(event=None)#eventli fonskiyonu cagırırken(14 gun sonraya ayarlama)
            else:
                if len(self.odunc.get())!=0:#odunc verilmisse
                    self.teslim.config(state='normal')
                    time1=self.teslim.get_date()
                    time2=date.today()
                    self.teslim.delete(0,END)
                    time3=str(time2).split("-")
                    time4=str(time3[2])+"."+str(time3[1])+"."+str(time3[0])
                    self.teslim.insert(0,time4)
                    gun=(time2-time1).days
                    if gun>0:
                        self.borc['text']=gun*1
                    else:
                        self.borc['text']=0
                else:
                    messagebox("Hata","Kitap ödünç verilmemiş")
                    self.kime.delete(0,END)
                    self.focus()


        else:
            self.sayi.set(1)#Rafta
            self.odunc.delete(0,END)
            self.teslim.delete(0,END) 
            self.odunc.config(state='disabled')
            self.teslim.config(state='disabled')
            


    def teslim_tarihi(self,event):
        date=self.odunc.get_date()#tarihi get_date() methoduyla date formatında alıyoruz
        datemodify=date+timedelta(days=14)
        date_m=str(datemodify).split("-")#listeye ceviriyor
        date_list=date_m[2]+"."+date_m[1]+"."+date_m[0]
        self.teslim.delete(0,END)
        self.teslim.insert(0,date_list)
        self.odunc.config(state='disabled')
        self.teslim.config(state='disabled')



    def kaydet(self):
        query="INSERT INTO kitaplar (barkod,baslik,yazar,sayi,raf,odunc,teslim) VALUES(?,?,?,?,?,?,?)"
        val=(self.barkod.get(),self.baslik.get(),self.yazar.get(),self.sayi.get(),self.raf.get(),self.odunc.get(),self.teslim.get())
        cursor.execute(query,val)#
        db.commit()

        self.temizle()

    def getir(self):
        query="SELECT * FROM kitaplar WHERE barkod=?"
        val=(self.barkod.get(),)
        cursor.execute(query,val)
        sonuc=cursor.fetchall()

        for i in sonuc:
            self.baslik.delete(0,END)
            self.baslik.insert(0,i[1])
            self.yazar.delete(0,END)
            self.yazar.insert(0,i[2])
            self.sayi.set(i[3])
            self.raf.delete(0,END)
            self.raf.insert(0,i[4])
            self.odunc.config(state='normal')
            self.odunc.delete(0,END)
            self.odunc.insert(0,i[5])
            self.odunc.config(state='disabled')
            self.teslim.config(state='normal')
            self.teslim.delete(0,END)
            self.teslim.insert(0,i[6])
            self.teslim.config(state='disabled')

        try:
            self.kime.delete(0,END)
            self.kime.insert(0,i[7])

        except TclError:
            pass
            
        self.referans=self.kime.get()

    def guncelle(self):
        if self.kime.get()=='Teslim Al':
            self.sayi.set(1)#Rafta
            self.odunc.config(state='normal')
            self.teslim.config(state='normal')
            self.odunc.delete(0,END)
            self.teslim.delete(0,END)
            self.kime.delete(0,END)


            query="UPDATE kitaplar SET baslik=?,yazar=?,sayi=?,raf=?,odunc=?,teslim=?,kime=? WHERE barkod=?"
            val=(self.baslik.get(),self.yazar.get(),self.sayi.get(),self.raf.get(),self.odunc.get(),self.teslim.get(),self.kime.get(),self.barkod.get())
            cursor.execute(query,val)
            db.commit()

            query="SELECT *FROM uyeler WHERE referans=?"
            val=(self.referans,)
            cursor.execute(query,val)
            sonuc=cursor.fetchall()
            for i in sonuc:
                self.onceki_borc=i[9]
            try: 
                query="UPDATE uyeler SET borc=? WHERE referans=?"
                val=(int(self.onceki_borc)+int(self.borc['text']),self.referans)
                cursor.execute(query,val)
                db.commit()

            except TypeError:
                query="UPDATE uyeler SET borc=? WHERE referans=?"
                val=(0+int(self.borc['text']),self.referans)
                cursor.execute(query,val)
                db.commit()


        else:
            query="UPDATE kitaplar SET baslik=?,yazar=?,sayi=?,raf=?,odunc=?,teslim=?,kime=?WHERE barkod=?"
            val=(self.baslik.get(),self.yazar.get(),self.sayi.get(),self.raf.get(),self.odunc.get(),self.teslim.get(),self.kime.get(),self.barkod.get())
            cursor.execute(query,val)
            db.commit()

        self.temizle()

    def sil(self):
        query="DELETE FROM kitaplar WHERE barkod=?"
        val=(self.barkod.get(),)
        cursor.execute(query,val)
        db.commit()
        self.temizle()

    def temizle(self):
        messagebox.showinfo("Başarılı","İşlem başarılı")
        self.barkod.delete(0,END)
        self.baslik.delete(0,END)
        self.yazar.delete(0,END)
        self.sayi.set(0)
        self.kime.delete(0,END)
        self.raf.delete(0,END)
        self.odunc.config(state='normal')
        self.teslim.config(state='normal')
        self.odunc.delete(0,END)
        self.teslim.delete(0,END)
        self.odunc.config(state='disabled')
        self.teslim.config(state='disabled')
        self.borc['text']=""
        self.focus()


class Kitaplık(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.wm_geometry("600x400+400+100")
        self.wm_title("Kitaplık")
       
        style=ttk.Style()
        style.theme_use=("clam")
        

        self.frame1=Frame(self,bg="#9E9D89",height=400,width=600)
        self.frame1.pack()

        Label(self.frame1,text="KİTAPLIK",bg="#9E9D89",font=("Garamond",25,"bold")).place(x=170)

        self.kaydirma=ttk.Scrollbar(self.frame1)
        self.kaydirma.place(x=530,y=50,height=300)

        self.agac=ttk.Treeview(self.frame1,yscrollcommand=self.kaydirma.set,
                                columns=("sutun1","sutun2","sutun3","sutun4"),show="headings")                                            
        
        self.agac.heading("sutun1",text="Barkod")
        self.agac.heading("sutun2",text="Kitap")
        self.agac.heading("sutun3",text="Yazar")
        self.agac.heading("sutun4",text="Raf")

        self.agac.column("sutun1",width=120)
        self.agac.column("sutun2",width=120)
        self.agac.column("sutun3",width=120)
        self.agac.column("sutun4",width=120)

        self.agac.place(x=50,y=50,height=300)
        self.kaydirma.config(command=self.agac.yview)

        self.barkod_listesi=[]
        self.kitap_listesi=[]
        self.yazar_listesi=[]
        self.raf_listesi=[]

        cursor.execute("SELECT * FROM kitaplar")
        sonuc=cursor.fetchall()
        print(sonuc)
        for i in sonuc:
            self.barkod_listesi.append(i[0])
            self.kitap_listesi.append(i[1])
            self.yazar_listesi.append(i[2])
            self.raf_listesi.append(i[4])

   
        self.kitaplik_listesi=list(zip(self.barkod_listesi,self.kitap_listesi,self.yazar_listesi,self.raf_listesi))
        print(self.kitaplik_listesi)

        for i in self.kitaplik_listesi:
            self.agac.insert("",END,values=(i[0],i[1],i[2],i[3]))


        self.dugme1=Button(self.frame1,text="EXCEL",font=("Garamond",15,"bold"),bg='#C1A3A3',
                            activebackground='#886F6F',command=self.excel).place(x=25,y=355,width=125)

        
        self.dugme1=Button(self.frame1,text="PDF",font=("Garamond",15,"bold"),bg='#C1A3A3',
                            activebackground='#886F6F',command=self.pdf).place(x=450,y=355,width=125)



    def excel(self):
        wb=Workbook()
        sheet=wb.active
        sheet.append(["Barkod","Kitap","Yazar","Raf"])
        for i in self.kitaplik_listesi:
            sheet.append(i)

        wb.save("kitaplik.xlsx")
        # os.startfile("kitaplik.xlsx")

        

    def pdf(self):
       pass









if __name__=="__main__":
    app = Kutuphane()
    app.mainloop()
