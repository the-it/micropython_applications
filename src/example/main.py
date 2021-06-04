import pyb
import utime


def control_led(light):
    pyb.LED(light).on()
    utime.sleep(3)
    pyb.LED(light).off()


def move_servo(light, angle, speed):
    servo1.angle(angle, speed)
    control_led(light)


control_led(4)

servo1 = pyb.Servo(1)

move_servo(3, 90, 2000)

move_servo(2, -90, 2000)

control_led(4)
