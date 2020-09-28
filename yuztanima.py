import numpy as np
import cv2
import sqlite3
import threading
import matplotlib.pyplot as plt
import math
import tkinter as tk
from PIL import Image,ImageTk
from imgpy import Img
import PIL
import json
from win32api import GetSystemMetrics
widthsec = GetSystemMetrics(0)
height = GetSystemMetrics(1)

print(widthsec)
print(height)
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
window = tk.Tk()  #Makes main window
window.wm_title("Cameralar")
window.config(background="#ffffff")
window.state('zoomed')
#Graphics window
imageFrame = tk.Frame(window, width=widthsec, height=height)
imageFrame.grid(row=0, column=0, padx=10, pady=2)
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
AdSoyad=[]




def ipcamera(input,i,j,conn):
    while(True):
        cap=cv2.VideoCapture(input)
        rec=cv2.face.LBPHFaceRecognizer_create()
        rec.read("recognizers/face-trainner.yml")
        id=0

        tempx=0
        tempy=0
        tempw=0
        temph=0

        ret, frame =cap.read()

        if not ret :
                print("err")
                img = Image.open("error.jpg")
                img = img.resize((int(widthsec/math.ceil(math.pow(len(ip_adress),1/2))),int(height/math.ceil(math.pow(len(ip_adress),1/2)))), PIL.Image.ANTIALIAS)

                output[(hi*i):(hi * (i+1)), (wi*j):(wi * (j+1))] = img
                img = Image.fromarray(cv2.cvtColor(output,cv2.COLOR_BGR2RGBA))
                imgtk = ImageTk.PhotoImage(image=img)
                lmain.imgtk = imgtk
                lmain.configure(image=imgtk)

                return
                pass
        frame=cv2.resize(frame, (int(widthsec/math.ceil(math.pow(len(ip_adress),1/2))),int(height/math.ceil(math.pow(len(ip_adress),1/2)))))
        gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        faces=face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
        for (x,y,w,h) in faces:
            roi_gray=gray[y:y+h,x:x+w]
            roi_color= frame[y:y+h,x:x+w]


            color=(255, 0, 0)
            stroke =1
            end_cord_x=x+w
            end_cord_y=y+h

            cv2.rectangle(frame, (x,y), (end_cord_x,end_cord_y), color,stroke)
            id,conf=rec.predict(roi_gray)

            if conf>=4 and conf <= 85 :
                cmd="SELECT Name,Surname FROM People WHERE ID="+str(id)
                cursor=conn.execute(cmd)
                for row in cursor:
                    a=row
                    AdSoyad.append(''.join(a))
                fontface = cv2.FONT_HERSHEY_SIMPLEX
                fontscale = 1
                fontcolor = (255, 0, 0)
                cv2.putText(frame, str(AdSoyad[0]), (x,y+h), fontface, fontscale, fontcolor)
                

        output[(hi*i):(hi * (i+1)), (wi*j):(wi * (j+1))] = frame



        img = Image.fromarray(cv2.cvtColor(output,cv2.COLOR_BGR2RGBA))
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)



        if cv2.waitKey(20)& 0xFF==ord('q'):
            break
            pass

################

n=0
conn = sqlite3.connect("Fasebase/FaseBase.db", check_same_thread=False)


a=conn.execute("SELECT Adres FROM IpAdress WHERE ID=0")
ip_adress=[]

for row in conn.execute('SELECT Adres FROM IpAdress'):
    a=row
    ip_adress.append(''.join(a))





i=0
j=0
hi=int(height/math.ceil(math.pow(len(ip_adress),1/2)))
wi=int(widthsec/math.ceil(math.pow(len(ip_adress),1/2)))
output = np.zeros((hi * math.ceil(math.pow(len(ip_adress),1/2)), wi * math.ceil(math.pow(len(ip_adress),1/2)), 3), dtype="uint8")
for i in range(math.ceil(math.pow(len(ip_adress),1/2))):
    for j in range(math.ceil(math.pow(len(ip_adress),1/2))):
        if n==len(ip_adress):
            break
        pass
        threading.Thread( target=ipcamera, args=(ip_adress[n],i,j,conn,)).start()
        n=n+1
    pass
    if n==len(ip_adress):
        break
    pass
pass


sliderFrame = tk.Frame(window, width=widthsec, height=height)
sliderFrame.grid(row = height, column=0, padx=10, pady=2)
window.mainloop()
conn.close()
cv2.destroyAllWindows()
