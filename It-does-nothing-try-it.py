import webbrowser
import time
import random

while True:
    nameOfWebSite = random.choice(['111111111111111111111111111111111111111111111111111111111111.com','stealthboats.com','ninjaflex.com','thatsthefinger.com','crossdivisions.com','movenowthinklater.com'])
    agadiko = "http://{}".format(nameOfWebSite)
    webbrowser.open(agadiko)
    timedifference = random.randrange(5,9)
    time.sleep(timedifference)
