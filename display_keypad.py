import lcd_kp as lib
import RPi.GPIO as GPIO
import time
import os
import sys
from evdev import InputDevice, categorize, ecodes
from select import select

#KeyPad a usar
dev = InputDevice("/dev/input/by-id/usb-05d5_KEYBOARD-event-kbd")
dev.grab() # mio!

# 96 = Enter, [71-73] -> [7-9], [75-77] -> [4-6] ... , 82 = 0, 14 = borrar
key_list = dict([(96,"Enter"),
                 (71,7),(72,8),(73,9),
                 (75,4),(76,5),(77,6),
                 (79,1),(80,2),(81,3),
                 (82,0),(14,"BckSpc")])

def main():

  GPIO.setwarnings(False)
  lib.setup()
  lib.lcd_init()
  
  lib.lcd_goto(1,0)
  lib.lcd_string("Device found:")
  lib.lcd_goto(2,1)
#  lib.lcd_string(dev.name)
#  time.sleep(2)

  for event in dev.read_loop():
    if event.code == 96:
      break
    if event.value == 0:
      if event.code == 14:
        lib.lcd_bcksp()
      elif event.code in key_list:
        lib.lcd_string(str(key_list[event.code]))
  
  time.sleep(1)
  lib.cleanup()



if __name__ == '__main__':
  main()
