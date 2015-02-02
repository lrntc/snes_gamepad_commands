import pygame

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
        runThis = False

        if BLUE == True:
            print("Blue button pressed")

        if RED == True:
            print("Red button pressed")

        if YELLOW == True:
            print("Yellow button pressed")

        if GREEN == True:
            print("Green button pressed")

        if RB == True:
            print("Right button pressed")

        if LB == True:
            print("Left button pressed")
        
