import cv2
import face_recognition
import pickle
import pandas as pd
from datetime import datetime
import os

# Load trained model
with open("encodings.pkl", "rb") as f:
    known_encodings, known_names = pickle.load(f)

# Attendance dictionary
attendance = {}

# Start webcam
cam = cv2.VideoCapture(0)
print("Press 'q' to quit")

while True:
    ret, frame = cam.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find faces
    face_locations = face_recognition.face_locations(rgb)
    face_encodings = face_recognition.face_encodings(rgb, face_locations)

    for encoding in face_encodings:
        matches = face_recognition.compare_faces(known_encodings, encoding)
        if True in matches:
            name = known_names[matches.index(True)]
            if name not in attendance:
                attendance[name] = datetime.now().strftime("%H:%M:%S")
                print(f"Attendance marked for {name}")

    cv2.imshow("Smart Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

# Save attendance to CSV
os.makedirs("output", exist_ok=True)  # optional folder
df = pd.DataFrame(attendance.items(), columns=["Name", "Time"])
output_dir = os.path.join(os.getcwd(), "output")
os.makedirs(output_dir, exist_ok=True)

csv_path = os.path.join(output_dir, "attendance.csv")
df.to_csv(csv_path, index=False)
print(f"Attendance saved at {csv_path}")