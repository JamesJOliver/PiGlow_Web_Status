PiGlow_Web_Status
=================

This is a small python file that will get the web status of a site (in this case http://www.raspberrypi.org/) and relay that to the user through the awesome [PiGlow](http://shop.pimoroni.com/products/piglow "PiGlow") by Pimoroni, using the bulit-in module "urllib" as well as an external one - "piglow" created by [Boeeerb](https://github.com/Boeeerb/PiGlow).

BTW part of this tutorial is "borrowed" from [Boeeerb](https://github.com/Boeeerb/)!

Files
------
web-status.py - this one test a web page and then lights the corresponding led

piglow.py - this is imported into the web-status.py

Requirements
------
The follwing module is required:
* python-smbus

SMBus allows python to communicate with the PiGlow over the ic2 bus.


Before Installation
------
Update the Raspberry Pi
```
sudo apt-get update
````

Now enable the ic2 driver by opening the following file in your Favourite text editor
````
sudo nano /etc/modules
````

And adding these two lines to the end of the file
````
i2c-dev
i2c-bcm2708
````

The file should now look like this
![alt text](https://raw.github.com/James12802/PiGlow_Web_Status/master/images/add_modules.jpg "Added the two files to modules")

Press Ctrl-X and when prompted press Y

Now edit the next file raspi-blacklist.conf
````
sudo nano /etc/modprobe.d/raspi-blacklist.conf
````
And add # (hash sybols) to the beggining of each line

![alt text](https://raw.github.com/James12802/PiGlow_Web_Status/master/images/hashing.jpg "Hashing")

Again press Ctrl-X and when prompted press Y

Now restart the Raspberry Pi
````
sudo reboot
````

Installation
-----
Create a directory for PiGlow and web-status to live in called src
````
sudo mkdir /src
```` 

Once this folder is created cd into it
````
cd /src
````
###Now for the actual installation

First install the PiGlow module
````
sudo wget https://raw.github.com/Boeeerb/PiGlow/master/piglow.py
````

Now the web-status.py file
````
sudo wget https://raw.github.com/James12802/PiGlow_Web_Status/master/web-status.py
````
Testing
-----
Now to test the file run
````
sudo python web-status.py
````

This will start outputing either green, red or orange and light up the corresponding leds.

![alt text](https://raw.github.com/James12802/PiGlow_Web_Status/master/images/working.jpg "Its Working!")

Press Ctrl-Z to end the program.

Customisation
-----
Now this is all well and good but what's the point of it? Well I run a web server off of my headless Pi and want to know if my site is up or down without having to open my browser. To change the site address to simply
````
sudo nano web-status.py
````

And edit the following line from
````
sitecode = urlopen("http://www.raspberrypi.org").getcode()
````

To

````
sitecode = urlopen("http://www.james12802.co.uk").getcode()
````

Or what ever you want.

Start on boot
-----
As I run my web server headless I don't want to keep having to start the script every time I boot up my Pi, so I have automated it.

First cd into the init.d directory by
````
cd /etc/init.d
````

Now create the file "web-status" 
````
sudo nano web-status
````

And enter the following
````
#! /bin/sh
# /etc/init.d/test

### BEGIN INIT INFO
# Provides:          clock
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Simple script to monitor the status of a website
# Description:       Simple script to monitor the status of a website
### END INIT INFO


 case "$1" in
  start)
    sudo python /src/web-status/web-status.py
    ;;
  stop)
   ;;
  *)
    killall python
    exit 1
    ;;

esac
exit 0
````
You should know it by now - press Ctrl-X and when prompted press Y

Now make the file an executable
````
sudo chmod +x web-status
````

And add it to the start up scripts by
````
sudo update-rc.d web-status defaults
````

![alt text](https://raw.github.com/James12802/PiGlow_Web_Status/master/images/exe.jpg "Making the file executable")

Now reboot your Pi
````
sudo reboot
````

And enjoy

James12802 =D