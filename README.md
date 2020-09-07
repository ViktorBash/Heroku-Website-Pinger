# Heroku-Website-Pinger
This script pings your Heroku website so it won't go to sleep, as long as the script is running. 

# How To Use:
Go into [heroku_ping.py](heroku_ping.py) and change the YOUR_URL variable to your website URL. If your website uses HTTPS make sure to change that in the variable as well.

##### Optional:

Change HOW_OFTEN_TO_PING to how often you want your website to be pinged in minutes. If you're using Heroku beware that anything above 30 minutes will mean your website will be down.