#!/usr/bin/env python

# imports

from rfid import rfid

from recognition import rec
from led import green_led_on, green_led_off, red_led_off, red_led_on


def main():


    rfid()
    rec()




if __name__ == '__main__':
    while True:
        main()

""" 
SDA = Pin 24
SCK = Pin 23
MOSI = Pin 19
MISO = Pin 21
GND = Pin 6
RST = Pin 22
3.3V = Pin 1
"""
