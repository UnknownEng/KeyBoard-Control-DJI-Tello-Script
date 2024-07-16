from djitellopy import tello
from time import sleep
import kp

me = tello.Tello()

print("Conecting ...")

me.connect()

print("Connected")

print (me.get_battery())

kp.init()

me.takeoff()

me.send_rc_control(0,0,0,0)
   

while True:
    if kp.getKey("a"):
        me.send_rc_control(30,0,0,0)
        print("move Left")
        sleep(3)
    elif kp.getKey("d"):
        me.send_rc_control(-30,0,0,0)
        print("move right")
        sleep(3)
    elif kp.getKey("w"):
        me.send_rc_control(0,30,0,0)
        print("move  forward")
        sleep(3)
    elif kp.getKey("s"):
        me.send_rc_control(0,0,0,0)
        print("Hovering")
        sleep(3)
    elif kp.getKey("x"):
        me.send_rc_control(0,-30,0,0)
        print("move backward")
        sleep(3)
    elif kp.getKey("UP"):
        me.send_rc_control(0,0,30,0)
        print("move upward")
        sleep(3)
    elif kp.getKey("DOWN"):
        me.send_rc_control(0,0,-30,0)
        print("move downward")
        sleep(3)
    elif kp.getKey("z"):
        me.send_rc_control(0,0,0,30)
        print("Rotate clockwise")
        sleep(3)
    elif kp.getKey("c"):
        me.send_rc_control(0,0,0,-30)
        print("move anticlockwose")
        sleep(3)
    elif kp.getKey("v"):
        me.land()
        print("landed")
        sleep(3)
    elif kp.getKey("b"):
        me.takeoff()
        print("TAking OFF")
        sleep(2)

print("Program run succesfull")
    