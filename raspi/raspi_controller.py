import RPi.GPIO as GPIO


def should_drive_wheels(is_granted_access):
    servo_pin = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)
    p = GPIO.PWM(servo_pin, 50)  # GPIO 17 for PWM with 50Hz

    if is_granted_access:
        p.start(2.5)  # Initialization
        p.ChangeDutyCycle(7.5)
        return True
    p.stop()  # Stop
    p.ChangeDutyCycle(0)
    return False
