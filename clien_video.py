import cv2

cap = cv2.VideoCapture("tcp://rpi-server.local:5000")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Нет кадра")
        continue

    cv2.imshow("RPI Camera", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()