#!/usr/bin/python
#
# GDM1602K LCD and KeyPad Test Script for
# Raspberry Pi
#
# Made by: Jpa
# Heavily based on the work of: Matt Hawkins, Kenneth Burgener

import RPi.GPIO as GPIO
import time
 
# Define GPIO to LCD mapping
LCD_RS = 7
LCD_E  = 8
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18
 
# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False 
LCD_LINE_1 = 0x00 #0x00 # LCD RAM address for the 1st line
LCD_LINE_2 = 0x40 #0x40 # LCD RAM address for the 2nd line 
 
# Timing constants
E_DELAY = 0.002


def setup():

  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  GPIO.setup(LCD_E , GPIO.OUT, initial = GPIO.LOW) # E
  GPIO.setup(LCD_RS, GPIO.OUT, initial = GPIO.LOW) # RS
  GPIO.setup(LCD_D4, GPIO.OUT, initial = GPIO.LOW) # DB4
  GPIO.setup(LCD_D5, GPIO.OUT, initial = GPIO.LOW) # DB5
  GPIO.setup(LCD_D6, GPIO.OUT, initial = GPIO.LOW) # DB6
  GPIO.setup(LCD_D7, GPIO.OUT, initial = GPIO.LOW) # DB7

def lcd_goto(line, pos):
  if line == 1:
    lcd_nibble(0b0000,LCD_CMD)
  else:
    lcd_nibble(0b1100,LCD_CMD)
  lcd_nibble(0b0000+pos,LCD_CMD)    

def cleanup():
  GPIO.output(LCD_E, False)
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  GPIO.cleanup()
 
def lcd_init():

  # Initialise display
  time.sleep(0.04)
  E_DELAY = 0.005
  lcd_nibble(0b0011,LCD_CMD)
  lcd_nibble(0b0011,LCD_CMD)
  lcd_nibble(0b0011,LCD_CMD)
  lcd_nibble(0b0010,LCD_CMD)
  lcd_nibble(0b0010,LCD_CMD)
  lcd_nibble(0b1000,LCD_CMD)
  lcd_nibble(0b0000,LCD_CMD)
  lcd_nibble(0b1111,LCD_CMD) #display, cursor, blink
  lcd_nibble(0b0000,LCD_CMD)
  lcd_nibble(0b0110,LCD_CMD)
  E_DELAY = 0.002

def lcd_bcksp():
  lcd_byte(0b00000100,LCD_CMD)
  lcd_byte(0b00100000,LCD_CHR)
  lcd_byte(0b00000110,LCD_CMD)
  lcd_byte(0b00100000,LCD_CHR)
  lcd_byte(0b00000100,LCD_CMD)
  lcd_byte(0b00100000,LCD_CHR)
  lcd_byte(0b00000110,LCD_CMD)
 
def lcd_string(message):
  if len(message) > 16:
    message = message.ljust(LCD_WIDTH," ")  
  for i in range(len(message)):
    lcd_byte(ord(message[i]),LCD_CHR)

def lcd_nibble(bits, mode):

  GPIO.output(LCD_RS, mode)
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)
 
def lcd_byte(bits, mode):
  # Send byte to data pins
  # mode = True to write, False for command
  GPIO.output(LCD_RS, mode) # RS
   # High bits
  lcd_nibble(int(bits/16),mode)
   # Low bits
  lcd_nibble(bits%16,mode) 
  
