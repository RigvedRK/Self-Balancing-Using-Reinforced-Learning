import RPi.GPIO as gpio
from time import sleep
from numpy import sign


class Motors:
    def __init__(self):
        # set motor pins as outputs
        gpio.setmode(gpio.BOARD)
        gpio.setup(31,   gpio.OUT)
        gpio.setup(33,  gpio.OUT)
        gpio.setup(35,  gpio.OUT)
        gpio.setup(37, gpio.OUT)

        # create pwm objects
        self.pwm_right_forward   = gpio.PWM(33, 50)
        self.pwm_right_backward  = gpio.PWM(31, 50)
        self.pwm_left_forward  = gpio.PWM(37, 50)
        self.pwm_left_backward = gpio.PWM(35, 50)

        self.pwm_right_forward.start(0)
        self.pwm_right_backward.start(0)
        self.pwm_left_forward.start(0)
        self.pwm_left_backward.start(0)

        self.left = 0
        self.right = 0
    
    def stop(self):
        self.pwm_right_forward.ChangeDutyCycle(0)
        self.pwm_right_backward.ChangeDutyCycle(0)
        self.pwm_left_forward.ChangeDutyCycle(0)
        self.pwm_left_backward.ChangeDutyCycle(0)
        self.left = 0
        self.right = 0
    
    def cleanup(self):
        self.stop()
        self.pwm_left_forward.stop()
        self.pwm_left_backward.stop()
        self.pwm_left_forward.stop()
        self.pwm_left_backward.stop()
        gpio.setup(31,   gpio.IN)
        gpio.setup(33,  gpio.IN)
        gpio.setup(37,  gpio.IN)
        gpio.setup(35, gpio.IN)
    
    def forward(self):
        self.pwm_right_forward.ChangeDutyCycle(100)
        self.pwm_right_backward.ChangeDutyCycle(0)
        self.pwm_left_forward.ChangeDutyCycle(100)
        self.pwm_left_backward.ChangeDutyCycle(0)
    
    def backward(self):
        self.pwm_right_forward.ChangeDutyCycle(0)
        self.pwm_right_backward.ChangeDutyCycle(100)
        self.pwm_left_forward.ChangeDutyCycle(0)
        self.pwm_left_backward.ChangeDutyCycle(100)

motor = Motors()
motor.stop()
motor.forward()
sleep(1)
motor.backward()
sleep(1)
motor.cleanup()       
