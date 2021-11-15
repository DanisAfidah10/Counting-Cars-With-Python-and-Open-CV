from app.DroneV2 import Drone
import cv2
drone = Drone()

## example video call 
# you can pass the image to whatever ai function
for image in drone.video():
    cv2.imshow('Tello', image)
            
    cv2.waitKey(1)