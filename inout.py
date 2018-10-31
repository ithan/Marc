# libraries 
from subprocess import call
import datetime
import RPi.GPIO as GPIO
import pygame
import socket
import sys


# Host
HOST = ''   # IP or Hostname of you server
PORT = 8888 # Arbitrary non-privileged port
connected = False # Boolean To send events only if the socket is connected.

# Define last activity.
lastActivity = 0

# The index of the input should match the index of the sound.
inputs = [10, 12, 14, 16, 18, 20, 22, 24]
sounds = ["audioOne.mp3", "audioTwo.mp3", "audioTree.mp3", "audioFour.mp3", "audioFive.mp3", "audioSix.mp3", "audioSeven.mp3", "audioEight.mp3"]

# Stop inputs
stopInputs = [10, 12]

# Network setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORT))
	connected = True
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
	connected = False


def reproduceSound(audioFile):
	# Play audio
	pygame.mixer.init()
	pygame.mixer.music.load(audioFile)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		continue

# GPIO Define inputs
for v in inputs:
	GPIO.setup(v, GPIO.IN)

# While the script is runing check for inputs.
while 1:
	if GPIO.input(stopInputs[0]) and GPIO.input(stopInputs[1]):
		# stop
		call("sudo shutdown -h now", shell=True)
		break
		
	if lastActivity+datetime.timedelta(minutes = 20) > datetime.datetime.now():
		# stop
		call("sudo shutdown -h now", shell=True)
		break

	# Reproduce X audio file based on the input-.
	for i, v in enumerate(inputs):
		if GPIO.input(v):
			if connected:
				s.send(i)
			reproduceSound(sounds[i])
			lastActivity = datetime.datetime.now()

gpio.cleanup()
