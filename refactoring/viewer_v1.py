import cv2
import time

from contextlib import contextmanager


# @contextmanager
def open_camera(camera_num):
    camera = cv2.VideoCapture(camera_num)
    while camera.isOpened():
        ret, frame = camera.read()
        if ret:
            yield frame
    camera.release()

def process_frame(frame):
    frame = cv2.flip(frame, 1)
    cv2.imshow('frame', frame)
    return cv2.waitKey(1)


if __name__ == "__main__":
    camera_num=0
    for picture in open_camera(camera_num):
        if (process_frame(picture) & 0xFF) == ord('q'):
            break

    cv2.destroyAllWindows()