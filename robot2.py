import RPi.GPIO as gpio
import time

#This function sets up the GPIO ports and mode
def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(4, gpio.OUT)
    gpio.setup(17, gpio.OUT)
    gpio.setup(27, gpio.OUT)
    gpio.setup(22, gpio.OUT)

#It receives the time the wheels will be running forward
def forward(tf):
    init()
    gpio.output(4, False)
    gpio.output(17, True)
    gpio.output(27, True)
    gpio.output(22, False)
    time.sleep(tf)
    gpio.cleanup()

#It receives the time the wheels will be running backwards
def reverse(tf):
    init()
    gpio.output(4, True)
    gpio.output(17, False)
    gpio.output(27, False)
    gpio.output(22, True)
    time.sleep(tf)
    gpio.cleanup()


forward(1)
reverse(1)
