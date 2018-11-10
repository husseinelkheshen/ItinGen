# make calls to ticketmaster to find sporting events
import requests
# this is the credential file and is not in the repository
from tm_auth import *

# URI format
# https://app.ticketmaster.com/{package}/{version}/{resource}.json?apikey={key}
# 200 - successful operation
# maximum page size is 200
URI = "https://app.ticketmaster.com/%s/%s/%s/.json"
PAYLOAD = {
    "apikey": None
}

# check rate limit by:
# r = requests.get(URI)
# r.headers["Rate-Limit-Available"] <- will give back the number as a string
