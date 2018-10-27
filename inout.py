# Librarys
import datetime
import RPi.GPIO as GPIO
import pygame
import socket
import sys


# Host
HOST = ''   # IP or Hostname of you server
PORT = 8888 # Arbitrary non-privileged port
connected = False # To send events only if the socket is connected.

# Define last activity.
sleepMode = False
lastActivity = 0

# The index of the input should match the index of the sound.
inputs = [10, 12, 14, 16, 18, 20, 22, 24]
sounds = ["audioOne.wav", "audioTwo.wav", "audioTree.wav", "audioFour.wav", "audioFive.wav", "audioSix.wav", "audioSeven.wav", "audioEight.wav"]

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
	sleepMode = False
	pygame.mixer.init()
	pygame.mixer.music.load()
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
		shutdown -h now
	if lastActivity+datetime.timedelta(minutes = 20) > datetime.datetime.now():
		# stop
		shutdown -h now
	if lastActivity+datetime.timedelta(minutes = 5) > datetime.datetime.now():
		# sleep.
		sleepMode = True

	# Reproduce X audio file based on the input-.
	for i, v in enumerate(inputs):
		if GPIO.input(v):
			if connected:
				s.send(i)
			reproduceSound(sounds[i])
			lastActivity = datetime.datetime.now()
