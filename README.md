# rpi-power-switch

sudo apt-get install python-dev python-rpi.gpio
crontab -e
@reboot cd /home/pi/rpi-power-switch; python3 server.py

alias power_up='curl localhost:8000/cgi-bin/up.py'
alias power_down='curl localhost:8000/cgi-bin/down.py'
