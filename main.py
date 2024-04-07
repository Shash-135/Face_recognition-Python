import face_recognition
import cv2 
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# Loading Known Faces
shashs_image = face_recognition.load_image_file("faces/shashank.jpg")
shash_encoding = face_recognition.face_encodings(shashs_image)[0]
Alok_image = face_recognition.load_image_file("faces/Alok.JPG")
Alok_encoding = face_recognition.face_encodings(Alok_image)[0]
mahesh_image = face_recognition.load_image_file("faces/mahesh.jpg")
mahesh_encoding = face_recognition.face_encodings(mahesh_image)[0]


Known_face_encodings = [shash_encoding, Alok_encoding, mahesh_encoding]
Known_face_names = ["Shashank", "Alok", "Mahesh"]
students = Known_face_names.copy()
face_locations = []
face_encodings = []

# Getting Current Date and Time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Creating an csv file to keep an record of the students
f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

# Capturing faces through camera

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognizing the face in the frame

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    # Comparing the face with the data we have
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(Known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(Known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        # Checking the best match to the face
        if matches[best_match_index]:
            name: str = Known_face_names[best_match_index]

        # Displaying the students name if he is present
        if name in Known_face_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10, 100)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, name + " Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness,
                        lineType)

        # Saving the attendance time and name of the student in csv filecmp
        if name in students:
            students.remove(name)
            current_time = now.strftime("%H:%M:%S")

            lnwriter.writerow([name, current_time])

    cv2.imshow("Attendence", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
