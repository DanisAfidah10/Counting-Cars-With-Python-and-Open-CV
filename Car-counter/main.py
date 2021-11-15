
# Simple pygame test for the google coral
# Maps the gamepad for a Logitech controller
# Author: Danny Dasilva
# License: Public Domain 

import pygame
from time import sleep
from app.DroneV2 import Drone
import cv2
import threading
from feed_frames import people_counting
drone = Drone()

pygame.init()




totalFrames = 0
#thread that does video processing
def thread():

    totalFrames = 0
    trackers=[]
    down = 0
    up = 0 
    # feed frames from drone.video generator into car count open cv processing function
    
    for image in drone.video():
        totalFrames, trackers, down, up = people_counting(image, totalFrames=totalFrames, trackers=trackers, down=down, up=up)
                
threading.Thread(target=thread).start()







joystick_count = pygame.joystick.get_count()

if joystick_count == 0:
    # No joysticks!
    print("Error, I didn't find any joysticks.")
else:
    # Use joystick #0 and initialize it
    gamepad = pygame.joystick.Joystick(0)
    gamepad.init()
    print('init')

while True:
    pygame.event.get()
   

    if joystick_count != 0:
        rightsticky = gamepad.get_axis(1)
        leftsticky = gamepad.get_axis(4)

        rightstickx = gamepad.get_axis(0)
        leftstickx = gamepad.get_axis(3)
        Start = gamepad.get_button(7)
        Back = gamepad.get_button(6)
        x, y = gamepad.get_hat(0)

        X = gamepad.get_button(2)
        Y = gamepad.get_button(3)
        A = gamepad.get_button(0)
        B = gamepad.get_button(1)
    else:
        print("Error: no joysticks found")
        break
    

    
    deadzone = .05

    if Start == 1:
        print('Start pressed')
        drone.takeoff()
    
    if Back == 1:
        drone.land()
        print('Back pressed')

    if X == 1:
        drone.left(30)
    
    if B == 1:
        drone.right(30)

    if Y == 1 :
        drone.forward(30)

    if A == 1:
        drone.backward(30)

    if abs(leftsticky) > .05:
       
        drone.pitch(-leftsticky)
    else:
        drone.pitch(0)

    if abs(rightsticky) > .05:
      
        drone.throttle(-rightsticky)
    else:
        drone.throttle(0)
        
    if abs(leftstickx) > .05:
        print("call")
        drone.roll(leftstickx)
    else:
        drone.roll(0)
        
    if abs(rightstickx) > .05:
        drone.yaw(rightstickx)
    else:
        drone.yaw(0)
    
    sleep(.02)







