#!/usr/bin/env python

# Control Lasermodule from Raspberry Pi
# https://raspberrytips.nl/laser-module-aansturen-via-gpio/

import RPi.GPIO as GPIO
import time

LaserGPIO = 17, 23  # --> GPIO17 for Laser and GPIO23 for Oscilloscope


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LaserGPIO, GPIO.OUT)
    GPIO.output(LaserGPIO, GPIO.HIGH)


def loop(cycle, time_on, time_off):
    print(cycle, ' cycles; on/off: ', time_on, '/', time_off, ' sec')
    time.sleep(2)
    i = 1
    while i < cycle+1:
        print('Round ', i)
        print('Laser on: ', time_on, ' sec')
        GPIO.output(LaserGPIO, GPIO.HIGH)  # laser on
        time.sleep(time_on)
        print('Laser off: ', time_off, ' sec')
        GPIO.output(LaserGPIO, GPIO.LOW)  # laser off
        time.sleep(time_off)
        i+=1
    print('Finish! :)')


def destroy():
    GPIO.output(LaserGPIO, GPIO.LOW)
    GPIO.cleanup()
    i = 0


if __name__ == '__main__':
    setup()
    
    """ Input Values Start """
    # Unit second
    cycle = 64
    time_on = 0.85
    time_off = 2.15
    """ Input Values End """

    try:
        loop(cycle, time_on, time_off)

    except KeyboardInterrupt:
        destroy()
