import time
import notify2
from topnews import topStories

# notification window image path

ICON_PATH = "/mnt/c/Users/aroraan/Documents/Python/logo.jpg"

# fetching news items

newsitems = topStories()

# initialise the d-bus connection
            # This is the app name
notify2.init("News Notifier")           #  D-Bus is a message bus system, a simple way for applications to talk to one another.

# create notification object

n = notify2.Notification(None,icon = ICON_PATH)

# urgency level

n.set_urgency(notify2.URGENCY_NORMAL)

# timeout for notif
n.set_timeout(10000)

for newsitem in newsitems:
    # update notification data for notification object
    n.update(newsitem['title'], newsitem['description'])

    # show notif on screen
    n.show()

    # short delay between notifications
    time.sleep(15)