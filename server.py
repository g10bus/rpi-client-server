import cv2
import socket
import struct

HOST = "0.0.0.0"
PORT = 9999

server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)

print("Waiting for connection...")
conn, addr = server.accept()
print("Connected:", addr)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        continue

    # JPEG сжатие
    _, buffer = cv2.imencode(
        ".jpg",
        frame,
        [cv2.IMWRITE_JPEG_QUALITY, 70]
    )

    data = buffer.tobytes()

    # длина кадра (4 байта)
    conn.sendall(struct.pack(">L", len(data)))
    conn.sendall(data)