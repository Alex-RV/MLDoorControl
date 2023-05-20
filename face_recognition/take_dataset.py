import cv2
import os

current_directory = os.getcwd()
# Put dataset on the level of face_recognition
save_directory = os.path.join(current_directory, "dataset/")
file_prefix = "Person.1."

num_photos = 200

camera = cv2.VideoCapture(0)

cv2.namedWindow("Camera Preview", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Camera Preview", 800, 600)

for photo_num in range(101, num_photos + 1):
    _, frame = camera.read()

    cv2.imshow("Camera Preview", frame)

    file_name = save_directory + file_prefix + str(photo_num) + ".jpg"
    cv2.imwrite(file_name, frame)

    print(f"Captured photo {photo_num}")
    print(file_name)

    cv2.waitKey(500)

camera.release()
