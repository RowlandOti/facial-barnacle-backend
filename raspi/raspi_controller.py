import time

import RPi.GPIO as GPIO


def should_drive_wheels(is_granted_access):
    servo_pin = 12
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)
    servo = GPIO.PWM(servo_pin, 50)  # GPIO 12 for PWM with 50Hz

    if is_granted_access:
        servo.start(2.5)  # Initialization
        set_angle(180, servo)
        return True
    servo.stop()  # Stop
    servo.ChangeDutyCycle(0)
    return False


def set_angle(angle, servo):
    duty = int(angle / 18 + 2)

    for i in range(0, duty, 2):
        servo.ChangeDutyCycle(i)
        time.sleep(1)

    time.sleep(1)
    servo.ChangeDutyCycle(0)
