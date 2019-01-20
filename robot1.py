#This file simply setups the gpio pins to run all wheels
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(4, gpio.OUT)
gpio.setup(17, gpio.OUT)
gpio.setup(27, gpio.OUT)
gpio.setup(22, gpio.OUT)

gpio.output(4, True)
gpio.output(17, True)
gpio.output(27, True)
gpio.output(22, False)
time.sleep(0.5)

gpio.cleanup()


