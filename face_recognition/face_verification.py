import cv2
import numpy as np
import os 

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "cascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

#initiate id counter
id = 0

# Update these names. Make sure to add as many as IDs trained; assumes first ID is 0.
names = ['Person1', 'Aleks', 'Person3', 'Person4', 'Person5', 'Person6'] 

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()


import time

def face_verification():
    start_time = time.time()
    recognized_id = None
    
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            if confidence < 70:
                current_id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                current_id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
            
            cv2.putText(img, str(current_id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
            
            if recognized_id is None:
                recognized_id = current_id
                start_time = time.time()
            elif current_id != recognized_id:
                recognized_id = None
                start_time = time.time()
            
            elapsed_time = time.time() - start_time
            if elapsed_time >= 3:
                return True  
                
        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff  
        if k == 27:
            break
    
    return False

