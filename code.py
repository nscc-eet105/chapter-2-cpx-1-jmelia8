# Joe Melia EET-107

from adafruit_circuitplayground import cp
import time 

while True: 
    cp.red_led = True
    time.sleep(.5)
    cp.red_led = False
    time.sleep(.5)
    #neopixel
    cp.pixels[0] = (0, 100, 0)
    time.sleep(.5)
    cp.pixels[0] = (0, 0, 0)
    time.sleep(.5)
