import mraa
import time

relay_gpio = 6

relay = mraa.Gpio(relay_gpio)
relay.dir(mraa.DIR_OUT)

def toggle():
	relay.write(1)
	time.sleep(0.1)
	relay.write(0)

while True:

	toggle()
	time.sleep(3)