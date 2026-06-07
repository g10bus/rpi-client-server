import cv2
import socket
import struct
import numpy as np

RPI_IP = "rpi-server.local"
PORT = 9999

sock = socket.socket()
sock.connect((RPI_IP, PORT))

def recv_exact(sock, size):
    data = b""

    while len(data) < size:
        packet = sock.recv(size - len(data))

        if not packet:
            return None

        data += packet

    return data

while True:

    packed_size = recv_exact(sock, 4)

    if packed_size is None:
        break

    frame_size = struct.unpack(">L", packed_size)[0]

    frame_data = recv_exact(sock, frame_size)

    if frame_data is None:
        break

    frame = cv2.imdecode(
        np.frombuffer(frame_data, np.uint8),
        cv2.IMREAD_COLOR
    )

    cv2.imshow("Raspberry Camera", frame)

    if cv2.waitKey(1) == 27:
        break

sock.close()
cv2.destroyAllWindows()