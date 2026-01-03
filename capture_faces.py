import cv2
import os

name = input("Enter Person Name: ")
path = f"dataset/{name}"
os.makedirs(path, exist_ok=True)

cam = cv2.VideoCapture(0)
count = 0

print("Press 'c' to capture image, 'q' to quit")

while True:
    ret, frame = cam.read()
    cv2.imshow("Capture Face", frame)

    if cv2.waitKey(1) & 0xFF == ord('c'):
        cv2.imwrite(f"{path}/{count}.jpg", frame)
        print(f"Image {count} saved")
        count += 1

    if count == 25 or cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
