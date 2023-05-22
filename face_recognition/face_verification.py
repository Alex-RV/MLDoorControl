import cv2
import numpy as np
import os 
import time



#initiate id counter
id = 0

# Update these names. Make sure to add as many as IDs trained; assumes first ID is 0.
names = ['Person1', 'Aleks', 'Person3', 'Person4', 'Person5', 'Person6'] 



def face_verification():
    print("Verification started")
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    current_directory = os.getcwd()
    directory = os.path.join(current_directory, "face_recognition/trainer/trainer.yml")
    recognizer.read(directory)
    cascadePath = os.path.join(current_directory, "face_recognition/cascades/haarcascade_frontalface_default.xml")
    faceCascade = cv2.CascadeClassifier(cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX
    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    start_time = time.time()
    recognized_id = None

    while True:
        ret, img = cam.read()
        # img = cv2.imread(img, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )
        max_time = time.time() - start_time
        print(max_time)
        if max_time < 12:
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

                print(current_id)

                if current_id != recognized_id:
                    print("new face")
                    recognized_id = current_id
                    start_time_1 = time.time()
                elif current_id == recognized_id and current_id == "Aleks": #change it later on the name of authorized people
                    print("same face")
                    min_time = time.time() - start_time_1
                    print(min_time)
                    if min_time >= 3:
                        print("verified")
                        cam.release()
                        cv2.destroyAllWindows()
                        return True
        else:
            break

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break

    print("NOT verified")
    cam.release()
    cv2.destroyAllWindows()
    return False
