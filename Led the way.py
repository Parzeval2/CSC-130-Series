import RPi.GPIO as GPIO
from time import sleep

led = 17
button = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while (True):
	GPIO.output(led, GPIO.HIGH)
	sleep(0.5)
	GPIO.output(led, GPIO.LOW)
	sleep(0.5)
	while (GPIO.input(button)):
		GPIO.output(led, GPIO.HIGH)
		sleep(0.1)
		GPIO.output(led, GPIO.LOW)
		sleep(0.1)