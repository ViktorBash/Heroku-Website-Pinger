import requests
import time
from datetime import datetime

# Don't forget to change http to https if your website requires it.
YOUR_URL = "http://yourwebsite.herokuapp.com"
# How often to ping your website in minutes. Don't choose anything less than 30 minutes for Heroku!
HOW_OFTEN_TO_PING = 5


MINUTE = 60

while True:
    r = requests.get(YOUR_URL)
    print(f"Last ping at: {datetime.now()}")
    time.sleep(MINUTE*HOW_OFTEN_TO_PING)
