# make calls to ticketmaster to find sporting events
import requests
import geohash2
import time
import json
# this is the credential file and is not in the repository
from tm_auth import *
from tm_tests import *


# URI format
# https://app.ticketmaster.com/{package}/{version}/{resource}.json?apikey={key}
# 200 - successful operation
# maximum page size is 200
# check rate limit by:
# r = requests.get(URI)
# r.headers["Rate-Limit-Available"] <- will give back the number as a string
URI = "https://app.ticketmaster.com/%s.json"
EVENTS = "discovery/v2/events"
VENUES = "discovery/v2/venues"
CLASS_ID = {
                "Sports":       {"id": "KZFzniwnSyZfZ7v7nE",
                                 "name": "Sports"},
                "Music":        {"id": "KZFzniwnSyZfZ7v7nJ",
                                 "name": "Music"},
                "ArtsTheatre":  {"id": "KZFzniwnSyZfZ7v7na",
                                 "name": "Arts & Theatre"},
                "Film":         {"id": "KZFzniwnSyZfZ7v7nn",
                                 "name": "Film"}
}
CITY_LOCS = {
                "Chicago": {"lat": 41.8781,
                            "lon": -87.6298}
}


# around 30 mile range seems reasonable
def get_venues(city, range):
    '''
    finds venues by city and range around that city by miles

    inputs:
        city (str) - city, will use CITY_LOCS to get lat and lon values
        range (int) - miles around city to look for venues

    outputs:
        venues (dict) - dictionary of venues that follows structure in
                        tm_tests.py
    '''
    print("Running get_venues...")
    # URL base to use
    venues_url = URI % VENUES
    # check city validity
    if city not in CITY_LOCS:
        print("ERROR: city is not valid")
        return -1
    city = CITY_LOCS[city]
    # payload to use for our request
    payload = {
        "apikey": switch_key(),
        "radius": range,
        "unit": "miles",
        "size": 200,
        "page": 0,
        "geoPoint": geohash2.encode(city["lat"], city["lon"], precision=9)
    }
    # data structures to hold the responses
    venues = {"venues": []}
    cont = True
    # now we can make the request to get venues
    while cont:
        r = requests.get(venues_url, params=payload)
        if check_r_status(r):
            print("SOLUTION: switching api keys and trying again")
            payload["apikey"] = switch_key()
        else:
            # process the data that was requested
            data = r.json()
            v_list = process_venues(data)
            print("%d venues found on this page" % len(v_list))
            for v in v_list:
                if venue_check(v):
                    venues["venues"].append(v)
                else:
                    print("ERROR: venue did not pass the venue check")
                    print("Printing here and dropping the venue:")
                    print(v)
            # now we need to check whether or not to continue
            print("completed page: %d" % (data["page"]["number"] + 1))
            print("out of: %d" % data["page"]["totalPages"])
            if data["page"]["number"] < (data["page"]["totalPages"] - 1):
                payload["page"] += 1
                print("going to next page")
                # should pause for a sec to not get rate limited
                time.sleep(3)
            else:
                print("done running")
                cont = False

    return venues


def process_venues(data):
    '''
    takes a request response and extracts the relevant data and puts it into
    a dictionary

    inputs:
        data (dict) - response from the venue request

    outputs:
        venue_list (list) - list of dicts of venues
    '''
    venue_list = []
    # get to the actual list of venues
    venues_raw = data["_embedded"]["venues"]
    # iterate through and extractb relevant data
    for v in venues_raw:
        tmp = {}
        tmp["venue_id"] = v["id"]
        tmp["venue_name"] = v["name"]
        tmp["latitude"] = float(v["location"]["latitude"])
        tmp["longitude"] = float(v["location"]["longitude"])
        tmp["address1"] = v.get("address", {}).get("line1", "")
        tmp["address2"] = v.get("address", {}).get("line2", "")
        tmp["address3"] = v.get("address", {}).get("line3", "")
        tmp["city"] = v["city"]["name"]
        tmp["state"] = v["state"].get("stateCode", v["state"]["name"])
        tmp["zip_code"] = v.get("postalCode", "")
        # done getting info, add to list
        venue_list.append(tmp)

    return venue_list


def venue_demo():
    '''
    '''
    venues = get_venues("Chicago", 30)
    of = []
    for v in venues["venues"]:
        of.append(v)
    with open("venues_11122018.json", "w") as fp:
        json.dump(of, fp)
