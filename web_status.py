#web_status.py
#This file will get the web status of a site (in this case http://www.raspberrypi.org/) 
#and relay that to the user through the piglow, using the modules "urllib" as well as "piglow" by Boeeerb
#james12802

from urllib import urlopen, getcode
from piglow import PiGlow




