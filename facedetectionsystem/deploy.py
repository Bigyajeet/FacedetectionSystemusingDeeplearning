labels = ['Ritu']

import cv2
import urllib
import numpy as np

from tensorflow.keras.models import load_model

classifier = cv2.CascadeClassifier(r"C:/Users/BIGYAJEET/OneDrive/Pictures/Desktop/CTTC/facedetectionsystem/facedetectionsystem/haarcascade_frontalface_default.xml")

url = "http://192.168.0.0.4:8080/shot.jpg"

model = load_model("final_model.h5")

def preprocessing(img):
    img = cv2.resize(img, (100, 100))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img.reshape((1,100, 100, 1))
    img = img/255
    return img

def getLabel(img):
    code = model.predict(img)
    code1=np.argmax(code)
    return labels[code1]

while True:
    image_from_url = urllib.request.urlopen(url)
    frame = np.array(bytearray(image_from_url.read()), np.uint8)
    frame = cv2.imdecode(frame, -1)
    face = frame.copy()
    
    faces = classifier.detectMultiScale(frame, 1.3, 5)
    if len(faces)>0:
        for x,y,w,h in faces:
            face=frame[y:y+h,x:x+w].copy()
            face = preprocessing(face)
            
            cv2.rectangle(frame, (x,y), (x+w,y+h), 
                          (255, 255 , 0), 3)
            cv2.putText(frame, getLabel(face),
                    (x,y-50), cv2.FONT_HERSHEY_COMPLEX,
                    1, (255, 255, 0), 2)
    cv2.imshow("Live Image",frame)
    if cv2.waitKey(25) == 27:
        break

cv2.destroyAllWindows()
            
            
#import tensorflow
#tensorflow.__version__