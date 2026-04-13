import RPi.GPIO as GPIO
import time
from picamera2 import Picamera2
import smtplib
from email.message import EmailMessage
import os

GPIO.setmode(GPIO.BCM)

#segments for countdown

a, b, c, d, e, f, g = 6, 5, 22, 27, 17, 4, 18
segments = [a, b, c, d, e, f, g]

for pin in segments:
    GPIO.setup(pin, GPIO.OUT)

digits = {
    0: [1,1,1,1,1,1,0],
    1: [0,1,1,0,0,0,0],
    2: [1,1,0,1,1,0,1],
    3: [1,1,1,1,0,0,1],
    4: [0,1,1,0,0,1,1],
    5: [1,0,1,1,0,1,1],
    6: [1,0,1,1,1,1,1],
    7: [1,1,1,0,0,0,0],
    8: [1,1,1,1,1,1,1],
    9: [1,1,1,1,0,1,1]
}

def display_number(num):
    for i in range(7):
        GPIO.output(segments[i], digits[num][i])

def clear_display():
    for pin in segments:
        GPIO.output(pin, 0)

#LED traffic lights

roadA = {"pins": (12, 16, 21)}  #R Y G

for pin in roadA["pins"]:
    GPIO.setup(pin, GPIO.OUT)

def set_standard(light, state):
    r, y, g = light["pins"]
    GPIO.output(r, state == "RED")
    GPIO.output(y, state == "YELLOW")
    GPIO.output(g, state == "GREEN")

#email

SENDER_EMAIL = "rpiProjectCam@gmail.com"
SENDER_PASSWORD = "dgut odyb cglc xvyd"
RECEIVER_EMAIL = "rpiProjectCam@gmail.com"

#inputs

button = 19
IRsensor = 26
buzzer = 11

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(IRsensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer, GPIO.OUT)

#camera setup

cam = Picamera2()
cam.configure(cam.create_still_configuration())
cam.start()
time.sleep(2)

#email for camera setup

def capture_violation():
    filename = "/home/admin/Pictures/Violation_" + str(int(time.time())) + ".jpg"

    try:
        time.sleep(2)
        cam.capture_file(filename)
        print("Saved:", filename)
        send_email(filename)
    except:
        print("error taking picture")

def send_email(image_path):
    msg = EmailMessage()
    msg['Subject'] = 'Traffic Violation Detected'
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    msg.set_content("Car passed on red light")

    try:
        with open(image_path, 'rb') as f:
            img_data = f.read()
            msg.add_attachment(img_data, maintype='image', subtype='jpeg', filename='violation.jpg')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)

        print("Email sent!")

    except:
        print("email failed")

#sensor for detecting cars running on red light

last_sensor = 1
last_violation = 0

def car_detected_once():
    global last_sensor

    current = GPIO.input(IRsensor)

    if last_sensor == 1 and current == 0:
        last_sensor = current
        return True

    last_sensor = current
    return False

def check_violation():
    global last_violation

    if car_detected_once():
        now = time.time()

        if now - last_violation > 3:
            print("RED LIGHT VIOLATION")
            capture_violation()
            last_violation = now

#function for pedestrian countdown

def pedestrianCountdown():
    for i in range(10, 0, -1):
        display_number(i % 10)

        GPIO.output(buzzer, 1)
        time.sleep(0.2)
        GPIO.output(buzzer, 0)

        t = time.time() + 0.8

        while time.time() < t:
            check_violation()   #the sensor just checks for violantion here, only when the light is red
            time.sleep(0.05)

    clear_display()

try:
    set_standard(roadA, "GREEN")
    print("cars green")

    while True:

        if GPIO.input(button) == 1:
            print("button pressed")

            time.sleep(0.2)

            if GPIO.input(button) == 1:
               
                time.sleep(7) #this is just a delay until the lights actually start changing

                set_standard(roadA, "YELLOW")
                time.sleep(4)

                set_standard(roadA, "RED")
                print("cars RED")

                pedestrianCountdown()

                set_standard(roadA, "GREEN")
                print("cars GREEN again")

                while GPIO.input(button) == 1:
                    time.sleep(0.1)

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Stopped")

finally:
    clear_display()
    cam.stop()
    cam.close()
    GPIO.cleanup()
