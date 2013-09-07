PiGlow_Web_Status
=================

This is a small python that will get the web status of a site (in this case http://www.raspberrypi.org/) and relay that to the user through the awesome [PiGlow](http://shop.pimoroni.com/products/piglow "PiGlow") by Pimoroni, using the bulit-in module "urllib" as well as an external one - "piglow" created by [Boeeerb](https://github.com/Boeeerb/PiGlow).

BTW part of this is nicked strait from [Boeeerb](https://github.com/Boeeerb/PiGlow)!

Files
------
web_status.py - this one test a web page and then lights the corrisponding led
piglow.py - this is imported into the web_status.py

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

Now enable the ic2 driver by opening the following file in your faviourt text editor
````
sudo nano /etc/modules
````

And adding these two lines to the end of the file
````
i2c-dev
i2c-bcm2708
````

The file should now look like this
![alt text](https://github.com/James12802/PiGlow_Web_Status/blob/master/images/add_modules.jpg "Added the two files to modules")

Installation
-----





