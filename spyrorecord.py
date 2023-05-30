import cv2
import msvcrt

vid_capture = cv2.VideoCapture(0)

vid_cod = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter(r"C:\Users\jerom\Dropbox\My PC (DESKTOP-VN5I5A5)\Desktop\python\clips\vid1.mp4", vid_cod, 20.0, (640,480))

for i in range(1,1000):
    # Capture each frame of webcam video
    ret,frame = vid_capture.read()
    cv2.imshow("My cam video", frame)
    output.write(frame)
    # Close and break the loop after pressing "x" key
    #if cv2.waitKey(1) &0XFF == ord('x'):
        #break

print("Video is being captured.")