#Use 3 GPIO output pins to control the RGB-LED with the GUI below. By selecting different checkboxes,
#the RGB-LED should produce dufferent color after clicking shine.
#For example, by checking Red and Green and clicking "Shine!" , the LED color should be yellow.
#By checking Red, Green and Blue, the LED color should be white.
#(Black color means LED is off)

import tkinter as tk
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

LED_PINR = 23 #RED LED
LED_PING = 18 #GREEN LED
LED_PINB = 4  #BLUE LED

#Setting all pins as output pins
GPIO.setup(LED_PINR, GPIO.OUT) 
GPIO.setup(LED_PING, GPIO.OUT)
GPIO.setup(LED_PINB, GPIO.OUT)
mainwindow = tk.Tk()

def shine():
    if checkR.get() == 1:
        GPIO.output(LED_PINR, GPIO.HIGH) #if red box is checked, LED_PINR is set to HIGH powering on the Red LED
    else:
        GPIO.output(LED_PINR, GPIO.LOW)
    if checkG.get() == 1:
        GPIO.output(LED_PING, GPIO.HIGH)
    else:
        GPIO.output(LED_PING, GPIO.LOW)
    if checkB.get() == 1:
        GPIO.output(LED_PINB, GPIO.HIGH)
    else:
        GPIO.output(LED_PINB, GPIO.LOW)

checkR = tk.IntVar()
checkG = tk.IntVar()
checkB = tk.IntVar()

#Creating checking boxes
red_check = tk.Checkbutton(text='Red', onvalue=1, offvalue=0, variable=checkR)
green_check = tk.Checkbutton(text='Green', onvalue=1, offvalue=0, variable=checkG)
blue_check = tk.Checkbutton(text='Blue', onvalue=1, offvalue=0, variable=checkB)

#Creating shine button
shine_button = tk.Button(text='Shine!', command=shine)

#Displaying buttons on the window
red_check.pack(padx=2, pady=2)
green_check.pack(padx=2, pady=2)
blue_check.pack(padx=2, pady=2)
shine_button.pack(padx=2, pady=2)

mainwindow.mainloop()
GPIO.cleanup()

