from tkinter import *
from PIL import Image, ImageTk
import sqlite3
root = Tk()
root.geometry('500x500')
root.title("Registration Form")
ip=StringVar()

conn=sqlite3.connect("Fasebase/FaseBase.db")
def yeniIp():
    n=0
    for row in conn.execute('SELECT Adres FROM IpAdress'):
        n=n+1


    print(n)
    print(ip.get())
    conn.execute('INSERT INTO IpAdress (ID,Adres) VALUES(?,?)',(str(n),str(ip.get()),))
    conn.commit()

    pass
def silip():
    print(str(ip.get()))
    conn.execute("DELETE FROM IpAdress WHERE Adres=(?)",(str(ip.get()),))
    conn.commit()
    pass

label_0 = Label(root, text="İp Kayıt-Silme Formu",width=20,font=("bold", 20))
label_0.place(x=80,y=53)

label_1 = Label(root, text="Ip adresi (Lütfen .jpg uzantılı halde giriniz)",width=40,font=("bold", 10))
label_1.place(x=90,y=130)

entry_1 = Entry(root,textvar=ip,width=40)
entry_1.place(x=125,y=180)

Button(root, text='Kaydet',width=20,bg='brown',fg='white',command=yeniIp).place(x=80,y=380)
Button(root, text='Sil',width=20,bg='brown',fg='white',command=silip).place(x=280,y=380)
root.mainloop()
