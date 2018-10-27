#GPIO Library
import datetime
import RPi.GPIO as GPIO
import pygame

# Define last activity.
sleepMode = False
lastActivity = 0

def reproduceSound(audioFile):
	# Play audio
	sleepMode = False
	pygame.mixer.init()
	pygame.mixer.music.load()
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue

#GPIO Define inputs
GPIO.setup(10, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(14, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(20, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(24, GPIO.IN)

#While the script is runing check for inputs.
while 1:

	if GPIO.input(10) and GPIO.input(12):
		#stop
		shutdown -h now
	if lastActivity + datetime.timedelta(minutes = 20) > datetime.datetime.now():
		#stop
		shutdown -h now
	if lastActivity + datetime.timedelta(minutes = 5) > datetime.datetime.now():
		#sleep.
		sleepMode = True

	# Reproduce X audio file based on the input-.
	if GPIO.input(10):
		reproduceSound("audioOne.wav")
		lastActivity = datetime.datetime.now()
	if GPIO.input(12):
		reproduceSound("audioTwo.wav")
		lastActivity = datetime.datetime.now()
	if GPIO.input(14):
		reproduceSound("audioTree.wav")
		lastActivity = datetime.datetime.now()
	if GPIO.input(16):
		reproduceSound("audioFour.wav")
		lastActivity = datetime.datetime.now()
	if GPIO.input(18):
		reproduceSound("audioFive.wav")
		lastActivity = datetime.datetime.now()
	if GPIO.input(20):
		reproduceSound("audioSix.wav")
		lastActivity = datetime.datetime.now()
	if GPIO.input(22):
		reproduceSound("audioSeven.wav")
		lastActivity = datetime.datetime.now()
	if GPIO.input(24):
		reproduceSound("audioEight.wav")
		lastActivity = datetime.datetime.now()
