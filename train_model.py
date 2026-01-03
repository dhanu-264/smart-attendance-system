import face_recognition
import os
import pickle

dataset_path = "dataset"
known_encodings = []
known_names = []

print("Training model...")

for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)

    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)

        image = face_recognition.load_image_file(img_path)
        encodings = face_recognition.face_encodings(image)

        if encodings:
            known_encodings.append(encodings[0])
            known_names.append(person)

with open("encodings.pkl", "wb") as f:
    pickle.dump((known_encodings, known_names), f)

print("Model trained and saved successfully!")
