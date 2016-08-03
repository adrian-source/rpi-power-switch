#!/usr/bin/env python

import os
import RPi.GPIO as GPIO
from time import sleep

pin = 18 

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, GPIO.LOW)
print("up")
