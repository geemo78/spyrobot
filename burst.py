import cv2
import schedule
import os

cam = cv2.VideoCapture(1)
cv2.namedWindow("Webcam")
img_counter = 0
save_dir = 'D:\yolov5\snaps'

def capture():
    global img_counter
    img_name = "opencv_frame_{}.png".format(img_counter)
    #cv2.imwrite(img_name, frame)
    cv2.imwrite(os.path.join(save_dir,img_name), frame)
    print("screenshot taken")
    img_counter += 1


# Set up schedule before loop

schedule.every(10).seconds.do(capture)


while True:
    ret, frame = cam.read()

    if not ret:
        print("failed to grab frame")
        break

    cv2.imshow("test", frame)
    schedule.run_pending()

    k = cv2.waitKey(100)  # 1/10 sec delay; no need for separate sleep

    if k % 256 == 27:
        print("closing the app")
        break

cam.release()
cam.destroyAllWindows()