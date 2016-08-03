# rpi-power-switch

# install this

sudo apt-get install python-dev python-rpi.gpio

# change these permissions

chmod +x cgi-bin/up.py

chmod +x cgi-bin/down.py

# add to startup

crontab -e

@reboot cd /home/pi/rpi-power-switch; python3 server.py

# create aliases

alias power_up='curl localhost:8000/cgi-bin/up.py'

alias power_down='curl localhost:8000/cgi-bin/down.py'
