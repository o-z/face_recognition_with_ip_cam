from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import cv2
from tkinter import messagebox
import os
root = Tk()
root.geometry('500x500')
root.title("Registration Form")


id=StringVar()
name=StringVar()
surname=StringVar()
comNumber=StringVar()



def database():






    conn=sqlite3.connect("Fasebase/FaseBase.db")
    cmd="SELECT * FROM People WHERE ID="+str(id.get())
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1

    if isRecordExist==1:


        cursor.execute("""UPDATE People SET Name = ? ,Surname = ?,ComNumber = ? WHERE ID= ? """,
  (str(name.get()),str(surname.get()),str(comNumber.get()),str(id.get())))
        conn.execute(cmd)
        conn.commit()
        conn.close()
        pass
    else:
        conn.execute('INSERT INTO People (ID,Name,Surname,ComNumber) VALUES(?,?,?,?)',(str(id.get()),str(name.get()),str(surname.get()),str(comNumber.get()),))
        conn.commit()
        conn.close()

        pass


    cam=cv2.VideoCapture(0)
    detector=cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

    sampleNum=0
    bol=True
    while bol:
        ret,frame=cam.read(0)
        if ret == True:
            gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces=detector.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)

            for (x,y,w,h) in faces:
                sampleNum=sampleNum+1
                img_item="images/User."+str(id.get())+"."+str(sampleNum)+".jpg"
                cv2.imwrite(img_item,gray[y:y+h,x:x+w])
                cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0),1)

                cv2.imshow('frame',frame)
                cv2.waitKey(100)
                if sampleNum>20:
                    cam.release()
                    cv2.destroyAllWindows()
                    bol=False
                    break
                    pass
        pass
    messagebox.showinfo(":)", "Tarama Tamamlandı")




label_0 = Label(root, text="Kayıt Formu",width=20,font=("bold", 20))
label_0.place(x=90,y=53)







label_1 = Label(root, text="ID",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=id)
entry_1.place(x=240,y=130)




label_2 = Label(root, text="Name",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=name)
entry_2.place(x=240,y=180)


label_3 = Label(root, text="Surname",width=20,font=("bold", 10))
label_3.place(x=68,y=230)

entry_3 = Entry(root,textvar=surname)
entry_3.place(x=240,y=230)



label_4 = Label(root, text="ComNumber",width=20,font=("bold", 10))
label_4.place(x=68,y=280)

entry_4 = Entry(root,textvar=comNumber)
entry_4.place(x=240,y=280)




Button(root, text='Kaydet',width=20,bg='brown',fg='white',command=database).place(x=90,y=380)


root.mainloop()
