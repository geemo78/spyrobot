import cv2
import msvcrt
import time

vid_capture = cv2.VideoCapture(1)

vid_cod = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter(r"C:\Users\jerom\Dropbox\My PC (DESKTOP-VN5I5A5)\Desktop\python\clips\vid1.mp4", vid_cod, 20.0, (640,480))

# Capture each frame of webcam video

for i in range(1,200):

    ret,frame = vid_capture.read()
    cv2.imshow("My cam video", frame)
    output.write(frame)
        

print("Video has been captured.")
