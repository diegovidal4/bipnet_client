import lcd_kp as lib
import time
import os
import sys
from evdev import InputDevice


#KeyPad a usar
dev = InputDevice("/dev/input/by-id/usb-05d5_KEYBOARD-event-kbd")
dev.grab() # mio!

def main():

  lib.setup()
  lib.lcd_init()
  
  lib.lcd_goto(1,0)
  
  lib.lcd_string("Device found:")
  lib.lcd_goto(2,1)  

  print lib.kp_input(dev)

  time.sleep(1)
  lib.cleanup()

if __name__ == '__main__':
  main()
