import cv2

def main():
    # Replace 'rtsp://your_cctv_url' with your actual RTSP URL
    rtsp_url = 'rtsp://192.168.254.199:554/user=admin_password=S47rgdE4_channel=0_stream=0.sdp?real_stream'
    
    # Open the RTSP stream
    cap = cv2.VideoCapture(rtsp_url)

    # Check if the camera stream is opened successfully
    if not cap.isOpened():
        print("Error: Could not open the RTSP stream.")
        return

    while True:
        # Read frames from the camera stream
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            print("Error: Failed to receive a frame from the RTSP stream.")
            break

        # Display the frame in a window
        cv2.imshow('CCTV Stream', frame)

        # Exit the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the resources and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
