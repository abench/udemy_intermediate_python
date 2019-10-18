import cv2

camera_num=0
camera=cv2.VideoCapture(camera_num)

while(camera.isOpened()):
    ret,frame=camera.read()
    if ret==True:
        frame=cv2.flip(frame,1)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
camera.release()
cv2.destroyAllWindows()