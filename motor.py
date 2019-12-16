import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 16 #input 2
Motor1B = 18 #input 1
Motor1E = 22 #enable
EncoderA = 38 #A channel
EncoderB = 40 #B channel
Index = 36 #Index channel

#setting up GPIO pins on the pi for the l293d motor driver and for the encoder 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(EncoderA,GPIO.IN)
GPIO.setup(EncoderB,GPIO.IN)
GPIO.setup(Index,GPIO.IN)

print "Enabling motor"
GPIO.output(Motor1A, GPIO.LOW)
GPIO.output(Motor1B, GPIO.LOW)
GPIO.output(Motor1E, GPIO.HIGH) #turns motor on

var = 1
currentpos = 0
done = 0
counter = 0
aLastState = GPIO.input(38)
bLastState = GPIO.input(40)
tracker = 10
indexCount = 0
Max = 17400.0

def edgeCountA(channel):
        global counter
        counter = counter+1
        
GPIO.add_event_detect(38, GPIO.RISING, callback = edgeCountA)

while var == 1 :
	print "Type in angle between 0 - 360 degrees"
	x = input()	
	if x - currentpos >= 180.0 and x - currentpos <=360.0:
		print "Motor turning counter-clockwise"	
		temp = 360.0 / (360.0 - x)
		print "temp: ", temp
		while True : 
			GPIO.output(Motor1A,GPIO.HIGH)
			GPIO.output(Motor1B,GPIO.LOW) 
			if counter >= Max / temp :
                                print counter
				counter = 0
				GPIO.output(Motor1A,GPIO.LOW)
				GPIO.output(Motor1B,GPIO.LOW)
				break
	elif x - currentpos < 180 and x - currentpos >=0:
		print "Motor turning clockwise"
		temp = 360.0 / x 
		print "temp: ", temp
		while True : 
			GPIO.output(Motor1A,GPIO.LOW)
			GPIO.output(Motor1B,GPIO.HIGH)
			if counter >= Max / temp :
                                print counter
				counter = 0
				GPIO.output(Motor1A,GPIO.LOW)
				GPIO.output(Motor1B,GPIO.LOW)
				break
	else :
		break
 
print "Disabling motor"
GPIO.output(Motor1E,GPIO.LOW)
 
GPIO.cleanup()
