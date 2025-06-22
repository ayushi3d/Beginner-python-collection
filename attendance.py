import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# Load known faces
path = 'known_faces'
images = []
names = []
myList = os.listdir(path)

for filename in myList:
    img = cv2.imread(f'{path}/{filename}')
    images.append(img)
    names.append(os.path.splitext(filename)[0])  # Remove .jpg from name


def find_encodings(images):
    encode_list = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encode_list.append(encode)
    return encode_list


def mark_attendance(name):
    with open('attendance.csv', 'r+') as f:
        data = f.readlines()
        name_list = [line.split(',')[0] for line in data]
        if name not in name_list:
            time_now = datetime.now().strftime('%H:%M:%S')
            date_now = datetime.now().strftime('%Y-%m-%d')
            f.write(f'{name},{time_now},{date_now}\n')


# Encode known faces
known_encodings = find_encodings(images)
print("✅ Encodings Complete!")

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img_small = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)  # Resize for speed
    img_small = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)

    faces_cur_frame = face_recognition.face_locations(img_small)
    encodes_cur_frame = face_recognition.face_encodings(img_small, faces_cur_frame)

    for encode_face, face_loc in zip(encodes_cur_frame, faces_cur_frame):
        matches = face_recognition.compare_faces(known_encodings, encode_face)
        face_dist = face_recognition.face_distance(known_encodings, encode_face)
        match_index = np.argmin(face_dist)

        if matches[match_index]:
            name = names[match_index].capitalize()

            y1, x2, y2, x1 = face_loc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4  # Scale back up

            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            mark_attendance(name)

    cv2.imshow('Attendance System', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()