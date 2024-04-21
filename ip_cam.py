import cv2

camera_ip = "192.168.0.64"
username = "admin"
password = "camera201"

stream_url = f"rtsp://{username}:{password}@{camera_ip}/Streaming/channels/1/"

cap = cv2.VideoCapture(stream_url)

if not cap.isOpened():
    print("Error opening video capture")
    exit()

while True:

    ret, frame = cap.read()


    if not ret:
        print("Error capturing frame")
        break

    cv2.imshow('Rover Camera Feed(Science)', frame)

    # Exit on 'q' key press
    #if cv2.waitKey(1) == ord('q'):
       # break


cap.release()
cv2.destroyAllWindows()


