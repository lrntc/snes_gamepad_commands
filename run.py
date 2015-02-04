import pygame
import subprocess
import os

runThis = True

pygame.init()
pygame.joystick.init()
MyJoystick = pygame.joystick.Joystick(0)
MyJoystick.init()

print("Make a choice")
print("-------------")
print("BLUE -> pycam")
print("RED -> startx")
print("YELLOW -> timelapse")
print("GREEN -> HDR picture")
print("RB -> exit script")
print("LB -> shutdown")

while runThis:
    for event in pygame.event.get():
        BLUE = MyJoystick.get_button(0)
        RED = MyJoystick.get_button(1)
        YELLOW = MyJoystick.get_button(2)
        GREEN = MyJoystick.get_button(3)
        RB = MyJoystick.get_button(5)
        LB = MyJoystick.get_button(4)
        

        if BLUE == True:
            print("Blue button pressed")
            os.chdir("/home/pi/adafruit-pi-cam-master")
            subprocess.Popen(["python", "cam.py"])
            runThis = False

        if RED == True:
            print("Red button pressed")
            os.chdir("/home/pi/")
            subprocess.Popen(["sh", "gui_py.sh"])
            runThis = False
            
        if YELLOW == True:
            print("Yellow button pressed")
            os.chdir("/home/pi/Desktop/IR Project/pi-timelapse-process-hdr/")
            subprocess.Popen(["sh", "runtimelapse.sh"])

        if GREEN == True:
            print("Green button pressed")
            os.chdir("/home/pi/Desktop/IR Project/pi-timelapse-process-hdr/")
            subprocess.Popen(["sh", "hdr_picture.sh"])

        if RB == True:
            print("Right button pressed")
            exit()

        if LB == True:
            print("Left button pressed")
            subprocess.call("sudo halt")
        
