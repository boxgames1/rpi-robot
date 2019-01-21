import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk

#This function sets up the GPIO ports and mode
def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(4, gpio.OUT)
    gpio.setup(17, gpio.OUT)
    gpio.setup(27, gpio.OUT)
    gpio.setup(22, gpio.OUT)

#It receives the time the wheels will be running forward
def forward(tf):
    gpio.output(4, False)
    gpio.output(17, True)
    gpio.output(27, True)
    gpio.output(22, False)
    time.sleep(tf)
    gpio.cleanup()

#It receives the time the wheels will be running backwards
def reverse(tf):
    gpio.output(4, True)
    gpio.output(17, False)
    gpio.output(27, False)
    gpio.output(22, True)
    time.sleep(tf)
    gpio.cleanup()


#It receives the time the wheels will be turning left
def turn_left(tf):
    gpio.output(4, True)
    gpio.output(17, True)
    gpio.output(27, True)
    gpio.output(22, False)
    time.sleep(tf)
    gpio.cleanup()


#It receives the time the wheels will be turning right
def turn_right(tf):
    gpio.output(4, False)
    gpio.output(17, False)
    gpio.output(27, False)
    gpio.output(22, True)
    time.sleep(tf)
    gpio.cleanup()

#It receives the time the wheels will be pivoting left
def pivot_left(tf):
    gpio.output(4, True)
    gpio.output(17, False)
    gpio.output(27, True)
    gpio.output(22, False)
    time.sleep(tf)
    gpio.cleanup()

#It receives the time the wheels will be pivoting right
def pivot_right(tf):
    gpio.output(4, False)
    gpio.output(17, True)
    gpio.output(27, False)
    gpio.output(22, True)
    time.sleep(tf)
    gpio.cleanup()


def key_input(event):
    init()
    print 'Key: ', event.char
    key_press = event.char
    sleep_time = 0.030

    if key_press.lower() == 'w':
        forward(sleept_time)



command = tk.Tk()
command.bind('<KeyPress>',key_input)
command.mainloop()



