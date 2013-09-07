#web_status.py
#This is a small python file that will get the web status of a site (in this case http://www.raspberrypi.org/) 
#and relay that to the user through the awesome PiGlow by Pimoroni,
#using the bulit-in module "urllib" as well as an external one - "piglow" created by Boeeerb.

#james12802

#0 = not tested = orange
#202 = OK = green
#503 = server offline = red
#else = ERROR = red and orange

from piglow import PiGlow
from urllib import urlopen
from time import sleep

piglow = PiGlow()

#warm up the leds
piglow.all([0])
sleep(2)
piglow.all([50])
sleep(2)
piglow.all([0])

def site_test():
	
	sitecode = 123
	sitecode = urlopen("http://www.raspberrypi.org").getcode()
	
	if sitecode == 50:
		piglow.all([0])
        piglow.red([50])
        print "Red"

	if sitecode == 0:
		piglow.all([0])
       	piglow.orange([50])
        print "Orange"

	if sitecode == 200:
        piglow.all([0])
        piglow.green([50])
        print "Green"

	else:
		piglow.all([0])
		piglow.red([50])
		piglow.orange([50])
		print "Red and Orange"

#and so it beggins
site_test()

day = 1

while day == 1:
	sleep(60)
	site_test()




