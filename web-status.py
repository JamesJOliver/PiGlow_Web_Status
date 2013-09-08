#web_status.py
#This is a small python file that will get the web status of a site (in this case http://www.raspberrypi.org/) 
#and relay that to the user through the awesome PiGlow by Pimoroni,
#using the bulit-in module "urllib" as well as an external one - "piglow" created by Boeeerb.

#james12802

#404 = page not found = orange
#202 = OK = green
#503 = server offline = red
#else = ERROR = red and orange

from piglow import PiGlow
from urllib import urlopen
from time import sleep

piglow = PiGlow()

#warm up the leds
piglow.all(0)
sleep(2)
piglow.all(10)
sleep(2)
piglow.all(0)

def site_test():
	
	sitecode = 123
	sitecode = urlopen("http://www.raspberrypi.org").getcode()
	
	if sitecode == 503:
		piglow.all(0)
        	piglow.red(10)
        	print "Red"

	if sitecode == 200:
        	piglow.all(0)
        	piglow.green(10)
        	print "Green"

	if sitecode == 404:
		piglow.all(0)
        	piglow.red(10)
        	print "Orange"

	else:
		piglow.all(0)
		piglow.red(10)
		piglow.orange(10)
		piglow.yellow(10)
		print "Red, Orange and Yellow "

#and so it beggins
site_test()

day = 1

while day == 1:
	sleep(60)
	site_test()




