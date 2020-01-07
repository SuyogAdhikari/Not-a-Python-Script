import webbrowser
import time
import random

while True:
    nameOfWebSite = random.choice(['111111111111111111111111111111111111111111111111111111111111.com','stealthboats.com','ninjaflex.com','thatsthefinger.com','crossdivisions.com','movenowthinklater.com'])
    SitekoAttachments = "http://{}".format(nameOfWebSite)
    webbrowser.open(SitekoAttachments)
    timedifference = random.randrange(5,9)
    time.sleep(timedifference)
