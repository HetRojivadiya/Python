import cv2
from plyer import notification

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
video_cap = cv2.VideoCapture(0)
face_detected = False
count = 3

while True:
    ret, video_data = video_cap.read()
    gray_frame = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        face_detected = True
        for (x, y, w, h) in faces:
            cv2.rectangle(video_data, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        if face_detected:
            face_detected = False
            notification.notify(
                title="Warning",
                message="Please focus on the quiz and do not look away.",
                timeout=2
            )
            print("Please focus on the quiz and do not look away.")
            count-=1
    cv2.imshow("video_live", video_data)

    key = cv2.waitKey(10)
    if key == ord("q") or count==0:
        break

video_cap.release()
cv2.destroyAllWindows()
