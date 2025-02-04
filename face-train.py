import cv2
import os
import numpy as np
from PIL import Image



recognizer = cv2.face.LBPHFaceRecognizer_create()
path="images"
def getImagesWithID(path):
    imagePaths=(os.path.join(path,f)for f in os.listdir(path))
    faces=[]
    IDs=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L')
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        print(ID)
        IDs.append(ID)
        cv2.imshow("training",faceNp)
        cv2.waitKey(10)
        pass
    return IDs,faces
    pass
ıds,faces=getImagesWithID(path)
recognizer.train(faces,np.array(ıds))
recognizer.save("recognizers/face-trainner.yml")
cv2.destroyAllWindows()
